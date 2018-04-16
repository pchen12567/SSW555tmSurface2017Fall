"""
Created on Apr 15 19:10:24 2018
@author: Pan Chen
This program provides a function that implement US04 in Sprint 4.
US04: Marriage should occur before divorce of spouses, and divorce can only occur after marriage.
"""

from util.error_constructor import error_constructor
from util.date_parser import date_parser
import unittest

user_story = 4


def marry_before_divorce(info):
    fams = info['fams']
    rt = []
    for f in fams:
        fam = fams[f]
        marry = fam['MARRDATE']
        divorce = fam.get('DIVDATE')
        if divorce is not None:
            marry_date = date_parser(marry)
            divorce_date = date_parser(divorce)
            if marry_date > divorce_date:
                rt.append(error_constructor(error='ERROR',
                                            scope='FAMILY',
                                            user_story=user_story,
                                            line_number=fam['line'],
                                            _id=fam["FAM"],
                                            description='Marriage occurs after divorce'))
    return rt


class MarryBeforeDivorceTest(unittest.TestCase):
    info1 = {'fams':
                 {'F01': {'line': 44, 'FAM': 'F01', 'MARRDATE': '5 FEB 207', 'HUSB': 'I01', 'WIFE': 'I02',
                          'CHIL': ['I03', 'I04']},
                  'F02': {'line': 88, 'FAM': 'F02', 'MARRDATE': '26 JUN 228', 'DIVDATE': '18 SEP 234', 'HUSB': 'I03',
                          'WIFE': 'I05', 'CHIL': 'I07'},
                  'F03': {'line': 97, 'FAM': 'F03', 'MARRDATE': '10 OCT 237', 'HUSB': 'I03', 'WIFE': 'I06',
                          'CHIL': 'I08'},
                  'F04': {'line': 122, 'FAM': 'F04', 'MARRDATE': '18 AUG 234', 'HUSB': 'I04', 'WIFE': 'I09',
                          'CHIL': 'I10'}
                  },
             'indis':
                 {'I01': {'line': 5, 'INDI': 'I01', 'NAME': 'Yi /Sima/', 'BIRTDATE': '28 APR 179', 'SEX': 'M',
                          'DEATDATE': '7 SEP 251', 'FAMS': 'F01'},
                  'I02': {'line': 14, 'INDI': 'I02', 'NAME': 'Chunhua /Zhang/', 'BIRTDATE': '12 JUN 189', 'SEX': 'F',
                          'DEATDATE': '21 DEC 247', 'FAMS': 'F01'},
                  'I03': {'line': 23, 'INDI': 'I03', 'NAME': 'Shi /Sima/', 'BIRTDATE': '9 AUG 208', 'SEX': 'M',
                          'DEATDATE': '23 MAR 255', 'FAMC': 'F01', 'FAMS': ['F02', 'F03']},
                  'I04': {'line': 34, 'INDI': 'I04', 'NAME': 'Zhao /Sima/', 'BIRTDATE': '15 OCT 211', 'SEX': 'M',
                          'DEATDATE': '6 SEP 265', 'FAMC': 'F01', 'FAMS': 'F04'},
                  'I05': {'line': 52, 'INDI': 'I05', 'NAME': 'Wei /Xiahou/', 'BIRTDATE': '7 JUL 211', 'SEX': 'F',
                          'DEATDATE': '18 SEP 234', 'FAMS': 'F02'},
                  'I06': {'line': 61, 'INDI': 'I06', 'NAME': 'Weiyu /Yang/', 'BIRTDATE': '17 MAR 214', 'SEX': 'F',
                          'DEATDATE': '25 NOV 278', 'FAMS': 'F03'},
                  'I07': {'line': 70, 'INDI': 'I07', 'NAME': 'Rou /Sima/', 'BIRTDATE': '11 AUG 230', 'SEX': 'F',
                          'DEATDATE': '19 MAY 275', 'FAMC': 'F02'},
                  'I08': {'line': 79, 'INDI': 'I08', 'NAME': 'You /Sima/', 'BIRTDATE': '11 AUG 238', 'SEX': 'M',
                          'DEATDATE': '20 FEB 283', 'FAMC': 'F03'},
                  'I09': {'line': 104, 'INDI': 'I09', 'NAME': 'Yuanji /Wang/', 'BIRTDATE': '14 DEC 217', 'SEX': 'F',
                          'DEATDATE': '20 APR 268', 'FAMS': 'F04'},
                  'I10': {'line': 113, 'INDI': 'I10', 'NAME': 'Yan /Sima/', 'BIRTDATE': '21 JAN 236', 'SEX': 'M',
                          'DEATDATE': '16 MAY 290', 'FAMC': 'F04'}
                  },
             'errors': []
             }

    info2 = {'fams':
                 {'F01': {'line': 44, 'FAM': 'F01', 'MARRDATE': '5 FEB 207', 'HUSB': 'I01', 'WIFE': 'I02',
                          'CHIL': ['I03', 'I04']},
                  'F02': {'line': 88, 'FAM': 'F02', 'MARRDATE': '26 JUN 228', 'DIVDATE': '18 SEP 234', 'HUSB': 'I03',
                          'WIFE': 'I05', 'CHIL': 'I07'},
                  'F03': {'line': 97, 'FAM': 'F03', 'MARRDATE': '10 OCT 237', 'HUSB': 'I03', 'WIFE': 'I06',
                          'CHIL': 'I08'},
                  'F04': {'line': 122, 'FAM': 'F04', 'MARRDATE': '18 AUG 234', 'DIVDATE': '18 AUG 233', 'HUSB': 'I04',
                          'WIFE': 'I09',
                          'CHIL': 'I10'}
                  },
             'indis':
                 {'I01': {'line': 5, 'INDI': 'I01', 'NAME': 'Yi /Sima/', 'BIRTDATE': '28 APR 179', 'SEX': 'M',
                          'DEATDATE': '7 SEP 251', 'FAMS': 'F01'},
                  'I02': {'line': 14, 'INDI': 'I02', 'NAME': 'Chunhua /Zhang/', 'BIRTDATE': '12 JUN 189', 'SEX': 'F',
                          'DEATDATE': '21 DEC 247', 'FAMS': 'F01'},
                  'I03': {'line': 23, 'INDI': 'I03', 'NAME': 'Shi /Sima/', 'BIRTDATE': '9 AUG 208', 'SEX': 'M',
                          'DEATDATE': '23 MAR 255', 'FAMC': 'F01', 'FAMS': ['F02', 'F03']},
                  'I04': {'line': 34, 'INDI': 'I04', 'NAME': 'Zhao /Sima/', 'BIRTDATE': '15 OCT 211', 'SEX': 'M',
                          'DEATDATE': '6 SEP 265', 'FAMC': 'F01', 'FAMS': 'F04'},
                  'I05': {'line': 52, 'INDI': 'I05', 'NAME': 'Wei /Xiahou/', 'BIRTDATE': '7 JUL 211', 'SEX': 'F',
                          'DEATDATE': '18 SEP 234', 'FAMS': 'F02'},
                  'I06': {'line': 61, 'INDI': 'I06', 'NAME': 'Weiyu /Yang/', 'BIRTDATE': '17 MAR 214', 'SEX': 'F',
                          'DEATDATE': '25 NOV 278', 'FAMS': 'F03'},
                  'I07': {'line': 70, 'INDI': 'I07', 'NAME': 'Rou /Sima/', 'BIRTDATE': '11 AUG 230', 'SEX': 'F',
                          'DEATDATE': '19 MAY 275', 'FAMC': 'F02'},
                  'I08': {'line': 79, 'INDI': 'I08', 'NAME': 'You /Sima/', 'BIRTDATE': '11 AUG 238', 'SEX': 'M',
                          'DEATDATE': '20 FEB 283', 'FAMC': 'F03'},
                  'I09': {'line': 104, 'INDI': 'I09', 'NAME': 'Yuanji /Wang/', 'BIRTDATE': '14 DEC 217', 'SEX': 'F',
                          'DEATDATE': '20 APR 268', 'FAMS': 'F04'},
                  'I10': {'line': 113, 'INDI': 'I10', 'NAME': 'Yan /Sima/', 'BIRTDATE': '21 JAN 236', 'SEX': 'M',
                          'DEATDATE': '16 MAY 290', 'FAMC': 'F04'}
                  },
             'errors': []
             }

    def test_us04_marry_before_divorce001(self):
        self.assertEqual(marry_before_divorce(self.info1), [])

    def test_us04_marry_before_divorce002(self):
        self.assertEqual(marry_before_divorce(self.info2), [{'description': 'Marriage occurs after divorce',
                                                             'error': 'ERROR',
                                                             'id': 'F04',
                                                             'line_number': 122,
                                                             'scope': 'FAMILY',
                                                             'user_story': 'US4'}])


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
