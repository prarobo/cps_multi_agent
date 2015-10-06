import os
import networkx as nx
import subprocess
from copy import *
from GraphicalModels import *
#import paths
import itertools

class Automaton:
    """Base class for automata used for model checking and control synthesis 
    for discrete systems.  Constructing FSAs and BuchiAutomata from formulae
    requires installation of Ebru's code LangGuiCs (found on the hyness 
    website) and also installation of the lbt and lbt2dot utilities,respectively.
    Set the paths to the relevant utilities in Ebru's code via the paths.py module.

    Fields:
        graph: A networkx digraph that serves as the underlying representation 
            of the automata used in this module.  Although this field is 
            public, most manipulation of this graph will be done indirectly 
            via the module methods.
        states: A list of all of the states that are in the Automaton.
        inputLanguage: The input language of the automaton.  The permissible 
            inputs for the Automaton are contained in the power set of this 
            language.  Typically, this is the set of atomic propositions
            associated with the automaton.
        initialStates:  The set of states in which the Automaton may be 
            initially
        currentStates: The set of states in which the Automaton may currently be
        acceptingStates: The set of all final (accepting) states in the 
            Automaton
        lyapFun: A dict object whose keys are elements of states and whose item
            is the shortest distance from the key state to an accepting state.
            This field is only constructed if calculateDistanceToAccepting is 
            invoked.  It is necessary for calling makeNonBlocking.
    """
    
    def __init__(self):
        """Initializes an automaton with empty graph, state, and language 
        fields. """
        self.graph = nx.DiGraph()
        self.acceptingStates = set()
        self.currentStates = set()
        self.initialStates=set()
        self.states = set()
        self.inputLanguage=set()
        
    def addEdge(self,state1,state2,labelarg=None,initial1=False,accepting1=False,initial2=False,accepting2=False):
        """Creates an edge between two states in the automaton. 
        Inputs:
            state1: source of the edge
            state2: target of the edge
            labelarg: logical formula as a string that describes the inputs 
                corresponding to the edge
            initialx: bool describing whether statex is an initial state
            acceptingx: bool describing whether statex is an accepting state
        """
        self.graph.add_edge(state1,state2)
        self.graph[state1][state2][0] = dict()
        self.graph[state1][state2][0]['label']=labelarg
        for prop in stripProps(labelarg): self.inputLanguage.add(prop)
        self.addState(state1,initial1,accepting1)
        self.addState(state2,initial2,accepting2)
    
    def addMAEdge(self,state1,state2,labelarg=None,initial1=False,accepting1=False,initial2=False,accepting2=False):
        """Creates an edge between two states in the automaton. 
        Inputs:
            state1: source of the edge
            state2: target of the edge
            labelarg: logical formula as a string that describes the inputs 
                corresponding to the edge
            initialx: bool describing whether statex is an initial state
            acceptingx: bool describing whether statex is an accepting state
        """
        if (state1,state2) in self.graph.edges():
            if self.graph[state1][state2][0]['label'] == None:
                self.graph[state1][state2][0]['label']=labelarg                
            else:
                self.graph[state1][state2][0]['label']=self.graph[state1][state2][0]['label']+' | '+labelarg
        else:
            self.graph.add_edge(state1,state2)
            self.graph[state1][state2][0] = dict()
            self.graph[state1][state2][0]['label']=labelarg
            self.inputLanguage.add(labelarg)
            self.addState(state1,initial1,accepting1)
            self.addState(state2,initial2,accepting2)
    
    def addState(self,state,initial=False,accepting=False):
        """"
        Adds a state to the Automaton.
        Inputs:
            state: Automaton state to be added
            initial: bool describing whether state is an initial state
            accepting: bool describing whether state is an accepting state
        """
        self.graph.add_node(state)
        self.states.add(state)
        if initial: self.initialStates.add(state)
        if accepting: self.acceptingStates.add(state)
        
    def removeEdge(self,state1,state2):
        """Removes indicated edge from Automaton.
        Inputs:
            state1: source of edge to be removed
            state2: target of edge to be removed
        """
        self.removeState(state1)
        self.removeState(state2)

    def removeState(self,state):
        #modified by Kevin to remove state from the list of states, too
        """Removes state from Automaton.
        Inputs:
            state: state to be removed
        """
        if state in self.graph.nodes():
            self.graph.remove_node(state)
            self.states.remove(state)
            if state in self.initialStates: self.initialStates.remove(state)
            if state in self.acceptingStates: self.acceptingStates.remove(state)


    def checkSymbol(self,symbol,states='default'):
        """Checks whether the given input symbol  enables any out edges
        from the indicated set of states.
        Inputs:
            symbol: input to the Automaton, given as a list of strings 
            corresponding to atomic propositions of the Automaton,
            must be a subset of inputLanguage 
            states: set of states from which we check the input. It
                is currentStates by default.
        Returns:
            The set of all states that result from applying symbol
            to a state in the set states.  Returns None if the input
            doesn't enable any out edges from the states. 
            """
        if states is 'default': 
            states = self.currentStates
        nextStates = set()
        for state in states:
            if self.graph[state].keys() is not None:
                for key in self.graph[state].keys():
                    for key2 in self.graph[state][key].keys():
                        label = self.graph[state][key][key2]['label']
                        if isinstance(self,BuchiAutomaton) or isinstance(self,ProductBuchi):
                            label = buchiProcess(label) # maps formula from prefix form (output from ltb) to infix form
                        if isinstance(self,ProductBuchi) and symbol in str(label):nextStates.add(key)
                        elif parseTruth(str(label),symbol,self.inputLanguage): nextStates.add(key)
        if len(nextStates)==0:return None
        return nextStates     

    def checkSymbolOneState(self,symbol,state):
        """Checks whether the given input symbol  enables any out edges
        from the indicated set of states.
        Inputs:
            symbol: input to the Automaton, given as a list of strings 
            corresponding to atomic propositions of the Automaton,
            must be a subset of inputLanguage 
            state: a SINGLE STATE from which we check the input.
        Returns:
            The set of all states that result from applying symbol
            to a state in the set states.  Returns None if the input
            doesn't enable any out edges from the states. 
        #     """
        # print 'state:',state
        # print 'symbol:',symbol
        nextStates = set()
        if self.graph[state].keys() is not None:
            for key in self.graph[state].keys():
                label = self.graph[state][key][0]['label']
                # print "label:",label
                if isinstance(self,BuchiAutomaton) or isinstance(self,ProductBuchi):
                    label = buchiProcess(label) # maps formula from prefix form (output from ltb) to infix form
                if isinstance(self,ProductBuchi) and symbol in str(label):nextStates.add(key)
                elif parseTruth(str(label),symbol,self.inputLanguage): nextStates.add(key)
        if len(nextStates)==0:return None
        return nextStates
    
    def checkWord(self,word,states='default'):
        """ Checks a word (list of symbols) to see if the sequence of inputs
        enables any paths in the Automaton initiated from the selected set 
        of states.
        Inputs:
            word: list of symbols (i.e. a list of lists of strings) 
                corresponding to a sequence of inputs applied to the Automaton
            states: set of states from which we check if word can 
                generate any feasible paths.  By default it is set 
                to currentStates.
        Outputs:
            Returns True if word enables at least one path. Returns
            False if no path can be enabled.
        """
        if states=='default':states = self.currentStates
        for symbol in word:
            states = self.checkSymbol(symbol,states)
            if states is None: return False
        return True
    
    def input(self,action):
        """Similar to checkWord, but actually changes currentStates to the set of states 
        that results from applying the input word to the Automaton
        Inputs:
            word: list of symbols (i.e. a list of lists of strings) 
                corresponding to a sequence of inputs applied to the Automaton
        """
        for state in self.currentStates:
            curr = state
        for state in self.checkSymbolOneState(action,curr):
            # print "state:",state
            # print "action:",action
            # print "curr:",curr
            self.currentStates = set([state])
        
    def checkValidity(self,state):
        """ Checks whether or not a state has any out edges
        Inputs:
            state: state to be checked for out edges
        """
        return self.graph[state].keys() is not None    
    
    def calculateDistanceToacceptingStates(self):
        """Calculates the graph distance from each state in the
        Automaton to the nearest accepting state, that is it constructs
        the field lyapFun."""
        
        ###Find all shortest paths from each node to each accepting state ####
        dictList = list()
        for acceptingstate in copy.deepcopy(self.acceptingStates):
            nei = self.graph.predecessors(acceptingstate)
            if len(nei) > 0:
                nextDict = nx.single_source_dijkstra_path_length(copy.deepcopy(self.graph.reverse()),acceptingstate)
                dictList.append(nextDict)
            else:
                self.acceptingStates.remove(acceptingstate)
        self.lyapFun = dict()
        for state in self.graph.nodes():
            self.lyapFun[state] = None
        for state in self.acceptingStates:
            self.lyapFun[state] = 0.0
        for state in self.graph.nodes():
            for d in dictList:
                if state in d.keys():
                    if d[state] < self.lyapFun[state] or self.lyapFun[state] is None: 
                        self.lyapFun[state] = copy.deepcopy(d[state])# Find closest accepting state for each node

    def calculateGameDistance(self,gameProduct):
        """Calculates the graph distance from each state in the
        Automaton to the nearest accepting state, that is it constructs
        the field lyapFun."""
        
        ###Find all shortest paths from each node to each accepting state ####
        dictList = list()
        for acceptingstate in copy.deepcopy(self.acceptingStates):
            nei = self.graph.predecessors(acceptingstate)
            if len(nei) > 0:
                nextDict = nx.single_source_dijkstra_path_length(copy.deepcopy(self.graph.reverse()),acceptingstate)
                dictList.append(nextDict)
            else:
                self.acceptingStates.remove(acceptingstate)
        self.lyapFun = dict()
        for state in self.graph.nodes():
            self.lyapFun[state] = None
        for state in self.acceptingStates:
            self.lyapFun[state] = 0.0
        for state in self.graph.nodes():
            if gameProduct.gameStates[state[0]].userID[7][0]!='E': #not the environment's turn
                for d in dictList:
                    if state in d.keys():
                        if d[state] < self.lyapFun[state] or self.lyapFun[state] is None: 
                            self.lyapFun[state] = copy.deepcopy(d[state])# Find closest accepting state for each node
                    

                    
    def makeNonBlocking(self):
        """ Removes all states from the Automaton from which no
        accepting state can be reached.
        """
        if 'lyapFun' not in self.__dict__.keys(): self.calculateDistanceToacceptingStates()
        for state in self.graph.nodes():
            if self.lyapFun[state] is None: 
                self.removeState(state)  
                self.lyapFun.pop(state)
            
    
    def shortestPath(self,state1,state2):
        """Calculates the shortest path in the Automaton between
        two states.
        Inputs:
            state1: source of the path
            state2: target of the path
        Outputs:
            Returns the list of states in the shortest path (including state1 
            and state2) in sequence.
        """
        return nx.shortest_path(self.graph,state1,state2)
            
    
    def neighbors(self,state):
        return nx.neighbors(self.graph,state)

class BuchiAutomaton(Automaton):
    """An implementation of a Buchi automaton, that is an automaton
    for checking infinite time properties of omega regular languages.
    """
    
    def fromStatement(self,statement,fname):
        """ Populates the BuchiAutomaton's fields to construct an automaton
        that is used to check a given LTL formula.  Wraps to lbt.
        Inputs:
            statement: A string using ltl2ba syntax that gives the 
                LTL formula to be checked
            fname: file name used to save intermediate data
        """
        ###Begin wrapping to lbt####
#        txtfile= fname+ '.txt'
#        subprocess.call(['touch',txtfile])
#        fout = open(txtfile,'w');fout.write(statement);fout.close()
#        subprocess.call(paths.PATH_TO_IN2PRE+"in2preLTL " + txtfile + " " + txtfile,shell=True)
#        subprocess.call("lbt < "+ txtfile+" > automaton.txt",shell=True) 
#        subprocess.call("lbt2dot < automaton.txt > automaton.dot",shell=True)
        txtfile= fname+ '.txt'
        fout = open(txtfile,'w');fout.write(statement);fout.close()
        subprocess.call("./ltl2dot_new.sh "+fname,shell=True)
        #### End wrapping to lbt ###
        self.graph = nx.read_dot(fname+".dot")
        for node in self.graph.nodes():
            self.states.add(node)
            label = self.graph.node[node]['label']
            if self.graph.node[node]['shape'] == "doublecircle":
            #if 'n' in label:
            #if peripheries:
                self.acceptingStates.add(node)
        for edge in self.graph.edges():
            label = self.graph[edge[0]][edge[1]][0]['label']
            for prop in stripProps(buchiProcess(label)):
                self.inputLanguage.add(prop)
        self.calculateDistanceToacceptingStates()
        self.initialStates.add('0')
        self.currentStates.add('0')
    
    def readStatement(self,fname):
        """This is like fromStatement, but it just reads from a .dot file"""
        self.graph = nx.read_dot(fname+".dot")
        for node in self.graph.nodes():
            self.states.add(node)
            label = self.graph.node[node]['label']
            if self.graph.node[node]['shape'] == "doublecircle":
            #if 'n' in label:
            #if peripheries:
                self.acceptingStates.add(node)
        for edge in self.graph.edges():
            label = self.graph[edge[0]][edge[1]][0]['label']
            for prop in stripProps(buchiProcess(label)):
                self.inputLanguage.add(prop)
        self.calculateDistanceToacceptingStates()
        self.initialStates.add('0')
        self.currentStates.add('0')       
    
    def checkWord(self,prefix,suffix,states='default'):
        """ Similar to Automaton.checkWord, but also checks the Buchi acceptance
        condition, i.e. final state is reached infinitely often
        Inputs:
            prefix:  finite list of symbols (i.e. a list of lists of strings) 
                corresponding to a sequence of inputs initially applied to the 
                BuchiAutomaton
             suffix:  finite list of symbols (i.e. a list of lists of strings) 
                corresponding to a sequence of inputs applied to the 
                BuchiAutomaton after the prefix infinitely often
            states: set of states from which we check if word can 
                generate any feasible paths.  By default it is set 
                to currentStates.
        Outputs:
            Returns True if word enables at least one path. Returns
            False if no path can be enabled.
        """
        if states == 'default': states = self.currentStates
        for symbol in prefix:
            states = Automaton.checkSymbol(self,symbol,states)
            if states is None: return False
        if len(states & self.acceptingStates)== 0: return False
        for symbol in suffix:
            states = Automaton.checkSymbol(self,symbol,states)
            if states is None: return False
        if len(states & self.acceptingStates) > 0: return True
        return False

class ProductBuchi(BuchiAutomaton):
    """Product between BuchiAutomaton and a WeightedTransitionSystem.
    Used for control synthesis and model checking of the transition system for LTL
    formulae."""
    
    def fromStatementAndWTS(self,statement,fname,WTS,initialWTSState):
        """Creates the product between a Buchi Automaton used to enforce 
         an LTL formula and a labeled weighted transition system.
        Inputs:
            statement: A string using ltl2ba synteax that gives the 
                LTL formula to be checked
            fname: file name used to save intermediate data
            WTS: a WeightedTransitionSystem object
            initialWTSState: initial state of WTS
        """
        buchi = BuchiAutomaton()
        buchi.fromStatement(statement,fname)
        for state in buchi.initialStates:
            self.initialStates.add((initialWTSState,state))
            self.currentStates.add((initialWTSState,state))
        
        tsGraph = WTS.graphRepresentation
        for edge in tsGraph.edges():
            pr = WTS.labelOf(edge[1])
            for otherEdge in buchi.graph.edges():
                label = copy.copy(buchi.graph[otherEdge[0]][otherEdge[1]][0]['label'])
                label = buchiProcess(label)
                if parseTruth(label,pr,buchi.inputLanguage):
                    act = tsGraph[edge[0]][edge[1]]['action']
                    self.graph.add_edge((edge[0],otherEdge[0]),(edge[1],otherEdge[1]), # Construct edges in product that inherit properties from both graphs.
                                                      dict(copy.deepcopy(tsGraph[edge[0]][edge[1]].items())
                                                           +copy.deepcopy(buchi.graph[otherEdge[0]][otherEdge[1]].items())))
                    self.graph.node[(edge[0],otherEdge[0])]['likelihood'] = tsGraph.node[edge[0]]['likelihood']
                    self.graph.node[(edge[1],otherEdge[1])]['likelihood'] = tsGraph.node[edge[1]]['likelihood']
                    self.graph[(edge[0],otherEdge[0])][(edge[1],otherEdge[1])][0]['label']=act
                    self.inputLanguage.add(act)
        for nodeTuple in self.graph.nodes():
            if nodeTuple[1] in buchi.acceptingStates: self.acceptingStates.add(nodeTuple)
        self.makeNonBlocking()

    def possibleActions(self,state):
        actionSet = set()
        for neighbor in self.neighbors(state):
            actionSet.add(self.graph[state][neighbor][0]['label'])
        return actionSet

    def fromBAndTS(self,buchi,WTS,initialWTSState):
        """Creates the product between a Buchi Automaton used to enforce 
         an LTL formula and a labeled weighted transition system.
        Inputs:
            statement: A string using ltl2ba syntax that gives the 
                LTL formula to be checked
            fname: file name used to save intermediate data
            WTS: a WeightedTransitionSystem object
            initialWTSState: initial state of WTS
        """
        # buchi = BuchiAutomaton()
        # buchi.fromStatement(statement,fname)
        for state in buchi.initialStates:
            self.initialStates.add((initialWTSState,state))
            self.currentStates.add((initialWTSState,state))
        
        tsGraph = WTS.graphRepresentation
        for edge in tsGraph.edges():
            pr = WTS.labelMapping[edge[0]]
            for otherEdge in buchi.graph.edges():
                label = copy.copy(buchi.graph[otherEdge[0]][otherEdge[1]][0]['label'])
                label = buchiProcess(label)
                if parseTruth(label,pr,buchi.inputLanguage):
                    act = tsGraph[edge[0]][edge[1]]['action']
                    self.graph.add_edge((edge[0],otherEdge[0]),(edge[1],otherEdge[1]), # Construct edges in product that inherit properties from both graphs.
                                                      dict(copy.deepcopy(tsGraph[edge[0]][edge[1]].items())
                                                           +copy.deepcopy(buchi.graph[otherEdge[0]][otherEdge[1]].items())))
                    self.graph.node[(edge[0],otherEdge[0])]['likelihood'] = tsGraph.node[edge[0]]['likelihood']
                    self.graph.node[(edge[1],otherEdge[1])]['likelihood'] = tsGraph.node[edge[1]]['likelihood']
                    self.graph[(edge[0],otherEdge[0])][(edge[1],otherEdge[1])][0]['label']=act
                    self.inputLanguage.add(act)
        for nodeTuple in self.graph.nodes():
            if nodeTuple[1] in buchi.acceptingStates: self.acceptingStates.add(nodeTuple)
        # self.calculateDistanceToacceptingStates()
    
    def incrProd(self,newTrans,buchi,WTS):
        for edge in newTrans:
            pr = WTS.labelOf(edge[0])
            for otherEdge in buchi.graph.edges():
                label = copy.copy(buchi.graph[otherEdge[0]][otherEdge[1]][0]['label'])
                label = buchiProcess(label)
                if parseTruth(label,pr,buchi.inputLanguage):
                    act = WTS.graphRepresentation[edge[0]][edge[1]]['action']
                    self.graph.add_edge((edge[0],otherEdge[0]),(edge[1],otherEdge[1]), # Construct edges in product that inherit properties from both graphs.
                                                      dict(copy.deepcopy(WTS.graphRepresentation[edge[0]][edge[1]].items())
                                                           +copy.deepcopy(buchi.graph[otherEdge[0]][otherEdge[1]].items())))
                    self.graph.node[(edge[0],otherEdge[0])]['likelihood'] = WTS.graphRepresentation.node[edge[0]]['likelihood']
                    self.graph.node[(edge[1],otherEdge[1])]['likelihood'] = WTS.graphRepresentation.node[edge[1]]['likelihood']
                    self.graph[(edge[0],otherEdge[0])][(edge[1],otherEdge[1])][0]['label']=act
                    self.inputLanguage.add(act)


    def getAction(self,dist,state):
        next_ = self.graph.successors(state)
        currDist = dist[state]
        if currDist == 0: #this isn't useful! we will end up at an accepting state anyway
            for key in dist.keys():
                if dist[key] > currDist:
                    currDist = dist[key]
        bestS = ''
        for s in next_:
            # if state[1]=='2':
            #     if state[0][1] == 'E0_01_R0_00_R1_10_T_R0':
            #         print"WE MADE IT HERE"
            #         print "DIST:",dist[state]
            #         print "DIST[S]:",dist[s]
            #         print "S:",s
            #         # if dist[s] == 0:
            #         #     print "DIST == 0"
            #         # if s[0][1]==state[0][1]:
            #         #     print "STATES EQUAL"
            if dist[s] == 0 and s[0][1] == state[0][1]: #don't move if dist == 0 for next state and
                action = self.graph[state][s][0]['label']
                bestS = state
                break
            else:
                # if currDist == 0
                if dist[s]<= currDist:
                    currDist = dist[s]
                    bestS = s
        if not bestS:
            action = 'xx0'
        else:
            action = self.graph[state][bestS][0]['label']
        return action
    
    def policyDict(self, dist):
        policy = dict()
        for state in self.currentStates:
            currBuchi = state[1]
        for state in self.graph.nodes():
            if state[1] == currBuchi:
                action = self.getAction(dist,state)
                policy[state[0]] = action

        return policy

    def dijkstraGameEff(self,gameProduct,F):
        dist = dict()
        for state in self.graph.nodes():
            dist[state] = float('Inf')
        for state in F:
            dist[state] = 0
        Q = copy.deepcopy(self.graph.nodes())
        while Q:
            val = float('Inf')
            val2 = [dist[q] for q in Q]
            val = min(val2)
            # print 'val:',val
            for q in Q:
                if dist[q] == val:
                    qu = q
                    break
            if dist[qu] == float('Inf'):
                break
            Q.remove(qu)
            if self.graph.predecessors(qu):
                for p in self.graph.predecessors(qu):
                    # print "PREDECESSORS!!"
                    # vals = [dist[x] for x in self.graph.successors(p)]
                    if gameProduct.gameStates[p[0][1]].userID[7][0] == 'E':
                        vals = [dist[x] for x in self.graph.successors(p)]
                        if vals:
                            # dist[p] = max(vals)+1
                            if p not in F:
                                dist[p] = max(vals)+1
                                # for x in self.graph.successors(p):
                                #     if dist[x] == max(vals):
                        #check if can transition and if is not final state
                    else:
                        if dist[p] > dist[qu] + 1:
                            dist[p] = dist[qu] + 1
                           
        return dist

    def findEnergyGame(self,gameProduct):
        dist = self.dijkstraGameEff(gameProduct,self.acceptingStates)
        FStar = copy.deepcopy(self.acceptingStates)
        for f in FStar.copy():
            next_ = self.graph.successors(f)
            vals = [dist[x] for x in next_]
            if vals:
                if min(vals) == float('Inf'):
                    FStar.remove(f)
            else:
                FStar.remove(f)
        dist = self.dijkstraGameEff(gameProduct,FStar)
        
        return dist, FStar


def parseTruth(formula,pr,labels):
    """ Helper function used to determine if an input satisfies the
        Boolean formula on the edge label.
        Inputs: 
            formula: Boolean logical formula given as a string in ltl2ba
                syntax.
            input: input to the Automaton
            labels: set of possible inputs to the automaton.
        Outputs:
            Returns True if input satisfies formula; False if it does not.
    """
    if formula == '( <empty> )': 
        return len(pr) == 0
    truthValues = dict()
    for lab in labels:
        if pr is not None and lab in pr:
            truthValues[lab] = 'True';
        else:
            truthValues[lab] = 'False';
    for key in truthValues.keys():
        formula = formula.replace(key,truthValues[key])
    formula = formula.replace(' t ',' True ')
    formula = formula.replace(' f ',' False ')
    formula = formula.replace('(t)',' True ')
    formula = formula.replace('(f)',' False ')   
    formula = formula.replace('!',' not ')
    formula = formula.replace('&',' and ')
    formula = formula.replace('|',' or ')
    if isinstance(eval(formula),str):
        formula = eval(formula)
    return eval(formula)

def parseTruthMA(formula,pr,labels):
    """
    Multi-agent verison of parseTruth that is for inf horizon MA problem
    """
    if formula == '( <empty> )': 
        return len(pr) == 0
    truthValues = dict()
    for lab in labels:
        if pr is not None and lab in pr:
            truthValues[lab] = 'True';
        else:
            truthValues[lab] = 'False';
    for key in truthValues.keys():
        formula = formula.replace(str(key),truthValues[key]) #change is here
    formula = formula.replace(' t ',' True ')
    formula = formula.replace(' f ',' False ')
    formula = formula.replace('(t)',' True ')
    formula = formula.replace('(f)',' False ')   
    formula = formula.replace('!',' not ')
    formula = formula.replace('&',' and ')
    formula = formula.replace('|',' or ')
    return eval(formula)

def buchiProcess(label):
    """Does some string processing to take the prefix form of
    edge labels generated by lbt to an infix form that
    is both readable and usable by the parseTruth function.
    Inputs: 
        label: string LTL formula in prefix form
    Outputs:
        string LTL formula in infix form
    """
    label = label.replace('&&',' & ')
    label = label.replace("!"," ! ")
    label = label.replace("(","( ")
    label = label.replace(")"," )")
    label = label.replace("||", " | ")
    #label = subprocess.check_output(paths.PATH_TO_PRE2IN+"pre2inLTL '" + label + "'",shell=True)
    return copy.deepcopy(label)

def stripProps(formula):
    """Helper function used to find all of the atomic propositions
    contained in an ltl2ba syntax formula.  Used in the addEdge method
    to update the inputLanguage of the Automaton.
    Inputs:
        formula: string Boolean formula in ltl2ba syntax
    Outputs
        set of all propositions in formula.
    """
    f = str(formula).replace('!','')
    f=f.replace('(','')
    f=f.replace(')','')
    
    #PRASANNA_EDIT
    #Previously: return set(f.split(' '))- set(['&','!','t','f','(',')','|',''])
    return set(f.split(' '))- set(['&','!','t','f','(',')','|','','"'])