'''
Created on Mar 6, 2015

@author: prasanna
'''

import sys
sys.path.append("../gui")
sys.path.append("../fsa") 

import cPickle as pickle
from FSA import FSA

if __name__=="__main__":
    
    # Loading file from disk 
    gameAutomaton = pickle.load( open( "../gameAutomaton.p", "rb" ) )
    
    # Getting game transition system parameters
    # gameStates is the state space
    # gameAlphabet is the set of actions
    # gameTransitions is the transition table
    gameStates, gameAlphabet, gameTransitions = gameAutomaton.getFSA()  

####### Getting state labels ##########################################
# Use the lines below to get the state labels
# (or values of propositions) corresponding to a specific state.
# stateLabels is a dictionary. The keys of the dictionary correspond
# to the names of the each label name. A list is attached to each key.
# This list corresponds to the position in the arena grid where the
# corresponding label (or proposition) is true. In all other grid 
# squares, that proposition is false. The list contains linear indices
# of the grid squares computed through row-major rule.
# For example, lets say there are that there are three propositions
# hazard, occupied, comm_station. Hazard is true in (0,0), occupied 
# is true in (0,1), and comm_station is true in (1,0)  and (0,1) then 
# the stateLabels dictionary structure looks as follows.
# 
# stateLabels
#    hazard: [0]
#    occupied: [1]
#    comm_station: [2,1]
#
# Note the origin (0,0) is the lower left square in the grid.
# Also remember that the indexing starts from 0 and not 1.
#
# How to specify a state or stateID?
#
# A stateID is of the form: 
#                    
#        R[nn]E[nn]T[a]
#
# Here R refers to robot, the following nn refers to the position of the
# robot in the grid (eg (0,0) is specified as 00). Similarly E refers to
# environment or unknown adversary and the following nn refers to the
# position of the adversry in the grid. T refers to turn and the following
# character a can either be R (robot) or E (environment).
# 
# For example R00E11TR is a valid stateID
# 
# Be careful not to specify grid squares that are outside the arena
# dimensions in the GUI from which the game automaton was generated.
# This will throw a state not found in state space error. 
#########################################################################
    
    # Specifying a state to extract state labels
    currStateID = 'R30E03TR'

    # Verifying if the state specified is included in the statespace        
    if not(currStateID in gameStates):
        sys.stderr.write("State not in state space\n")
        sys.stderr.write("Exiting function")
        sys.exit()
    
    # Getting state labels    
    stateLabels = gameAutomaton.generateStateLabels(currStateID)
    
###### End of state labels code ###################################

    # Getting labels of all states
    gameStateLabels = {}
    for stateID in gameAutomaton.gameStates.keys():
        gameStateLabels[stateID] = gameAutomaton.generateStateLabels(stateID)

    
####### Drawing transition graph ##################################
# This feature is strictly to visualize the transition graph
# if the number of states is small. Comment the lines below if
# the number of states is too large. 
# You also need to specify an initial and final state for this.
# To see how to specify the states see the comments on how to generate
# state labels mentioned above. To avoid accidentally trying to 
# draw a transition graph visualization with too many states, this 
# section gets disabled if the number of states is greater than 50.
###################################################################
    
    # Checking if number of states is less than 50
    if len(gameStates)<=50: 
        # Setting initial and final states
        gameInitialState = 'R00E11TR'
        gameFinalStates = 'R11E00TR'
           
        # Verifying if the initial state and final state of the transition system 
        # is included in the statespace        
        if not(gameInitialState in gameStates) or not(gameFinalStates in gameStates):
            sys.stderr.write("Initial of final state not in state space\n")
            sys.stderr.write("Exiting function")
            sys.exit()
     
        #Drawing transition graph
        myFsa = FSA(gameStates, gameAlphabet, gameTransitions,
                    gameInitialState, [gameFinalStates])
        myFsa.view()
    else:
        print "Number of states: ", len(gameStates)
        print "Too many states, visualization of transition graph disabled"
        
###### End of draw transition graph code #####################    
     
    