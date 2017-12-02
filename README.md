# Advent of Code 2017 ([Calendar 2017](http://adventofcode.com/))

First year of doing advent of code. Will keep a running list of each day and my thought on how I solved it. 

## [Day 1](http://adventofcode.com/2017/day/1) ([My Solution](https://github.com/FranciscoAT/adventOfCode2017/tree/master/day1))
Quick and easy question where it feeds a list. Then if `a[i] == a[i+1]` then add `a[i]` to a building sum. Additionally this array wraps. So my solution was to loop through the array, run the check and add or do not add accordingly. Then run a quick check for `a[n] == a[0]` and add accordingly then return. 
