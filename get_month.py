import datetime
now = datetime.datetime.now()
def getSeason(date):
    if now.month == 1 or now.month == 2 or now.month == 12:
        return "khari"
    elif now.month == 8:
        return "Rabi"
    else:
        month = int(input("Enter the month"))
        while(month < 0 or month > 12):
            month = int(input("Enter valid month"))
        return month
getSeason(now)