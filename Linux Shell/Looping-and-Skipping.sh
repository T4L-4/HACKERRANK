# Question link: https://www.hackerrank.com/challenges/bash-tutorials---looping-and-skipping/problem
# Difficulty: Easy
# Author: PRASHANTB1984

#!/bin/bash
for i in {1..99}
do
    if [ $((i%2)) == 1 ];
    then
        echo "$i"
    fi
done
