import datetime

def dayOfYear(date):
    year = int(date[0:4])
    month = int(date[5:7])
    day = int(date[-2:])
    return (datetime.date(year,month,day) - datetime.date(year-1,12,31)).days

print(dayOfYear('2019-01-09'))