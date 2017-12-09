import sys
import os
import time
from datetime import datetime
from datetime import timedelta

# print "Time in seconds since the epoch: %s" %time.time()
# print "Current date and time: " , datetime.datetime.now()
# print "Or like this: " ,datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
#
#
# print "Current year: ", datetime.date.today().strftime("%Y")
# print "Month of year: ", datetime.date.today().strftime("%B")
# print "Week number of the year: ", datetime.date.today().strftime("%W")
# print "Weekday of the week: ", datetime.date.today().strftime("%w")
# print "Day of year: ", datetime.date.today().strftime("%j")
# print "Day of the month : ", datetime.date.today().strftime("%d")
# print "Day of week: ", datetime.date.today().strftime("%A")
#
# mydate = datetime.date(1943,3, 13)  #year, month, day
# print(mydate.strftime("%A"))

def difference_in_days(date1, date2):
    date1 = datetime.strptime(date1, '%m-%d-%Y')
    date2 = datetime.strptime(date2, '%m-%d-%Y')
    return (date2 - date1).days

difference_in_days('8-22-1982','12-5-2017')
