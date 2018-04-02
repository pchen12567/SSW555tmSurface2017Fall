"""
Created on Thu Feb 25 22:50:18 2018
@author: Pan Chen
This program provides a function that implement US23 in Sprint 1.
"""

user_story = 23


def unique_indi(info):
    indis = info['indis']
    l = []
    rt = []
    for i in indis:
        item = indis[i]
        tup = (item.get('NAME'), item.get("BIRTDATE"))
        if l.count(tup) != 0:
            rt.append(
                {'error': 'ERROR',
                 'scope': 'INDIVIDUAL',
                 'user_story': 'US' + str(user_story),
                 'line_number': str(item['line']),
                 'id': item['INDI'],
                 'description': 'Duplicate name and birthday'})
        l.append(tup)
    return rt
