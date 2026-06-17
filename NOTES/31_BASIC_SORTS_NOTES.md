
# Basic Sorts 

## 115 Bubble Sort: Intro

simple sorting algorithm that repeatedly steps through a list, **compares adjacent elements, and swaps them if they are in the wrong order**. This process is repeated until the entire list is sorted. It gets its name because the larger (or smaller) elements gradually "bubble" to the top (end) of the list with each pass


4 2 6 5 1 3 



Initial state
    █
    █ █
█   █ █
█   █ █   █
█ █ █ █   █
█ █ █ █ █ █
-----------
4 2 6 5 1 3


1. Compare 4 and 2 
because 4 > 2 → swap

    █
    █ █
  █ █ █
  █ █ █   █
█ █ █ █   █
█ █ █ █ █ █
-----------
2 4 6 5 1 3

2. Compare 4 and 6 → no swap

3. Compare 6 and 5 → swap

      █
    █ █
  █ █ █
  █ █ █   █
█ █ █ █   █
█ █ █ █ █ █
-----------
2 4 5 6 1 3


4. Compare 6 and 1 → swap

        █
    █   █
  █ █   █
  █ █   █ █
█ █ █   █ █
█ █ █ █ █ █
-----------
2 4 5 1 6 3

5. Compare 6 and 3 → swap

          █
    █     █
  █ █     █
  █ █   █ █
█ █ █   █ █
█ █ █ █ █ █
-----------
2 4 5 1 3 6


Now the largest element (6) has **bubbled up** to the end.
We had 6 items in list and we did 5 comparisons


Now 5 items left to sort 

          █
    █     █
  █ █     █
  █ █   █ █
█ █ █   █ █
█ █ █ █ █ █
-----------
2 4 5 1 3 6

1. 2 and 4 → no swap

2. 4 and 5 → no swap

3. 5 and 1 → swap

          █
      █   █
  █   █   █
  █   █ █ █
█ █   █ █ █
█ █ █ █ █ █
-----------
2 4 1 5 3 6


4. 3 and 5 → swap

          █
        █ █
  █     █ █
  █   █ █ █
█ █   █ █ █
█ █ █ █ █ █
-----------
2 4 1 3 5 6

we did 4 comparisons

2nd largest item in the list has been sorted - bubbled up

1. 2 and 4 → no swap

2. 4 and 1 → swap

          █
        █ █
    █   █ █
    █ █ █ █
█   █ █ █ █
█ █ █ █ █ █
-----------
2 1 4 3 5 6


3. 4 and 3 → swap

          █
        █ █
      █ █ █
    █ █ █ █
█   █ █ █ █
█ █ █ █ █ █
-----------
2 1 3 4 5 6

We did 3 comparisons

1. 2 and 1 → swap


          █
        █ █
      █ █ █
    █ █ █ █
  █ █ █ █ █
█ █ █ █ █ █
-----------
1 2 3 4 5 6

2. 2 and 3 → no swap

we did 2 comparisons 


1. 1 and 2 → no swap

now we have complete sorted list 



## 117  Selection Sort

Selection Sort is a sorting algorithm that repeatedly:
  Finds the smallest element in the unsorted part of the list
  Swaps it with the first unsorted position

It divides the array into:
  a sorted section on the left
  an unsorted section on the right

After every pass, one more element is permanently placed in the correct position.


Initial state:
```
      █
      █ █
  █   █ █
  █   █ █   █
  █ █ █ █   █
  █ █ █ █ █ █
  -----------
 [4 2 6 5 1 3]

  0 1 2 3 4 5
  ^
```
We start at index 0.
min_index = 0 (index where the minimim value is)

- Pass 1
Find the smallest number in:
4 2 6 5 1 3

Smallest = 1
Swap 4 and 1

[1] 2 6 5 4 3  [sorted part]

Now 1 is permanently sorted.

- Pass 2
Search smallest in remaining unsorted section:
2 6 5 4 3 

Smallest = 2

Already in correct place → no swap needed.

Sorted part:
[1 2] 6 5 4 3

- Pass 3
Search smallest in:
6 5 4 3 

Smallest = 3
Swap 6 and 3

[1 2 3] 5 4 6


- Pass 4
Search smallest in:
5 4 6 

Smallest = 4
Swap 5 and 4

[1 2 3 4] 5 6


- Pass 5
Search smallest in:

5 6 

Smallest = 5
Already correct.

Done ✅


Time Complexity

  Case Complexity 
  Best O(n²)
  Average O(n²)
  Worst O(n²)


## 119 Insertion sort 

  take one element
  place it into the correct position among already sorted elements

The left side of the array is always kept sorted.

Example 
  1 2 4 3 5 6

Notice this array is already almost sorted. Insertion Sort works very well for nearly sorted arrays.


Main Idea
At each step:
  Pick the next element
  Compare it with elements to its left
  Shift larger elements right
  Insert the element into the correct position


Initial state:
[1] 2 4 3 5 6

Start with the first element.
1
This is already sorted by itself.
Sorted part:
[1]
Unsorted part:
2 4 3 5 6

- Pass 1
Take the next element: 2
Compare it with 1.
Since 2 > 1, it is already in the correct position.

[1 2] 4 3 5 6


- Pass 2
Take the next element: 4
Compare it with 2.
Since 4 > 2, no movement is needed.
Result:
[1 2 4] 3 5 6

- Pass 3
Take the next element: 3
Now compare from right to left.
Compare 3 with 4:

4 > 3
shift 4 one position to the right

Temporary state:
1 2 3 4 5 6
Now compare 3 with 2:

2 < 3
stop shifting

Insert 3 after 2.
Result:
[1 2 3 4] 5 6


- Pass 4
Take the next element: 5
Compare with 4.
5 is already larger than 4, so no movement is needed.
Result:
1 2 3 4 5 6

- Pass 5
Take the next element: 6
Compare with 5.
6 is already larger, so no movement is needed.
Final result:
1 2 3 4 5 6

Done ✅



Complexity
  Case Time
  Best O(n)
  Average O(n²)
  Worst O(n²)


Key Difference
  Algorithmn Main Ideam
  Bubble Sort Swap neighbors repeatedly
  Selection Sort Select minimum element
  Insertion Sort Insert into sorted section


## 121 Insertion Sort Big O

Insertion sort has loop within a loop - O(N^2)

1 2 [4 3] 5 6 
When we have almost sorted data, time complexity - O(N)

Space complexity:
  Bubble, Selection, and Insertion Sort have O(1) space complexity:
  They sort the list in place - they dont have to create copies of the list 



