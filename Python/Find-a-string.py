"""
Question link: https://www.hackerrank.com/challenges/find-a-string/problem
Difficulty: Easy
Author: harsh_beria93
"""

def count_substring(string, sub_string):
    count = 0
    
    while True:
        if string.find(sub_string) == -1:
            break
        else:
            count += 1
            index = string.find(sub_string)
            string = string[(index + 1):]
        
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)