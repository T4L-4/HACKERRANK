/*
Question link: https://www.hackerrank.com/challenges/sum-numbers-c/problem
Difficulty: Easy
Author: mahak_bagha1
*/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
	int x1, x2;
    float y1, y2;
    
    scanf("%d", &x1);
    scanf("%d", &x2);
    scanf("%f", &y1);
    scanf("%f", &y2);
    
    printf("%d %d\n%.1f %.1f", (x1 + x2), (x1 - x2), (y1 + y2), (y1 - y2));
    return 0;
}
