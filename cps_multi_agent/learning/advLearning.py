'''
Created on Sep 25, 2015

@author: prasanna
'''

import itertools
import random
from copy import deepcopy
from cpsFsmStrings import generateKSubsequences
import cPickle as pickle
import scipy.io as io
import matplotlib.pyplot as plt

def getNextPosition(arenaDimensions, currPosition, action):
    '''Get the positions after action'''
    
    actionType = action[:2]
    actionParam = int(action[-1])
    
    if actionType == 'nn':
        resPosition = [currPosition[0], currPosition[1]+actionParam]
    elif actionType == 'ss':
        resPosition = [currPosition[0], currPosition[1]-actionParam]
    elif actionType == 'ee':
        resPosition = [currPosition[0]+actionParam, currPosition[1]]
    elif actionType == 'ww':
        resPosition = [currPosition[0]-actionParam, currPosition[1]]
    elif actionType == 'ne':
        resPosition = [currPosition[0]+actionParam, currPosition[1]+actionParam]
    elif actionType == 'nw':
        resPosition = [currPosition[0]-actionParam, currPosition[1]+actionParam]
    elif actionType == 'se':
        resPosition = [currPosition[0]+actionParam, currPosition[1]-actionParam]
    elif actionType == 'sw':
        resPosition = [currPosition[0]-actionParam, currPosition[1]-actionParam]
    elif actionType == 'oo':
        resPosition = [currPosition[0], currPosition[1]]
    else:
        raise "Unknown action type"
    
    if resPosition[0]>=arenaDimensions[0] or resPosition[1]>=arenaDimensions[1]:
        resPosition = None
        
    return resPosition

def getFeasibleActions(alphabet, currPosition, arenaDimensions):
    '''Returns a list of feasible actions from the current state'''
    feasibleActions = set()
    for a in alphabet:
        resPosition = getNextPosition(arenaDimensions, currPosition, a)
        
        if resPosition:
            feasibleActions.add(a)
             
    return feasibleActions

if __name__ == '__main__':
    # Initialize experiments
    numRuns = 10
    numWords = 20
    wordLength = 15
    runData = {}
    numFactorList = []
    
    # Initialize arena dimensions and factor set
    arenaDimensions = [5,5]
    # advAlphabet = set(['nn1','ss1','ee1','ww1','oo0'])
    advAlphabet = set(['nn1','ss1','ee1','ww1','ne1','nw1','se1','sw1','oo0'])
    factorLen = 2
    
    # Initialize grammar factors
    allFactors = set(itertools.product(advAlphabet, repeat=factorLen))
    forbiddenFactors = set([('nn1','nn1'),('ss1','ss1'),('ee1','ee1'),('ww1','ww1')])
    # forbiddenFactors = set(itertools.product(advAlphabet, ['nn1']))
    # forbiddenFactors.remove(('oo0','nn1'))
    allowedFactors = allFactors.difference(forbiddenFactors)

    for i in xrange(numRuns):
         
        # Initialize starting position of game
        startState = [random.randint(0, arenaDimensions[0]), random.randint(0, arenaDimensions[1])]
        currState = startState
        numIter = 0
        numFactors= [1]
        currFactors = set([('oo0','oo0')])
        
        for t in xrange(numWords):
            moveSeq = ['oo0','oo0']
            
            # Missing factors
            missingFactors = allowedFactors.difference(currFactors)
       
            # Iterate till learned factors match adversary model
            while currFactors != allowedFactors:
        
                feasibleActions = getFeasibleActions(advAlphabet, currState, arenaDimensions)
        
                # If there are no feasible actions available
                if (not feasibleActions) or len(moveSeq)>wordLength:
                    break
                
                print "Run: %d\t Iteration: %d\t Word: %d\t factor (%d|%d)" %(i, numIter, t, len(currFactors), len(allowedFactors))
                while feasibleActions:
                
                    # If there are no feasible actions available
                    if not feasibleActions:
                        break
                    
                    chosenAction = random.choice(list(feasibleActions))
                    
                    tentativeMoveSeq = moveSeq+[chosenAction]
                    
                    # Compute all k-subsequences
                    tempFactors = generateKSubsequences(tentativeMoveSeq, 2)
                                        
                    # Check if the factors generated are subset of allowed factors
                    if tempFactors.issubset(allowedFactors):
                        currState = getNextPosition(arenaDimensions, currState, chosenAction)
                        currFactors.update(tempFactors)
                        moveSeq = deepcopy(tentativeMoveSeq)
                        numIter += 1
                        numFactors.append(len(currFactors))
                        break
                    else:
                        feasibleActions.remove(chosenAction)                
        
        # Check if learning is complete or not
        if currFactors == allowedFactors:
            learningComplete = True
        else:
            learningComplete = False
            
        # Saving run data
        runData[i] = {'startState': startState,
                      'moveSeq': moveSeq,
                      'learningComplete': learningComplete,
                      'currFactors': currFactors,
                      'allFactors': allFactors,
                      'allowedFactors': allowedFactors,
                      'numIter': numIter}
        
        numFactorList.append(deepcopy(numFactors))
        
        # plt.plot(numFactors)
        # plt.show()
 
    pickle.dump(runData, open("adv_learning.p","wb"))
    io.savemat('adv_learning_results', {'numFactorList': numFactorList})
   
            
        
        
        