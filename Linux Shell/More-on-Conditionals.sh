# Question link: https://www.hackerrank.com/challenges/bash-tutorials---more-on-conditionals/problem
# Difficulty: Easy
# Author: PRASHANTB1984


#!/bin/bash

read x
read y
read z

if [ $x -eq $y ] && [ $x -eq $z ];
then
echo "EQUILATERAL"

elif ([ $x -eq $y ] && [ $x -ne $z ]) || ([ $x -eq $z ] && [ $x -ne $y ]) || ([ $z -eq $y ] && [ $z -ne $x ]);
then
echo "ISOSCELES"

else
echo "SCALENE"
fi