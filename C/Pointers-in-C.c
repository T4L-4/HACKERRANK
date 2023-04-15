/*
Question link: https://www.hackerrank.com/challenges/pointer-in-c/problem
Difficulty: Easy
Author: abhiranjan
*/

#include <stdio.h>

void update(int *a, int *b) {
    int temp;
    temp = *a;
    *a = *a + *b;
    *b = (temp - *b) < 0 ? (*b -temp) : (temp - *b);
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}