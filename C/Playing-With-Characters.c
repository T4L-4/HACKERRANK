/*
Question link: https://www.hackerrank.com/challenges/playing-with-characters/problem
Difficulty: Easy
Author: mahak_bagha1
*/

#include <stdio.h>

int main() 
{
    char ch;
    char s[100];
    char sen[100];
    
    scanf("%c", &ch);    
    scanf("%s\n", &s);
    scanf("%[^\n]%*c", &sen);
    
    printf("%c\n", ch);
    printf("%s\n", s);
    printf("%s\n", sen);
    return 0;
}