# RAMDISP

*This is still a work in progress. It may be changed in the future.*

*This article is a stub, which means that it is not detailed enough and needs to be expanded. Please help us by adding some more information.*

**RAMDISP** is an esolang made by [User:Otesunki](https://esolangs.org/wiki/User:Otesunki) ([talk](https://esolangs.org/w/index.php?title=User_talk:Otesunki)).

**Contents**
1. Instructions
2. Arithmetic with arrays
3. Code examples
    1. Hello World
    2. Truth Machine
    3. 99 Bottles of beer
4. Interpreters

# Instructions

| Function | Description |
|:--------:|:------------|
|`P[vfff...]`|Pipe: Starts with the value v, passes it to each function, and sets the new value to the value returned from the function call. Ignores all further arguments passed to it.|
|`D[fff...]`|Disperse: Passes all arguments passed to it to each function in order.|
|`;[aaa...]`|Output: Outputs all arguments as strings to the console.|
|`I[f[aaa...]]`|Ignore: Forces the function to execute with the arguments specified. Ignores all further arguments passed to it.|
|`S[[f[aaa...]]b]`|Swap: Forces the function inside to curry backwards instead of forwards, inner function recieves args baaa...|
|`R[v]`|Range: Creates a range from 1-v (inclusive)|
|`A[a]`|Anti: Reverses the array, and all items of the array.|
|`M[fa]`|Map: For each item in the array, calls the function with the item as an argument.|
|`~[v]`|Negate: Negates the value from v to -v.|
|`-[ab]`|Subtract: Subtracts b from a.|
|`+[ab]`|Add: Adds b to a.|
|`*[ab]`|Multiply: Multiplies b with a.|
|`/[ab]`|Divide: Divides a by b, rounds down to the nearest integer.|
|`%[ab]`|Modulo: Divides a by b, and returns the remainder|

# Arithmetic with arrays
---

Numbers are represented by nested arrays, so 0 is [], 1 is [[]], 2 is [[[]]], etc... The code

    [*[[[[]]][[[[]]]]]]

calculates 2*3, and returns it.

# Code examples
---

## Hello World
    [;[Hello, World!]]
## Truth Machine
    [P[:~R[M[I[;1]]][I[;0]]]]
## 99 Bottles of beer
    [P[[[[[[[[[[[[]]]]]]]]]]][*[[[[[[[[[[[]]]]]]]]]]]][S[-1]]RA[M[D[[S[; bottles of beer on the wall!
    
    ]][S[; bottles of beer on the wall,
    ]][S[; bottles of beer!
    Take one down, pass it around,
    ]]]]][I[;No more bottles of beer on the wall!
    
    No more bottles of beer on the wall,
    No more bottles of beer!
    Go to the store and buy some more,
    99 bottles of beer on the wall!]]]]

# Interpreters
---
[RAMDISP on GitHub](https://github.com/Oderjunkie/RAMDISP/)
