# Works with diff between 2 different class and date 
from datetime import timedelta, date

t1 = date(year=2020, month=11, day=13)
t2 = date(year=1990, month=9, day=13)

t3 = t1- t2
print(t3)