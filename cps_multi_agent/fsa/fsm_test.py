'''
Created on Nov 11, 2014

@author: prasanna
'''
import FSA
from reCompiler import compileRE

if __name__ == '__main__':
    myFSA = compileRE('a(b|c*)')
    myFSA.view()
    
#     states = ['r1','r2']
#     alphabet = ['a','b']
#     transitions = [[]]