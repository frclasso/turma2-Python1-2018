#!/usr/bin/env python3

from datetime import datetime

now = datetime.now()

"""Utilizaremos a função datetime.strftime()"""

"""Formatting days:
   %a = abbreviated day of week: Mon, Tues, Wed
   %A = full name of the day of week: Monday, Tuesday, Wednesday
   %d  = day of month, ex: 10th of January"""

print(now.strftime("%a, %A, %d"))

"""Formatting months:
   %b = abbreviated month name: Jan, Feb
   %B = full month name: January, February
   %m = month as number: 01 for Januray"""

print(now.strftime("%b, %B, %m"))

"""Formatting times
   %H hours
   %M minutes
   %S seconds
   %p AM or PM"""

print(now.strftime("%H:%M:%S %p"))

"""Formatting years
   %y abbreviated year  as tow numbers: 18
   %Y year as four numbers: 2018"""

print(now.strftime("%y, %Y"))


"""Juntand tudo"""
print(f"Today is {now.strftime('%B')} {now.strftime('%d')}(th/rd/nd),"
                                           f" at time {now.strftime('%H:%M:%S %p')}"
                                           f", Year:{now.strftime('%Y')}")