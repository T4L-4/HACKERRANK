"""
Question link: https://www.hackerrank.com/challenges/python-string-formatting/problem
Difficulty: Easy
Author: shashank21j
"""

def print_formatted(number):
    rJustCount = len(str(bin(number))[2:])
    for i in range(1, number + 1):
        decimal = str(i).rjust(rJustCount)
        octal = str(oct(i))[2:].rjust(rJustCount)
        hexadecimal = (str(hex(i))[2:]).upper().rjust(rJustCount)
        binary = str(bin(i))[2:].rjust(rJustCount)

        print(decimal, octal, hexadecimal, binary)
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


""" 
# Another answer

def print_formatted(number):
    rJustCount = len(f"{number:b}")
    for i in range(1, number + 1):
        decimal = f"{i}".rjust(rJustCount)
        octal = f"{i:o}".rjust(rJustCount)
        hexadecimal = f"{i:X}".rjust(rJustCount)
        binary = f"{i:b}".rjust(rJustCount)
        
        print(decimal, octal, hexadecimal, binary)
            
            
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

"""