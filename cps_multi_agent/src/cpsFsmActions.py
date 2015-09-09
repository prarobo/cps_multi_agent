'''
Created on Nov 14, 2014

@author: prasanna
@about: Fuctions that deal with different type of agent actions,
the causal and effect relationships are dealt here.
'''

'''
Some example actions are of the form N1, E3, W4, S5. 
Here the first charater refers to the direction: North, South, East and West.
The following number refers to the number of squares moved in that direction.
There is a special move O0 which refers to stay in place. 

All agents (robot and env) have an action library attached to them. By default the 
action library of all agents supports moves N1-5, S1-5, E1-5, W1-5, O0.
Though the action library supports 26 actions, it does not mean all agents are capable
of performing these actions or other words only a subset of these actions correspond to the
agent dynamics or the agent semi-automata alphabet. 

Update: Extended to n-dimensions
'''
import sys

class fsmActions(object):
    '''
    Class of possible actions for agents
    '''
    

    def __init__(self, arenaDimensions, 
                 inputActionSet = [['nn',1,3],['ss',1,3],['ee',1,3],['ww',1,3],['oo',0,0],
                                   ['ne',1,3],['nw',1,3],['se',1,3],['sw',1,3]]):
        '''
        Constructor
        '''
        self.arenaDimensions = arenaDimensions
        self.numDimensions = len(arenaDimensions)
        
        self.actionList = {}
        self.generateActionLibrary(inputActionSet)
        
        return

    def generateActionLibrary(self, actionInput):
        '''
        Generates a default library of actions
        '''
        for action in actionInput:
            actionName = action[0]
            for i in range(action[1],action[2]+1):
                actionID = actionName+str(i)
                self.actionList[actionID]=[actionName,i]
        return set(self.actionList.keys())  
        
    def generateActionList(self, actionInput):
        '''
        Generates a list of actions
        '''
        actionIDList = set([])
        for action in actionInput:
            actionName = action[0]
            for i in range(action[1],action[2]+1):
                actionID = actionName+str(i)
                if actionID in self.actionList.keys():
                    actionIDList.update([actionID])
        return actionIDList  
    
    def actionResult(self, actionID, stateID):
        '''
        Gives the output state user id after an action
        '''
        statePos = map(int, list(stateID[1]))
        outPos = self.actionResultPos(actionID, statePos[:])
        if outPos == None:
            return None
        else:        
            return "".join( map(str, outPos))
        
    def actionResultPos(self, actionID, statePos):
        '''
        Gives the output position after an action
        '''
        actionType = self.actionList[actionID]
        if actionType[0]=='nn':
            outStatePos = self.actionNN(actionType[1], statePos)
        elif actionType[0]=='ss':
            outStatePos = self.actionSS(actionType[1], statePos)
        elif actionType[0]=='ee':
            outStatePos = self.actionEE(actionType[1], statePos)
        elif actionType[0]=='ww':
            outStatePos = self.actionWW(actionType[1], statePos)
        elif actionType[0]=='ne':
            outStatePos = self.actionNN(actionType[1], statePos)
            outStatePos = self.actionEE(actionType[1], outStatePos[:])
        elif actionType[0]=='nw':
            outStatePos = self.actionNN(actionType[1], statePos)
            outStatePos = self.actionWW(actionType[1], outStatePos[:])
        elif actionType[0]=='se':
            outStatePos = self.actionSS(actionType[1], statePos)
            outStatePos = self.actionEE(actionType[1], outStatePos[:])
        elif actionType[0]=='sw':
            outStatePos = self.actionSS(actionType[1], statePos)
            outStatePos = self.actionWW(actionType[1], outStatePos[:])
        elif actionType[0]=='oo':
            return statePos
        else:
            sys.stderr.write("Undefined action %s\n" % actionID)
            sys.stderr.write("Exiting function")
            sys.exit()        
            
        if self.feasibilityCheck(outStatePos):
            return outStatePos
        else:
            return None
        
    def actionNN(self, actionLength, statePos):
        statePos[1]=statePos[1]+actionLength
        return statePos

    def actionSS(self, actionLength, statePos):
        statePos[1]=statePos[1]-actionLength
        return statePos

    def actionEE(self, actionLength, statePos):
        statePos[0]=statePos[0]+actionLength
        return statePos

    def actionWW(self, actionLength, statePos):
        statePos[0]=statePos[0]-actionLength
        return statePos
    
    def feasibilityCheck(self, statePos):
        '''Checks if an action is feasible, i.e. checks
        if the result of an action is within arena bounds'''
        if statePos[0]>self.arenaDimensions[0]-1 or \
            statePos[0]<0 or \
            statePos[1]>self.arenaDimensions[1]-1 or \
            statePos[1]<0:
            return False
        else:
            return True
    
    def getActionID(self, gridSq1, gridSq2):        
        '''Get the action that causes a movement between 
        two input grid squares. If A is the actions, the action A when the
        agent is on gridSq1 results in the agent moving to gridSq2'''
        for actionID in self.actionList.keys():
            outPos = self.actionResultPos(actionID, gridSq1[:])
            if outPos==gridSq2:
                return actionID
        return None
    
    def filterViableActions(self, inActionList):
        '''Matches an input list of actions to the action list and only returns
        matching actions from the list'''
        return list(set([act for act in inActionList if act in self.actionList]))
    
if __name__=="__main__":
    myAction = fsmActions([5,5])
    print myAction.generateActionList([['n',1,5],['s',1,5]])
    print myAction.feasibilityCheck([1,1])
    print myAction.actionN(4, [1,1])
    print myAction.actionS(4, [1,1])
    print myAction.actionE(4, [1,1])
    print myAction.actionW(4, [1,1])
    print myAction.actionResult('n3', ['robot',1,1])
    
          
    
            