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

## [Day 3](http://adventofcode.com/2017/day/3) ([My Solutions](#))

## [Day 4](http://adventofcode.com/2017/day/4) ([My Solutions](https://github.com/FranciscoAT/adventOfCode2017/tree/master/day4))

### Part 1
Very simple and straightforward question. The question gave me a list of passphrases which are a series of words. They then asked how many of them are valid. They defined valid as a passphrase where no two words are the same, eg. `aa bb` is valid while `aa bb aa` is not. The solution in Python3 was simply to give the passphrase to the `set()` object which automatically eliminates duplicates. Then return if the number of words in the `set` is the same as the number of words in the passed in passphrase. 

### Part 2
Same as Part 1 except they define a valid passphrase where no two words in the passphrase are anagrams, eg. `abcde dcba` is valid while `abcde edcba` is invalid. Here what I did was I passed in each word, turned them into an array and sorted that array then joined them back together. Now if any word is anagram it will be the exact same. Then like Part 1, throw that into a `set` and check the lengths.

## [Day 5](http://adventofcode.com/2017/day/5) ([My Solutions](https://github.com/FranciscoAT/adventOfCode2017/tree/master/day5))

### Part 1
Question involved was given an array like `[0,3,0,1,-3]` starting at index `0`. We move our index around based on the value at the current index. Then after moving, increment the index value we were just on by 1. So in the example given it would take 5 steps. The solution here was simply to run a while loop and move and increment appropriately until `index < 0` or `index > len(arr)`. 

### Part 2
Same as part one, except if `a[index] > 2` decrement after moving else increment like before. The solution is the exact same except involves a new checker to see if we should increment or decrement.
