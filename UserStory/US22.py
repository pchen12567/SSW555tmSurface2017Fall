user_story = 22


# for this method, it is solved in the parsing gedcom method, since we can't have duplicated key in a dict.

def unique_id(info):
    rt = []
    fams = info['fams']
    indis = info['indis']
    scope = "INDIVIDUAL"
    ids = []
    for i in indis:
        item = indis[i]
        for inid in ids:
            if inid == item['INDI']:
                rt.append({'error': 'ERROR',
                           'scope': scope,
                           'user_story': 'US' + str(user_story),
                           'line_number': item['line'],
                           'id': item['INDI'],
                           'description': "ID is duplicated with " + inid})
        ids.append(item['INDI'])
    scope = "FAMILY"
    ids = []
    for i in fams:
        item = fams[i]
        for inid in ids:
            if inid == item['FAM']:
                rt.append({'error': 'ERROR',
                           'scope': scope,
                           'user_story': 'US' + str(user_story),
                           'line_number': item['line'],
                           'id': item['INDI'],
                           'description': "ID is duplicated with " + inid})
        ids.append(item['FAM'])
    return rt