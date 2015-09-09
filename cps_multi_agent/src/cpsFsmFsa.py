'''
Created on Aug 10, 2015

@author: prasanna
@about: Finite state machine (Fsm) operations
'''
from copy import deepcopy
from types import TupleType
__author__="prasanna kannappan <prasanna@udel.edu>"

# setting system paths
import sys
sys.path.append("../fsa")

from FSA import FSA
import itertools
import re
import types
import os, tempfile
import string

# Special constants for
OP_ANY = "ANY"
OP_NONE = "NONE"

class CustomFSA(object):
    '''Customized fsa operations to overcome problems in osteel's code'''
    
    def __init__(self, states, alphabet, transitions, initStates, finalStates, simplifyActions = True):
        '''Constructor'''
        self.states = states
        self.alphabet = set(alphabet)
        self.initStates = initStates
        self.finalStates = set(finalStates)
        self.simplifyActions = simplifyActions
        
        # Change actions in transitions to sets
        self.transitions = set(self.filterTransitions(alphabet, transitions))
        
        return
        
    def filterTransitions(self, alphabet, transitions):
        '''Filter transitions with special actions and repetitions'''
        nTransitions = set()
        for t in transitions:
            startNode = t[0]
            endNode = t[1]
            
            if self.simplifyActions:
                actionSet = list(processActions(alphabet, t[2]))
            else:
                actionSet = [t[2]]
            
            for k in actionSet:
                nTransitions.add((startNode, endNode, k))      
            
        return nTransitions
    
    def view(self, titleStr=""):
        '''Display FSA using dot graph'''
        
        output = []
        output.append('digraph '+titleStr+' {');
        output.append('\trankdir=LR;');
        if self.finalStates:
            output.append('\tnode [shape = doublecircle]; ' + string.join(map(modifyStateNames, self.finalStates), '; ') + ';' );
        if self.initStates:
            output.append('\tnode [shape = circle, style = bold]; ' + string.join(map(modifyStateNames, self.initStates), '; ') + ';' );
        output.append('\tnode [shape = circle, style = ""];');
        #output.append('\t%s [style = bold];' % (modifyStateNames(self.initState),))
        transitions = list(self.transitions)
        transitions.sort()
        for (s0, s1, label) in transitions:
            output.append('\t%s -> %s  [label = "%s"];' % (modifyStateNames(s0), modifyStateNames(s1), string.replace(modifyStateNames(label), '\n', '\\n')));
        output.append('}');
        myStr = string.join(output, '\n')
    
        dotfile = tempfile.mktemp()
        psfile = tempfile.mktemp()
        open(dotfile, 'w').write(myStr)
        dotter = 'dot'
        psviewer = 'gv'
        psoptions = '-antialias'
        os.system("%s -Tps %s -o %s" % (dotter, dotfile, psfile))
        os.system("%s %s %s&" % (psviewer, psoptions, psfile))

        return
    
    def generateAdjacencyMat(self, specDynamics):
        '''Generate an adjacency matrix for custom fsa'''
        
        # Synchronize state order for all agents
        if isinstance(specDynamics, dict):
            keyList = specDynamics.keys()
            if keyList:
                if not set(specDynamics[keyList[0]].states) == set(self.states):
                    raise "State sets not matching"
                else:
                    self.states = deepcopy(specDynamics[keyList[0]].states)
        elif isinstance(specDynamics, CustomFSA):
            if not set(specDynamics.states) == set(self.states):
                raise "State sets not matching"
            else:
                self.states = deepcopy(specDynamics.states)    
                                
        states = self.states
        numStates = len(states)
        
        # Initializing adjacency matrix with zeroes
        adjMat = [[0]*numStates for _ in xrange(numStates)]
        
        for i in self.transitions:
            if adjMat[states.index(i[0])][states.index(i[1])] == 0:
                adjMat[states.index(i[0])][states.index(i[1])] = [i[2]]
            else:
                adjMat[states.index(i[0])][states.index(i[1])].append(i[2])
                
        self.adjMat = adjMat
        return
    
def serializeFsaStates(inFsa, serialStartVal = 0):
    '''Serialize state labels to numbers'''
    states = inFsa.states
    transitions = list(inFsa.transitions)
    numStates = len(states)
    serialCharTupleMap = {}
    serialTupleCharMap = {}
    serialStates = []
    serialInitStates = []
    serialFinalStates = []
    serialTransitions = set()
    
    # Serializing states and getting serialization map
    for i,j in zip(states, xrange(0+serialStartVal, numStates+serialStartVal)):
        serialCharTupleMap[str(j)] = str(i)
        serialTupleCharMap[str(i)] = str(j)
        serialStates.append(str(j))
    
    # Serializing initial states    
    for i in inFsa.initStates:
        serialInitStates.append(serialTupleCharMap[str(i)])

    # Serializing final states    
    for i in inFsa.finalStates:
        serialFinalStates.append(serialTupleCharMap[str(i)])
        
    # Serialize transitions
    for t in transitions:
        serialTransitions.add((serialTupleCharMap[t[0]], serialTupleCharMap[t[1]], t[2]))
    
    # Get serialized fsa
    outFsa = CustomFSA(serialStates, inFsa.alphabet, serialTransitions, 
                       serialInitStates, serialFinalStates, simplifyActions = False)        
    
    return outFsa, serialCharTupleMap, serialTupleCharMap
    
def modifyStateNames(inVal):
    '''Modify names of states for display purposes'''
    if isinstance(inVal, types.TupleType) or isinstance(inVal, types.ListType):
        tempVal = list(deepcopy(inVal))
        try:
            float(tempVal[0])
            tempVal[0]='N'+str(tempVal[0])
        except:
            pass
            
        return '_'.join(tempVal)
    elif isinstance(inVal, types.StringTypes):
        return inVal
    
def processActions(alphabet, expr):
    '''Convert an action expression into an appropriate set'''
    
    #Remove all white spaces
    expr = ''.join(expr.split())
    
    expr = re.sub(r'([&(~]?)([a-z])([&)~]?)',r'\1set(["\2"])\3', expr) #Replace a-z with corresponding sets
    expr = expr.replace('~',str(set(alphabet))+'-') #Replacing negations with difference from alphabet
    expr = expr.replace(OP_NONE, str(set([]))) #Replace none actions
    expr = expr.replace(OP_ANY, str(set(alphabet))) #Replace any actions
    
    return eval(expr)       
    
def generateSPkSingleFactorFsa(alphabet, factor, grammarParams):
    '''Generate the strictly piecewise automata for a single factor of length 2'''
    
    states = map(str, xrange(grammarParams))
    alphabet = set(alphabet)
    initStates = ['0']
    finalStates = states[:]
    simplifyActions = False
    
    transitions = set()
    
    for i in xrange(grammarParams):
        tempSet = list(set.difference(alphabet,set(factor[i])))
        
        # Self loops
        for j in tempSet:
            transitions.add((states[i],states[i],j))
        
        # Connecting transition       
        if i != len(factor)-1:
            transitions.add((states[i],states[i+1],factor[0]))
            
    return CustomFSA(states, alphabet, transitions, initStates, finalStates, simplifyActions)

def generateSLkSingleFactorFsa(alphabet, factor, grammarParams):
    '''Generate the strictly local automata for a single factor of length 2'''
    
    states = map(str, xrange(grammarParams))
    alphabet = set(alphabet)
    initStates = ['0']
    finalStates = states[:]
    simplifyActions = False
    
    transitions = set()
    
    for i in xrange(grammarParams):
        tempSet = list(set.difference(alphabet,set(factor[i])))
        
        if i != len(factor)-1:
            # Self loops
            for j in tempSet:
                transitions.add((states[i],states[i],j))
        else:
            for j in tempSet:
                transitions.add((states[i],states[0],j))            
        
        # Connecting transition       
        if i != len(factor)-1:
            transitions.add((states[i],states[i+1],factor[0]))
            
    return CustomFSA(states, alphabet, transitions, initStates, finalStates, simplifyActions)
    
def generateSPkFactorFsa(alphabet, factors, grammarParams):
    '''Generate the strictly piecewise automata from a list of k-sequences'''
    
    outFsa = generateDefaultFsa(alphabet)
    
    for factor in factors:
        
        # Get fsa corresponding to single factor
        currFsa = generateSPkSingleFactorFsa(alphabet, factor, grammarParams)

        # Recursively intersect fsas
        outFsa = customFSAIntersection(outFsa, currFsa, simplifyActions = False)
    
    return outFsa

def generateSLkFactorFsa(alphabet, factors, grammarParams):
    '''Generate the strictly piecewise automata from a list of k-sequences'''
    
    outFsa = generateDefaultFsa(alphabet)        
        
    for factor in factors:
        
        # Get fsa corresponding to single factor
        currFsa = generateSLkSingleFactorFsa(alphabet, factor, grammarParams)

        # Recursively intersect fsas
        outFsa = customFSAIntersection(outFsa, currFsa, simplifyActions = False)

    return outFsa

def generateDefaultFsa(alphabet):
    '''Get the default fsa that allows all transitions'''
    
    states = ['0']
    transitions = [('0','0','ANY')]
    initStates = states[:]
    finalStates = states[:] 
    simplifyActions = True
    
    return CustomFSA(states, alphabet, transitions, initStates, finalStates, simplifyActions)
            
def generateFactorFsa(alphabet, factors, grammarName, grammarParams):
    '''Generate fsa using grammar type input'''
    if grammarName == 'SL':
        return generateSLkFactorFsa(alphabet, factors, grammarParams)
    elif grammarName == 'SP':
        return generateSPkFactorFsa(alphabet, factors, grammarParams)
    else:
        raise "Unknown factor type"
    return
    
def customFSAIntersection(fsaA, fsaB, simplifyActions = True):
    '''Intersection of two fsa'''
    
    states = list(itertools.product(fsaA.states, fsaB.states))
    alphabet = set.union(fsaA.alphabet, fsaB.alphabet)
    initStates = list(itertools.product(fsaA.initStates, fsaB.initStates))
    finalStates = list(itertools.product(fsaA.finalStates, fsaB.finalStates))
    
    transitions = []
    for ti in fsaA.transitions:
        for tj in fsaB.transitions:
            if ti[2]==tj[2]:

                if isinstance(ti[0], TupleType):
                    ti_start = ti[0]
                    ti_end = ti[1]
                else:
                    ti_start = (ti[0],)
                    ti_end = (ti[1],)

                if isinstance(tj[0], TupleType):
                    tj_start = tj[0]
                    tj_end = tj[1]
                else:
                    tj_start = (tj[0],)
                    tj_end = (tj[1],)
                    
                transitions.append((ti_start+tj_start, ti_end+tj_end, ti[2]))
    
    return CustomFSA(states, alphabet, transitions, initStates, finalStates, simplifyActions)
   
def osteelFSAToCustomFSA(ofsaA):
    '''Create custom fsa objects from osteel fsa'''
    states = [str(i) for i in ofsaA.states]
    alphabet = ofsaA.alphabet
    transitions = [(str(i[0]), str(i[1]), str(i[2])) for i in ofsaA.transitions]
    initStates = [str(ofsaA.initialState)]
    finalStates = [str(i) for i in ofsaA.finalStates]
    return CustomFSA(states, alphabet, transitions, initStates, finalStates)

def removeFsaFromProduct(inFsa, agentStateTupleRefIndex = 0):
    '''Remove elements of an fsa from a product fsa'''
    strf = agentStateTupleRefIndex
    states = [i[strf] for i in inFsa.states]
    alphabet = inFsa.alphabet
    initStates = [i[strf] for i in inFsa.initStates]
    finalStates = [i[strf] for i in inFsa.finalStates]
    simplifyActions = False
    
    transitions = set()
    
    for i in inFsa.transitions:
        transitions.add((i[0][strf], i[1][strf], i[2])) 
    transitions = list(transitions)
    
    return CustomFSA(states, alphabet, transitions, initStates, finalStates, simplifyActions)

if __name__ == '__main__':
    str1 = ''
    str2 = 'a'
    str3 = '(a)'
    str4 = '~a'
    str5 = '~a&~b'
    str6 = '(~a&b)&~c'
    
    alphabet = ['a','b','c','d']

    print processActions(alphabet,str6)
    
    alphabet = set(['a','b','c'])
    factors = ['aa']
    
    currFsa = generateSPkFactorFsa(alphabet, factors, 2)
    currFsa.view()
    
    
    
    