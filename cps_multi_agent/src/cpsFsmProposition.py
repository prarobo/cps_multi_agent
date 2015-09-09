'''
Created on Nov 11, 2014

@author: prasanna
@about: Datastructures connected to propositions and the functions
that operate on propositions
'''

import sys
from UtilityFunction import *

class fsmProposition(object):
    '''
    FSM atomic proposition class
    '''
    def __init__(self, name, valueSet, defaultValue):
        '''
        Constructor
        '''
        self.name = name    #Name of proposition
        self.positions = [] #Position where the proposition is true
        self.valueSet = valueSet    #Set of values the proposition can take
        
        if (defaultValue in self.valueSet):
            self.defaultValue = defaultValue    #default value of proposition
            self.currentValue = defaultValue    #current value of proposition
        else:
            sys.stderr.write("Default proposition value not in value set for proposition %s\n" % self.name)
            sys.stderr.write("Exiting function")
            sys.exit()        
        return
    def assignPropositionValue(self, value):
        '''
        Assign value to proposition
        '''
        if (value in self.valueSet):
            self.currentValue = value    #current value of proposition
        else:
            sys.stderr.write("Proposition value not in value set for proposition %s\n" % self.name)
            sys.stderr.write("Exiting function")
            sys.exit()        
        return
    def copyProposition(self):  
        '''
        Copy constructor or deep copy a proposition
        '''  
        outCopy = fsmProposition(self.name, self.valueSet, self.defaultValue) 
        outCopy.currentValue = self.currentValue
        return outCopy  
 
class fsmPropositionList():
    '''
    FSM atomic proposition list
    '''    
    def __init__(self, propositionNames=None):
        '''
        Constructor
        inputPropositionList = [proposition name]
        inputPropositionList = ['prop1','prop2']
        '''
        self.propositionList = {}
        if propositionNames!=None:            
            self.generatePropositionGrid(propositionNames)                                 
        return
    
    
    def generatePropositionGrid(self, propositionNames):
        '''
        Generate list of propositions
        '''          
        for currItem in propositionNames:
            self.propositionList[currItem] = []                      
        return
    
    def assignPropositionGrid(self, inputPropositionList):
        '''
        Assign proposition values 
        inputPropositionList = [[proposition name, linear index of grid],...]
        e.g. inputPropositionList = [['prop1',10],['prop2',20]]
        '''
        for currItem in inputPropositionList:
            if (currItem[0] in self.propositionList.keys()):
                if isNumber(currItem[1]):
                    self.propositionList[currItem[0]].append(currItem[1])        
                else:
                    self.propositionList[currItem[0]].extend(currItem[1])
                self.propositionList[currItem[0]] = list(set(self.propositionList[currItem[0]]))
            else:
                sys.stderr.write("Proposition key not found\n")
                sys.stderr.write("Exiting function")
                sys.exit()                        
        return
    
    def copyPropositionGrid(self):
        ''' Deep copy of proposition grid'''        
        outCopy = fsmPropositionList()
        outCopy.propositionList = dict(self.propositionList)
        return outCopy
     
    def mergePropositionGrids(self, prop):
        '''
        Merge proposition grids with
        a special merge function for duplicate propositions
        '''
        
        for propi in prop:
            propSelf = self.propositionList.copy()
            propCurr = propi
            
            propNamesSelf = set(propSelf.keys())       
            propNamesCurr = set(propCurr.keys())
            
            #Intersection
            propNamesIntersect = propNamesSelf.intersection(propNamesCurr)
            
            #Set 0 only
            propNamesSelfOnly = propNamesSelf.difference(propNamesIntersect)
            
            #Set 1 only
            propNamesCurrOnly = propNamesCurr.difference(propNamesIntersect)
            
            #Union
            propNamesUnion = propNamesSelf.union(propNamesCurr)
            
            for i in propNamesUnion:
                if i in propNamesSelfOnly:
                    self.assignPropositionGrid([[i, propSelf[i][:]]])
                elif i in propNamesCurrOnly:
                    self.assignPropositionGrid([[i, propCurr[i][:]]])
                else: #Common propositions
                    posListSelf = set(propSelf[i][:])
                    posListCurr = set(propCurr[i][:])
                    
                    #Assigning only common proposition values
                    posList = posListSelf.union(posListCurr)
                    self.assignPropositionGrid([[i, posList]])
        return
                
if __name__=="__main__":
    '''
    Unit test for proposition classes
    '''

    testFsmPropositionList = fsmPropositionList(['test1','test2'])
    testFsmPropositionList.assignPropositionGrid([['test1',0], ['test2',[1,2]]])
        
    pass   