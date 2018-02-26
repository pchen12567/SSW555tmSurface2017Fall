"""
Created on Thu Feb 25 22:50:18 2018
@author: Pan Chen
This program provides a function that implement US23 in Sprint 1.
"""

def unique_indi(info):
    indis = info.INDIS
    l = []
    for i in indis:
        item = indis[i]
        tup = (item.get('NAME'), item.get("BIRTDATE"))
        if l.count(tup) != 0:
            return False
        l.append(tup)

    return True