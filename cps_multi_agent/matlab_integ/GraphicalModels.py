import networkx as nx
import copy
import numpy as np
from scipy.io import savemat
from multiprocessing import Process, Queue, JoinableQueue, Manager
#from Automata import ProductBuchi

class GraphicalModel:
    """Base class for graph-based planning models, e.g. MDPs and transition
    systems.  This is used to give a common interface for neighborhood enumeration
    and graph search operations.  
    
    fields:
        states: list of all states in the model
        transitions: edges in the graph given in a dict object.  Not sure if used.
        labels: Set of all possible state labels
        labelMapping: Mapping of states to labels
        graphRepresentation:  Representation of the graphical model as a 
                              networkx digraph.  Most of the methods implemented
                              by children class use this as the "base" object
                              for computation.
    """
    
    def __init__(self):
        """Initializes all fields with empty objects."""
        
        self.labels = set()
        self.labelMapping = dict()
        self.states = set()
        self.transitions = dict()
        self.graphRepresentation = nx.DiGraph()
        
    
        
    def findNeighborhood(self,state,horizon):
        """ Finds the states within a given radius of an anchor state.
        
        Inputs:
            state: center of the neighborhood
            horizon: radius of the neighborhood
        
        Outputs: 
            a set of states that are horizon edges away from state
            
        """
        neighborhood=set()
        k = 0;
        prevSet = set()
        prevSet.add(state)
        nextSet = set()
        while k < horizon:
            nextSet.clear()
            for node in prevSet: 
                nextSet=nextSet.union(set(nx.neighbors(self.graphRepresentation,node)))
            if len(nextSet) == 1 and None in nextSet: return neighborhood
            if None in nextSet: nextSet.remove(None)
            neighborhood=neighborhood.union(nextSet)
            prevSet = copy.deepcopy(nextSet)
            k+=1
        return neighborhood
       
        
    def findInverseReachability(self,state,horizon):
        """ Finds the set of states that can reach the given state.
          See GraphicalModel.findReachability."""
        k = 0;
        prevSet = set()
        prevSet.add(state)
        nextSet = set()
        while k < horizon:
            nextSet.clear()
            for node in prevSet: 
                reversedGraph = self.graphRepresentation.reverse(True)
                nextSet = nextSet.union(set(nx.neighbors(reversedGraph,node)))
            if len(nextSet) == 1 and None in nextSet: return None
            if None in nextSet: nextSet.remove(None)
            prevSet = copy.deepcopy(nextSet)
            k+=1
        return nextSet
    
    def findReachability(self,state,horizon):
        """ Finds a reachable set on the graph.
        
        Inputs: 
            state: starting point of reachability search
            horizon: number of edges away from state to be searched.
        
        Outputs: the set of all states that are reachable from state
                 in exactly horizon transitions.
        """
        k = 0;
        prevSet = set()
        prevSet.add(state)
        nextSet = set()
        while k < horizon:
            nextSet.clear()
            for node in prevSet: 
                nextSet = nextSet.union(set(nx.neighbors(self.graphRepresentation,node)))
            if len(nextSet) == 1 and None in nextSet: return None
            if None in nextSet: nextSet.remove(None)
            prevSet = copy.deepcopy(nextSet)
            k+=1
        return nextSet
        

class WeightedTransitionSystem(GraphicalModel):
    """ A class that represents a deterministic transition
        system with weighted edges. 
        """
        
    def getPossibleActions(self,state):
        """ Returns the set of possible actions that can be taken
        at a particular state."""
        return self.transitions[state].keys()
    
    def pathFromActions(self,initState,actionSequence):
        """ Returns a path (sequence of states) over the transition
        system that is produced by a sequence of inputs.
        
        Inputs:
            initState: beginning state of the path
            actionSequence: sequence of inputs to be applied to the transition system
        
        Outputs:
            list of states in the path induced y the inputs
            """
        path =list()
        path.append(initState)
        currState = initState
        for k in range(len(actionSequence)):
            currState = self.transitions[currState][actionSequence[k]][1]
            path.append(copy.deepcopy(currState))
        return path

    def findShortestPath(self,source,destination):
        """Finds the shortest path on the transition system from 
        source to destination."""
        return nx.shortest_path(self.graphRepresentation,source,destination)
    
   
    def addState(self,name,labelarg=None,likelihoodFunctionarg=None):
        """
        Add a state to the transition system.
        
        Inputs:
            name: identity associated with the state.  This is the 
                  representation of the node used in the underlying networkx
                  representation
            labelarg (optional): label associated with the state
            likelihoodFunctionarg(optional): the Estimation.LikelihoodFunction associated
                  with the given state.  For use with the informative planning algorithms.
        """
        self.graphRepresentation.add_node(name,label=labelarg,likelihood=likelihoodFunctionarg)
        self.states.add(name)
        self.transitions[name] = dict()
        self.labelMapping[name]=set()
        if labelarg is not None:
            for lab in labelarg: 
                self.labels.add(lab)
                self.labelMapping[name].add(lab)
        
        
    def labelState(self,state,label):
        """ Applies a label to the indicated transition system state."""
        if state in self.states:
            if state not in self.labelMapping.keys(): self.labelMapping[state]=set()
            for lab in label: 
                self.labels.add(lab)
                self.labelMapping[state].add(lab)
    
    def labelOf(self,state):
        """ Returns the label set of the indicated state."""
        if state not in self.labelMapping.keys(): return None
        return self.labelMapping[state]
    
    def addLikelihood(self,state,likelihood):
        """Associates an Estimation.LikelihoodFunction with the given state in the transition system.
           Used in the informative planning algorithms."""
        self.graphRepresentation.node[state]['likelihood']=likelihood
        
    def getLikelihood(self,state):
        """ Returns the Estimation.LikelihoodFunction associated with the given state.  Used
            in informative planning algorithms."""
        return self.graphRepresentation.node[state]['likelihood']
    
    
    def addTransition(self,state1,actionarg,weightarg,state2,label1=None,label2=None,likelihood1=None,likelihood2=None):
        """Adds a (deterministic) transition to  the system.  If the states in the added
        transition are not already included in the object, they will be added along with
        the additional information from the input arguments.
        
        Inputs: 
            state1: source state in the transition
            actionarg: action that enables the transition
            weightarg: weight (cost) of the added transition.  The
                uniform value of 1 is typically used.
            state2: destination state in the transition
            label1(optional): label associated with state1
            label2(optional): label associated with state2
            likelihood1(optional): Estimation.LikelihoodFunction associated with state1
            likelihood2(optional): Estimation.LikelihoodFunction associated with state2
        """
        # self.states.add(state1); self.states.add(state2)
        self.addState(state1)
        self.addState(state2)
        if state1 not in self.transitions.keys(): self.transitions[state1]=dict()
        self.transitions[state1][actionarg] = (weightarg,state2)
        self.graphRepresentation.add_edge(state1,state2,weight=weightarg,action=actionarg)
        if label1 is not None: self.labelState(state1,label1)
        if label2 is not None: self.labelState(state2,label2)
        if likelihood1 is not None: self.addLikelihood(state1,likelihood1)
        if likelihood2 is not None: self.addLikelihood(state2,likelihood2)
        
   
    def calculatePathWeight(self,path):
        """Returns the total accumulated weight(cost) of the input
        path."""
        weight = 0.0
        for k in range(len(path)-1):
            weight += self.graphRepresentation[path[k]][path[k+1]]['weight']
        return weight

    def TSfromGame(self,gameStates,gameTransitions,gameLabels):
        for trans in gameTransitions:
            self.addTransition(trans[0],trans[2],1,trans[1])
        for state in gameStates:
            # First convert labels into strings of the form p1&p2&p3 for all propositions that are true 
            label = '' 
            #PRASANNA_EDIT
            #Previously: props = gameLabels[state].propositionList
            props = gameLabels[state[1]]
            for i in xrange(len(props)-1):
                if props['p'+str(i+1)] != []:
                    if len(label) == 0:
                        label = 'p'+str(i+1)
                    else:
                        label = label+'&p'+str(i+1)
            # If length of label is 0 then, highest proposition (null proposition) is true
            if len(label)==0:
                label = 'p'+str(len(props))
            self.addState(state)
            self.labelMapping[state] = set()
            self.labelMapping[state].add(label)
        # for edge in self.graphRepresentation.edges():
        #     if edge[0][0] == '3':
        #         print edge
        #     if edge[0][1][-2] == 'R':
        #         print edge
        # print self.graphRepresentation.edges()


    def incrTrans(self,newTransitions):
        for edge in newTransitions:
            self.addTransition(edge[0],edge[2],1,edge[1])