'''
Created on Nov 22, 2014

@author: prasanna
@about: Labelling functions
'''

'''
Label categories and definition
-------------------------------------

Each label consists of two parts a label name and label position(s)

There are two types of labels defined here: static labels and dynamic labels

Static labels correspond to labels that do not change throughout the game 
and the position here refers to the absolute position in the game grid. It
is generally referred by a [x,y]. The static labels here are saved in form
of a dictionary where the keys correspond to the label names and the values
are of the form [[x1,y1], [x2,y2], ...]. The value records all positions
where the corresponding label is true. A label is true only in the grid
squares mentioned in the dictionary's value list. In all other positions,
the label is by definition false.

Dynamic labels are also stored similar to static labels. They are also in form
of a dictionay where the label name acts as a key and the value 
[[x1,y1], [x2,y2], ...] here is relative to the current position of the agent.
Lets say the agent is currently in grid square [x',y'] the the value [x1,y1]
refers to the grid square [x'+x1,y'+y1]. These labels get updated when the 
agent moves.

The label positions are linearized using row-major rule and only a single
position index is finally saved.

Function Reference
----------------------

robotLabelFunction: User defines the dictionary corresponding to the
static and dynamic labels connected with robot agent.

envLabelFunction: User defines the dictionary corresponding to the
static and dynamic labels connected with environment agent.

labelAssignFunction: Assigns label values to the datastructures of an
agent object.
'''

import sys
import numpy as np
from copy import deepcopy

def robotLabelFuction(agentObj, machineID, labelInit={}):
    '''Label function for robot agent'''
    #Static labels and position
    staticLabels = enterLabels('staticLabels', labelInit)
        
    #staticLabels['point_of_interest'] = [[0,2]]
    #staticLabels['comm_station'] = [[0,1]]
    
    #Dynamic label
    dynamicLabels = enterLabels('dynamicLabels', labelInit)       
    #dynamicLabels['occupied'] = [[0,0]]

    #Conditional label
    condLabels = enterLabels('condLabels', labelInit)
    #     condLabels = {}    
    #     condLabels['p2']=[[0,0]]
    #     condLabels['p1']=[[2,2]]
    
    #Default label
    defaultLabels = {}

    return labelAssignFunction(agentObj, machineID, 
                               staticLabels, dynamicLabels, condLabels, defaultLabels)


def envLabelFuction(agentObj, machineID, labelInit={}):
    '''Label function for environment agent''' 
    #Static labels and position
    staticLabels = enterLabels('staticLabels', labelInit)
    #staticLabels['obstacle'] = [[0,0]]
    
    #Dynamic label
    dynamicLabels = enterLabels('dynamicLabels', labelInit)
    #dynamicLabels['hazard'] = [[0,0]]
    
    #Conditional label
    condLabels = enterLabels('condLabels', labelInit)
    
    #Default label
    defaultLabels = {}
    
    return labelAssignFunction(agentObj, machineID, 
                               staticLabels, dynamicLabels, condLabels, defaultLabels)
    
def gameLabelFunction(agentObj, machineID, prop):
    '''Interation label function for game'''
    
    # Get env agent position
    envPosition = agentObj.gameStates[machineID].userID[1]
    
    # Get robot agent positions
    robotPositions = []
    for p in xrange(1,agentObj.numAgents):
        robotPositions.append(agentObj.gameStates[machineID].userID[p*2+1])
    
    interactLabels = 'p3'
    defaultLabels = 'p4'

    labelNames = [interactLabels]+[defaultLabels]
    statePropositions = agentObj.gameStates[machineID].generateStatePropositionGrid(labelNames)
    
    if envPosition in robotPositions: 
        agentObj.gameStates[machineID].assignStatePropositionGrid(statePropositions, 
                                                                  interactLabels, 
                                                                  map(int, list(envPosition)))
    
    #Default propositions
    assignedCells = set(sum(statePropositions.propositionList.values(),[]))
    for propi in prop:
        assignedCells.update(sum(propi.propositionList.values(),[]))

    emptyCells = set(range(np.prod(agentObj.arenaDimensions))).difference(assignedCells)
    
    statePropositions.propositionList[defaultLabels] = list(emptyCells)
        
    return statePropositions

def enterLabels(labelType, labelInit):
    outLabels = {}
    if labelInit.has_key(labelType):
        for labelName in labelInit[labelType].keys():
            outLabels[labelName] = deepcopy(labelInit[labelType][labelName])
    return outLabels 

def labelAssignFunction(agentObj, machineID, staticLabels, dynamicLabels, condLabels, defaultLabels):
    '''Assigns label values to an agent object'''    
    
    #All label names static + dynamic
    labelNames = staticLabels.keys()+dynamicLabels.keys()+condLabels.keys()+defaultLabels.keys()
    statePropositions = agentObj.states[machineID].generateStatePropositionGrid(labelNames)
    
    agentPosition = map(int, list(agentObj.states[machineID].userID[1]))
    
    #Static propositions
    for prop in staticLabels.keys():
        for pos in staticLabels[prop]:
            agentObj.states[machineID].assignStatePropositionGrid(statePropositions, prop, pos)

    #Dynamic propositions
    for prop in dynamicLabels.keys():
        for pos in dynamicLabels[prop]:
            dynamicPos = np.add(pos, agentPosition)
            agentObj.states[machineID].assignStatePropositionGrid(statePropositions, prop, dynamicPos)
            
    #Conditional propositions
    for prop in condLabels.keys():
        for pos in condLabels[prop]:
            if pos==agentPosition:
                agentObj.states[machineID].assignStatePropositionGrid(statePropositions, prop, pos)
                
    
    #Default propositions
    assignedCells = set(sum(statePropositions.propositionList.values(),[]))
    emptyCells = set(range(np.prod(agentObj.arenaDimensions))).difference(assignedCells)
    
    for prop in defaultLabels.keys():
        statePropositions.propositionList[prop] = list(emptyCells)
        
    return statePropositions

if __name__ == '__main__':
    numRobots = 2
    arenaDimensions = [3,3]
    
    robotLabelInit = {}
    robotLabelInit['condLabels'] = {}
    robotLabelInit['condLabels']['p1'] = [[0,0],[2,2]]
    robotLabelInit['condLabels']['p2'] = [[2,0],[0,2]]     
    
    agentsLabelInitList = [{}] + [robotLabelInit]*numRobots  
    
#     robotList = []
#     for i in xrange(numRobots):
#         robotList.append( cpsFsmIndividual.fsmIndiv(arenaDimensions, robotLabelFuction,
#                                    agentName='R'+str(i),
#                                    agentAlphabetInput=[['nn',1,1],['ss',1,1],['ee',1,1],['ww',1,1],
#                                                        ['oo',0,0],['ne',1,1],['nw',1,1],['se',1,1],['sw',1,1]]) )
# 
#     env = cpsFsmIndividual.fsmIndiv(arenaDimensions, envLabelFuction, 
#                     agentName='E0',
#                     agentAlphabetInput=[['oo',0,0]])
# 
#     turnProduct = cpsFsmTurnProduct.fsmTurnProduct([env]+robotList, arenaDimensions)
#     
#     gameStateLabels = {}
#     for stateID in turnProduct.gameStates.keys(): 
#         currLabel = turnProduct.generateStateLabels(stateID, agentsLabelInitList)
#         gameStateLabels[stateID] = currLabel.propositionList    #robotLabelFuction(None, None, labelInit)
    pass


