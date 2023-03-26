# Question link: https://www.hackerrank.com/challenges/bash-tutorials---getting-started-with-conditionals/problem
# Difficulty: Easy
# Author: PRASHANTB1984

#!/bin/bash
read c

if [ "$c" = "Y" ] || [ "$c" = "y" ];
then
echo "YES"
elif [ "$c" = "N" ] || [ "$c" = "n" ];
then
echo "NO"
fi