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
        else:
            gamePolicy = self.gtsNonMatlabPolicyGenerator(gameProduct, gameStateLabels, initState, numEnv)
            
        return gamePolicy

    def gtsPolicyUpdater(self, gameProduct, gamePolicy, stateHistory, numAgents, 
                            numEnv, lastAction, currState):

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
        else:
            gamePolicy = self.gtsNonMatlabPolicyUpdater(gameProduct, numEnv, lastAction, currState)
            
        return gamePolicy
    
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
    
    def policyActionToState(self, actionPolicy, gameProduct, numEnv):
        '''Convert action policy to policy with end states'''
        
        statePolicy = {}
        for currState in actionPolicy.keys():
            agName = gameProduct.gameStates[currState].userID[-1]
            agIndex = gameProduct.agentNames.index(agName)
            
            if actionPolicy[currState] and actionPolicy[currState] in gameProduct.agents[agIndex].alphabetList:
                agPos = [map(int, list(gameProduct.gameStates[currState].userID[i*2+1])) for i in xrange(gameProduct.numAgents)]
                agentUserID = [agName]
                agentUserID.extend([agPos[agIndex]])
                endGridSq = map(int, list(gameProduct.agents[agIndex].actionObj.actionResult(actionPolicy[currState], agentUserID)))
                agPos[agIndex] = endGridSq
                statePolicy[currState] = self.getMachineID(agPos, agIndex, gameProduct)
            else:
                statePolicy[currState] = None
                
        return statePolicy

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
        
        # Get the game parameters
        gameStates, prodTransitions, newTransitions = gameProduct.computeGrammarProduct()

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

        # Create GTS
        # For more details, see the synthesis.py
        # Details on WeightedTransitionSystems can be found in GraphicalModels.py
        self.GTS = WeightedTransitionSystem()
        self.GTS.TSfromGame(gameStates, prodTransitions, gameStateLabels)
        
        # Now take product
        self.P = ProductBuchi()
        self.P.fromBAndTS(self.buchi, self.GTS, initState)
        
        # dijkStart = time.clock()
        # This is the same as findEnergyGame from matlab
        self.dist, self.FStar = self.P.findEnergyGame(gameProduct)
        # dijkTime = time.clock() -dijkStart
        
        #######################################################################################
        
        actionPolicy = self.P.policyDict(self.dist)
        gamePolicy = self.policyActionToState(actionPolicy, gameProduct, numEnv)
        return gamePolicy
    
#         gamePolicy
#         for state in self.P.currentStates:
#             self.policyAction = self.matlabObj.P.getAction(self.matlabObj.dist, state)

        
    def gtsNonMatlabPolicyUpdater(self, gameProduct, numEnv, lastAction, currState):
        '''Generating GTS directly from python without matlab
        This is only used to incremental update the policy and does not initialize Buchi
        For initialization see function gtsNonMatlabPolicyGenerator'''
        
        # Get the game parameters
        gameStates, prodTransitions, newTransitions = gameProduct.computeGrammarProduct()
        
        # Check if the GTS is initialized before it is incrementally updated
        assert (hasattr(self, 'GTS') and hasattr(self,'buchi') and hasattr(self,'P')), "Trying to update GTS before initialization" 

        ######################## KEVIN EDIT NEEDED ###########################################
        
        #Finally, update GTS and product
        # To get new policy, findEnergyGame needs to be run again
        self.GTS.incrTrans(newTransitions)
        self.P.incrProd( newTransitions, self.buchi, self.GTS)
        self.dist, self.FStar = self.P.findEnergyGame(gameProduct)
        self.P.input(lastAction) 
        
        #######################################################################################
        
        actionPolicy = self.P.policyDict(self.dist)
        gamePolicy = self.policyActionToState(actionPolicy, gameProduct, numEnv)
        return gamePolicy
         
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
        