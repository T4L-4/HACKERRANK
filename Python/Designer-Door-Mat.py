"""
Question link: https://www.hackerrank.com/challenges/designer-door-mat/problem
Difficulty: Easy
Author: -
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

def designer(N, M):
    dashCount = ((M - 1)/ 2) - 1
    for i in range(int((N - 1) / 2)):
        print("-" * int(dashCount - (i * 3)) + ".|." * ((2 * (i + 1)) - 1) + "-" * int(dashCount - (i * 3)))
    print("-" * int((M - 7) / 2) + "WELCOME" + "-" * int((M - 7) / 2))
    for i in range(int(((N - 1) / 2) - 1), -1, -1):
        print("-" * int(dashCount - (i * 3)) + ".|." * ((2 * (i + 1)) - 1) + "-" * int(dashCount - (i * 3)))
    
N, M = map(int, input().split())
designer(N, M)

