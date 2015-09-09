from __future__ import print_function
'''
Created on Jul 24, 2015

@author: prasanna
@about: Compares log files between runs in different computers
'''

'''The results of the project when run in different computers yields different results
This file compares the logs from differnet runs to establish the differences'''

__author__="Prasanna Kannappan <prasanna@udel.edu>"

from pprint import pprint
import sys
sys.path.append("../gui")
sys.path.append("../fsa")
sys.path.append("../src")
sys.path.append("../matlab_integ")

import cPickle as pickle
import os
from deepdiff import DeepDiff
from Automata import ProductBuchi

class RunComparer(object):
    '''Provides run comparison functions by verifying run logs'''
    def __init__(self, numRuns, logFilenames, logFileExtn, logFolders):
        # Sanity check
        assert len(logFolders)==numRuns, "Mismatch between number of log folders and number of runs to compare"

        self.logFilenames = logFilenames
        self.logFileExtn = logFileExtn
        self.logFolders = logFolders 
        self.numRuns = numRuns
        
        # Datastructure that stores all run information
        self.runData = [{} for _ in xrange(self.numRuns)]
        
    def loadAllLogs(self):
        '''Loads all available log files'''
        map(self.loadLog, self.logFilenames)
        return
        
    def loadLog(self, logFilename):
        '''Loads a given log file from different runs'''
        logData = []
        for r in xrange(self.numRuns):
            currFilepath = os.path.join(self.logFolders[r], logFilename + self.logFileExtn)
            
            if os.path.isfile(currFilepath):
                logData.append(pickle.load(open(currFilepath,"rb")))
            else:
                print ("File not found:", currFilepath)
                print ("Skipping file loading")
                return        
        
        # Saving loaded files into rundata
        print ("Log load: %s loaded" % logFilename)
        for r in xrange(self.numRuns):
            self.runData[r][logFilename] = logData[r]
            
        return
    
    def compareAllLogs(self):
        '''Loads all available log files'''
        map(self.compareLog, self.logFilenames)
        return
    
    def compareLog(self, logFilename):
        '''Compare a log file from different runs'''
        refLog = self.runData[0][logFilename]
        
        for r in xrange(1,self.numRuns):
            if not refLog == self.runData[r][logFilename]:
                print ("Log comparison: %s match failed" % logFilename)
                return False
            
        print ("Log comparison: %s match success" % logFilename)
        return True   
    
    def compareSpecificStatePolicies(self, states): 
        '''Compare the policies at specific states'''
        
        for st in states:
            for r in xrange(self.numRuns):
                print (self.runData[r]['policyLog'][1][st])
                
    def comparePolicyMismatches(self, policyIndex):
        '''Display the mismatches at a policy given by policy index
        between different runs'''
        
        print ("\nComparing Policies:\t",)
        if self.runData[0]['policyLog'][policyIndex] == self.runData[1]['policyLog'][policyIndex]:
            print ("No mismatch found in policy")
            return
        else:
            print ("Mismatch found")
            
        numMismatches = 0
        
        for st in self.runData[0]['policyLog'][policyIndex].keys():
            if self.runData[0]['policyLog'][policyIndex][st] \
            != self.runData[1]['policyLog'][policyIndex][st]:
                print (st, "\t:\t", self.runData[0]['policyLog'][policyIndex][st], "\t",) 
                print (self.runData[1]['policyLog'][policyIndex][st])
                numMismatches += 1
        print ("Mismatch stat:\t", numMismatches, " (out of", len(self.runData[0]['policyLog'][policyIndex].keys()), ")") 
        return
    
    def compareTurnProductMismatches(self):
        '''Compares mismatches in turn product'''
        
        print ("\nComparing turn product:\t",)
        if self.runData[0]['gameAutomaton'] == self.runData[1]['gameAutomaton']:
            print ("No mismatch found")
            return
        else:
            print ("Mismatch found")
        
        objectAttr = self.runData[0]['gameAutomaton'].__dict__.keys()
        for currAttr in objectAttr:
            if getattr(self.runData[0]['gameAutomaton'], currAttr) \
            != getattr(self.runData[1]['gameAutomaton'], currAttr):
                print ("Mismatch found:\t\t", currAttr)
            else:
                print ("No mismatch found:\t", currAttr)
                
        print ("\nComparing turn product states keys:\t",)
        if sorted(self.runData[0]['gameAutomaton'].gameStates.keys()) \
        == sorted(self.runData[1]['gameAutomaton'].gameStates.keys()):
            print ("No mismatch found")
            return
        else:
            print ("Mismatch found")        
        return    
    
    def compareInitLog(self):
        '''Compares the initial input that goes into generating policy'''
        
        print ("\nComparing init log:\t",)
        if self.runData[0]['initLog'] == self.runData[1]['initLog']:
            print ("No mismatch found")
            return
        else:
            print ("Mismatch found")            

        objectAttr = self.runData[0]['initLog'].keys()
        for currAttr in objectAttr:
            if self.runData[0]['initLog'][currAttr] != self.runData[1]['initLog'][currAttr]:
                print ("Mismatch found:\t\t", currAttr)
            else:
                print ("No mismatch found:\t", currAttr)
        return             

    def compareInitMatlabObj(self):
        '''Compares the initial input that goes into generating policy'''
        
        print ("\nComparing init matlab obj:\t",)
        if self.runData[0]['initLog']['matlabObj'] == self.runData[1]['initLog']['matlabObj']:
            print ("No mismatch found")
            return
        else:
            print ("Mismatch found")            

        objectAttr = self.runData[0]['initLog']['matlabObj'].__dict__.keys()
        for currAttr in objectAttr:
            if getattr( self.runData[0]['initLog']['matlabObj'], currAttr) \
            != getattr( self.runData[1]['initLog']['matlabObj'], currAttr):
                print ("Mismatch found:\t\t", currAttr)
            else:
                print ("No mismatch found:\t", currAttr)
                
        print ("\nComparing init matlab obj dist keys:\t",)
        if sorted(self.runData[0]['initLog']['matlabObj'].dist.keys()) \
        == sorted(self.runData[1]['initLog']['matlabObj'].dist.keys()):
            print ("No mismatch found")
            return
        else:
            print ("Mismatch found")  
                       
        objectAttr = self.runData[0]['initLog']['matlabObj'].dist.keys()
        for currAttr in objectAttr:
            if self.runData[0]['initLog']['matlabObj'].dist[currAttr] \
            != self.runData[1]['initLog']['matlabObj'].dist[currAttr]:
                print ("Mismatch found:\t\t", currAttr, "\t",
                       self.runData[0]['initLog']['matlabObj'].dist[currAttr], "\t",
                       self.runData[1]['initLog']['matlabObj'].dist[currAttr])
            else:
                print ("No mismatch found:\t", currAttr)                               
        return    
    
    def productAutomatonTest(self):
        '''Computes product automaton intermediate result and saves to pickle file'''
        print ("Computing product automaton ...")
        Buchi = self.runData[1]['initLog']['matlabObj'].buchi
        GTS = self.runData[1]['initLog']['matlabObj'].GTS
        
        P=ProductBuchi()
        P.fromBAndTS(Buchi,GTS,'E0_22_R0_00_R1_10_T_E0')
        pickle.dump(P, open('productAutomaton.p', 'wb'))
       
if __name__=="__main__":
    # Folders where logs files are stored
    folder1 = "kevin_logs3"
    folder2 = "prasanna_logs4"
    logFolders = [folder1, folder2]
    
    # Log file names
    logFilenames = ["actionLog",
                    "gameAutomaton",
                    "gameLabels",
                    "policyLog",
                    "stateLog",
                    "sysLog",
                    "initLog"]
    
    logFileExtn = ".p"
    numRuns = 2
    
    # States where policies are to be compared
    states = ['E0_12_R0_00_R1_10_T_R0','E0_12_R0_11_R1_10_T_R1']
    
    # Declare run comparer object
    myRunComparer = RunComparer(numRuns, logFilenames, logFileExtn, logFolders)
    
    # Load all log files
    myRunComparer.loadAllLogs()
    
    # Compare all log files
    myRunComparer.compareAllLogs()
    
    # Compare mismatches in turn product
    myRunComparer.compareTurnProductMismatches()
    
    # Compare mismatches in policies
    #myRunComparer.comparePolicyMismatches(0)
    
    # Compare mismatches in initial inputs for policy generation
    myRunComparer.compareInitLog()

    # Compare mismatches in initial matlab for policy generation
    #myRunComparer.compareInitMatlabObj()
        
    # Print specific state policies
    # myRunComparer.compareSpecificStatePolicies(states)
    
    # Saves the product automaton
    myRunComparer.productAutomatonTest()
    
    
    
    
