#!/usr/bin/env python3

'''
OPS445 Assignment 1
Program: assignment1.py 
The python code in this file is original work written by
"Prasad Mistry". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.

Author: Prasad Mistry
Student Number: 111964193
Student Email: pmistry21@myseneca.ca
Course: OPS445
Section: ZAA
Semester: Fall 2024
Professor: Leo Lu
Description:  
'''

import sys

def day_of_week(date: str) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    day, month, year = (int(x) for x in date.split('/'))
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + day) % 7
    return days[num]

def leap_year(year: int) -> bool:
    "return true if the year is a leap year"
    ...
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:  
        return False

def mon_max(month:int, year:int) -> int:
    "returns the maximum day for a given month. Includes leap year check"
    ...
    if month == 2:
            if leap_year(year):
                return 29
            else:
                return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def after(date: str) -> str: 
    '''
    after() -> date for next day in DD/MM/YYYY string format

    Return the date for the next day of the given date in DD/MM/YYYY format.
    This function has been tested to work for year after 1582
    '''
    day, mon, year = (int(x) for x in date.split('/'))
    day += 1  # next day

    lyear = year % 4
    if lyear == 0:
        leap_flag = True
    else:
        leap_flag = False  # this is not a leap year

    lyear = year % 100
    if lyear == 0:
        leap_flag = False  # this is not a leap year

    lyear = year % 400
    if lyear == 0:
        leap_flag = True  # this is a leap year
    
    mon_dict= {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
           7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if mon == 2 and leap_flag:
        mon_max = 29
    else:
        mon_max = mon_dict[mon]
    
    if day > mon_max:
        mon += 1
        if mon > 12:
            year += 1
            mon = 1
        day = 1  # if tmp_day > this month's max, reset to 1 
    return f"{day:02}/{mon:02}/{year}"

def before(date: str) -> str:
    "Returns previous day's date as DD/MM/YYYY"
    ...
    day, mon, year = (int(x) for x in date.split('/'))
    day = day - 1  

    if day == 0:  
        mon = mon - 1
        if mon == 0:  
            year = year - 1
            mon = 12
        day = mon_max(mon, year)

    return f"{day:02}/{mon:02}/{year}"

def usage():
    "Print a usage message to the user"
    print("Usage: " + str(sys.argv[0]) + " DD/MM/YYYY NN")
    sys.exit()

def valid_date(date: str) -> bool:
    "check validity of date"
    ...
    validity = date.split('/')
    if len(validity) != 3:
        return False

    day = int(validity[0])
    mon = int(validity[1])
    year = int(validity[2])

    if len(str(year)) != 4:
        return False

    if mon < 1 or mon > 12:
        return False

    if day < 1 or day > mon_max(mon, year):
        return False

    return True

def day_iter(start_date: str, num: int) -> str:
    "iterates from start date by num to return end date in DD/MM/YYYY"
    ...
    iterates = start_date
    count = 0

    if num > 0:
        while count < num:
            iterates = after(iterates)
            count = count + 1
    elif num < 0:
        while count > num:
            iterates = before(iterates)
            count = count - 1
    return iterates

if __name__ == "__main__":
    # check length of arguments
    if len(sys.argv) != 3:
        usage()
        
    # check first arg is a valid date
    is_valid_date = sys.argv[1]

    if not valid_date(is_valid_date):
        usage()

    # check that second arg is a valid number (+/-)
    is_valid_number = sys.argv[2]

    if is_valid_number.startswith('-'):
        check = is_valid_number[1:]
    else:
        check = is_valid_number

    if not check.isdigit():
        usage()

    # call day_iter function to get end date, save to x
    is_valid_number = int(is_valid_number)
    
    end_date = day_iter(is_valid_date, is_valid_number)

    # print(f'The end date is {day_of_week(x)}, {x}.')
    print(f"The end date is {day_of_week(end_date)}, {end_date}.")
    
    pass