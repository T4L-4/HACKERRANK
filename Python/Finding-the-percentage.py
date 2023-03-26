"""
Question link: https://www.hackerrank.com/challenges/finding-the-percentage/problem
Difficulty: Easy
Author: harsh_beria93
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        
    query_name = input()
    average = (student_marks[query_name][0] + student_marks[query_name][1] + student_marks[query_name][2]) / 3
    print("%.2f" % average)