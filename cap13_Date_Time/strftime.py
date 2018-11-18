import time

t = (2016, 2 ,15, 10, 13, 38, 1, 48, 0)

t = time.mktime(t)

print(time.strftime("%B %d %Y %H:%M:%S", time.localtime(t)))

"""Utilizaremos a função datetime.strftime()"""

"""Formatting days:
   %a = abbreviated day of week: Mon, Tues, Wed
   %A = full name of the day of week: Monday, Tuesday, Wednesday
   %d  = day of month, ex: 10th of January"""

"""Formatting months:
   %b = abbreviated month name: Jan, Feb
   %B = full month name: January, February
   %m = month as number: 01 for Januray"""

"""Formatting times
   %H hours
   %M minutes
   %S seconds
   %p AM or PM"""

"""Formatting years
   %y abbreviated year  as tow numbers: 18
   %Y year as four numbers: 2018"""


