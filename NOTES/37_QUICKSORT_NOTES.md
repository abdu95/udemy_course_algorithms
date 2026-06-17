
# 37 Quick Sort 

Quick sort is a divide-and-conquer sorting algorithm. It works by selecting a special element called a pivot, then rearranging (partitioning) the other elements so that:

- All values smaller than the pivot go to its LEFT 
- All values greater than the pivot go to its RIGHT
After that, the same process is applied recursively to the left and right parts until the entire list is sorted.

It is called quick sort because, in practice, it is usually very fast compared to other sorting algorithms (like bubble sort or selection sort).
The main reasons:

It reduces unnecessary comparisons by splitting the problem quickly
It works efficiently on large datasets
Its average time complexity is O(n log n), which is very good

Even though in the worst case it can be slower (O(n²)), good pivot selection usually keeps it “quick”.


STEPS:
- Choose a pivot element (first, last, or middle element)
- Partition the array:
    Move smaller elements to the left
    Move larger elements to the right
- Place the pivot in its correct position
- Recursively apply the same process on:
    Left subarray
    Right subarray
- Stop when subarrays have 1 or 0 elements (already sorted)


        █   
    █   █     
    █   █     █
  █ █   █     █
  █ █   █ █   █
  █ █   █ █ █ █
  █ █ █ █ █ █ █
  -----------
  4 6 1 7 3 2 5



Initial Array
4 6 1 7 3 2 5

- Step 1: Choose Pivot
Pivot = 4 (first element)

- Step 2: Partition Around Pivot (4)
We rearrange elements so:
    Smaller than 4 → go left
    Greater than 4 → go right

Process the list:
    6 → greater
    1 → smaller
    7 → greater
    3 → smaller
    2 → smaller
    5 → greater


So we group them as:
    Smaller → 1 3 2
    Pivot → 4
    Greater → 6 7 5
New arrangement: 1 3 2 | 4 | 6 7 5

Now 4 is in its correct sorted position


- Step 3: Sort Left Subarray (1 3 2)
Choose pivot = 1
    Partition:
    Smaller → (none)
    Pivot → 1
    Greater → 3 2

Result: 1 | 3 2


Sort (3 2)
Choose pivot = 3
    Partition:
    Smaller → 2
    Pivot → 3
    Greater → (none)

Result: 2 | 3

So left side becomes: 1 2 3


- Step 4: Sort Right Subarray (6 7 5)
Choose pivot = 6
    Partition:
    Smaller → 5
    Pivot → 6
    Greater → 7

Result: 5 | 6 | 7

Final Sorted Array: 1 2 3 4 5 6 7


✅ Summary:
4 splits the array into:
(1 3 2) + 4 + (6 7 5)
Then each side is recursively sorted the same way.


## 129 Pivot Intro 

pivot(list) helper function for quick sort

Pick a pivot
All items < pivot: on one side
All items > pivot: on other side
Move pivot to position where it will be when list is sorted 
Return index of pivot 


                  █   
              █   █          
              █   █     █
            █ █   █     █
            █ █   █ █   █
            █ █   █ █ █ █
            █ █ █ █ █ █ █
            -----------
            4 6 1 7 3 2 5
    [pivot] ^ ^ ^ 
         [swap] i

declare pivot index
declare swap index 

if i < pivot and swap > pivot:
    swap

after finishing the iteration, swap position of pivot and swap - to put pivot in right position

return index of swap (now this position is where pivot stay)

- after this, we do quick sort again on left side, starting from start position up to but not including swap index
- we do quick sort again on right side, starting from pivot+1 position up to the end of list



## 130 Pivot Code

```python

def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp

# rearrange items so that items < pivot are on left and items > pivot are on right
# put pivot in correct position
# return index of pivot 

def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index

    # for loop goes up to but not including - hence end_index+1
    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)

    # now move the pivot to its correct position:
    # put pivot var to swap var positions
    swap(my_list, pivot_index, swap_index)
    return swap_index

```

## 131 Quick Sort Code 


                  █   
              █   █          
              █   █     █
            █ █   █     █
            █ █   █ █   █
            █ █   █ █ █ █
            █ █ █ █ █ █ █
            -------------
            4 6 1 7 3 2 5

pivot function returns this:
    rearrange items so that items < pivot are on left and items > pivot are on right
    put pivot in correct position
    return index of pivot 

             █
           █ █ 
           █ █ █
        █  █ █ █
     █  █  █ █ █
 █   █  █  █ █ █
 █ █ █  █  █ █ █
-----------------
[2 1 3] 4 [6 7 5] 
        ^ 
      pivot

quick_sort():
    recursively run pivot() again on left and right sides

when quick_sort() runs pivot() on left side:
    everything less than pivot - will move to the left <<
    everything more than pivot - will move to the right >>


     █
   █ █
 █ █ █
[1 2 3]
   ^
 pivot

now we call quick_sort() recursively on left [1] and right [3]
only one item in each side - so we stop calling quick_sort() - already sorted


when quick_sort() runs pivot() on right side:
    everything less than pivot - will move to the left <<
    everything more than pivot - will move to the right >>
 
 
     █
   █ █
 █ █ █
 █ █ █
 █ █ █
 █ █ █
 █ █ █
[5 6 7]
   ^
 pivot

now we call quick_sort() recursively on left [5] and right [7]
only one item in each side - so we stop calling quick_sort() - already sorted

Final result: 

             █
           █ █
         █ █ █
       █ █ █ █
     █ █ █ █ █
   █ █ █ █ █ █ 
 █ █ █ █ █ █ █
[1 2 3 4 5 6 7]


```python 

def quick_sort(my_list, left, right):
    # base case:
    if left < right:
        pivot_index = pivot(my_list, left, right)

        # starting from 0 up until pivot index 
        quick_sort(my_list, left, pivot_index-1)

        # starting from pivot + 1 until end
        quick_sort(my_list, pivot_index + 1, right)

    return my_list
    
```


## 132 Quick Sort Big O

Quick Sort - O(N logN) (best case and average case)
    uses pivot() function. It has FOR loop that iterates over a list - O(N)
    quick_sort() is called recursively. 8 items 3 steps: 2^3 = 8. O(log N)

Quick Sort - Worst Case
    when we are given already sorted list
    we run pivot() function in each element of the list: O(N) runs N times = O(N^2)

    

