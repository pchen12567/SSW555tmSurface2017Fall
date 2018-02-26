"""
Created on Thu Feb 26 13:15:18 2018
@author: Pan Chen
This program provides a function that implement US21 in Sprint 1.
"""


def correct_gender(info):
    fams = info['fams']
    indis = info['indis']
    rt = []
    for i in fams:
        id_husb = fams[i]['HUSB']['value']
        gender_husb = indis[id_husb]['SEX']['value']
        if gender_husb == 'F':
            rt.append(
                {'error': 'Error', 'scope': 'individual', 'user_story': 'US23', 'line_number': indis[id_husb]['NAME']['line'],
                 'id': indis[id_husb]['INDI']['value'], 'description': 'Husband gender should be M'})

        id_wife = fams[i]['WIFE']['value']
        gender_wife = indis[id_wife]['SEX']['value']
        if gender_wife == 'M':
            rt.append(
                {'error': 'Error', 'scope': 'individual', 'user_story': 'US23', 'line_number': indis[id_wife]['NAME']['line'],
                 'id': indis[id_wife]['INDI']['value'], 'description': 'Wife gender should be F'})

    return rt
