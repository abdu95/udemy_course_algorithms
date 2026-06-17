# 102 List: Remove Element ( ** Interview Question)

""" 
Given a list of integers nums and an integer val, write a function remove_element that removes all occurrences of val in the list in-place and returns the new length of the modified list.
The function should not allocate extra space for another list; instead, it should modify the input list in-place with O(1) extra memory.

Input: 
    A list of integers nums .
    An integer val representing the value to be removed from the list.

Output: An integer representing the new length of the modified list after removing all occurrences of val.

Constraints:

    Do not use any built-in list methods, except for pop() to remove elements.
    It is okay to have extra space at the end of the modified list after removing elements.
"""

def remove_element(nums, val):
    for num in nums: 
        if num == val:
            nums.pop(num)

    return len(nums)

"""
🔴 Problem 1: pop(num) is wrong: pop() expects an index, not a value
🔴 Problem 2: Modifying list while iterating
When you remove elements during a for loop:

Python shifts elements left
Some elements get skipped

"""

def remove_element(nums, val):
    i = 0

    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)  # remove current
        else:
            i += 1  # only move forward if NOT removed

    return len(nums)


# 103 List: Find Max Min ( ** Interview Question)

"""
Write a Python function that takes a list of integers as input and returns a tuple containing the maximum and minimum values in the list.

The function should have the following signature:
    def find_max_min(myList):


Where myList is the list of integers to search for the maximum and minimum values.

The function should traverse the list and keep track of the current maximum and minimum values. It should then return these values as a tuple, with the maximum value as the first element and the minimum value as the second element.

For example, if the input list is [5, 3, 8, 1, 6, 9], the function should return (9, 1) since 9 is the maximum value and 1 is the minimum value.
"""


def find_max_min(my_list):
    max_min_d = {
        "max": my_list[0],
        "min": my_list[0]
    }

    for num in my_list:
        if num > max_min_d["max"]:
            max_min_d["max"] = num
        if num < max_min_d["min"]:
            max_min_d["min"] = num

    return (max_min_d["max"], max_min_d["min"])


# 104 List: Find Longest String ( ** Interview Question)

""" 
Write a Python function called find_longest_string that takes a list of strings as an input and returns the longest string in the list. 
The function should iterate through each string in the list, check its length, and keep track of the longest string seen so far. 
Once it has looped through all the strings, the function should return the longest string found.
"""

def find_longest_string(strings):
    max_len = 0
    max_string = ""
    
    for string in strings:
        if len(string) > max_len:
            max_len = len(string)
            max_string = string
    
    return max_string


# 105 List: Remove Duplicates ( ** Interview Question)

"""
Given a sorted list of integers, rearrange the list in-place such that all unique elements appear at the beginning of the list.

Your function should return the new length of the list containing only unique elements. Note that you should not create a new list or use any additional data structures to solve this problem. The original list should be modified in-place.

Constraints:
    The input list is sorted in non-decreasing order.
    The input list may contain duplicates.
    The function should have a time complexity of O(n), where n is the length of the input list.
    The function should have a space complexity of O(1), i.e., it should not use any additional data structures or create new lists (this also means you cannot use a set like we did earlier in the course).


Example:

Input: nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4] Function call: new_length = remove_duplicates(nums) Output: new_length = 5 Modified list: nums = [0, 1, 2, 3, 4, 2, 2, 3, 3, 4] (first 5 elements are unique)

Explanation: The function modifies the original list nums in-place, moving unique elements to the beginning of the list, followed by duplicate elements. The new length returned by the function is 5, indicating that there are 5 unique elements in the list. The first 5 elements of the modified list nums are the unique elements [0, 1, 2, 3, 4].
"""

"""
This is a classic two-pointer problem, very similar to the one you just solved 👍

✅ Key Idea
Since the list is sorted, duplicates will always be next to each other.
👉 So we dont need extra memory — we just:

Keep one pointer for unique elements
Scan with another pointer
"""

def remove_duplicates(nums):
    if not nums:
        return 0

    k = 0  # index of last unique element

    for i in range(1, len(nums)):
        if nums[i] != nums[k]:
            k += 1
            nums[k] = nums[i]

    return k + 1


# 106 List: Max Profit ( ** Interview Question)

""" 
You are given a list of integers representing stock prices for a certain company over a period of time, where each element in the list corresponds to the stock price for a specific day.

You are allowed to buy one share of the stock on one day and sell it on a later day.

Your task is to write a function called max_profit that takes the list of stock prices as input and returns the maximum profit you can make by buying and selling at the right time.

Note that you must buy the stock before selling it, and you are allowed to make only one transaction (buy once and sell once).

Constraints: Each element of the input list is a positive integer representing the stock price for a specific day.

Function signature: def max_profit(prices):

Example:

Input: prices = [7, 1, 5, 3, 6, 4]
Function call: profit = max_profit(prices)
Output: profit = 5

Explanation: The maximum profit can be achieved by buying the stock on day 2 (price 1) and selling it on day 5 (price 6), resulting in a profit of 6 - 1 = 5.

"""

def max_profit(prices):
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        # Update minimum price
        if price < min_price:
            min_price = price

        # Calculate profit
        profit = price - min_price

        # Update maximum profit
        if profit > max_profit:
            max_profit = profit

    return max_profit


# 107 List: Rotate ( ** Interview Question)

"""
You are given a list of n integers and a non-negative integer k.

Your task is to write a function called rotate that takes the list of integers and an integer k as input and rotates the list to the right by k steps.

The function should modify the input list in-place, and you should not return anything.

Constraints:
    Each element of the input list is an integer.
    The integer k is non-negative.

Function signature: def rotate(nums, k):

Example:

Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
Function call: rotate(nums, k)
Output: nums = [5, 6, 7, 1, 2, 3, 4]


Explanation: The list has been rotated to the right by 3 steps:
    [7, 1, 2, 3, 4, 5, 6]
    [6, 7, 1, 2, 3, 4, 5]
    [5, 6, 7, 1, 2, 3, 4]

"""

def rotate(nums, k):
    n = len(nums)
    k = k % n  # handle k > n

    # Helper function to reverse in-place
    def reverse(left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    # Step 1: reverse whole array
    reverse(0, n - 1)

    # Step 2: reverse first k elements
    reverse(0, k - 1)

    # Step 3: reverse remaining elements
    reverse(k, n - 1)


# 108 List: Max Sub Array ( ** Interview Question)

""" 
Given an array of integers nums, write a function max_subarray(nums) that finds the contiguous subarray (containing at least one number) with the largest sum and returns its sum.

Remember to also account for an array with 0 items.

Function Signature:
def max_subarray(nums):


Input: A list of integers nums.
Output: An integer representing the sum of the contiguous subarray with the largest sum.

Example:

max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
Output: 6
Explanation: The contiguous subarray [4, -1, 2, 1] has the largest sum, which is 6.
"""

def max_subarray(nums):
    # Edge case: empty list
    if not nums:
        return 0
    
    current_sum = nums[0]
    max_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum


#  https://scottbarrett.com