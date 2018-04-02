"""
:return a array of personal and family objects.
"""
from prettytable import PrettyTable
import time

from UserStory.US21 import correct_gender
from UserStory.US22 import unique_id
from UserStory.US23 import unique_indi
from UserStory.US25 import unique_first_name

from UserStory.US10 import marriage_after_14
from UserStory.US16 import same_sur_name


def read_gedcom_file(path):
    '''
       Read a GEDCOM file and inspect the TAGs are valid or not, then output to a new file.
       :param infile: input file name
       :param outfile: output file name
       :return:
       '''
    f = open(path, 'r')
    result = list()
    line_number = 1
    for line in f.readlines():
        line = line.strip()
        msg = line.split(" ")
        level = msg[0]
        valid_tag_l0 = ['HEAD', 'TRLR', 'NOTE']
        valid_tag_l0_reverse = ['INDI', 'FAM']
        valid_tag_l1 = ['NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC',
                        'FAMS', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV']
        valid_tag_l2 = ['DATE']
        if level == '0':
            if msg[1] in valid_tag_l0:
                tag = msg[1]
                flag = 'Y'
                argument = ' '.join(msg[2:])
            elif msg[2] in valid_tag_l0_reverse:
                tag = msg[2]
                flag = 'Y'
                argument = msg[1]
            else:
                tag = msg[1]
                flag = 'N'
                argument = ' '.join(msg[2:])
        elif level == '1':
            tag = msg[1]
            argument = ' '.join(msg[2:])
            if msg[1] in valid_tag_l1:
                flag = 'Y'
            else:
                flag = 'N'
        elif level == '2':
            tag = msg[1]
            argument = ' '.join(msg[2:])
            if msg[1] in valid_tag_l2:
                flag = 'Y'
            else:
                flag = 'N'
        else:
            tag = msg[1]
            flag = 'N'
            argument = ' '.join(msg[2:])
        result.append({'level': level, 'tag': tag, 'flag': flag, 'argument': argument, 'line_number': line_number})
        line_number += 1
    f.close()
    return result


def write_gedcom_file(path, obj):
    pass


def parse_getcom(obj):
    indis = {}
    fams = {}
    current = ()
    line = 1
    errors = []
    for i in obj:
        if i['level'] == "0":
            if ["HEAD", "NOTE", "TRLR"].count(i['tag']) == 1:
                line += 1
                continue
            current = {'scope': i['tag'], 'id': i['argument']}
            if i['tag'] == "FAM":
                # US22 report duplicate id.
                for fam in fams:
                    if i['argument'] == fam:
                        errors.append({'error': 'ERROR',
                                       'scope': "FAMILY",
                                       'user_story': 'US22',
                                       'line_number': line,
                                       'id': i['argument'],
                                       'description': "ID is duplicated with " + fams[fam]["FAM"]})
                fams[i['argument']] = {'line': line}
                fams[i['argument']][i['tag']] = i['argument']
            if i['tag'] == "INDI":
                for indi in indis:
                    if i['argument'] == indi:
                        errors.append({'error': 'ERROR',
                                       'scope': "INDIVIDUAL",
                                       'user_story': 'US22',
                                       'line_number': line,
                                       'id': i['argument'],
                                       'description': "ID is duplicated with " + indis[indi]["INDI"]})
                indis[i['argument']] = {'line': line}
                indis[i['argument']][i['tag']] = i['argument']
        elif i['level'] == '1':
            has_l2 = ['BIRT', 'DEAT', 'MARR', 'DIV']
            if has_l2.count(i['tag']) == 1:
                l1_name = i['tag']
            elif current['scope'] == "FAM":
                if fams[current['id']].get(i['tag']) is not None:
                    if type(fams[current['id']][i['tag']]) is str:
                        fams[current['id']][i['tag']] = [fams[current['id']][i['tag']]]
                    fams[current['id']][i['tag']].append(i['argument'])
                else:
                    fams[current['id']][i['tag']] = i['argument']
            elif current['scope'] == "INDI":
                if indis[current['id']].get(i['tag']) is not None:
                    if type(indis[current['id']][i['tag']]) is str:
                        indis[current['id']][i['tag']] = [indis[current['id']][i['tag']]]
                    indis[current['id']][i['tag']].append(i['argument'])
                else:
                    indis[current['id']][i['tag']] = i['argument']
        elif i['level'] == '2':
            if i['tag'] == "DATE":
                if current['scope'] == "FAM":
                    fams[current['id']][l1_name + i['tag']] = i['argument']
                elif current['scope'] == "INDI":
                    indis[current['id']][l1_name + i['tag']] = i['argument']
        line += 1
    return {"fams": fams, "indis": indis, 'errors':errors}


def print_fams(info):
    fams = info["fams"]
    indis = info["indis"]
    fams_table = PrettyTable(
        ["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"])
    for id in fams:
        fam = fams[id]
        line = []
        line.append(fam["FAM"])
        line.append(fam["MARRDATE"])
        line.append(fam.get("DIVDATE"))
        line.append(fam["HUSB"])
        line.append(indis[fam["HUSB"]]["NAME"])
        line.append(fam["WIFE"])
        line.append(indis[fam["WIFE"]]["NAME"])
        line.append(fam.get("CHIL"))
        fams_table.add_row(line)
    print(fams_table)


def print_indis(info):
    indis = info["indis"]
    indis_table = PrettyTable(["ID", "Name", "GENDER", "BIRTHDAY", "Age", "Alive", "Death", "Child", "Spouse"])
    for id in indis:
        indi = indis[id]
        line = []
        line.append(indi["INDI"])
        line.append(indi["NAME"])
        line.append(indi["SEX"])
        line.append(indi["BIRTDATE"])
        year_birth = int(indi["BIRTDATE"].split(" ")[2])
        year_death = int(indi["DEATDATE"].split(' ')[2])
        if (year_death == None):
            now_year = int(time.strftime("%Y", time.localtime(time.time())))
            line.append(now_year - year_birth)
        else:
            line.append(year_death - year_birth)
        death_date = indi.get("DEATDATE")
        line.append(death_date is None)
        line.append(death_date)
        famc = indi.get("FAMC")
        line.append(famc)
        line.append(indi.get("FAMS"))
        indis_table.add_row(line)
    print(indis_table)


def print_errors(errors):
    for error in errors:
        print_error(error)


def print_error(err):
    # error dict{'error','scope','user_story','line_number','id','description'}
    print(err['error'] + ": " + err['scope'] + ": " + err['user_story'] + ": " + str(err[
                                                                                         'line_number']) + ": " + err[
              'id'] + ": " + err['description'])


def test_gedcom(info):
    rt = []
    # user story
    rt += info['errors']
    rt += unique_indi(info)
    rt += correct_gender(info)
    rt += unique_id(info)
    rt += unique_first_name(info)  # US25
    rt += marriage_after_14(info)
    rt += same_sur_name(info)
    print_errors(rt)


def main():
    get_gedcom_test_result('../Input/Project01-Pan_Chen.txt')
    get_gedcom_test_result('../Input/bug.txt')


def get_gedcom_test_result(file_name):
    info = parse_getcom(read_gedcom_file(file_name))
    print_indis(info)
    print_fams(info)
    test_gedcom(info)


if __name__ == '__main__':
    main()
