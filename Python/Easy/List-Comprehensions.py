"""
Question link: https://www.hackerrank.com/challenges/list-comprehensions/problem
Difficulty: Easy
Author: harsh_beria93
"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    # I used x+1, y+1, z+1 instead of x,y,z. Because: if I used x instead of x+1, the situation would be 0<=i<n, not 0<=i<=n
    mylist = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k)!=n]
    print(mylist)