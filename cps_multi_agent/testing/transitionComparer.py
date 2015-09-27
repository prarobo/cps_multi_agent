'''
Created on Sep 25, 2015

@author: prasanna
'''

import cPickle as pickle

if __name__ == '__main__':
    transitions1 = pickle.load(open('../transitions1.p','rb'))
    transitions2 = pickle.load(open('../transitions2.p','rb'))
    
    print "Transtions1: %d"%(len(transitions1))
    print "Transtions2: %d"%(len(transitions2))
    
    oCounter1, eCounter1, wCounter1 = 0, 0, 0
    oTransitions1, eTransitions1, wTransitions1, oTransitions1_1, oTransitions1_2 = set(), set(), set(), set(), set()
    
    for t in transitions1:
        if t[2] == 'oo0': 
            oCounter1 += 1
            oTransitions1.add(t)
            if t[0][0] == '1':
                oTransitions1_1.add(t)
            if t[0][0] == '2':
                oTransitions1_2.add(t)
        if t[2] == 'ww1': 
            wCounter1 += 1
            wTransitions1.add(t)
        if t[2] == 'ee1': 
            eCounter1 += 1
            eTransitions1.add(t)

    oCounter2, eCounter2, wCounter2 = 0, 0, 0
    oTransitions2, eTransitions2, wTransitions2, oTransitions2_1, oTransitions2_2 = set(), set(), set(), set(), set()
            
    for t in transitions2:
        if t[2] == 'oo0': 
            oCounter2 += 1
            oTransitions2.add(t)
            if t[0][0] == '2':
                oTransitions2_1.add(t)
            if t[0][0] == '1':
                oTransitions2_2.add(t)
        if t[2] == 'ww1': 
            wCounter2 += 1
            wTransitions2.add(t)
        if t[2] == 'ee1': 
            eCounter2 += 1
            eTransitions2.add(t)
            
    oTransDiff = oTransitions2.difference(oTransitions1)
    
    wTransCommon = wTransitions2.intersection(wTransitions1)
    wTransDiff = wTransitions2.difference(wTransitions1)
        
    print "oCounter = %d\t%d"%(oCounter1, oCounter2)
    print "eCounter = %d\t%d"%(eCounter1, eCounter2)
    print "wCounter = %d\t%d"%(wCounter1, wCounter2)
    pass
    