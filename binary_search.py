# 8 Sep 2021 
# https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index_n = -1

        if len(nums) % 2 == 0:
            # array has even number of elements
            if nums[len(nums)//2 -1] < target:
                # work with right half, target is not in left half, drop left half
                start = len(nums) // 2
                end = len(nums) - 1
                for item in range(start, end+1):
                    if target == nums[item]:
                        index_n = item
            else:
                # work with left half
                start = 0
                end = len(nums)//2 -1
                for item in range(start, end+1):
                    if target == nums[item]:
                        index_n = item        
        else:
            # array has odd number of elements
            middle = len(nums)//2
            if target == nums[middle]:
                index_n = middle
            elif target > nums[middle]:
                # work with right half, target is in the right half
                start = middle + 1
                end = len(nums) - 1
                for item in range(start, end+1):
                    if target == nums[item]:
                        index_n = item
            else:
                # work with left half, target is in the left half
                start = 0
                end = middle - 1
                for item in range(start, end + 1):
                    if target == nums[item]:
                        index_n = item
        
        return index_n
    
