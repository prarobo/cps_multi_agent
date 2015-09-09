'''
Created on Aug 26, 2015

@author: prasanna
@about: compute the product automaton of agent transitions and agent grammar
'''
from FSA import FSA, compileRE, complement
from copy import deepcopy
from itertools import permutations
from cpsFsmFsa import generateFactorFsa, CustomFSA, customFSAIntersection, removeFsaFromProduct, serializeFsaStates
from types import TupleType

__author__ = 'Prasanna Kannappan <prasanna@udel.edu>'

class fsmProductAutomaton(object):
    def __init__(self):
        '''Constructor'''
        self.grammarFsa = []
        self.transitionFsa = []
        self.productFsa = []
        return
    
    def computeFsaProductTransitions(self, gameStates, gameTransitions, advGrammarObj, advAlphabet, advName):
        '''Computes the transitions from product automaton'''
                
        gameTransitions = set([tuple(i) for i in gameTransitions])
        
        # Getting grammar fsa
        self.grammarFsa, self.serialCharTupleMap, self.serialTupleCharMap = serializeFsaStates( self.generateGrammarFsa(advGrammarObj, 
                                                                                                                        advAlphabet), 
                                                                                      serialStartVal = 1)
        
        # Get adversary game parameters
        advStates, advTransitions = self.filterGameParameters(gameStates, gameTransitions, advName)
               
        # Getting transition fsa
        self.transitionFsa = CustomFSA(advStates, advAlphabet, advTransitions, advStates, advStates, simplifyActions = False)
        
        # Get product of grammar and transition fsa
        self.productFsa = customFSAIntersection(self.grammarFsa, self.transitionFsa, simplifyActions = False)
        
        # Reduce product fsa
        # reducedProductFsa = removeFsaFromProduct(self.productFsa, agentStateTupleRefIndex = 1)
                
        # Product states and transitions 
        productTransitions = self.productFsa.transitions
        productStates = self.productFsa.states
        
        # Agent transitions and states
        agentTransitions = gameTransitions.difference(advTransitions)
        agentStates = set(gameStates.keys()).difference(advStates)
        
        # Add dummy index to make agent states and transitions consistent with product states and transitions
        agentStates, agentTransitions = self.addDummyStateTupleIndex(agentStates, agentTransitions, dummyIndexVal = 0)
        
        # Combine agent and adversary parameters
        totalStates = set.union(set(productStates), agentStates)
        totalTransitions = set.union(productTransitions, agentTransitions)
        
        # Get the updated set of transitions
        # updateTransitions = gameTransitions.difference(advTransitions)
        # updateTransitions.update(transitions)
        
        # Sanity check to see if there are any transitions lost while updates
        # prevAdvTransitions = advTransitions.difference(gameNewTransitions)
        # t = prevAdvTransitions.difference(transitions)
        # assert not t, "Some transitions are lost!"
        
        # Sanity check to see if there is any change between game and update transitions
        # assert gameTransitions == updateTransitions, "Game and update transitions are different!"
                 
        return totalStates, totalTransitions

    def filterGameParameters(self, gameStates, gameTransitions, advName):
        '''Filter adversary's game parameters'''
        
        # Filter adversary states
        advStates = set()
        for i in gameStates.keys():
            if gameStates[i].userID[-1] == advName:
                advStates.add(i)
                
        # Filter transitions based on whose turn it is    
        advTrans = set()
        for t in gameTransitions:
            if gameStates[t[0]].userID[-1] == advName:
                advTrans.add(t)
                
        return advStates, advTrans
     
    def generateGrammarFsa(self, grammarObj, agentAlphabet):
        '''Generate the fsa corresponding to grammar'''
        
        grammarName = grammarObj.grammarName
        grammarParams = grammarObj.grammarParams[0]
        grammarFactors = grammarObj.grammar
        alphabet = list(agentAlphabet)
        
        # The alphabet length is less than the kFactor length, repeat
        if len(alphabet) < grammarParams:
            alphabet = [alphabet[0]]*grammarParams
        
        allFactors = set(permutations(alphabet, grammarParams))
        complementFactors = allFactors.difference(grammarFactors)
        
        grammarFsa = generateFactorFsa(alphabet, complementFactors, grammarName, grammarParams)
        
        return grammarFsa
    
    def addDummyStateTupleIndex(self, states, transitions, dummyIndexVal = 0):
        '''Add an tuple index dimension to each state in fsa parameters'''
        
        outStates = []
        outTransitions = set()
        
        for s in states:
            if isinstance(s, TupleType):
                outStates.append( (str(dummyIndexVal),) + s )
            else:
                outStates.append( (str(dummyIndexVal),) + (s,) )
            
        for t in transitions:
            if isinstance(t[0], TupleType):
                outTransitions.add( ( (str(dummyIndexVal),) + t[0], (str(dummyIndexVal),) + t[1], t[2] ,) )
            else:
                outTransitions.add( ( (str(dummyIndexVal), t[0]), (str(dummyIndexVal), t[1]) , t[2] ,) )
                       
        return outStates, outTransitions        
        
if __name__ == '__main__':
    tempFsa = compileRE('.*b.*b')
    tempFsa.view()
    
    tempFsa2 = complement(compileRE('.*b.*b'))
    tempFsa2.view()
    
    
    
    
    
    