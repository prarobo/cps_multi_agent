'''
Created on Nov 17, 2014

@author: prasanna
'''
from types import ListType

def generateKFactors(inStr, kF, saveSmallerFactors = True):
    '''
    Generate all k factors of a input string
    '''
    assert isinstance(inStr, ListType), "Input not a string, error!" 
    assert kF>=0, "K-value of grammar has to be greater than 0" 
    
    kFactors = set([])
    
    currStrList = list(inStr)
    
    #Check if string length is less than k factor
    if len(currStrList)<=kF:
        if saveSmallerFactors:
            kFactors.add(tuple(currStrList))
        return kFactors

    else:
        saveSmallerFactors = False
           
        #Getting k factors
        for i in range(len(currStrList)-kF+1):
            subStr = currStrList[i:i+kF]
            kFactors.add(tuple(subStr))
    
    if kF == 0:    
        return kFactors
    else:
        if saveSmallerFactors:
            return kFactors.union(generateKFactors(inStr, kF-1, saveSmallerFactors))
        else:
            return kFactors

def generateKSubsequences(inStr, kF, saveSmallerFactors = True):
    '''
    Generate all k subsequences of a input string
    '''
    kSeq = set([])
    
    currStrList = list(inStr)

    # Check if kF is 1
    if kF==1 or kF==0:
        return generateKFactors(inStr,1)    

    #Check if string length is less than k factor
    if len(currStrList)<=kF:
        if saveSmallerFactors:
            kSeq.add(tuple(currStrList))
        return kSeq
    else:
        saveSmallerFactors = False
        
        # Recursive case
        for i in range(len(currStrList)):
            currChar = currStrList[i]
            currRemStr = currStrList[i+1:]
            outFactor = generateKSubsequences(currRemStr, kF-1, saveSmallerFactors)
            kSeq.update([tuple([currChar]+list(i)) for i in outFactor if i])
        
    #maxFLen = max(len(x.split('-')) for x in kSeq);
    #kSeq = [x for x in kSeq if len(x.split('-'))==maxFLen]
    
    if kF == 0:    
        return kSeq
    else:
        if saveSmallerFactors:
            return kSeq.union(generateKSubsequences(inStr, kF-1, saveSmallerFactors))
        else:
            return kSeq
        
    
'''
    Unit tests
'''
if __name__=="__main__":
    kFactors = generateKFactors('g-o-o-d-g-o-o-g'.split('-'), 3)
    print kFactors    
    
    kSeq = generateKSubsequences('a-b-c-d'.split('-'), 3)
    print kSeq