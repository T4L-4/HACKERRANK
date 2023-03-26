"""
Question link: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
Difficulty: Easy
Author: harsh_beria93
"""

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    
    arr = sorted(set(arr))
    print(arr[-2])