"""
Created on Thu Feb 26 13:15:18 2018
@author: Pan Chen
This program provides a function that implement US21 in Sprint 1.
"""

user_story = 21


def correct_gender(info):
    fams = info['fams']
    indis = info['indis']
    rt = []
    for i in fams:
        rt.append(proper(fams, i, indis))

        id_wife = fams[i]['WIFE']
        gender_wife = indis[id_wife]['SEX']
        if gender_wife == 'M':
            rt.append(
                {'error': 'ERROR', 'scope': 'INDIVIDUAL', 'user_story': 'US21', 'line_number': indis[id_wife]['line'],
                 'id': indis[id_wife]['INDI'], 'description': 'Wife gender should be F'})

    return rt


def proper(fams, i, indis):
    id_husb = fams[i]['HUSB']
    gender_husb = indis[id_husb]['SEX']
    if gender_husb == 'F':
        return {'error': 'ERROR', 'scope': 'INDIVIDUAL', 'user_story': 'US' + str(user_story),
             'line_number': indis[id_husb]['line'],
             'id': indis[id_husb]['INDI'], 'description': 'Husband gender should be M'}