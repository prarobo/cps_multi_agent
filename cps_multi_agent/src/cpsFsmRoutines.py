'''
Created on Nov 13, 2014

@author: prasanna

General routines/ helper functions
'''

'''Nests each element in an input list inside another list'''
def PutListElementsInList(inList):
    outList = []
    for i in inList:
        outList.append([i])       
    return outList

'''Unit Test'''
if __name__=="__main__":
    temp = PutListElementsInList([1,2,3])
    print temp

    
