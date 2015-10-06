'''
Created on Apr 2, 2015

@author: prasanna
'''

import sys
from copy import deepcopy
sys.path.append("../src")
sys.path.append("../fsa") 
sys.path.append("../matlab_integ") 

from cpsFsmTurnProduct import fsmTurnProduct
from cpsFsmIndividual import fsmIndiv
from cpsFsmLabelFunctions import *
import cPickle as pickle
from FSA import FSA
from scipy import io
import matlab.engine
import matlab
import StringIO
import numpy as np
import os
from Automata import *
from cpsFsmFsa import traverseTransitions


class matlabLinker(object):
    '''Function to facilitate linking with matlab'''
    
    def __init__(self, useMatlab=False):
        '''Constructor'''
        self.useMatlab = useMatlab
    
    def initializeMatlab(self, wsDir, matlabPaths=[]):
        if self.useMatlab:
            self.wsDir = wsDir
            self.matlabEng = matlab.engine.start_matlab()    
            self.matlabOut = StringIO.StringIO()
            self.matlabErr = StringIO.StringIO()
            
            for i in matlabPaths:
                self.matlabEng.addpath(i,nargout=0)
        
    def initializeGame (self):
        '''Initialize game parameters and objects'''
        arenaDimensions = [4,4]
        
        # Creating robot agent semi-automata
        self.robot = fsmIndiv(arenaDimensions, robotLabelFuction,
                         agentName= 'R',
                         agentAlphabetInput=[['nn',1,1],['ss',1,1],['ee',1,1],['ww',1,1],['oo',0,0]])
        
        # Creating env agent semi-automata
        self.env = fsmIndiv(arenaDimensions, envLabelFuction,
                         agentName='E',
                         agentAlphabetInput=[])
        
        # Generating turn-based product
        self.gameProduct = fsmTurnProduct([self.robot,self.env], arenaDimensions, 
                                          drawTransitionGraph=False, labelFunction=gameLabelFunction)
        
        # Specifying environment dynamics
        self.gameProduct.addAgentActions('E', ['oo0'])
        
        # Getting transition system parameters
        self.gameStates, self.gameAlphabet, self.gameTransitions, self.newTransitions = self.gameProduct.getFSA()
        
        # Getting labels of all states
        self.gameStateLabels = {}
        for stateID in self.gameProduct.gameStates.keys(): 
            self.gameStateLabels[stateID] = self.gameProduct.generateStateLabels(stateID).propositionList
        return
    
    def saveToDisk(self):
        # gameAutomaton = pickle.load( open( "gameAutomaton.p", "rb" ) )
        # gameStates, gameAlphabet, gameTransitions = gameAutomaton.getFSA()    
        # gameStateLabels = pickle.load( open( "gameLabels.p", "rb" ) )

        # Saving files to disk
        pickle.dump(self.gameProduct, open("gameAutomaton.p","wb"))
        pickle.dump(self.gameStateLabels, open("gameLabels.p","wb"))
        
        # Saving as mat files 
        io.savemat('gameAlphabet.mat',mdict={'gameAlph':self.gameAlphabet})
        io.savemat('gameStates.mat',mdict={'gameStates':self.gameStates})
        io.savemat('gameTransitions.mat',mdict={'gameTrans':self.gameTransitions})  
        io.savemat('gameStateLabels.mat',mdict={'gameLabels':self.gameStateLabels})
        return  
    
    def convertLabels(self, inLabels):
        convLabels = [] 
        for stateID in inLabels.keys():
            convLabels.append([stateID,'p1',matlab.int64(inLabels[stateID]['p1'][:])])
            convLabels.append([stateID,'p2',matlab.int64(inLabels[stateID]['p2'][:])])
            convLabels.append([stateID,'p3',matlab.int64(inLabels[stateID]['p3'][:])])
            convLabels.append([stateID,'p4',matlab.int64(inLabels[stateID]['p4'][:])])
        return convLabels 
    
    def gtsPolicyGenerator(self, gameProduct, gameStateLabels, initState, numAgents, numEnv):
        '''Generates robot policy with or without using matlab
        This only initializes the policy the the first time. It does not do incremental update'''
                
        if self.useMatlab:

            # Get FSA parameters
            gameStates, gameAlphabet, gameTransitions, _ = gameProduct.getFSA()
            
            convLabels = self.convertLabels(gameStateLabels)
            gameTransitionsNum = self.convertGameTransitions(gameStates, gameTransitions)
            
            gamePolicy = self.matlabEng.gameInteg(gameAlphabet, gameStates, 
                                                  gameTransitionsNum, convLabels, [initState], self.wsDir, numAgents, 
                                                  stdout=self.matlabOut,stderr=self.matlabErr, nargout=1)
            return gamePolicy
        else:
            gamePolicy, currProdState = self.gtsNonMatlabPolicyGenerator(gameProduct, gameStateLabels, initState, numEnv)
            
            return gamePolicy, currProdState

    def gtsPolicyUpdater(self, gameProduct, gameStateLabels, gamePolicy, stateHistory, numAgents, 
                            numEnv, lastAction, currState, initState):

        # Specifying environment dynamics
        # self.gameProduct.addAgentActions('E', ['n1'])        
        if self.useMatlab:
            # Getting transition system parameters
            gameStates, _, _, newTransitions = gameProduct.getFSA()  

            stateHistory = [str(i) for i in stateHistory]
            if newTransitions:
                newTransitionsNum = self.convertGameTransitions(gameStates, newTransitions)
                gamePolicy = self.matlabEng.gameUpdateInteg(self.wsDir, stateHistory, numAgents,
                                                            newTransitionsNum, 
                                                            stdout=self.matlabOut,
                                                            stderr=self.matlabErr, nargout=1)
            else:
                gamePolicy = self.matlabEng.gameUpdateInteg(self.wsDir, stateHistory,
                                                            stdout=self.matlabOut,
                                                            stderr=self.matlabErr, nargout=1)
            return gamePolicy
        else:
            gamePolicy, currProdState = self.gtsNonMatlabPolicyUpdater(gameProduct, gameStateLabels, numEnv, lastAction, 
                                                                       currState, initState,stateHistory)
            
            return gamePolicy, currProdState
    
    def convertGameTransitions(self, gameStates, gameTransitions):
        gameTransNum = []
        for tr in gameTransitions:
            source = gameStates.index(tr[0])+1
            dest = gameStates.index(tr[1])+1
            gameTransNum.append([source, dest])
            
        return gameTransNum
                 
    def policyConverter(self, inPolicy):
        outPolicy = {}
        for key in inPolicy.keys():
            if inPolicy[key] != 0:
                outPolicy[key[:-1]] = inPolicy[key][:-1]
            else:
                outPolicy[key[:-1]] = 0
        return outPolicy    
    
    def policyActionToState(self, actionPolicy, prodTransitions):
        '''Convert action policy to policy with end states'''
        
        statePolicy = {}
        for key in actionPolicy.keys():
            if actionPolicy[key] and actionPolicy[key] is not 'xx0':
                statePolicy[key] = traverseTransitions(key, [actionPolicy[key]], prodTransitions)
            else:
                # print 'key:',key
                statePolicy[key] = None
        return statePolicy

#     def policyActionToState(self, actionPolicy, gameProduct, numEnv, stateNonGrammarInd = 1):
#         '''Convert action policy to policy with end states'''
#         
#         statePolicy = {}
#
#         for key in actionPolicy.keys():
#             currState = key[stateNonGrammarInd]
#             
#             # Sanity check
#             assert currState in gameProduct.gameStates.keys(), "Invalid state key in policy"                
#                 
#             agName = gameProduct.gameStates[currState].userID[-1]
#             agIndex = gameProduct.agentNames.index(agName)
#             
#             if actionPolicy[key] and actionPolicy[key] in gameProduct.agents[agIndex].alphabetList:
#                 agPos = [map(int, list(gameProduct.gameStates[currState].userID[i*2+1])) for i in xrange(gameProduct.numAgents)]
#                 agentUserID = [agName]
#                 agentUserID.extend([agPos[agIndex]])
#                 endGridSq = map(int, list(gameProduct.agents[agIndex].actionObj.actionResult(actionPolicy[key], agentUserID)))
#                 agPos[agIndex] = endGridSq
#                 targetState = self.getMachineID(agPos, agIndex, gameProduct)
#                 
# #                 if statePolicy.has_key(currState) and statePolicy[currState] and \
# #                     targetState and statePolicy[currState] != targetState:
# #                     print "Prev policy: ", currState, " -> ", statePolicy[currState]
# #                     print "Curr policy: ", currState, " -> ", targetState
# #                     raise "State policy for different grammar elements not matching"
# #                 else:
# #                     statePolicy[currState] = targetState
#                 statePolicy[key] = targetState
#             else:
#                 statePolicy[key] = None

    def getMachineID(self, agentPos, agentIndex, gameProduct):
        userID = []
        for ag in xrange(gameProduct.numAgents):            
            agPosStr = ''.join(map(str,agentPos[ag]))
            userID.extend([gameProduct.agentNames[ag], agPosStr])
        
        nextAgent = (agentIndex+1) % gameProduct.numAgents
        userID.extend(['T', gameProduct.agentNames[nextAgent]])
                     
        return gameProduct.generateMachineID(userID)            
    
    def gtsNonMatlabPolicyGenerator(self, gameProduct, gameStateLabels, initState, numEnv):
        '''Generating GTS directly from python without matlab
        This is only used to initialize the policy and does not perform incremental update'''
        
        # print gameStateLabels.keys()

        # Get the game parameters
        gameStates, prodTransitions, _, currProdState, _ = gameProduct.computeGrammarProduct(initState, initState,
                                                                                          performStateTrace = True)
        
        # Sanity checks
        self.sanityChecksForStatesAndTransitions((gameStates)+[currProdState], prodTransitions)             

        # prodTransitions contains the transitions in form of a set. each element of the set is a
        # tuple with three elements
        #
        # Each element is of the form (startState, endState, action)
        # Start state and end state are again tuples
        # Start (end) state example: (1, E0_00_R0_11_R1_22_T_E0)
        # 
        # The first element of the state tuple is a number. The second element is the state name based on the previously
        # used convention. I had to do a product of two automatons. That is why the states are now inform of tuples.
        #
        # newTransitions is a subset of prodTransitions. It only contains transitions that were
        # obtained during the last update. This can be used for incremental update purposes.
        
        ######################## KEVIN EDIT NEEDED ###########################################
        
        # Get Buchi Automaton from specification:
        # [] <> p1 && [] <> p2 && [] ! p3
        # other specifications can be accomodated when we need them
        # This process can be updated to automatically generate a buchi from a new specificaiton, but the required
        # process has a lot of dependencies, so for now, we will just read in a buchi from a file.
        # More information on BuchiAutomata can be found in Automata.py
        # self.buchi = BuchiAutomaton()
        # self.buchi.readStatement('../matlab_integ/learnSpec2') #read .dot file containing Buchi Automaton for specification
        self.buchi = pickle.load(open("../matlab_integ/buchiTest.p","rb"))
        # print 'accepting:',self.buchi.acceptingStates
        # Create GTS
        # For more details, see the synthesis.py
        # Details on WeightedTransitionSystems can be found in GraphicalModels.py
        self.GTS = WeightedTransitionSystem()
        self.GTS.TSfromGame(gameStates, prodTransitions, gameStateLabels)
        
        # Now take product
        self.P = ProductBuchi()
        self.P.fromBAndTS(self.buchi, self.GTS, currProdState)
        # print "INPUT LANGUAGE:",self.P.inputLanguage
        # print "Number of Accepting States:",len(self.P.acceptingStates)

        # dijkStart = time.clock()
        # This is the same as findEnergyGame from matlab
        self.dist, self.FStar = self.P.findEnergyGame(gameProduct)
        # dijkTime = time.clock() -dijkStart
        
        #######################################################################################
        
        actionPolicy = self.P.policyDict(self.dist)
        gamePolicy = self.policyActionToState(actionPolicy, prodTransitions)
        # gamePolicy = self.policyActionToState(actionPolicy, gameProduct, numEnv)
        return gamePolicy, currProdState
    
#         gamePolicy
#         for state in self.P.currentStates:
#             self.policyAction = self.matlabObj.P.getAction(self.matlabObj.dist, state)
        
    def gtsNonMatlabPolicyUpdater(self, gameProduct, gameStateLabels, numEnv, lastAction, currState, initState, stateHistory):
        '''Generating GTS directly from python without matlab
        This is only used to incremental update the policy and does not initialize Buchi
        For initialization see function gtsNonMatlabPolicyGenerator'''


        # Get the game parameters
        prodStates, prodTransitions, _, currProdState, transitionsUpdated = gameProduct.computeGrammarProduct(initState, currState, 
                                                                                                              performStateTrace = True)
        
        # Save transitions for verification
        # pickle.dump(prodTransitions, open("../transitions.p","wb"))
        
        # Sanity checks
        # self.sanityChecksForStatesAndTransitions(list(prodStates)+[currProdState], prodTransitions)     
                
        # Check if the GTS is initialized before it is incrementally updated
        assert (hasattr(self, 'GTS') and hasattr(self,'buchi') and hasattr(self,'P')), "Trying to update GTS before initialization" 

        ######################## KEVIN EDIT NEEDED ###########################################
        
        #Finally, update GTS and product
        # To get new policy, findEnergyGame needs to be run again
        # self.GTS.incrTrans(newTransitions)
        # self.P.incrProd( newTransitions, self.buchi, self.GTS)
        # self.dist, self.FStar = self.P.findEnergyGame(gameProduct)
        # self.P.input(lastAction) 

        # KEVIN CHANGES 2015-09-23
        # print "StateLog:",self.StateLog
        # print "State:",self.StateLog[-1]
        # print "Label",gameLabels[self.StateLog[-1]]

        label = '' 
        #PRASANNA_EDIT
        #Previously: props = gameLabels[state].propositionList
        props = gameStateLabels[stateHistory[-2]]
        # print props
        # print "state[1]:",state[1]
        for i in xrange(len(props)-1):
            if props['p'+str(i+1)] != []:
                if len(label) == 0:
                    label = 'p'+str(i+1)
                else:
                    label = label+'&p'+str(i+1)
        # If length of label is 0 then, highest proposition (null proposition) is true
        if len(label)==0:
            label = 'p'+str(len(props))

        # print 'Label:', label

        #Get current Buchi State from self.P
        for state in self.P.currentStates:
            self.BState = state[1]
        # print "Buchi State:",self.BState

        self.acceptBState = self.buchi.acceptingStates.intersection(self.buchi.checkSymbolOneState(label,self.BState))
        if self.acceptBState:
            self.nextBState = self.acceptBState
        else:
            maxS = 0
            for s in self.buchi.checkSymbolOneState(label,self.BState):
                if s >= maxS:
                    self.nextBState = s
                    maxS = s
            if not self.nextBState:
                self.nextBState = '0' #reset Buchi if no 'good' transition is available

        for x in self.nextBState:
            nextB = x

        # Create GTS
        # For more details, see the synthesis.py
        # Details on WeightedTransitionSystems can be found in GraphicalModels.py
        self.GTS = WeightedTransitionSystem()
        self.GTS.TSfromGame(prodStates, prodTransitions, gameStateLabels)
        
        # Now take product
        self.P = ProductBuchi()
        self.P.fromBAndTS(self.buchi, self.GTS, currProdState)
        
        # print 'P State Old:', self.P.currentStates
        for state in self.P.currentStates:
            self.P.currentStates = set([(state[0],nextB)])

        # print 'P State New:', self.P.currentStates
        # dijkStart = time.clock()
        # This is the same as findEnergyGame from matlab
        self.dist, self.FStar = self.P.findEnergyGame(gameProduct)
        # for state in self.P.currentStates:
        #     print "State:",state
        #     print "Dist:", self.dist[state]
        #######################################################################################
        # for key in self.dist.keys():
        #     if self.dist[key] != float('Inf'):
        #         print "state:",key
        #         print "dist:",self.dist[key]
        actionPolicy = self.P.policyDict(self.dist)
        # gamePolicy = self.policyActionToState(actionPolicy, gameProduct, numEnv)
        gamePolicy = self.policyActionToState(actionPolicy, prodTransitions)
        return gamePolicy, currProdState

    def sanityChecksForStatesAndTransitions(self, states = [], transitions = []):    
        '''Check if all states and transitions are of the right form'''
        for state in list(states):
            assert len(state[0]) < 3, "First component of state too long: %s" % (str(state))
            assert len(state[1]) == 22, "Second component of state not the right size: %s" % (str(state))
        for t in transitions:
            for state in t[:2]:
                assert len(state[0]) < 3, "First component of state too long: %s" % (str(t))
                assert len(state[1]) == 22, "Second component of state not the right size: %s" % (str(t))        
        return
             
    def destructor(self):
        self.matlabEng.quit() 
        return
    

if __name__ == '__main__':
    
    matlabObj = matlabLinker()
    
    # Creating the game without GUI
    matlabObj.initializeGame()

    # Initializing matlab engine
    wsDir = os.path.dirname(os.path.realpath(__file__))
    parentDir = os.path.dirname(wsDir)  
    matlabPaths = [str(parentDir+'/matlab_files'), str(parentDir+'/matlab_integ')]
    matlabObj.initializeMatlab(wsDir, matlabPaths)
 
    out = StringIO.StringIO()
    err = StringIO.StringIO()    
    tempAlphabet = ['nn1','ss1']
    tempState = [str('E0_00_R0_00_T_R'),str('E0_10_R0_00_T_R')]
    tempTrans = [['E0_00_R0_00_T_R0', 'E0_00_R0_00_T_E0', 'n1'], ['R10E00TR', 'R10E00TE', 'e1']]
    tempLabels = {}
    tempLabels['R00E00TR'] = matlabObj.gameProduct.generateStateLabels('R00E00TR').propositionList
    tempLabels['R00E01TR'] = matlabObj.gameProduct.generateStateLabels('R00E01TR').propositionList
    convLabels = matlabObj.convertLabels(tempLabels)
    matlabObj.matlabEng.matlabTest(tempState, stdout=out,stderr=err,nargout=0)    
    print out.getvalue()
    
    # Generate policy
    matlabObj.gamePolicy = matlabObj.gtsPolicyGenerator(matlabObj.gameAlphabet, matlabObj.gameStates, 
                                                        matlabObj.gameTransitions, matlabObj.gameStateLabels)

    # Generate policy
    matlabObj.gamePolicyUpdate = matlabObj.gtsPolicyUpdater(matlabObj.gamePolicy, matlabObj.newTransitions)
    
    # Saving to disk
    matlabObj.saveToDisk()
    
    # Closing matlab engine
    matlabObj.destructor()
        