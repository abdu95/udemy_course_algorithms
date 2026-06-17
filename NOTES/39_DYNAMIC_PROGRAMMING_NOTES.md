
# 39 Dynamic Programming 

## 133 Overlapping Subproblems 

Dynamic Programming is a problem-solving technique used to efficiently solve complex problems by breaking them into smaller overlapping subproblems, solving each subproblem once, and storing their results to avoid redundant computations.

Instead of solving the same problem again and again:
    Break the problem into smaller parts
    Solve each part only once
    Store the result (in a table, array, or memory)
    Reuse stored results when needed


Dynamic Programming is needed when:
1. Overlapping Subproblems:
    The same smaller problems occur multiple times.
2. Optimal Substructure
    The optimal solution can be built from optimal solutions of subproblems.

Why not use normal recursion?
- Without DP:
    Repeats same calculations
    Exponential time (very slow)

- With DP:
    Stores results → avoids recomputation
    Polynomial time (much faster)


Two things required for Dynamic Programming:
    Overlapping Subproblems
    Optimal Substructure

Without DP:
    You can take a Problem
    Divide it into Subproblems
    Solve each Subproblem 
    Put them back together
    Solve overall problem 

[PROBLEM]
[SUB] [SUB] [SUB] [SUB] [SUB] [SUB] [SUB] [SUB] 

Overlapping Subproblems
    Overlapping Subproblems = Repeating  Subproblems
    Here some subproblems may repeat 
    Subproblem 1s are similar 

[PROBLEM]
[1] [1] [2] [3] [1] [2] [3] [3]
10  10  20  30  10  20  30  30 

Subproblem 1 includes many operations and take a lot of time. It returns 10. 

When we face identical subproblem again, we already know what it returns. Its inefficient to do multiple operations again. It is better to store 10 in a list

    10 20 30
 [0 1  2  3 4 5 6 7] - index

When we face Subproblem 1 next time, we check if there is a value in index of 1. We already have value. Now instead of doing multiple operations, we simply use 10 - it becomes O(1) operation.

Now when we have solution to each subproblem, we can now solve overall problem

This process of storing answer to subprobems is called MEMOIZATION


This example is not Overlapping Subproblems. 
MergeSort:
- divides items in half, and again divides them into half. These operations are not overlapping, they are different, unique problems. None of them are repeating subproblems
- merges items and sorts. Each of this merging is different from each other. There are no overlapping subproblems



## 134 Optimized Substructure

Take a problem
Divide it into overlapping subproblems
Subproblems need to have optimized substructure

[PROBLEM]
[1] [1] [2] [3] [1] [2] [3] [3]
10  10  20  30  10  20  30  30 


Lowest cost path for getting from A => D:
    A >> C then C >> D: cost 50
    A >> B then B >> D: cost 25

        10
    A - - -  B
    |        |
 30 |        | 15
    |        |
    C - - -  D
        20

Get from A => D. 
Subproblems:
    how to go from A >> B
    how to go from B >> D

If you get optimal way of going from A >> B and get optimal way of going from B >> D, it gives you the optimal way of going from A >> D.


[PROBLEM]
[1] [1] [2] [3] [1] [2] [3] [3]

Optimized Substructure:
    If you have the optimal solution for Subproblem 1 and Subproblem 2 and Subproblem 3, that gives the optimal solution for optimal PROBLEM. 


Highest cost path for getting from A => C:
    A >> B then B >> D then D >> C: cost 45
Highest cost path for getting from C => D:
    C >> A then A >> B then B >> D: cost 55
    
Highest cost path that has no overlap and retracing.

In this situation you cant take the optimal solution for each subproblem and solve the overall PROBLEM. Therefore you can't solve this with Dynamic Programming 



- in optimized substructure, is it correct to say optimal solution for overall problem is the sum of optimal solution for each subproblem?
Not exactly — that statement is too strong and only true in some special cases.

✅ Correct principle of optimal substructure:
A problem has optimal substructure if:
    An optimal solution to the problem contains optimal solutions to its subproblems.



## 135 Fibonacci Sequence

    1   1   2
    ^ + ^ = ^

    1 1 2 3 5 8 13 (in Math)

  0 1 1 2 3 5 8 13 (in Computer Science)
                    arrays start at index of 0

```python 

def fib(n):
    if n == 0 or n == 1:
        return n 
    return fib(n - 1) + fib(n - 2)
```


print(fib(2))

CALL STACK:

        | 1 |           | 0 |
| 2 |   | 2 |   | 2 |   | 2 |   | 2 |
|___|   |___|   |___|   |___|   |___|   |___|


 0  1   1
-----------
[0] [1] [2]

illustrated as tree:

fib(2)

    fib(2)
    /  \
fib(1)  fib(0)


fib(3)

            fib(3)  
            /    \
        fib(2)  <fib(1)>
        /   \
<fib(1)>   fib(0)


Here fib(1) is OVERLAPPING SUBPROBLEM 


OPTIMIZED SUBSTRUCTURE
    if you have the optimum solution for each of these functions, it gives you the overall optimal solution to the PROBLEM



fib(7)

fib(7)
├── fib(6)
│   ├── <fib(5)>
│   │   ├── fib(4)
│   │   │   ├── fib(3)
│   │   │   │   ├── fib(2)
│   │   │   │   │   ├── fib(1)
│   │   │   │   │   └── fib(0)
│   │   │   │   └── fib(1)
│   │   │   └── fib(2)
│   │   │       ├── fib(1)
│   │   │       └── fib(0)
│   │   └── fib(3)
│   │       ├── fib(2)
│   │       │   ├── fib(1)
│   │       │   └── fib(0)
│   │       └── fib(1)
│   └── fib(4)
│       ├── fib(3)
│       │   ├── fib(2)
│       │   │   ├── fib(1)
│       │   │   └── fib(0)
│       │   └── fib(1)
│       └── fib(2)
│           ├── fib(1)
│           └── fib(0)
└── <fib(5)>
    ├── fib(4)
    │   ├── fib(3)
    │   │   ├── fib(2)
    │   │   │   ├── fib(1)
    │   │   │   └── fib(0)
    │   │   └── fib(1)
    │   └── fib(2)
    │       ├── fib(1)
    │       └── fib(0)
    └── fib(3)
        ├── fib(2)
        │   ├── fib(1)
        │   └── fib(0)
        └── fib(1)

fib(5) forming identical pyramids
fib(4) too

there are a lot of operations that are repeated - we can make this more efficient 

- Big O of doing Fibonacci in this way is O(2^N)
- With Memoization it will take O(N)


```python 
# number of function calls
counter = 0

def fib(n):
    global counter 
    counter += 1 

    if n == 0 or n == 1:
        return n 
    return fib(n - 1) + fib(n - 2)


n = 7
print('\nFib of', n, '=', fib(n))
print('\nCounter:', counter)

```

Fib of 7 = 13
Counter: 41


Fib of 35 = 9227465
Counter: 29 860 703


## 136 Memoization 

add memoization to previous code 


- 100 indexes with None

    memo = [None] * 100

None None None None None None None None
[0   1    2    3    4    5    6    7]

 0 1 1 2 3 5 8 13
[0 1 2 3 4 5 6 7 ] 

- if the number is already in the list, retrieve it from the list instead of calculating it

    if memo[n] is not None:

- but what if we face new value that is not in memo yet? save it in memo

    memo[n] = fib(n - 1) + fib(n - 2)


```python 

memo = [None] * 100

def fib(n):
    if memo[n] is not None:
        return memo[n]

    if n == 0 or n == 1:
        return n 

    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]

```

imagine memoization list is empty

None None None None None None None None
[0   1    2    3    4    5    6    7]

then we call fib(7)
this line is called:
    memo[n] = fib(n - 1) + fib(n - 2)

here is the call stack:

| 1 |
| 2 |
| 3 |
| 4 |
| 4 |
| 5 | fib(n - 2)
| 6 | fib(n - 1)
| 7 |
|___|

fib(1) - does not call any other instance because:
    if n == 0 or n == 1:
        return n 

n is returned and fib(1) is popped from call stack

fib(0) fib(1) fib(2) fib(3)
 0     1      1      2       3 5 8 13
[0     1      2      3       4 5 6 7]


- fib(3) should call fib(2) and fib(1). But because we already have ready calculated values of fib(2) and fib(1) and memoized, it simply gets them, adds them up, and uses them. It does not call any function

```python
    if memo[n] is not None:
        return memo[n]

```

the same goes on for further function calls: fib(4), fib(5)


Big O with memoization: O(2N - 1)

N = 7
O(2N - 1) = 2*7 - 1 = 13
13: number of functions went onto and off the call stack

O(2N - 1)
    drop non-dominant: O(2N)
    drop the constant: O(N)


- Without memoization: O(2^N)
- With memoization: O(N)


```python 

memo = [None] * 100

# number of function calls
counter = 0

def fib(n):
    global counter 
    counter += 1 
    
    if memo[n] is not None:
        return memo[n]

    if n == 0 or n == 1:
        return n 

    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]


n = 7
print('\nFib of', n, '=', fib(n))
print('\nCounter:', counter)

```

Fib of 7 = 13
Counter: 13

Fib of 35 = 9 227 465
Counter: 69 
        (vs 29 million without memoization)


## 137 Bottom Up 

There are 2 ways of solving problems in Dynamic Programming:
1. Top Down 
2. Bottom Up

- Solving *recursively* (previous example) - top down
First we try to solve highest number

fib(7):
fib(7) -> fib(6) -> fib(5)

- Solving *iteratively*  we start from bottom and we build our way to the top: bottom up 


         0 1 1 2 3 5 8 13
        [0 1 2 3 4 5 6 7]
        ^             ^
     Top Down       Bottom Up

Top Down: we start from the right side of the list 
Bottom Up: we start from left side of the list


```python 
def fib(n):
    # initialize list with 0 and 1
    fib_list = [0, 1]
    
    # 2: first index we need to calculate
    # n + 1: include last element as well
    for index in range(2, n + 1):
        # sum of two previous elements
        next_fib = fib_list[index - 1] + fib_list[index - 2]
        fib_list.append(next_fib)
    
    return fib_list[n]

```

Big O using Bottom Up: O(N - 1)
    drop non-dominant: O(N)
fib(7) = O(N - 1) = 6 operations



```python 
counter = 0

def fib(n):
    # initialize list with 0 and 1
    fib_list = [0, 1]
    global counter 
    
    # 2: first index we need to calculate
    # n + 1: include last element as well
    for index in range(2, n + 1):
        counter += 1

        # sum of two previous elements
        next_fib = fib_list[index - 1] + fib_list[index - 2]
        fib_list.append(next_fib)
    
    return fib_list[n]

```

Fib of 7 = 13 
Counter: 6



Fib of 35 = 9227465
Counter: 34

we find fib(7). we return it
if we want to run it second time, it is O(N) because we have to iterate over list again.

We could use memoization with Bottom Up.
we find fib(7). we return it
if we want to run it second time, it is O(1)

Time Complexity - we get efficiency
Space Complexity - takes more memory 