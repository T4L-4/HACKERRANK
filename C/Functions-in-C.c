/*
Question link: https://www.hackerrank.com/challenges/functions-in-c/problem
Difficulty: Easy
Author: abhiranjan
*/

#include <stdio.h>
int max_of_four(int a, int b, int c, int d);

int main() {
    int a, b, c, d;
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}

int max_of_four(int a, int b, int c, int d){
    int max_value = a;
    if (max_value < b){
        max_value = b;
    }
    if (max_value < c) {
        max_value = c;
    }
    if (max_value < d) {
        max_value = d;
    }
    return max_value;
}