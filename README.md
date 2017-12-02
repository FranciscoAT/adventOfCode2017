# Advent of Code 2017 ([Calendar 2017](http://adventofcode.com/))

First year of doing advent of code. Will keep a running list of each day and my thought on how I solved it. 

## [Day 1](http://adventofcode.com/2017/day/1) ([My Solutions](https://github.com/FranciscoAT/adventOfCode2017/tree/master/day1))

### Part 1
Quick and easy question where it feeds a list. Then if `a[i] == a[i+1]` then add `a[i]` to a building sum. Additionally this array wraps. So my solution was to loop through the array, run the check and add or do not add accordingly. Then run a quick check for `a[n] == a[0]` and add accordingly then return. 

### Part 2
Here the question was same as part 1 except basically if the integer halfway around the circular array is the same add it. So the soultion is the same except to now check for if `a[i] == a[(i+n/2)%n]` then add. Only need to loop through the array once. 

## [Day 2](http://adventofcode.com/2017/day/2) ([My Solutions](https://github.com/FranciscoAT/adventOfCode2017/tree/master/day2))

### Part 1
This question involved getting a few rows of values. Then look for the maximum difference on each row and add those values up. This solution was straight forward, I took in each row then sorted the row. Took the last value in the sorted row and subtracted it from the first value in the sorted row. This being the largest value, then added those values up for the final result. 

### Part 2
Like the first it involved several rows of values. However each row only has two values `a`,`b` where `a%b==0`. So for this one I came up with a quick brute force method which would sort the row then look at `a[i]` where `0<i<n-1`. Then check if `a[j]%a[i]==0` where `i<j<n`. If yes would return `a[j]/a[i]` else `0` (although each row was guarenteed a non-zero return). Added these values up and returned the final result.