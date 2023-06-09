"""
Question link: https://www.hackerrank.com/challenges/write-a-function/problem
Difficulty: Medium
Author: shashank21j
"""

def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
    
    if year % 100 == 0:
        if year % 400 == 0:
            leap = True
        else:
            leap = False
    return leap

year = int(input())
print(is_leap(year))