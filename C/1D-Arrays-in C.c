/*
Question link: https://www.hackerrank.com/challenges/1d-arrays-in-c/problem
Difficulty: Medium
Author: -
*/

#include <stdio.h>

int main() {
    int n, i = 0, sum = 0;
    scanf("%d", &n);
    int arr[n];
        
    for (i=0; i<n; i++){
        scanf("%d", &arr[i]);
    }
    
    for (i=0; i<n; i++){
        sum += arr[i];
    }

    printf("%d", sum);       
    return 0;
}