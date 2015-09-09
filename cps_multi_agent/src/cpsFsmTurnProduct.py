#!/usr/bin/python2.7
'''
Created on Nov 14, 2014

@author: prasanna
@about: calculates the turn-based product for the game. It takes
the robot agent and environment agent semi-automata as inputs and combines
them into a single turn-based product.
'''

import sys
sys.path.append("../gui")
sys.path.append("../fsa") 

import cpsFsmIndividual
from cpsFsmState import fsmState
from FSA import FSA
import numpy as np
import time
import cPickle as pickle
import cpsFsmLabelFunctions
import itertools
from copy import deepcopy
from cpsFsmProductAutomaton import fsmProductAutomaton

class fsmTurnProduct(object):
    '''
    Implements turn based product for semi-automata
    '''    

    def __init__(self, agents, arenaDimensions=[2,2], 
                    drawTransitionGraph = False, 
                    labelFunction = cpsFsmLabelFunctions.gameLabelFunction):
        '''
        Constructor
        '''
        # Verify if inputs are good (sanity check)
        assert self.validateInputs(agents, arenaDimensions)
        
        self.labelFunction = labelFunction #Labeling function
        
        # Input data
        self.agents = agents
        self.arenaDimensions = arenaDimensions
                                
        # Number of agents
        self.numAgents = len(agents) 
        
        # Names of agents
        self.agentNames = [agents[i].agentName for i in range(self.numAgents)]  
        
        # States of all agents
        self.agentStates = [agents[i].states.copy() for i in range(self.numAgents)]
        
        # Proposition Names of all agent
        # self.agentPropositionNames = [agents[i].propositionNames for i in range(self.numAgents)]
        
        # Agent alphabets
        self.agentAlphabet = [agents[i].alphabetList for i in range(self.numAgents)]            
        
        # Agent last updated alphabet list
        self.agentPrevAlphabet = [set([]) for i in range(self.numAgents)]
        
        # Transitions from product of transition graph and grammar
        self.prevProdTransitions = set()
        
        # Create product automaton object
        self.prodAutomaton = fsmProductAutomaton()

        
        #Insert dummy states for each agent
        #self.insertDummyStates() 
        
        #All propositions in game
        #self.gamePropositionNames = []
        #for i in range(self.numAgents):
        #    self.gamePropositionNames.extend(self.agentPropositionNames[i])
        #self.gamePropositionNames = set(self.gamePropositionNames)
        
        #All alphabets in game
        self.gameAlphabet = set([])
        for i in range(self.numAgents):
            self.gameAlphabet.update(self.agentAlphabet[i])

        #State space size sanity check
        self.totalStates = (np.prod(arenaDimensions)**self.numAgents)*self.numAgents    #Total number of states
        self.maxTotalStates = 500000  #Maximum allowed states

        # Checking if state space size is too big
        # print "Number of states: ", arenaDimensions,"Total",self.totalStates, "Max allowed", self.maxTotalStates
        if self.totalStates>self.maxTotalStates:
            sys.stderr.write("Turn product state space cardinality greater than %d, allowed maximum limit %d\n" % self.totalStates, self.maxTotalStates)
            sys.stderr.write("Exiting function")
            sys.exit()             
        
        #All game states    
        self.gameStates = {}    #Game states, combining all agent states
        self.generateGameStates()   #Generate states of the game
        
        #FSA transition table
        self.fsaTransitions = []
        
        #Current transition graph
        _ , _, self.fsaTransitions, _=self.getFSA()

        #FSA
        if drawTransitionGraph:
            self.testFSA()
                    
        return
    
    def validateInputs(self, agents, arenaDimensions):
        '''
        Sanity check to see if the arena dimension is consistent
        in all the input agent semi-automata
        '''        
        for ag in agents:
            if ag.arenaDimensions != arenaDimensions:
                return False
        return True
    
    def insertDummyStates(self, agentStates=None, agentNames=None, numSuffixDigits=2):
        '''
        Inserts dummy states as place holders (not used in this implementation)
        '''
        if agentStates==None:   agentStates=self.agentStates
        if agentNames==None:   agentNames=self.agentNames
        for i in range(self.numAgents):
            dummyState = agentNames[i]+'o'*numSuffixDigits
            userID = [agentNames[i], None, None]
            machineID = self.agents[i].generateMachineID(userID)
            agentStates[i][dummyState]=fsmState(userID, machineID, 
                                              self.agentPropositionNames[i], self.arenaDimensions)
        return
    
    def generateGameStates(self):
        '''
        Generate game states
        '''
        agentStateKeys = [ag.keys() for ag in self.agentStates]
        
        for agS in itertools.product(self.agentNames, *agentStateKeys):
            #Creating game state
            
            # Getting list of agent positions
            agentPos = []
            for i in agS[1:]:
                agentPos.extend(i.split('_'))
            
            # Getting agent whose move it is                    
            agentTurn = agS[0]
                    
            userID = agentPos + ['T',agentTurn]            
            machineID = self.generateMachineID(userID)
            self.gameStates[machineID]=fsmState(userID, machineID,
                                                self.arenaDimensions,
                                                isInitial=True)
        return
                    
    def generateStateLabels(self, machineID, agLabelInitList):
        '''
        Generate state labels
        '''
        userID = self.gameStates[machineID].userID
        
        # Generate machine ID
        agMachineID = [None]*self.numAgents
        for ag in xrange(self.numAgents):
            agMachineID[ag] = self.agents[ag].generateMachineID(userID[ag*2 : ag*2+2])
                    
        # Propositions of both agents
        prop = [None]*self.numAgents
        for ag in xrange(self.numAgents):
            prop[ag] = self.agents[ag].generateStateLabels(agMachineID[ag], agLabelInitList[ag])

        # Get the interation propositions
        interactProp = self.labelFunction(self, machineID, prop) 
        
        # List of proposition names
        propNames = []        
        for i in xrange(self.numAgents):
            propNames.extend(prop[i].propositionList.keys())
        propNames = propNames +interactProp.propositionList.keys()
                    
        statePropositionList = self.gameStates[machineID].generateStatePropositionGrid(propNames)
        
        # Merging the propositions of both agents into turn-product
        propList = [propi.propositionList for propi in prop]
        statePropositionList.mergePropositionGrids(propList)
        
        # Add the interation propositions
        statePropositionList.mergePropositionGrids([interactProp.propositionList])                             
        
        return statePropositionList

    def testFSA(self):
        '''
        Used to generate an fsa and display transition graph
        '''
        fsaStates = self.gameStates.keys()
        #print fsaStates
        fsaAlphabet = list(self.gameAlphabet)
        
        fsaInitialState = fsaStates[0]
        fsaFinalStates = fsaStates[-1]
        
        if not(fsaInitialState in fsaStates) or not(fsaFinalStates in fsaStates):
            sys.stderr.write("Initial of final state not in state space")
            sys.stderr.write("Exiting function")
            sys.exit()
     
        #fsaInitialState = self.gameStates.keys()[4]
        #fsaFinalStates = self.gameStates.keys()[7]
        
        fsaTransitions = self.transitionTableGenerator()
        myFsa = FSA(fsaStates, fsaAlphabet, fsaTransitions,
                    fsaInitialState, [fsaFinalStates])
        myFsa.view()
        return fsaStates, fsaAlphabet, fsaTransitions
    
    def getFSA(self):
        '''Returns the components of the FSA at current status of learning'''
        fsaStates = self.gameStates.keys()
        fsaAlphabet = list(self.gameAlphabet)
        fsaTransitions, newTransitions = self.transitionTableGenerator()
        self.agentPrevAlphabet = [self.agents[i].alphabetList.copy() for i in range(self.numAgents)]
        return fsaStates, fsaAlphabet, fsaTransitions, newTransitions        

    def transitionTableGenerator(self): 
        '''
        Generate all transitions from states
        '''   
        fsaTransitions = deepcopy(self.fsaTransitions)
        newTransitions = []     
        for key in self.gameStates.keys():
            for i in self.getCurrentAlphabet(key):
                currTransition = self.transitionGenerator(key, i)
                if currTransition != None:
                    fsaTransitions.append(currTransition)
                    newTransitions.append(currTransition)
                    #print currTransition
                    
        self.fsaTransitions = deepcopy(fsaTransitions)
        return fsaTransitions, newTransitions
    
    def transitionGenerator(self, machineID, actionID):
        '''
        Generate transition for a specific state and action
        '''
        userID = self.gameStates[machineID].userID
        #print userID
        
        agentName = userID[-1]
        agentIndex = self.agentNames.index(agentName)
        agentAlphabet = set(self.agentAlphabet[agentIndex])
        
        agentUserIDIndex = userID.index(agentName)
        agentPos = userID[agentUserIDIndex+1:agentUserIDIndex+2]
        agentUserID = [agentName]
        agentUserID.extend(agentPos)

        nextAgentName = self.agentNames[(agentIndex+1) % len(self.agentNames)]
        
        if actionID in agentAlphabet:
            #print agentUserID, actionID
            outPos = self.agents[agentIndex].actionObj.actionResult(actionID,agentUserID)
            if outPos != None:
                outState = [agentUserID[0]]+[outPos]
            else:
                outState = None
        else:
            outState = None
            
        if outState != None:
            outStateID = userID[:]
            outStateID[agentUserIDIndex:agentUserIDIndex+2]=outState
            outStateID[-1] = nextAgentName
            #print agentUserID, actionID, outStateID
            
            outStateMachineID = self.generateMachineID(outStateID)
            return([machineID, outStateMachineID, actionID])
        else:
            return None
    
    def generatePossibleTransitionStates(self, currStateID):
        '''Generates the list of states the automaton can transition to 
        from the current state'''
        
        possibleTransitionStates = []
        for i in self.getCurrentAlphabet(currStateID):
            currTransition = self.transitionGenerator(currStateID, i)
            if currTransition != None:
                possibleTransitionStates.append(currTransition)
        return possibleTransitionStates
    
    def getActionFromTransitionStates(self, startStateID, endStateID):
        '''Compute the action that resulted in a specific transition'''
        possibleActions = []
        for i in self.getCurrentAlphabet(startStateID):
            currTransition = self.transitionGenerator(startStateID, i)
            if currTransition != None and currTransition[1]==endStateID:
                possibleActions.append(currTransition[2])
        return possibleActions       
            
    def generateMachineID(self, userID):
        '''
        Generate a unique machineID string for each state
        '''
        return "_".join(map(str, userID))
        
    def getCurrentAlphabet(self, machineID):
        '''Get the list of alphabets based on who's turn it is'''
        turn = self.gameStates[machineID].userID[-1]
        for ag in range(self.numAgents):
            if self.agentNames[ag] == turn:
                return self.agentAlphabet[ag].difference(self.agentPrevAlphabet[ag])
        
        # If turn name does not match agent list
        sys.stderr.write("Agent name not found: %s\n" % turn)
        sys.stderr.write("Exiting function")
        sys.exit()
        return
    
    def getAgentIndex(self, agentName):
        '''Get the index of the agent from the name'''
        for ag in range(self.numAgents):
            if self.agentNames[ag] == agentName:
                return ag

        # If turn name does not match agent list
        sys.stderr.write("Agent name not found: %s\n" % agentName)
        sys.stderr.write("Exiting function")
        sys.exit()
        return
    
    def addActionToAgent(self, agentName, gridSq1, gridSq2, addAction=True):
        ''' This function finds if there is a viable action that
        can result in the given agent (agent name) moving from gridSquare1 (gridSq1)
        to gridSq2. If the addAction flag is set as true, the action gets added to the
        given agent's alphabet (dynamics). If the agent's alphabet already contains the
        action, it is ignored. If the addAction flag is set as false, the function checks 
        the current action is a part of the agent alphabet. If it is not a part of the agent
        alphabet and when the addAction flag is false, the function returns a false. The 
        function also returns false when the action is not viable (i.e not a part
        of action library or is outside the grid limits.'''
        
        agentIndex = self.getAgentIndex(agentName)
        actionID = self.agents[agentIndex].actionObj.getActionID(gridSq1,gridSq2)
        if actionID != None:
            if addAction:
                self.agents[agentIndex].alphabetList.update([actionID])
                self.agentAlphabet[agentIndex].update([actionID])
                self.gameAlphabet.update([actionID])
                self.agents[agentIndex].addToAgentWord(actionID)
                return True
            else:
                if actionID in self.agentAlphabet[agentIndex]:
                    self.agents[agentIndex].addToAgentWord(actionID)
                    return True
                else:
                    return False
        else:
            return False
        
    def addAgentActions(self, agentName, actionList):
        ''' Add given set of actions to agent dynamics'''
        
        agentIndex = self.getAgentIndex(agentName)
        viableActions = self.agents[agentIndex].actionObj.filterViableActions(actionList)
        self.agents[agentIndex].alphabetList.update(viableActions)
        self.agentAlphabet[agentIndex].update(viableActions)
        self.gameAlphabet.update(viableActions)  
        return        
    
    def getTransitionAction(self, st1, st2):
        '''Returns the action that causes transition between two states
        Transition: st1 --> st2'''
        
        # Find whose turn it is in the states
        turn1 = self.gameStates[st1].userID[-1]
        turn2 = self.gameStates[st2].userID[-1]
        
        # Find the IDs of agents making the turns
        turnID1 = self.agentNames.index(turn1)
        turnID2 = self.agentNames.index(turn2)   
        
        if not (turnID1+1) % self.numAgents == turnID2:
            print "Cannot get transition action, the input states turns do not match (%s, %s)" %(st1, st2)
            return None
        
        # Get the index of the agent with turn in userID
        agID = self.gameStates[st1].userID.index(turn1)
        
        # Check if rest of the userID is compatible
        temp = self.gameStates[st1].userID[:]
        temp[-1] = turn2
        temp[agID+1] = self.gameStates[st2].userID[agID+1]
        
        if not temp == self.gameStates[st2].userID:
            print "No transition available between states (%s, %s)" % (st1, st2)
            return None
                
        agPos1 = map(int,list(self.gameStates[st1].userID[agID+1]))
        agPos2 = map(int,list(self.gameStates[st2].userID[agID+1]))
                
        return self.agents[turnID1].actionObj.getActionID(agPos1, agPos2)  
    
    def computeGrammarProduct(self): 
        '''Get the product automaton of grammar and transition graph'''
        
        # Get fsa parameters
        _ , _, self.fsaTransitions, _ = self.getFSA()
        gameTransitions = set([tuple(i) for i in self.fsaTransitions])
        
        # Get adversary ID
        for i in xrange(self.numAgents):
            if self.agents[i].agentType == 'UNKNOWN':
                agentID = i
                break
            
        # Get adversary parameters
        advGrammarObj = self.agents[agentID].grammarObj
        advAlphabet = self.agentAlphabet[agentID] 
        advName = self.agents[agentID].agentName
            
        # Update product automaton and get product transitions
        prodStates, prodTransitions = self.prodAutomaton.computeFsaProductTransitions(self.gameStates, gameTransitions, advGrammarObj, 
                                                                          advAlphabet, advName)                
        
        # Get the new transitions
        newTransitions = prodTransitions.difference(self.prevProdTransitions)
        
        self.prevProdTransitions = prodTransitions
        return prodStates, prodTransitions, newTransitions

'''Unit Test'''
if __name__=="__main__":
    start_time = time.time()
    arenaDimensions = [3,3] #Grid dimensions (x-dir,y-dir) or (col, row)
    numRobots = 2
    
    ##################### Creating robot agent #######################################################
    #
    # arenaDimensions: size of arena (x-dir cells, y-dir-cells)
    # arenaDimensions should be consistent for all agents and the turn-based product
    # of the game. Turn-based product verifies this and throws an error if there is a mismatch.
    # 
    # robotLabelFuction: User-defined label function for the robot agent. For more documentation on label
    # functions and to see the default robot and env agent label functions, refer to the module
    # cpsFsmLabelFunctions.py
    #
    # agentAlphabetInput: Prior knowledge on the dynamics of the agent or in other words
    # the agent alphabet. This should be a subset of the action library (contains 26 actions) connected
    # with the agent. To see more details about the action library, see the documentation of
    # the module cpsFsmActions.py
    #
    # syntax: agentAlphabetInput=[['dir1',min_step1, max_step1], ['dir2',min_step2, max_step2], ...]
    # e.g. agentAlphabetInput=[['n',1,3], ['e',1,1]]
    #
    # This example implies that the agent can move in the north direction a minimum of 1 square
    # and a maximum of 3 squares, and it can also move 1 square in the east direction.
    # All possible actions here are (N1, N2, N3, E1)
    #
    # For the robot agent we fix its dynamics as
    # agentAlphabetInput=[['n',1,1],['s',1,1],['e',1,1],['w',1,1],['o',0,0]]
    # 
    # i.e. 1 square in each direction and also stay in place.
    #
    # For more information about the module used to create individual agent objects
    # refer to the source in module cpsFsmIndivual.py
    ###################################################################################################
    
    robotList = []
    for i in xrange(numRobots):
        robotList.append( cpsFsmIndividual.fsmIndiv(arenaDimensions, cpsFsmLabelFunctions.robotLabelFuction,
                                                    agentName= 'R'+str(i),
                                                    agentAlphabetInput=[['oo',0,0]]))
    
    #[['nn',1,1],['ss',1,1],['ee',1,1],['ww',1,1],['oo',0,0]]
    
    ############################# Creating environment agent ##########################################
    # This is similar to creating the robot agent. By default we leave the env agent dynamics or env 
    # agent alphabet here as empty as we do not know anything about the env agent.
    ###################################################################################################
    
    env = cpsFsmIndividual.fsmIndiv(arenaDimensions, cpsFsmLabelFunctions.envLabelFuction,
                                    agentName='E0',
                                    agentAlphabetInput=[])
    
    ########################### Creating turn-based product for the game ###############################
    # The turn-based product takes the semi-automata of robot agent and environment agent as inputs
    # 
    # drawTransitionGraph: if this flag is set as true, a transition graph is drawn.
    # This is not advisable if the number of states is too large
    #
    # The source in this module (cpsFsmTurnProduct.py) handles the creation of turn-based product
    ####################################################################################################
    
    gameProduct = fsmTurnProduct([env]+robotList, arenaDimensions, drawTransitionGraph=False)
    
    ########################### Getting the parameters of the game automaton ##########################
    # The module cpsFsmLoadGameAutomaton.py which reads a saved file from the GUI
    # interface primariy uses the function (as below) to get the automatom parameters
    #
    # gameStates, gameAlphabet, gameTransitions = gameProduct.getFSA()
    ####################################################################################################
    
    gameStates, gameAlphabet, gameTransitions, newTransitions = gameProduct.getFSA()
    
    ########################### Adding actions to agents ###############################################
    # Lets say that we want to add actions to the environment agent without using the GUI.
    # The function below does it (in fact this is how the GUI interacts with the back-end code.
    # 
    # syntax: gameProduct.addActionToAgent(agentName, gridSq1, gridSq2, addAction=True)
    # 
    # The addActionToAgent function finds if there is a viable action that
    # can result in the given agent (agent name) moving from gridSquare1 (gridSq1)
    # to gridSq2. If the addAction flag is set as true, the action gets added to the
    # given agent's alphabet (dynamics). If the agent's alphabet already contains the
    # action, it is ignored. If the addAction flag is set as false, the function checks 
    # the current action is a part of the agent alphabet. If it is not a part of the agent
    # alphabet and when the addAction flag is false, the function returns a false. The 
    # function also returns false when the action is not viable (i.e not a part
    # of action library or is outside the grid limits.
    # 
    # addAction flag: default true
    # For robot agent set as false (we do not want the robot dynamics to change during the game)
    # For env agent set as true (we need to iteratively learn the env dynamics during the game) 
    # 
    # e.g. usage gameProduct.addActionToAgent('E', [1,1], [1,0], addAction=True)
    #
    # This means that the env agent ('E') moves from square (1,1) to (1,0). This is going to result
    # in action S1. So the env alphabet will be updated with S1.
    #
    # This function only verifies if the given move is viable, the function does not remember the history of
    # the game. This function does not verify if the last known position of an agent is same as
    # the starting position of the current move. This allows moves to be entered in any order and
    # not necessarily in a specific viable sequence. 
    #####################################################################################################       
    
    gameProduct.addActionToAgent('E0', [1,1], [1,0], addAction=True)
    gameProduct.addAgentActions('E0', ['nn1','ee1'])
    
    ######################## Getting the game automaton parameters after adding an action ###############
    # The same getFSA() function can be used to get the automaton parameters as before.
    #####################################################################################################
    
    gameStates, gameAlphabet, gameTransitions, newTransitions = gameProduct.getFSA()
    
    ########################## Generating State Labels ##################################################
    # Any point in the game, the labels or propositions can be generated with a given input game state 
    # using the function below.
    #
    # Syntax: propositionList = gameProduct.generateStateLabels(stateID)
    #
    # e.g. usage propositionList = gameProduct.generateStateLabels('R00E11TR')
    #
    # For more information on label function of robot and env refer to the module cpsFsmLabelFunctions.py
    #
    # The generateStateLabels function first generates the state labels for both robot and env separately
    # using their respective label functions. Then these labels/propositions are merged together. All
    # functions connected with handling proposition datastructures can be found in module
    # cpsFsmProposition.py. The function that specifically does the merging of the propositions
    # is called mergePropositionGrids.
    #
    # The merge function assigns all the propositions coming down from each agent to the game. If there
    # is a conflict in a proposition value between the two agents, the proposition is saved as true.
    #
    # The output value propositionList is a dictionary datastructure where the dictionary keys correspond
    # to the names of the propositions and the values connected with the dictionary are the linear indices
    # of the grid squares where the proposition is true (linearization of grid squares from 2D to 1D is
    # done through row-major rule). If the proposition is not explicity specified as true, it is considered
    # by default as false. 
    #
    # The cpsFsmLoadGameAutomaton provides an example for the proposition datastructure and explains
    # how to read it.
    #####################################################################################################
    
    #propList = gameProduct.generateStateLabels('R00E11TR')
    
    finishTime = time.time() - start_time
    print "Code execution time :", finishTime
    
#     pickle.dump(gameProduct, open("tempPickle.p","wb"))
#     newGameProduct = pickle.load( open( "tempPickle.p", "rb" ) )
#     print newGameProduct.arenaDimensions

    # Tests for getTransitionAction(st1, st2)
    st1 = 'E0_22_R0_00_R1_10_T_R0'
    st2 = 'E0_22_R0_11_R1_10_T_R1'
    print gameProduct.getTransitionAction(st1, st2)
    
    
    