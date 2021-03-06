'''
Created on Aug 26, 2015

@author: prasanna
@about: compute the product automaton of agent transitions and agent grammar
'''
from FSA import FSA, compileRE, complement
from copy import deepcopy
import itertools
from cpsFsmFsa import generateFactorFsa, CustomFSA, customFsaProduct
from cpsFsmFsa import customFSAInefficientIntersection, removeFsaFromProduct, serializeFsaStates
from types import TupleType
import cPickle as pickle

__author__ = 'Prasanna Kannappan <prasanna@udel.edu>'

class fsmProductAutomaton(object):
    def __init__(self):
        '''Constructor'''
        self.grammarFsa = []
        self.transitionFsa = []
        self.productFsa = []
        self.nextPlayerName = None
        self.outStates = []
        self.outTransitions = []
        return
    
    def computeFsaProductTransitions(self, gameStates, gameTransitions, advGrammarObj, 
                                        advAlphabet, advName, numAgents):
        '''Computes the transitions from product automaton'''
                
        gameTransitions = set([tuple(i) for i in gameTransitions])
        
        # Getting grammar fsa
        self.grammarFsa, self.serialCharTupleMap, self.serialTupleCharMap = serializeFsaStates( self.generateGrammarFsa(advGrammarObj, 
                                                                                                                        advAlphabet), 
                                                                                               serialStartVal = 1)
        # self.grammarFsa.view()
        
        # Get adversary game parameters
        advStates, advTransitions, agentStates, agentTransitions = self.filterAdversaryFromGameParameters(gameStates, 
                                                                                                          gameTransitions, 
                                                                                                          advName)
        # Getting transition fsa
        self.transitionFsa = CustomFSA(advStates, advAlphabet, advTransitions, advStates, advStates, simplifyActions = False)
        
        # Get product of grammar and transition fsa
        self.productFsa = customFsaProduct(self.grammarFsa, self.transitionFsa, simplifyActions = False)
        # temp = customFSAInefficientIntersection(self.grammarFsa, self.transitionFsa, simplifyActions = False)
        
        # Sanity check
        # assert self.productFsa == temp, "Efficient and inefficient products not matching"
        
        # Reduce product fsa
        # reducedProductFsa = removeFsaFromProduct(self.productFsa, agentStateTupleRefIndex = 1)
        
        # Save transitions for verification
        # pickle.dump(self.productFsa.transitions, open("../transitions.p","wb"))
        
        # Sanity checks
        self.sanityChecksForStatesAndTransitions(numAgents, self.productFsa.states, self.productFsa.transitions)            
                
        # Product states and transitions from adversary specific parameters
        self.outStates, self.outTransitions = self.filterGameFromAdversaryParameters(self.productFsa.states, 
                                                                                   self.productFsa.transitions,
                                                                                   agentStates, agentTransitions)

        # Sanity checks
        #self.sanityChecksForStatesAndTransitions(outStates, outTransitions)                 
        
        # Agent transitions and states
        # agentTransitions = gameTransitions.difference(advTransitions)
        # agentStates = set(gameStates.keys()).difference(advStates)
        
        # Add dummy index to make agent states and transitions consistent with product states and transitions
        # agentStates, agentTransitions = self.addDummyStateTupleIndex(agentStates, agentTransitions, dummyIndexVal = 0)
        
        # Sanity checks
        # self.sanityChecksForStatesAndTransitions(agentStates, agentTransitions)              

        # Combine agent and adversary parameters
        # totalStates = set.union(set(productStates), agentStates)
        # totalTransitions = set.union(productTransitions, agentTransitions)
        
        # Get the updated set of transitions
        # updateTransitions = gameTransitions.difference(advTransitions)
        # updateTransitions.update(transitions)
        
        # Sanity check to see if there are any transitions lost while updates
        # prevAdvTransitions = advTransitions.difference(gameNewTransitions)
        # t = prevAdvTransitions.difference(transitions)
        # assert not t, "Some transitions are lost!"
        
        # Sanity check to see if there is any change between game and update transitions
        # assert gameTransitions == updateTransitions, "Game and update transitions are different!"
                 
        # return totalStates, totalTransitions
        return self.outStates, self.outTransitions

    def filterAdversaryFromGameParameters(self, gameStates, gameTransitions, advName):
        '''Filter adversary's game parameters'''

        advStates = set()
        advTrans = set()
        agentStates = set()
        agentTrans = set()
            
        # Filter adversary states
        for i in gameStates.keys():
            if gameStates[i].userID[-1] == advName:
                advStates.add(i)
            else:
                agentStates.add(i)
                
        # Filter transitions based on whose turn it is    
        for t in gameTransitions:
            if gameStates[t[0]].userID[-1] == advName:
                targetStateUserID = deepcopy(gameStates[t[1]].userID)
                self.nextPlayerName = targetStateUserID[-1]
                targetStateUserID[-1] = advName
                targetStateMachineID = "_".join(map(str, targetStateUserID))                
                advTrans.add((t[0], targetStateMachineID, t[2]))
            else:
                agentTrans.add(t)
                        
        return advStates, advTrans, agentStates, agentTrans

    def filterGameFromAdversaryParameters(self, prodInStates, prodInTransitions, 
                                                agentStates, agentTransitions,
                                                stateNonGrammarInd = 1, stateGrammarInd = 0):
        '''Filter adversary's game parameters'''

        prodOutStates = deepcopy(prodInStates)
        prodOutStates.extend(itertools.product(self.grammarFsa.states, agentStates))
        
        prodOutTrans = set()
        tempDict = {}
        
        # Sanity check to see if next player name is available
        assert self.nextPlayerName, "Next player name not available"
                
        # Filter transitions based on whose turn it is    
        for t in prodInTransitions:
            targetStateMachineID = t[1][stateNonGrammarInd][:-2]+self.nextPlayerName
            tempTrans = (t[0], (t[1][stateGrammarInd], targetStateMachineID), t[2])                
            prodOutTrans.add(tempTrans)
            if tempDict.has_key(targetStateMachineID):
                tempDict[targetStateMachineID].add(t[1][stateGrammarInd])
            else:
                tempDict[targetStateMachineID] = set([t[1][stateGrammarInd]])
        
        updated = True
        while(updated): 
            updated = False   
            tempDict1 = {}
            
            for t in agentTransitions:
                if tempDict.has_key(t[0]):
                    updated = True
                    for g in tempDict[t[0]]:
                        tempTrans = ((g, t[0]), (g, t[1]), t[2])
                        prodOutTrans.add(tempTrans)
                        
                        if tempDict1.has_key(t[1]):
                            tempDict1[t[1]].add(g)
                        else:
                            tempDict1[t[1]] = set([g])
                            
            tempDict = deepcopy(tempDict1)
                                    
        return prodOutStates, prodOutTrans

    def generateGrammarFsa(self, grammarObj, agentAlphabet):
        '''Generate the fsa corresponding to grammar'''
        
        grammarName = grammarObj.grammarName
        grammarParams = grammarObj.grammarParams[0]
        grammarFactors = grammarObj.grammar
        alphabet = list(agentAlphabet)
        
        # The alphabet length is less than the kFactor length, repeat
        if len(alphabet) < grammarParams:
            alphabet = [alphabet[0]]*grammarParams
        
        allFactors = set(itertools.product(alphabet, repeat=grammarParams))
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
                outTransitions.add( ( (str(dummyIndexVal),) + t[0], (str(dummyIndexVal),) + t[1], t[2]) )
            else:
                outTransitions.add( ( (str(dummyIndexVal), t[0]), (str(dummyIndexVal), t[1]), t[2]) )
                       
        return outStates, outTransitions    
    
    def sanityChecksForStatesAndTransitions(self, numAgents, states = [], transitions = [], maxGrammarLen = 3):    
        '''Check if all states and transitions are of the right form'''
        for state in list(states):
            assert len(state[0]) < maxGrammarLen, "First component of state too long: %s" % (str(state))
            assert len(state[1]) == numAgents*6+4, "Second component of state not the right size: %s" % (str(state))
        for t in transitions:
            for state in t[:2]:
                assert len(state[0]) < maxGrammarLen, "First component of state too long: %s" % (str(t))
                assert len(state[1]) == numAgents*6+4, "Second component of state not the right size: %s" % (str(t))        
        return
       
if __name__ == '__main__':
    tempFsa = compileRE('.*b.*b')
    tempFsa.view()
    
    tempFsa2 = complement(compileRE('.*b.*b'))
    tempFsa2.view()
    
    
    
    
    
    