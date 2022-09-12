from calendar import month
from datetime import datetime

now = datetime.now()
# print(now)
# time = now.strftime("%H:%M:%S")
# print(time)

# s1 = now.strftime("%m/%d/%Y %H:%M:%S")
# print(s1)

# ...........date time to string using strftime()
year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")

#*******Creating string from timestamp
timestamp = 23456789
date_time = datetime.fromtimestamp(timestamp)
print(date_time)

date = date_time.strftime("%m-%d-%Y %H:%M:%S")
print(date)

date2 = date_time.strftime("%d %b, %Y %H:%M:%S")
print(date2)

date3 = date_time.strftime("%d %B, %Y %H:%M:%S")
print(date3)

time2 = date_time.strftime("%I %p")
print(time2)

#..... Local Appropiate date and time 
timestamp = 1014567892
date_time = datetime.fromtimestamp(timestamp)
print(date_time)
dl = date_time.strftime("%c")
print(dl)