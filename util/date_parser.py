from datetime import date,timedelta

dic_m = {
    "JAN": 1,
    "FEB": 2,
    "MAR": 3,
    "APR": 4,
    "MAY": 5,
    "JUN": 6,
    "JUL": 7,
    "AUG": 8,
    "SEP": 9,
    "OCT": 10,
    "NOV": 11,
    "DEC": 12
}


def date_parser(input_date):
    [day, month, year] = [i for i in input_date.split(' ')]
    return date(year=int(year), month=dic_m[month], day=int(day))


def time_delta(date1,date2):
    return time_delta(date1,date2)
