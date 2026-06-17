
# CODING EXERCISE 57

"""
HT: Item In Common ( ** Interview Question)
Write a function item_in_common(list1, list2) that takes two lists as input and returns True if there is at least one common item between the two lists, False otherwise.

Use a dictionary to solve the problem that creates an O(n) time complexity.
"""

def item_in_common(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True
    
    for j in list2:
        if j in my_dict:
            return True
        
    return False


# list1 = [1,3,5]
# list2 = [2,4,5]

# print(item_in_common(list1, list2))


# CODING EXERCISE 58

"""
HT: Find Duplicates ( ** Interview Question)
find_duplicates()

Problem: Given an array of integers nums, find all the duplicates in the array using a hash table (dictionary).
Input: A list of integers nums.
Output: A list of integers representing the numbers in the input array nums that appear more than once. If no duplicates are found in the input array, return an empty list [].
"""

def find_duplicates(nums):
    nums_d = {}
    dups = []
    
    for item in nums:
        if item in nums_d:
            nums_d[item] += 1
        else: 
            nums_d[item] = 1
    
    for key, value in nums_d.items():
        if value > 1:
            dups.append(key)
    return dups


# CODING EXERCISE 58

"""
HT: First Non-Repeating Character ( ** Interview Question)
You have been given a string of lowercase letters.

Write a function called first_non_repeating_char(string) that finds the first non-repeating character in the given string using a hash table (dictionary). If there is no non-repeating character in the string, the function should return None.

For example, if the input string is "leetcode", the function should return "l" because "l" is the first character that appears only once in the string. Similarly, if the input string is "hello", the function should return "h" because "h" is the first non-repeating character in the string.
"""

def first_non_repeating_char(string):
    chars_dict = {}
    
    # count each character
    for char in string:
        chars_dict[char] = chars_dict.get(char, 0) + 1
        
    
    # Find first character with count 1
    for ch in string:
        if chars_dict[ch] == 1:
            return ch

    return None


# CODING EXERCISE 60

"""
HT: Group Anagrams ( ** Interview Question)
You have been given an array of strings, where each string may contain only lowercase English letters. You need to write a function group_anagrams(strings) that groups the anagrams in the array together using a hash table (dictionary). The function should return a list of lists, where each inner list contains a group of anagrams.

For example, if the input array is ["eat", "tea", "tan", "ate", "nat", "bat"], the function should return [["eat","tea","ate"],["tan","nat"],["bat"]] because the first three strings are anagrams of each other, the next two strings are anagrams of each other, and the last string has no anagrams in the input array.

You need to implement the group_anagrams(strings) function and return a list of lists, where each inner list contains a group of anagrams according to the above requirements.
"""

def group_anagrams(strings):
    words_dict = {}
    
    for word in strings:
        sorted_word = "".join(sorted(word))
        
        # Add to dictionary
        if sorted_word not in words_dict:
            words_dict[sorted_word] = []

        words_dict[sorted_word].append(word)
    
    
    # return grouped values
    return list(words_dict.values())


# CODING EXERCISE 61

"""
HT: Two Sum ( ** Interview Question)
two_sum()

Problem: Given an array of integers nums and a target integer target, find the indices of two numbers in the array that add up to the target.

The main challenge here is to implement this function in one pass through the array. This means you should not iterate over the array more than once. Therefore, your solution should have a time complexity of O(n), where n is the number of elements in nums.

Input:
    A list of integers nums .
    A target integer target.

Output: A list of two integers representing the indices of the two numbers in the input array nums that add up to the target. If no two numbers in the input array add up to the target, return an empty list [].
"""

"""
For a number num, the value we need is:
complement = target - num

👉 If we've seen complement before → we found the answer!
"""


def two_sum(nums, target):
    nums_d = {}
    
    
    for i, num in enumerate(nums):
        complement = target - num

        # Step 1: Check if complement already exists
        if complement in nums_d:
            return [nums_d[complement], i]

        # Step 2: Store current number
        nums_d[num] = i

    return []


# CODING EXERCISE 62

"""
HT: Subarray Sum ( ** Interview Question)
Given an array of integers nums and a target integer target, write a Python function called subarray_sum that finds the indices of a contiguous subarray in nums that add up to the target sum using a hash table (dictionary).

Your function should take two arguments:
    nums: a list of integers representing the input array
    target: an integer representing the target sum

Your function should return a list of two integers representing the starting and ending indices of the subarray that adds up to the target sum. If there is no such subarray, your function should return an empty list.
"""

"""
👉 While iterating:

Keep track of prefix sums in a dictionary
Check if (current_sum - target) has been seen before

If yes 👉 you found the subarray ✅
"""


def subarray_sum(nums, target):
    prefix_sum = 0
    seen = {0: -1}  # prefix_sum -> index

    for i, num in enumerate(nums):
        prefix_sum += num

        # Check if we have seen the needed prefix
        if (prefix_sum - target) in seen:
            start = seen[prefix_sum - target] + 1
            end = i
            return [start, end]

        # Store current prefix_sum
        seen[prefix_sum] = i

    return []


# 63 SET: REMOVE DUPLICATES

"""
You have been given a list my_list with some duplicate values. Your task is to write a Python program that removes all the duplicates from the list using a set and then prints the updated list.

You need to implement a function remove_duplicates(my_list) that takes in the input list my_list as a parameter and returns a new list with no duplicates.

Your function should not modify the original list, instead, it should create a new list with unique values and return it.
"""

def remove_duplicates(my_list):
    return list(set(my_list))



# 64 Has Unique Chars ( ** Interview Question)

"""
Write a function called has_unique_chars that takes a string as input and returns True if all the characters in the string are unique, and False otherwise.

For example, has_unique_chars('abcdefg') should return True, while has_unique_chars('hello') should return False.
"""

def has_unique_chars(string):
    input_list_len = len(string)
    set_len = len(set(string))
    if input_list_len == set_len:
        return True
    else:
        return False


# 65 Set: Find Pairs ( ** Interview Question)

"""
You are given two lists of integers, arr1 and arr2, and a target integer value, target. Your task is to find all pairs of numbers (one from arr1 and one from arr2) whose sum equals target.

Write a function called find_pairs that takes in three arguments: arr1, arr2, and target, and returns a list of all such pairs.

Assume that each array does not contain duplicate values.

The tests for this exercise assume that arr1 is the list being converted to a set.

Pairs should be returned in the order they are found while iterating through arr2.

Input
    arr1: a list of integers
    arr2: a list of integers
    target: an integer

Output: Your function should return a list of tuples, where each tuple contains two integers from arr1 and arr2 that add up to target. The first element of each tuple should be from arr1 and the second from arr2.
"""

def find_pairs(arr1, arr2, target):
    result = []
    arr1_set = set(arr1)  # O(1) lookup

    for num in arr2:
        needed = target - num

        if needed in arr1_set:
            result.append((needed, num))

    return result


# 66 Set: Longest Consecutive Sequence ( ** Interview Question)

"""

Given an unsorted array of integers, write a function that finds the length of the  longest_consecutive_sequence (i.e., sequence of integers in which each element is one greater than the previous element).
Use sets to optimize the runtime of your solution.

Input: An unsorted array of integers, nums.
Output: An integer representing the length of the longest consecutive sequence in nums.


👉 Only start counting when you find the beginning of a sequence
A number num is the start of a sequence if:
num - 1 NOT in set

✅ That means it's the first number in that chain
"""

def longest_consecutive_sequence(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        # Step 1: Check if this is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            # Step 2: Count forward
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            # Step 3: Update max length
            longest = max(longest, current_length)

    return longest


