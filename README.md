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

## [Day 3](http://adventofcode.com/2017/day/3) ([My Solutions](https://github.com/FranciscoAT/adventOfCode2017/tree/master/day3/part1))

### Part 1
Here we had an interesting spiral that lists the numbers. My solution was using some simple math I was able to calculate the range at each of the layers. So it would loop until it found a layer where the number I was looking for was located in. Then it would find where it is in the layer. That being either in one of the corners. One of the middles `N,S,E,W`. Or between one corner or one `N,S,E,W`. From there it would do some simple calculations based on its layer and location to return the number of required steps.

### Part 2
Credit where credit is due: https://oeis.org/A141481


## [Day 4](http://adventofcode.com/2017/day/4) ([My Solutions](https://github.com/FranciscoAT/adventOfCode2017/tree/master/day4))

### Part 1
Very simple and straightforward question. The question gave me a list of passphrases which are a series of words. They then asked how many of them are valid. They defined valid as a passphrase where no two words are the same, eg. `aa bb` is valid while `aa bb aa` is not. The solution in Python3 was simply to give the passphrase to the `set()` object which automatically eliminates duplicates. Then return if the number of words in the `set` is the same as the number of words in the passed in passphrase. 

### Part 2
Same as Part 1 except they define a valid passphrase where no two words in the passphrase are anagrams, eg. `abcde dcba` is valid while `abcde edcba` is invalid. Here what I did was I passed in each word, turned them into an array and sorted that array then joined them back together. Now if any word is anagram it will be the exact same. Then like Part 1, throw that into a `set` and check the lengths.

## [Day 5](http://adventofcode.com/2017/day/5) ([My Solutions](https://github.com/FranciscoAT/adventOfCode2017/tree/master/day5))

### Part 1
Question involved was given an array like `[0,3,0,1,-3]` starting at index `0`. We move our index around based on the value at the current index. Then after moving, increment the index value we were just on by 1. If the new index is outside of the array the algorithm is considered "complete". So in the example given it would take 5 steps. The solution here was simply to run a while loop and move and increment appropriately until `index < 0` or `index > len(arr)`. 

### Part 2
Same as part one, except if `a[index] > 2` decrement after moving else increment like before. The solution is the exact same except involves a new checker to see if we should increment or decrement.

## [Day 6](http://adventofcode.com/2017/day/6) ([My Solutions](https://github.com/FranciscoAT/adventOfCode2017/tree/master/day6))

### Part 1
This question gave an array of "Memory Banks" (array of ints). Each Memory Bank had a certain number of "Memory Blocks" defined by the value at that index in the array. It then asked to redistribute the Memory Banks by finding the largest Memory Bank (if a tie it would grab the first from the left) then removing all of its Memory Blocks and giving one of the removed Blocks to the next Bank, then another to the following one, etc... (if you reached the end of the Memory Banks it would loop back around to the first one). Then repeat this process until it notices a loop forms, ie. if it detects that the current state of the Memory Banks is the same as a previous state encoutered before. The solution was rather straightforward. Simply it would loop through and run the restribution algorithm. Each time it finishes the redistribution algorithm it would store the state of the Banks into a Python `set`. If it found that after running the alogirthm we are back in a seen before state it would stop looping and return the current reallocation count. 

### Part 2
Same as part one but instead it wants to know how many steps the loop is, e.g if given `[0,2,7,0]` you'll find that after the first iteration you'll get `[2,4,1,2]` and after the 5th iteration you'll get `[2,4,1,2]` again. Therefore it has a loop length of `4`. The algorithm to solve was the exact same as the first except we didnt need to keep count of how many times the Banks were reallocated. Instead we stored each bank config encoutered into a Python `list`, then when we found one that we encoutered before we break from the loop, and return the length of the `list` subtract the index of where the current Banks configuration was placed intially.

## [Day 7](http://adventofcode.com/2017/day/7) ([My Solutions](https://github.com/FranciscoAT/adventOfCode2017/tree/master/day7))

### Part 1
There are a bunch of programs. Each of which either have branches to other programs or not. The question here was to find the root program. This solution here was to create to `sets`. One which are the programs that have branches and the other being all the branches themselves. Then we run a difference on these sets where we find the difference in the `set` of programs that have branches. Naturally there would be only one program that would not be in the branches as no other program branches to it, this being the root.

### Part 2
This was a little more complicated. Using the solution from Part 1. I created a dictionary of all the programs, their weight and their branches. Then I set the root as the one from Part 1. Then ran a recursive program that would calculate the `tree_weight` at each of the programs. This being the weight of the sum of itself and all of its children. Then from here I made a loop that starting at the root, would find the oddly weighted tree, and repeat until it found a layer where the trees are all weighted. Then it would return the previously oddly weighted layer. Find the program in this layer that is oddly weighted, then return what the value of this oddly weighted program should be to balance the entire tree.

## [Day 8](http://adventofcode.com/2017/day/8) ([My Solutions](https://github.com/FranciscoAT/adventOfCode2017/tree/master/day8))

### Part 1
This question involved a series of "Register operations" that came in the form `register_x (inc|dec) num_1 if register_y (<|<=|>|>=|==|!=) num_2` (note `register_x` can also be `register_y`). So the solution was I made two dictionaries. One was a dictionary of all the registers and their values. The other was an operations dictionary. That would take in `inc,dec,<,<=,...` and parse them to the proper operator accordingly. Then for each instruction I passed it to a function that would take it in. It would first check if `register_x` and `register_y` where in the `register_dictionary`. If not it would add them in with an initial value of `0`. Then it would run the operation on the second half and check if `register_y operator num_2` is valid. If yes it would then apply the operation defined to `register_x` and return the register. The question then asks, "What is the highest valued register?". This was then a simple task of looping through the dictionary and finding the highest value then returining that.

### Part 2
The exact same as Part 1, but asks, "During the operations, what was the highest value that any one register reached?". So here we modified our parsing function slightly to accept a `highest_value` integer which is initilized to `0`. Then in the parsing function if the condition is met and the operation it applied it checks to see if the value in this new register is higher than `highest_value`, then update or will not update `highest_value` accordingly. So by the time we reach the end of the register operations we'll have the highest value any one register met.

## [Day 9](http://adventofcode.com/2017/day/9) ([My Solutions](https://github.com/FranciscoAT/adventOfCode2017/tree/master/day9))

### Part 1
We're given a stream of characters. The important characters being `{`,`}`,`<`,`>`,`!`. The `{,}` characters represents a `group`. A `group` can contain anything inside it, including other `groups`. While `<,>` represents `garbage`. Anything inside `garbage` is ignored in the grand scheme of things. `!` represents the ignore character, any character that follows it is ignored, including braces and another `!`. However we also note that the `!` character is only found inside `garbage`. Part 1 asked what is the score of the input? The score being calculated based on a complete `group` and the depth of that `group`. So `{}` would have a score of `1` while `{{}}` would have a score of 3 as the group inside is 1 deep so has a score of `2` while the outer group is 0 deep and so has a score of `1`. The solution here was to simply iterate over the string of characters. If we are not inside `garbage`, then if we hit a `{` increment the `depth` by one, if `}` increase the `score` by `depth+1` then decrement `depth`, if `<` then we toggle that we are inside `garbage`. Now if we are inside `garbage` then if we hit `!` we increase our `index` by one so we'll skip the next character, if `>` then we toggle that we are no longer inside `garbage`. At the end of this we return the `score`.

### Part 2
Same as part one but wants us to return how many characters are inside garbage excluding `!` and characters ignored by `!`.  So here if we are in `garbage` we simply ignore everything until we hit `<` and toggle that we are in `garbage`. Then while in `garbage` if we hit `>` we toggle that we are no longer in `garbage`. If we hit `!` we increase the `index` to skip the next character. Else we increment our `garbage_count`. Then we return `garbage_count`.

## [Day 10](http://adventofcode.com/2017/day/10) ([My Solutions](https://github.com/FranciscoAT/adventOfCode2017/tree/master/day10))

### Part 1
Long problem to explain so will leave to potential reader. Solution here was to simply take in the lenghts. The for each length run the algorithm by iterating thorugh a `for loop` half the amount of the length and swapping the first and last, second and second-last, etc... Then return that, then we can easily multiply the first two values.

### Part 2
By using the algorithm in Part 1, I slightly modified it so that it will take in `step`, `index`, `commands` and `values`. So that the `step` and `index` are preserved and we allow for the `values` to keep changing throughout the `64` times we run the hash. Then I run the `values` through a function that will take each set of 16 values run the `XOR` operation on each of the values and append that to our new `dense_hash` list. Then I run these values through another function that will turn each of them into their `hex` values after which with some quick manual manipulation we can remove the `0x`'s and add in a `0` if needed. 

## [Day 11](http://adventofcode.com/2017/day/11) ([My Solutions](https://github.com/FranciscoAT/adventOfCode2017/tree/master/day11))

### Part 1
The question was, you are given a series of inputs that are directions to navigate in a hex grid. The input directions can be defined by `N,NE,NW,S,SW,SE` (flat-top hexes). Then at the end of the isntructions how many steps away is the final location from the center? By looking at a great resource online https://www.redblobgames.com/grids/hexagons/, we can quickly build a function that will increase `x,y,z` accordingly to input. Then we note that the `max` of the `abs` of `x,y,z` indicates the ring we are on. So we simply increase/decrease `x,y,z` according to our resource then output the absolute max of the 3 values which will give us the ring, and we know that the ring nubmer also indicates the exact number of steps we need to take to get to it. Note another solution to getting the final distance according to the resource is to sum the absolute values of `x,y,z` and divide it by 2. 

### Part 2
Same as the first but wants us to see what is the furthest the path takes us. So here we simply keep a `max_distance` value which at the end of each step will check if that value is greater than `max(abs(x),abs(y),abs(z))`, if yes replace the `max_distance` value with the `current_distance` otherwise continue looping through the path instructions. At the end ouput the `max_distance`. 

## [Day 12](http://adventofcode.com/2017/day/12) ([My Solutions](https://github.com/FranciscoAT/adventOfCode2017/tree/master/day12))

### Part 1
Todays question was that given a list of programs, and a related list to each of those programs indicating which program they can talk to. The communication was bidirectional. What was the number of programs in the group for program `0`. My solution was I created a dictionary of each program and their related programs. Then starting at the related programs to `0`, I recursively went through them creating a list of programs in this group. If the program was already in the group it would skip it as it would have had to have been checked. In addition I used a `set` to ensure no duplicates snuck their way in. Then I returned this `set` and printed the length which is the number of programs in the group.

### Part 2
Now this question asks how many groups are there. Here I kept my ground work from Part 1. But I created a simple `list` that had values `0` to `n`. Then I create a new `inital_set` for the program at index `0` in this `list`. I ran my recursive algorithm and then removed all the values that the alogrithm found from the `list`, shrinking the list and incrementing a `num_groups` variable. I repeated this process until the length of my `list` was `0`, indicating that it had gone through every possible program. Then I printed the `num_groups`.
