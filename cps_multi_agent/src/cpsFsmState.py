'''
Created on Nov 11, 2014

@author: prasanna
@about: state datastructure
'''

from cpsFsmProposition import fsmPropositionList
import numpy as np

class fsmState(object):
    '''
    FSM State class
    '''
    
    def __init__(self, userID, machineID, arenaDimensions,
                  isInitial=False, isFinal=False, isSuccess=False):
        '''
        Constructor
        '''
        self.userID = userID    #Unique identifier to a state containing a tuple
        self.machineID = machineID   #Unique string identifier to a state
        self.arenaDimensions = arenaDimensions #List of state space dimension size
        #Propositions attached to the states
        #self.statePropositionNames = propositionNames 
        #Assigning the list of propositions
        #self.statePropositionList = self.generateStatePropositionGrid(propositionNames) 
        self.isInitial = isInitial  #is initial state (default true)
        self.isFinal = isFinal  #is final state (default false)
             
        return
    
    def setInitial(self, value=True):
        '''
        Sets if a state can be a initial state (default true)
        '''
        self.isInitial = value
        return
    
    def setFinal(self, value=True):
        '''
        Sets if a state can be a final state (default false)
        '''
        self.isFinal = value
        return
    
    def assignStatePropositionGrid(self, statePropositionList, propositionName, gridPos):
        '''
        Assigning proposition values in a state
        Proposition Name 'hazard'
        Grid Pos [1,2]
          '''
        
        #Checking if proposition is inside arena bounds
        boundCheck = True
        for i in range(len(gridPos)):
            boundCheck = boundCheck and gridPos[i] < self.arenaDimensions[i]
        
        if boundCheck:    
            gridLinearIndex = np.ravel_multi_index(gridPos,self.arenaDimensions)
            statePropositionList.assignPropositionGrid([[propositionName, gridLinearIndex]])
        else:
            print "Warning: Proposition ", propositionName," in grid position ", gridPos, "Out of bounds"
        return
    
    def generateStatePropositionGrid(self, propositionNames):
        '''
        Generate list of propositions for each state
        '''
        statePropositionGrid = fsmPropositionList(propositionNames)
        return statePropositionGrid
    
if __name__=="__main__":
    '''
    Unit test for fsm state class
    '''
    myFsmState=fsmState(1,1,['prop1','prop2'],[2,2],'robot',[0,0])
    myFsmState.assignStatePropositionGrid('prop1', [0,1])
    myFsmState.assignStatePropositionGrid('prop2', [1,1])
    pass
