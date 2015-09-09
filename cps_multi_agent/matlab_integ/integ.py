import sys
sys.path.append('../gui')
sys.path.append('../fsa')
sys.path.append('../src')

import cPickle as pickle
from Automata import *
from cpsFsmTurnProduct import *
from cpsFsmIndividual import fsmIndiv
from cpsFsmState import fsmState
from FSA import FSA
import numpy as np
import time
from cpsFsmLabelFunctions import *
import itertools

# startTime = time.clock()

# Create turn-based product. Normally, this will be output from the GUI.
arenaDimensions = [4,4] #Grid dimensions (x-dir,y-dir) or (col, row)
numRobots = 2

robotLabelInit = {}
robotLabelInit['condLabels'] = {}
robotLabelInit['condLabels']['p1'] = [[0,0],[3,3]]
robotLabelInit['condLabels']['p2'] = [[3,0],[0,3]]  

robotList = []
for i in xrange(numRobots):
    robotList.append( fsmIndiv(arenaDimensions, robotLabelFuction,
                               agentName= 'R'+str(i),
                               agentAlphabetInput=[['oo',0,0],['nn',1,1],['ss',1,1],['ee',1,1],['ww',1,1]]))

for i in xrange(numRobots):
    for key in robotList[i].states.keys():
        env = fsmIndiv(arenaDimensions, envLabelFuction,
                 agentName='E',
                 agentAlphabetInput=[['oo',0,0]])

gameProduct = fsmTurnProduct([env]+robotList, arenaDimensions, drawTransitionGraph=False)
gameStates, gameAlphabet, gameTransitions, newTransitions = gameProduct.getFSA()

p1Set = set(['00','33'])
p2Set = set(['30','03'])

gameStateLabels = {}
for stateID in gameProduct.gameStates.keys():
    gameStateLabels[stateID] = gameProduct.generateStateLabels(stateID,[{},robotLabelInit,robotLabelInit])
    if gameProduct.gameStates[stateID].userID[3] in p1Set or gameProduct.gameStates[stateID].userID[5] in p1Set:
        gameStateLabels[stateID].propositionList['p1'] = '1'
    if gameProduct.gameStates[stateID].userID[3] in p2Set or gameProduct.gameStates[stateID].userID[5] in p2Set:
        gameStateLabels[stateID].propositionList['p2'] = '1'

initState = 'E_00_R0_33_R1_33_T_E'

######################
# Here is new code from Kevin:
######################

# Get Buchi Automaton from specification:
# [] <> p1 && [] <> p2 && [] ! p3
# other specifications can be accomodated when we need them
# This process can be updated to automatically generate a buchi from a new specificaiton, but the required
# process has a lot of dependencies, so for now, we will just read in a buchi from a file.
# More information on BuchiAutomata can be found in Automata.py
buchi = BuchiAutomaton()
buchi.readStatement('learnSpec2') #read .dot file containing Buchi Automaton for specification

# Create GTS
# For more details, see the synthesis.py
# Details on WeightedTransitionSystems can be found in GraphicalModels.py
GTS = WeightedTransitionSystem()
GTS.TSfromGame(gameStates,gameTransitions,gameStateLabels)


# Now take product
P = ProductBuchi()
P.fromBAndTS(buchi,GTS,initState)

# dijkStart = time.clock()
# This is the same as findEnergyGame from matlab
dist,FStar = P.findEnergyGame(gameProduct)
# dijkTime = time.clock() -dijkStart

# We don't need to compute the policy ahead of time, we can just choose the best move for a given state
# This means that the product only needs to be updated when new transitions are observed
for p in P.initialStates:
    action = P.getAction(dist,p)

# Take the optimal action (this can be done even for the adversary's turn)
P.input(action)

# Add new actions and get new transitions
gameProduct.addActionToAgent('E', [1,1], [1,0], addAction=True)
gameProduct.addAgentActions('E', ['nn1','ee1'])

gameStates, gameAlphabet, gameTransitions, newTransitions = gameProduct.getFSA()

#Finally, update GTS and product
# To get new policy, findEnergyGame needs to be run again
GTS.incrTrans(newTransitions)
P.incrProd(newTransitions,buchi,GTS)

# totTime = time.clock() - startTime

# print 'Dijkstra Time:',dijkTime
# print 'Overall Time:',totTime