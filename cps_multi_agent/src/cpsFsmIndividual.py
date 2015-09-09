'''
Created on Nov 12, 2014

@author: prasanna

Generates the Semi-automata of an individual agent 
'''

import sys
sys.path.append("../gui")
sys.path.append("../fsa") 

import numpy as np
from cpsFsmActions import fsmActions
from cpsFsmState import fsmState
from cpsFsmGrammar import fsmGrammar
from FSA import FSA
import cpsFsmLabelFunctions

class fsmIndiv(object):
    '''
    Agent class that contains the semi-automata for an individual agent
    '''
    def __init__(self, arenaDimensions=[2,2], 
                 labelFunction= cpsFsmLabelFunctions.robotLabelFuction,
                 initialPositions=[[0,0]],
                 goalPositions=[[1,1]],
                 agentName = 'robot',
                 agentAlphabetInput = [['nn',1,5],['ss',1,5],['ee',1,5],['ww',1,5],['oo',0,1],
                                       ['ne',1,5],['nw',1,5],['se',1,5],['sw',1,5]],
                 drawTransitionGraph = False,
                 grammarType = 'SL_1',
                 agentType = 'KNOWN'):
        '''
        Constructor
        '''
        self.arenaDimensions = arenaDimensions  #Grid dimensions
        self.labelFunction = labelFunction #Labeling function
        
        self.totalStates = np.prod(arenaDimensions)    #Total number of states
        self.maxTotalStates = 10000  #Maximum allowed states
        
        self.agentType = agentType #KNOWN or UNKNOWN dynamics
        
        # Checking if state size is too big
        # print "Number of states: ", arenaDimensions,"Total",self.totalStates
        if self.totalStates>self.maxTotalStates:
            sys.stderr.write("State space greater than %d" % self.totalStates)
            sys.stderr.write("Exiting function")
            sys.exit()             
        
        self.goalStates = [] #List of goal states
        self.initialStates = [] #List of initial states
        
        self.agentName = agentName #Name of agent
        
        self.actionObj = fsmActions(arenaDimensions) #Generate related action class objects
        
        self.grammarObj = fsmGrammar(grammarType) #Generate related grammar object
         
        self.alphabetList = self.actionObj.generateActionList(agentAlphabetInput) #List of alphabets
        
        self.states = {}  #List of states
        
        self.generateStates() #Initialize list of states 
        self.setInitialFinalStates(initialPositions, goalPositions) #Setting initial and final states  
        
        self.agentWord = []
        
        # initializing grammar of unknown agent
        if agentType == 'UNKNOWN' and len(self.alphabetList) != 1:
            raise "Unknown agent should be initialized with 1 action"
        elif agentType == 'UNKNOWN':
            self.addToAgentWord(list(self.alphabetList)[0])
        
        if drawTransitionGraph:
            self.testFSA()

        return
    
    def addToAgentWord(self, inAct):
        self.agentWord.append(inAct)
        
        # If unknown dynamics then update grammar
        if self.agentType == 'UNKNOWN':
            self.grammarObj.addMove(inAct)
            
        return
    
    def generateStates(self):
        '''
        Generate states of Agent Semi-automata
        '''
        for i in range(self.totalStates):
            agentPos = "".join(map(str, list(np.unravel_index(i,self.arenaDimensions))))
            userID = [self.agentName]+[agentPos]                            
            machineID = self.generateMachineID(userID)
            self.states[machineID] = fsmState(userID, machineID,
                                                    self.arenaDimensions)
        return
    
    def generateMachineID(self, stateUserID):
        '''
        Generate a unique machineID string for each state
        '''
        return stateUserID[0]+'_'+ "".join(map(str,stateUserID[1:]))
    
    def setInitialFinalStates(self, initialPositions, goalPositions):
        '''
        Assign labels to states initially and set goal states initially
        '''
        
        for key in self.states.keys():
                        
            #Get name of proposition 'occupied'
            #propName = self.propositionNames[0]
            agentPosition = self.states[key].userID[1:]
            
            #Assign 'occupied' to occupied cell
            #self.states[key].assignStatePropositionGrid(propName, agentPosition)
                                                 
            if agentPosition in goalPositions:
                self.states[key].setFinal()
                self.goalStates.append(key)
                
            if agentPosition in initialPositions:
                self.states[key].setInitial()
                self.initialStates.append(key)            
        return
    
    def generateStateLabels(self, machineID, labelInit = {}):
        return self.labelFunction(self, machineID, labelInit)

            
    def testFSA(self):
        '''
        Generate inputs required for Fsa
        '''
        fsaStates = list(self.states.keys())
        fsaAlphabet = self.alphabetList
        fsaInitialStates = self.initialStates
        fsaFinalStates = self.goalStates
        fsaTransitions = self.transitionTableGenerator()
        
        self.fsa = FSA(fsaStates, fsaAlphabet, fsaTransitions,
                             fsaInitialStates[0],  fsaFinalStates) #FSA processing
        self.fsa.view()
        return          
    
    def transitionTableGenerator(self): 
        '''
        Generate all transitions from states
        '''      
        fsaTransitions = []  
        for key in self.states.keys():
            for i in self.alphabetList:
                currTransition = self.transitionGenerator(key, i)
                if currTransition != None:
                    fsaTransitions.append(currTransition)
        return fsaTransitions
    
    def transitionGenerator(self, inStateID, actionID):
        '''
        Generate transition for a specific state and action
        '''
        outPos = self.actionObj.actionResult(actionID, 
                                        self.states[inStateID].userID)
        if outPos != None:
            outState = [self.states[inStateID].userID[0]] + outPos 
            outStateMachineID = self.generateMachineID(outState)
            return [inStateID, outStateMachineID, actionID]
        else:
            return None

if __name__=="__main__":
    myFsm = fsmIndiv()
    propList = myFsm.generateStateLabels('robot00')

    pass                    