"""
Created on Thu Feb 02 17:19:18 2018
@author: Pan Chen
This program provides a function that read a GEDCOM file and inspect the TAGs are valid or not,
then outputs to a new file.
"""


def test_tag(infile, outfile):
    '''
    Read a GEDCOM file and inspect the TAGs are valid or not, then output to a new file.
    :param infile: input file name
    :param outfile: output file name
    :return:
    '''
    f = open(infile, 'r')
    result = list()
    for line in f.readlines():
        line = line.strip()
        input = "--> " + line
        print(input)
        result.append(input)
        msg = line.split(" ")
        level = msg[0]
        valid_tag1 = ['HEAD', 'TRLR', 'NOTE']
        valid_tag2 = ['INDI', 'FAM']
        valid_tag3 = ['NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC',
                      'FAMS', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV']
        valid_tag4 = ['DATE']
        if level == '0':
            if msg[1] in valid_tag1:
                tag = msg[1]
                flag = 'Y'
                argument = ' '.join(msg[2:])
                l = "<-- %s|%s|%s|%s" % (level, tag, flag, argument)
            elif msg[2] in valid_tag2:
                tag = msg[2]
                flag = 'Y'
                ID = msg[1]
                l = "<-- %s|%s|%s|%s" % (level, tag, flag, ID)
            else:
                tag = msg[1]
                flag = 'N'
                argument = ' '.join(msg[2:])
                l = "<-- %s|%s|%s|%s" % (level, tag, flag, argument)

        elif level == '1':
            tag = msg[1]
            argument = ' '.join(msg[2:])
            if msg[1] in valid_tag3:
                flag = 'Y'
            else:
                flag = 'N'
            l = "<-- %s|%s|%s|%s" % (level, tag, flag, argument)

        elif level == '2':
            tag = msg[1]
            argument = ' '.join(msg[2:])
            if msg[1] in valid_tag4:
                flag = 'Y'
            else:
                flag = 'N'
            l = "<-- %s|%s|%s|%s" % (level, tag, flag, argument)

        else:
            tag = msg[1]
            flag = 'N'
            argument = ' '.join(msg[2:])
            l = "<-- %s|%s|%s|%s" % (level, tag, flag, argument)

        print(l)
        result.append(l)

    output = open(outfile, 'w')
    for line in result:
        output.write(line)
        output.write('\n')

    f.close()
    output.close()


def main():
    f1 = 'Project01-Pan_Chen-0.txt'
    f2 = 'PJ02-Output-Pan_Chen.txt'
    f3 = 'proj02test.ged'
    f4 = 'PJ02-Test-Output-Pan_Chen.txt'
    test_tag(f1, f2)
    print('-----------------------------------------------------')
    test_tag(f3, f4)


if __name__ == '__main__':
    main()
