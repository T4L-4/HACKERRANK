/*
Question link: https://www.hackerrank.com/challenges/java-if-else/problem
Difficulty: Easy
Author: aa1992
*/

import java.util.*;

public class Solution {
    private static final Scanner scanner = new Scanner(System.in);
    public static void main(String[] args) {
        int n = scanner.nextInt();
        if(n%2==1) {
            System.out.println("Weird");
        }
        
        if(n%2==0) {
            if(n>=2 && n<=5) {
                System.out.println("Not Weird");
            }
            else if(n>=6 && n<=20) {
                System.out.println("Weird");
            }
            else if(n>=20) {
                System.out.println("Not Weird");
            }
        }
        scanner.close();
    }
}