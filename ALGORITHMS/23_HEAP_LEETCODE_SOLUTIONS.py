from typing import List


"""
    01/05/2026
    
    I want to solve this heap related problem on leetcode. 
    506. Relative Ranks
    I don't need code or full explanation. I want to solve by myself. Give only guidance.
    1. I learned heaps and I am not sure I learned enough to solve this problem. 
    2. I know in heap, max or min element should be on top. I also have bubble up in heap - when you insert an item to the end of the heap and bubble it up until it finds the appropriate spot. While doing bubble up, you compare the current node with the parent node in each step. If the current node is bigger, you swap both items positions.
    3. Let's say I did bubble up. But now, how I turn this heap to same order as input list 
"""

# My first attempt

# def findRelativeRanks(score):
#     score_position = [] 
#     for i in range(len(score)): 
#         score_position.append([score[i], i])
#     max_heap = []
#     # add each item from list to max_heap
#     for i in range(len(score_position)):
#         # add node to back of max_heap 
#         node_to_add = score_position[i]
#         max_heap.append(node_to_add)
#         if len(max_heap) == 1:
#             continue 
#         else:
#             # bubble up: compare current node with its parent 
#             # if current node > parent_node, then swap
#             # iterate through whole max_heap until node_to_add < parent_node
#             current_index = len(max_heap)-1
#             parent_index = (current_index-1) 
#             while max_heap[parent_index][0] < node_to_add[0]:
#                 # swap logic
#                 max_heap[parent_index], max_heap[current_index] = max_heap[current_index], max_heap[parent_index]
#                 current_index = parent_index 
#                 parent_index = (current_index -1) // 2
    
#     answer = [None] * len(score)
#         # rank = max_heap.index(max_heap[len(max_heap)-1])
#     for i in range(len(max_heap)):
#         rank = len(max_heap) 
#         score_original_index = max_heap.pop()
#         if rank == 1:
#             rank = 'Gold Medal'
#         elif rank == 2:
#             rank = 'Silver Medal'
#         elif rank == 3:
#             rank = 'Bronze Medal'
#         answer[score_original_index[1]] = str(rank)

#     return answer 
    



def findRelativeRanks(score):
    # pair score with original index
    score_index = [(s, i) for i, s in enumerate(score)]
    
    # sort by score descending
    score_index.sort(reverse=True, key=lambda x: x[0])
    
    answer = [""] * len(score)
    
    # ( rank_number , (score_value, original_index) )
    for rank, (val, idx) in enumerate(score_index, start=1):
        if rank == 1:
            answer[idx] = "Gold Medal"
        elif rank == 2:
            answer[idx] = "Silver Medal"
        elif rank == 3:
            answer[idx] = "Bronze Medal"
        else:
            answer[idx] = str(rank)
    
    return answer


# result = findRelativeRanks([10,3,8,9,4])
# result = findRelativeRanks([5,4,3,2,1])
result = findRelativeRanks([1,2,3,4,5])
# print(result)


# 703. Kth Largest Element in a Stream 
"""     
    2, 4, 5, 8 
    3 - 2, 3, 4, 5, 8 => 4
    5 - 2, 3, 4, 5, 5, 8 => 5
    10 - 2, 3, 4, 5, 5, 8, 10 => 5
    9 -  2, 3, 4, 5, 5, 8, 9, 10 => 8
    4 -  2, 3, 4, 4, 5, 5, 8, 8, 9, 10 => 8


    4, 5, 8, 2
"""

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.rank = k
        self.scores = nums

    def add(self, val: int) -> int:
        self.scores.append(val)
        self.scores.sort(reverse = True)
        return self.scores[self.rank-1]
        

kthobj = KthLargest(3, [4, 5, 8 ,2])
print(kthobj.add(3))
print(kthobj.add(5)) 
print(kthobj.add(10)) 
print(kthobj.add(9)) 
print(kthobj.add(4)) 