'''
Created on Nov 16, 2014

@author: prasanna
'''

def isNumber(val):
    '''
    Tests is the input is a number
    '''
    try:
        val + 1
        return True
    except TypeError:
        return False