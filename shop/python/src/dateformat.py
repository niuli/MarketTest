import datetime

d1 = "2013.03.31"
d2 = "2014.02.17"

def check_date(date):
    date = date.split('.')
    y = int(date[0])
    m = int(date[1])
    d = int(date[2])
    try:
        datetime.date(y,m,d)
        return True
    except:
        return False

def compare_date(d1, d2):
    s, e = d1.split('.'),d2.split('.')

    y1,m1,d1 = int(s[0]), int(s[1]), int(s[2])
    y2,m2,d2 = int(e[0]), int(e[1]), int(e[2])
    date1 = datetime.datetime(y1,m1,d1)
    date2 = datetime.datetime(y2,m2,d2)
    return (date2-date1).days

if __name__ == "__main__":
    print check_date(d1)
    print check_date(d2)
    print compare_date(d1,d2)
