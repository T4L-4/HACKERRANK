"""
Question link: https://www.hackerrank.com/challenges/python-lists/problem
Difficulty: Easy
Author: shashank21j
"""

class List:
    def __init__(self):
        self.myList = []
    def listInsert(self, i, v):
        self.myList.insert(i, v)       
    def listRemove(self, v):
        self.myList.remove(v)
    def listAppend(self, v):
        self.myList.append(v)
    def listPrint(self):
        print(self.myList)
    def listSort(self):
        self.myList = sorted(self.myList)
    def listPop(self):
        self.myList.pop()
    def listReverse(self):
        self.myList = self.myList[::-1]
    
if __name__ == '__main__':
    N = int(input())
    lst = List()
    for i in range(N):
        ch = input().split()
        if ch[0] == "insert":
            lst.listInsert(int(ch[1]), int(ch[2]))
        if ch[0] == "remove":
            lst.listRemove(int(ch[1]))
        if ch[0] == "append":
            lst.listAppend(int(ch[1]))
        if ch[0] == "print":
            lst.listPrint()
        if ch[0] == "sort":
            lst.listSort()
        if ch[0] == "pop":
            lst.listPop()
        if ch[0] == "reverse":
            lst.listReverse()