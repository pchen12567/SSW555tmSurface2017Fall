from util.date_parser import date_parser, time_delta
from util.error_constructor import error_constructor
import unittest

user_story = 9


def birth_before_death_of_parents(info):
    fams = info['fams']
    indis = info['indis']
    rt = []
    for i in indis:
        indi = indis[i]
        famc = indi.get('FAMC')
        if famc is None:
            continue
        fam = fams.get(famc)
        if fam is None:
            continue
        c_birth = date_parser(indi["BIRTDATE"])
        try:
            mather = indis[fam["WIFE"]]
            m_death = date_parser(mather['DEATDATE'])
            if time_delta(c_birth, m_death) < 0:
                rt.append(
                    error_constructor("ERROR", "INDIVIDUAL", user_story, indi['line'], i,
                                      "Birth after mother's death."))
        except:
            pass
        try:
            father = indis[fam["HUSB"]]
            f_death = date_parser(father["DEATDATE"])
            if time_delta(c_birth, f_death) < -270:
                rt.append(error_constructor("ERROR", "INDIVIDUAL", user_story, indi['line'], i,
                                            "Birth after 9 months of father's death."))
        except:
            pass
    return rt


class TestBirthBeforeDeathOfParents(unittest.TestCase):
    info1 = {
        'fams': {
            'F01': {
                'line': 44,
                'FAM': 'F01',
                'MARRDATE': '5 FEB 207',
                'HUSB': 'I01',
                'WIFE': 'I02',
                'CHIL': [
                    'I03',
                    'I04'
                ]
            },
            'F02': {
                'line': 88,
                'FAM': 'F02',
                'MARRDATE': '26 JUN 228',
                'DIVDATE': '18 SEP 234',
                'HUSB': 'I03',
                'WIFE': 'I05',
                'CHIL': 'I07'
            },
            'F03': {
                'line': 97,
                'FAM': 'F03',
                'MARRDATE': '10 OCT 237',
                'HUSB': 'I03',
                'WIFE': 'I06',
                'CHIL': 'I08'
            },
            'F04': {
                'line': 122,
                'FAM': 'F04',
                'MARRDATE': '18 AUG 234',
                'HUSB': 'I04',
                'WIFE': 'I09',
                'CHIL': 'I10'
            }
        },
        'indis': {
            'I01': {
                'line': 5,
                'INDI': 'I01',
                'NAME': 'Yi /Sima/',
                'BIRTDATE': '28 APR 179',
                'SEX': 'M',
                'DEATDATE': '7 SEP 251',
                'FAMS': 'F01'
            },
            'I02': {
                'line': 14,
                'INDI': 'I02',
                'NAME': 'Chunhua /Zhang/',
                'BIRTDATE': '12 JUN 189',
                'SEX': 'F',
                'DEATDATE': '21 DEC 247',
                'FAMS': 'F01'
            },
            'I03': {
                'line': 23,
                'INDI': 'I03',
                'NAME': 'Shi /Sima/',
                'BIRTDATE': '9 AUG 208',
                'SEX': 'M',
                'DEATDATE': '23 MAR 255',
                'FAMC': 'F01',
                'FAMS': [
                    'F02',
                    'F03'
                ]
            },
            'I04': {
                'line': 34,
                'INDI': 'I04',
                'NAME': 'Zhao /Sima/',
                'BIRTDATE': '15 OCT 211',
                'SEX': 'M',
                'DEATDATE': '6 SEP 265',
                'FAMC': 'F01',
                'FAMS': 'F04'
            },
            'I05': {
                'line': 52,
                'INDI': 'I05',
                'NAME': 'Wei /Xiahou/',
                'BIRTDATE': '7 JUL 211',
                'SEX': 'F',
                'DEATDATE': '18 SEP 234',
                'FAMS': 'F02'
            },
            'I06': {
                'line': 61,
                'INDI': 'I06',
                'NAME': 'Weiyu /Yang/',
                'BIRTDATE': '17 MAR 214',
                'SEX': 'F',
                'DEATDATE': '25 NOV 278',
                'FAMS': 'F03'
            },
            'I07': {
                'line': 70,
                'INDI': 'I07',
                'NAME': 'Rou /Sima/',
                'BIRTDATE': '11 AUG 230',
                'SEX': 'F',
                'DEATDATE': '19 MAY 275',
                'FAMC': 'F02'
            },
            'I08': {
                'line': 79,
                'INDI': 'I08',
                'NAME': 'You /Sima/',
                'BIRTDATE': '11 AUG 238',
                'SEX': 'M',
                'DEATDATE': '20 FEB 283',
                'FAMC': 'F03'
            },
            'I09': {
                'line': 104,
                'INDI': 'I09',
                'NAME': 'Yuanji /Wang/',
                'BIRTDATE': '14 DEC 217',
                'SEX': 'F',
                'DEATDATE': '20 APR 268',
                'FAMS': 'F04'
            },
            'I10': {
                'line': 113,
                'INDI': 'I10',
                'NAME': 'Yan /Sima/',
                'BIRTDATE': '21 JAN 236',
                'SEX': 'M',
                'DEATDATE': '16 MAY 290',
                'FAMC': 'F04'
            }
        },
        'errors': []
    }

    info2 = {
        'fams': {'F01': {'line': 44, 'FAM': 'F01', 'MARRDATE': '5 FEB 207', 'HUSB': 'I01', 'WIFE': 'I02',
                         'CHIL': ['I03', 'I04']},
                 'F02': {'line': 88, 'FAM': 'F02', 'MARRDATE': '26 JUN 228', 'DIVDATE': '18 SEP 234',
                         'HUSB': 'I03', 'WIFE': 'I05', 'CHIL': 'I07'},
                 'F03': {'line': 122,
                         'FAM': 'F03',
                         'MARRDATE': '18 AUG 232',
                         'HUSB': 'I04',
                         'WIFE': 'I09',
                         'CHIL': 'I10'}},
        'indis': {
            'I01': {'line': 5, 'INDI': 'I01', 'NAME': 'Yi /Sima/', 'BIRTDATE': '28 APR 179', 'SEX': 'F',
                    'DEATDATE': '7 SEP 251', 'FAMS': 'F01'},
            'I02': {'line': 14, 'INDI': 'I02', 'NAME': 'Chunhua /Zhang/', 'BIRTDATE': '12 JUN 189', 'SEX': 'M',
                    'DEATDATE': '21 DEC 247', 'FAMS': 'F01'},
            'I03': {'line': 23, 'INDI': 'I03', 'NAME': 'Shi /Sima/', 'BIRTDATE': '9 AUG 208', 'SEX': 'M',
                    'DEATDATE': '23 MAR 255', 'FAMC': 'F01', 'FAMS': ['F02', 'F03']},
            'I04': {'line': 34, 'INDI': 'I04', 'NAME': 'Shi /Sima/', 'BIRTDATE': '28 APR 179', 'SEX': 'M',
                    'DEATDATE': '6 SEP 265', 'FAMC': 'F01', 'FAMS': 'F04'},
            'I05': {'line': 52, 'INDI': 'I05', 'NAME': 'Wei /Xiahou/', 'BIRTDATE': '7 JUL 211', 'SEX': 'F',
                    'DEATDATE': '18 SEP 234', 'FAMS': 'F02'},
            'I06': {'line': 61, 'INDI': 'I06', 'NAME': 'Weiyu /Yang/', 'BIRTDATE': '17 MAR 214', 'SEX': 'F',
                    'DEATDATE': '25 NOV 278', 'FAMS': 'F03'},
            'I07': {'line': 70, 'INDI': 'I07', 'NAME': 'Rou /Sima/', 'BIRTDATE': '11 AUG 256', 'SEX': 'F',
                    'DEATDATE': '19 MAY 275', 'FAMC': 'F02'},
            'I08': {'line': 79, 'INDI': 'I08', 'NAME': 'You /Sima/', 'BIRTDATE': '11 AUG 238', 'SEX': 'M',
                    'DEATDATE': '20 FEB 283', 'FAMC': 'F03'},
            'I09': {'line': 104, 'INDI': 'I09', 'NAME': 'Yuanji /Wang/', 'BIRTDATE': '14 DEC 217', 'SEX': 'F',
                    'DEATDATE': '20 APR 268', 'FAMS': 'F04'},
            'I10': {'line': 113, 'INDI': 'I10', 'NAME': 'Yan /Sima/', 'BIRTDATE': '21 JAN 236', 'SEX': 'M',
                    'DEATDATE': '16 MAY 290', 'FAMC': 'F04'}}, 'errors': [
            {'error': 'ERROR', 'scope': 'FAMILY', 'user_story': 'US22', 'line_number': 122, 'id': 'F03',
             'description': 'ID is duplicated with F03'}]}

    def test_no_bigamy_1(self):
        self.assertEqual(birth_before_death_of_parents(self.info1), [])

    def test_no_bigamy_2(self):
        self.assertEqual(birth_before_death_of_parents(self.info2), [
            {
                'description': "Birth after mother's death.",
                'error': 'ERROR',
                'id': 'I07',
                'line_number': 70,
                'scope': 'INDIVIDUAL',
                'user_story': 'US9'},
            {
                'description': "Birth after 9 months of father's death.",
                'error': 'ERROR',
                'id': 'I07',
                'line_number': 70,
                'scope': 'INDIVIDUAL',
                'user_story': 'US9'}
        ])
