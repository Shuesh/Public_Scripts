import datetime

def What_day():
    month,day,year = input('What is the date in question?\n').split(sep=['/','-',',',' '])
    num_of_day = datetime.date(year,month,day).weekday()
    weekday = "Invalid Entry"
    if (num_of_day == 0):
        weekday = 'Sunday'
    elif (num_of_day == 1):
        weekday = 'Monday'
    elif (num_of_day == 2):
        weekday = 'Tuesday'
    elif (num_of_day == 3):
        weekday = 'Wednesday'
    elif (num_of_day == 4):
        weekday = 'Thursday'
    elif (num_of_day == 5):
        weekday = 'Friday'
    elif (num_of_day == 6):
        weekday = 'Saturday'
    else:
        raise Exception("Invalid Entry")
    
    print(weekday)

def Date_to_week():
    month,day,year = input('For what date would you like to get the week number?\n').split(sep=['/','-',',',' '])
    (year,week,day) = datetime.date(year, month, day).isocalendar()
    print(week)

def Week_to_date():
    week = int(input('What week would you like to get the range for?\n'))
    year = int(input('In which year?\n'))
    print(week)
    print(year)
    first_day = datetime.date().fromisocalendar(year, week, 1)
    last_day = datetime.date().fromisocalendar(year, week, 5)
    print('{} - {}'.format(first_day, last_day))
