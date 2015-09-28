'''
Created on Jul 30, 2015

@author: prasanna
'''

from cpsFsmStrings import generateKFactors, generateKSubsequences
import itertools

class fsmGrammar(object):
    '''Class for computing the grammar''' 

    def __init__(self, grammarType):
        '''Constructor'''
        self.grammarName, self.grammarParams = self.identifyGrammarType(grammarType)
        self.moveSeq = [] #Sequence of moves played by agent
        self.grammar = set() #Grammar of agent (move grammar + default grammar)
        self.moveGrammar = set() #Grammar computed from moves of agent
        self.defaultGrammar = set() #Default grammar to be used along with the computed grammar
        return
        
    def identifyGrammarType(self, grammarType):
        '''Parse grammar string to identify the type of grammar'''
        grammarName = grammarType.split('_')[0]
        grammarParams = map(int,grammarType.split('_')[1:])
        return grammarName, grammarParams
        
    def addMove(self, currMove):
        '''Add an input move to the sequence of moves used to compute grammar'''
        # Add new move to move list
        self.moveSeq.append(currMove)
        
        # Make the move sequence equal to k value of grammar by repeating first move k times
        if len(self.moveSeq) < self.grammarParams[0]:
            self.moveSeq = self.moveSeq*self.grammarParams[0]
        
        # Compute new grammar    
        self.moveGrammar = self.computeGrammar(self.moveSeq)
        
        # Update final grammar
        self.grammar = set.union(self.moveGrammar, self.defaultGrammar)
        
        return
        
    def computeGrammar(self, moveSeq):
        '''Compute the grammar from the input move sequence'''
        if self.grammarName == 'SL':
            return self.computeSLkGrammar(self.grammarParams[0], moveSeq)
        elif self.grammarName == 'SP':
            return self.computeSPkGrammar(self.grammarParams[0], moveSeq)
        else:
            print "Unknown grammar type"
            return None        
        
    def computeSLkGrammar(self, kval, moveSeq):
        '''Compute the SL-k grammar from the input move sequence'''
        return generateKFactors(moveSeq, kval)
        
    def computeSPkGrammar(self, kval, moveSeq):
        '''Compute the SP-k grammar from the input move sequence'''
        return generateKSubsequences(moveSeq, kval)
    
    def computeDefaultGrammar(self, defaultAction, alphabetList):
        '''Compute default grammar. Useful to avoid deadlocks'''
        
        self.defaultGrammar.update(set(itertools.product([defaultAction], alphabetList)))
        self.defaultGrammar.update(set(itertools.product(alphabetList, [defaultAction])))
        return
                                   
    
'''Unit tests'''
if __name__ == "__main__":
    moveSeq = ['a','b','c','d','e','f','g','h']
    myFsmGrammar = fsmGrammar('SP_2')
    
#     for i in moveSeq:
#         myFsmGrammar.addMove(i)
#         print myFsmGrammar.grammar

    for i in moveSeq:
        myFsmGrammar.addMove(i)
        print myFsmGrammar.grammar        
