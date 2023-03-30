"""
Question link: https://www.hackerrank.com/challenges/string-validators/problem
Difficulty: Easy
Author: -
"""

if __name__ == '__main__':
    s = input()
    alnum = False
    al =False
    dig = False
    low = False
    up = False
    
    for l in s:
        if l.isalnum():
            alnum = True
        if l.isalpha():
            al = True
        if l.isdigit():
            dig = True
        if l.islower():
            low = True
        if l.isupper():
            up = True
    print(alnum)
    print(al)
    print(dig)
    print(low)
    print(up)
                        