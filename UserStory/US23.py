"""
Created on Thu Feb 25 22:50:18 2018
@author: Pan Chen
This program provides a function that implement US23 in Sprint 1.
"""


def unique_indi(info):
    indis = info['indis']
    l = []
    rt = []
    for i in indis:
        item = indis[i]
        tup = (item.get('NAME')['value'], item.get("BIRTDATE")['value'])
        if l.count(tup) != 0:
            rt.append(
                {'error': 'Error', 'scope': 'individual', 'user_story': 'US23', 'line_number': item.get('NAME')['line'],
                 'id': item['INDI']['value'], 'description': 'Duplicate name and birthday'})
        l.append(tup)

    return rt
