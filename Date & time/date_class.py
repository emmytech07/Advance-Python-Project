from datetime import datetime

print(datetime.now())
# @@@@@@@ Getting current Date
import datetime
print(datetime.date.today())

# Getting Date time attribute 
print(dir(datetime))

# ''''''''''' Create a date object 
date = datetime.date(2020, 12, 2)
print(date)
print(type(date))

# .... getting date froma timestamp
from datetime import date

time_stamp = date.fromtimestamp(21099999999)
print(time_stamp)

today = date.today()
print (today)
print (today.year)
print (today.month)
print (today.day)

from datetime import time

time1 = time()
print(time1)
time2 = time(hour=12, minute=30, second=30)
print(time2)

from datetime import datetime
time_1 = datetime(2100,1,1, 20, 30, 20)
print("Year: ", time_1.year)
print("Month: ", time_1.month)
print("Day: ", time_1.day)
print("Hours: ", time_1.hour)
print("Hours: ", time_1.hour)
print("Hours: ", time_1.timestamp)