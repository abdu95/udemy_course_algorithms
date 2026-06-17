# 34 MERGE SORT

## 122 Merge Sort  

- divide-and-conquer sorting algorithm. It works by repeatedly splitting a list into smaller sublists, sorting those sublists, and then combining (merging) them back together in the correct order.

Steps: 
1. Divide
Split the list into two halves until each sublist has only one element.

2. Conquer (Sort)
A single-element list is already sorted, so no work is needed here.

3. Merge
Combine the smaller sorted lists into bigger sorted lists until the full list is reconstructed.


✅ Example: Sorting
Given list: 5 4 7 1 3 2 8 6

- Step 1: Divide repeatedly
Split the list until single elements:

5 4 7 1 3 2 8 6
→ 5 4 7 1 | 3 2 8 6
→ 5 4 | 7 1 | 3 2 | 8 6
→ 5 | 4 | 7 | 1 | 3 | 2 | 8 | 6


- Step 2 & 3: Merge while sorting
Now merge sorted pairs step by step:

    Merge 5 and 4 → 4 5
    Merge 7 and 1 → 1 7
    Merge 3 and 2 → 2 3
    Merge 8 and 6 → 6 8

Now we have: 4 5 | 1 7 | 2 3 | 6 8


Next level merging:

Merge 4 5 and 1 7 → 1 4 5 7
Merge 2 3 and 6 8 → 2 3 6 8

Now: 1 4 5 7 | 2 3 6 8


Final merge:
Merge both halves:

1 4 5 7 and 2 3 6 8 →
1 2 3 4 5 6 7 8


✅ Final Result
Sorted list: 1 2 3 4 5 6 7 8

✅ Key Characteristics
    Time Complexity: O(n log n)
    Stable sort (preserves order of equal elements)
    Works well for large datasets


## 123 Merge Helper Function

Merge Sort has 3 steps. 3rd step - Merge. 
We write this helper function merge(): 
    accepts two sorted lists and merges them

Two sorted lists: [1 3 7 8] & [2 4 5 6]

- Loop through each list: i & j
- Compare item i & item j
- Whichever lowest - add to new combined list
- Go to next item
- Another loop over whichever list still has items - add them to list

[1 3 7 8] & [2 4 5 6]
 ^           ^
 i           j


## 125 Merge Sort Intro

merge_sort():
- accepts a list
- breaks a list into a half until there is only one item in each list
Then we use merge() helper function to combine each separate lists and create one sorted list 

We use recursion

merge_sort():
- Breaks lists in half (make problem smaller, breaks list into half)
- Base case: when len(the_list) = 1
- Use merge to combine lists



## 126 Merge Sort Code 

3 1 4 2 

```python 
def merge_sort(my_list):
    # base case 
    if len(my_list) == 1:
        return my_list
    # mid point to split in half
    mid_index = int(len(my_list)/2)
    # recursion
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])

    return merge(left, right)

```


merge_sort() will be called recursively - we will have multiple instances of MS on the call stack

Call Stack:

                               |    MS     |                    |    MS     |                    |  merge()  |
                               |   [3]     |                    |    [1]    |                     [3 1]=>[1 3]
               |    MS     |   |    MS     |    |    MS     |   |    MS     |    |    MS     |   |    MS     |
               |   [3 1]   |   |   [3 1]   |    |   [3 1]   |   |   [3 1]   |    |   [3 1]   |   |   [3 1]   |
|    MS     |  |    MS     |   |    MS     |    |    MS     |   |    MS     |    |    MS     |   |    MS     | 
| [3 1 4 2] |  | [3 1 4 2] |   | [3 1 4 2] |    | [3 1 4 2] |   | [3 1 4 2] |    | [3 1 4 2] |   | [3 1 4 2] |
|___________|  |___________|   |___________|    |___________|   |___________|    |___________|   |___________| 


## 127 Merge Sort Big O

SPACE COMPLEXITY - O(N)

We start from one list 
1 2 3 4 5 6 7 8 
Then divide it into two and create 2 lists
1 2 3 4 | 5 6 7 8 
Then we create 4 lists 
1 2 | 3 4 | 5 6 | 7 8 
Then we create 8 lists
1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 

Number of items stored in memory has doubled. 

TIME COMPLEXITY:O(N log N)

Merge Sort - Step 1: 
    divide items into half - O(log N)
It took 3 steps to dive one list into 8 lists
1 2 3 4 5 6 7 8 => 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 
logN - 2^3 = 8 
It took 3 steps to break this in half with 8 items

Merge Sort - Step 2: 
    merge items - O(N)
merge() helped function:
    while loops to combine lists into sorted list

O(N log N)

Previous three sort algorithms - O(N^2)
Merge Sort - O(N logN) - more efficient 

