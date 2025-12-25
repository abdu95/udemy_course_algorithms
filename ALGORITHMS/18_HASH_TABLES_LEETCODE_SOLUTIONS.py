# HASH TABLES
 
# 25 Dec 2025 


# 2956. Find Common Elements Between Two Arrays
# Status: Solved 

# my initial solution
def findIntersectionValues(nums1, nums2):
    answer1, answer2 = (0, 0)
    answer1_dict, answer2_dict = {}, {}
    
    for num in nums1:
        answer1_dict[num] = True
    
    for num in nums2:
        answer2_dict[num] = True
    
    for num in nums1:
        if num in answer2_dict:
            answer1 += 1
        
    for num in nums2:
        if num in answer1_dict:
            answer2 += 1
        
    return [answer1, answer2]


print(findIntersectionValues([2,3,2], [1,2]))

# simplify using dictionary 
def findIntersectionValues(self, nums1, nums2):
    d1, d2 = {}, {}

    for x in nums1:
        d1[x] = 1
    for x in nums2:
        d2[x] = 1

    a1 = sum(x in d2 for x in nums1)
    a2 = sum(x in d1 for x in nums2)

    return [a1, a2]


# simplify using set

def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
    set1 = set(nums1)
    set2 = set(nums2)

    answer1 = sum(num in set2 for num in nums1)
    answer2 = sum(num in set1 for num in nums2)

    return [answer1, answer2]
