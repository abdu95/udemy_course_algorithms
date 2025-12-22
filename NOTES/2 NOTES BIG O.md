Learning sequence:
1. watch course video
2. watch again and take minimal notes
3. try to write a code for an exercise for 30min
4. if no success, watch video solution 
5. now write a code to this solution without watching a video
6. If interview question: 
    1. repeat steps 3-5
    2. find a related Leetcode problem
    3. try to write a code for a problem for 30min
    4. if no success, watch Neetcode explanation video
    5. now repeat his code independently 

For each coding exercise, one python file that has code, logic, tests 



section   | coding | interview ex  
S&Q       | 8      | 4
Trees     | 7      | 1
HasTables | 8 | 11
Graph | 8 | 
Heaps | 7 | 2
Recursion | 3+7 | 2
BST | 9 | 2
Basic sorts | 8 | 3
Merge sort | 6 | 1
Quick sort | 5 | 
Dynamic programming | 5 | 7




# Section 2: Big O 
## 2.3 Intro
    way of comparing algorithms 

    Time Complexity 
        not measured in time. 
        measured in number of operations needed to complete algorithm 
    
    Space Complexity 
        how much space algorithm takes 

## 2.4 Worst case 

    Omega - Best case - find first item in a list = 1 operation
    Theta - Average case - find middle element = N/2 operations
    Omicron - Worst case - find last element = N operations

    Big O = Omicron - Big O always analyzes the worst case



## 2.5 O(N)

    Number of operations of algorithm is equal to number of input = N
    Function = Linear graph
        Y = number of operations
        X = N (input)

    Example:
```python 
    def print_items(n):
        for i in range(n):
            print(i)
```


## 2.6 Drop constants

```python 
    def print_items(n):
        for i in range(n):
            print(i)
        for j in range(n):
            print(j)
```

    runs N + N = 2N times 
    O(2N) -> simplify, drop constant = O(N)


## 2.7 (On^2)

    loop inside the loop 

```python 
    def print_items(n):
        for i in range(n):
            for j in range(n):
                print(i, j)

    print_items(10)
``` 
    prints N * N = 10*10 = 100 items 
    O(N*N) = O(N^2)

    Function = parabola - steeper - less efficient than O(N)

## 2.8 Drop non-dominants 


```python 
    def print_items(n):
        for i in range(n):
            for j in range(n):
                print(i, j)

        for k in range(n):
            print(k)

    print_items(10)
``` 
    
    O(N^2) + O(N)

    as N increases, O(N^2) increases significantly but not O(N). N^2 - dominant, N - non-dominant. Drop non-dominant
    O(N^2 + N) = O(N^2)


## 2.9 O(1)
    most efficient Big O

```python 
    def print_items(n):
        return n+n
```

    No matter how much input increases, the number of operations that algorithm performs remain constant (1 operation)


## 2.10 O(log N)


    O(log N)
        I have input N. If I iterate over each item - it would take O(n) - long time. I need faster algorithm.
        Instead, I want to cut input size in half in each iteration. In that way, how many operations I will have to perform? 
        More clearly, how many times I should cut input size in half until I find item (to reach base case)? 
        The answer is, as much as the logarithm of input. 

        Example:
        Input = 8. 
        Task: how many operations needed to perform to find any element in the list?
        The number of operations the algorithm performs is log2 N = log2 8 = 3. 
        2 to the what power is N = 8 ?

        Any algorithm that reduces the problem size by a constant fraction (like half) at each step will have a logarithmic time complexity.

        log 2 n and log10 n differ by a constant factor. But In Big O notation, we drop constant factors because they don't affect the growth rate. 


## 2.11 Different input terms 

O(N + N) = O(2N) = O(N)
```python 
    def print_items(n):
        for i in range(n):
            print(i)
        for j in range(n):
            print(j)
```


O(a + b)
```python 
    def print_items(a, b):
        for i in range(a):
            print(i)
        for j in range(b):
            print(j)
```

O(a*b)
```python 
    def print_items(a, b):
        for i in range(a):
            for j in range(b):
                print(i, j)
```

## 2.12 Big O: Lists
    list.append(10) -add item to the end of list - one operation = O(1)
    list.pop() - remove from the end of the list - one operation = O(1)
    list.pop(0) - remove from the beginning of the list = O(N)
        remove and reindex each element of the list (iterate over each item of the list)
    list.insert(0, 11) - insert element to the beginning of the list = O(N)
        insert and reindex each element of the list (iterate over each item of the list)
    
    If operation is related to the end of the list (append, pop) - its O(1)
    If operation is related to the beginning of the list ( pop(0), insert(0, X) ) - its O(N) - because of reindexing

    Look up by value = O(N) 
        value is unknown. So iterate over each item until value is found
    Look up by index = O(1)
        we just go to index - one operation 
    

## 2.13 

    sorted by efficiency descending:
    O(N^2)
    O(N logN) - most efficient sorting algorithm
    O(N)
    O(log N)
    O(1)

    As N grows, O(N^2) grows very fast - its very inefficient

    O(N^2) - loop within a loop
    O(N)   - proportional 
    O(logN) - divide and conquer 
    O(1)   - constant 



    Big O cheatsheet -         https://www.bigocheatsheet.com/
    Array sorting algorithms 
        Time complexity: Best Average Worst 
        Space complexity: Worst




8 Apr 2025
# Section 3: Classes & Pointers

## 3.14 Classes

=> self parameter

    In Python, the self parameter in class methods refers to the instance of the class itself. It's used to access variables and methods associated with the class instance. Here's a simple example:

```python
class MyClass:
    def __init__(self, value):
        self.value = value

    def display_value(self):
        print(self.value)
```
    In this example, self.value refers to the value attribute of the instance of MyClass.

    You can technically use any name instead of self, like instance, but it's strongly recommended to stick with self because it's a widely accepted convention in the Python community. Using self makes your code more readable and understandable to others who are familiar with Python.

    The term self is used because it clearly indicates that the parameter refers to the object itself. It's a way to make the code more intuitive and easier to follow.

=> why self is first parameter?

*When you call a method on an instance of a class, Python automatically passes the instance as the first argument to the method.* This is  what makes self refer to the instance.

    Here's a breakdown of what happens behind the scenes:

    Instance Creation: When you create an instance of a class, Python allocates memory for the new object and initializes it using the __init__ method.

obj = MyClass(10)
Method Call: When you call a method on the instance, Python implicitly passes the instance as the first argument to the method.

obj.display_value()
This is equivalent to:

MyClass.display_value(obj)
    
    In the method definition, self is used to refer to the instance that was passed as the first argument. This allows you to access attributes and other methods of the instance.
    You can use any name instead of self, but it's a convention to use self for clarity and readability. Here's an example using instance instead of self:

```python
class MyClass:
    def __init__(instance, value):
        instance.value = value

    def display_value(instance):
        print(instance.value)
```

    While this code works, it's less conventional and might confuse other Python developers who are used to seeing self.


## Pointers

INTEGER = immutable 
    num2 = num1
        pointing to same address
        changing value of num2 doesn't change value of num1

DICT = mutable
    dict2 = dict1
        pointing to same address
        changing key's value in dict2 will change key's value of dict1 too


=> id() and other functions

    In Python, the id() function returns the "identity" of an object, which is typically its memory address. While id() gives you a unique identifier for the object, there are other ways to inspect and interact with objects in memory, though Python abstracts away many low-level memory details for safety and simplicity.
    Here are a few other useful functions and modules for inspecting objects:

    sys.getsizeof(): 
        This function returns the size of an object in bytes.

```python
import sys
num1 = 10
print(sys.getsizeof(num1))  # Output: size of num1 in bytes
```    
    gc module: The garbage collection module can provide insights into objects and memory management.

import gc
print(gc.get_objects())  # Returns a list of all objects tracked by the garbage collector

    inspect module: This module provides several useful functions to get information about live objects, including classes, methods, functions, and code objects.

import inspect
print(inspect.getmembers(num1))  # Returns all the members of the object
    
    memoryview: This built-in function allows you to access the internal data of an object that supports the buffer protocol without copying it.

byte_array = bytearray('hello', 'utf-8')
mem_view = memoryview(byte_array)
print(mem_view[0])  # Output: 104 (ASCII value of 'h')
These tools can help you understand more about the objects you're working with, but Python intentionally limits direct memory manipulation to maintain safety and simplicity.

