
# * Get the current datetime

from datetime import datetime

dateTimeNow = datetime.now()
print('The current date time is', dateTimeNow)
dateNow = dateTimeNow.date()
print('The current date is', dateNow)
timeNow = dateTimeNow.time()
print('The current time is', timeNow)
yearNow = dateTimeNow.year
print('The current year is', yearNow)
monthNow = dateTimeNow.month
print('The current month is', monthNow)
dayNow = dateTimeNow.day
print('The current day is', dayNow)
hourNow = dateTimeNow.hour
print('The current hour is', hourNow)
minutesNow = dateTimeNow.minute
print('The current minutes is', minutesNow)
secondsNow = dateTimeNow.second
print('The current seconds is', secondsNow)
milliSecondsNow = dateTimeNow.microsecond
print('The current milliseconds are', milliSecondsNow)

# * Get the current date using the date class

from datetime import date

todaysDate = date.today()
print("Today's date is", todaysDate)

# * Get the current time

import time
print("The time now is", time.time())
print("The time now is", time.ctime())
 