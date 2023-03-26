"""
Question link: https://www.hackerrank.com/challenges/nested-list/problem
Difficulty: Easy
Author: harsh_beria93
"""

if __name__ == '__main__':
    myList = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        myList.append([name, score])
    
    scores = list()
    
    for i in myList:
        scores.append(i[1])
    
    scores = sorted(set(scores))
    
    names = []
    for i in myList:
        if i[1] == scores[1]:
            names.append(i[0])

    names = sorted(names)
    for name in names:
        print(name)