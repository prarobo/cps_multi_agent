import os
os.chdir('C:\\Users\HynessLab\Dropbox\Learning_UDel\cps_fsm')
import sys
sys.path.append("gui")
sys.path.append("fsa")
sys.path.append("src")
import cPickle as pickle
from FSA import FSA
import scipy
from scipy import io
gameAutomaton = pickle.load( open( ".\gameAutomaton.p", "rb" ) )
gameStates, gameAlphabet, gameTransitions = gameAutomaton.getFSA()
scipy.io.savemat('gameAlphabet.mat',mdict={'gameAlph':gameAlphabet})
scipy.io.savemat('gameStates.mat',mdict={'gameStates':gameStates})
scipy.io.savemat('gameTransitions.mat',mdict={'gameTrans':gameTransitions})  