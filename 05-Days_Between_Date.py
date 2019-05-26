# Ai Assignment 05 - calculate number of days between two dates
import datetime
date1 = input("Enter First  Date [DD/MM/YYYY] : ")
date2 = input("Enter Second Date [DD/MM/YYYY] : ")
d1, m1, y1 = map(int, date1.split('/'))
d2, m2, y2 = map(int, date2.split('/'))
date1 = datetime.date(y1, m1, d1)
date2 = datetime.date(y2, m2, d2)
period = date2 - date1
print("Number of Days................ : ",period.days)