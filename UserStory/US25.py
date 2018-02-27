user_story = 25


def unique_first_name(info):
    rt = []
    fams = info['fams']
    indis = info['indis']
    for i in fams:
        fam = fams[i]
        fc = fam['CHIL']
        if type(fc) is str:
            fc = [fc]
        children = [indis[child]['NAME'].split(' ')[0] for child in fc]
        for child in children:
            if children.count(child) > 1:
                rt.append({'error': 'ERROR',
                           'scope': "FAMILY",
                           'user_story': 'US' + str(user_story),
                           'line_number': fam['line'],
                           'id': fam['FAM'],
                           'description': "Duplicated first name of child in the same family."})
                break
    return rt
