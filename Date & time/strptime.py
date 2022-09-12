from datetime import datetime

date_str = "21 December, 2022"
print(type(date_str))

date_obj = datetime.strptime(date_str, "%d %B, %Y")
print(date_obj)


date_str2 = "21 Sep, 2022"
date_obj1 = datetime.strptime(date_str2, "%d %b, %Y")
print(date_obj1)

date_str3 = "18/01/2022 18:08:39"
date_str4 = "01/29/2022 18:08:39"
date_obj5 = datetime.strptime(date_str3, "%d/%m/%Y %H:%M:%S")
print(date_obj5)