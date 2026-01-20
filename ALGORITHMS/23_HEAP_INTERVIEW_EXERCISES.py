# Coding Exercise 77: Heap Kth Smallest Element in an Array 

class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if (left_index < len(self.heap) and 
                    self.heap[left_index] > self.heap[max_index]):
                max_index = left_index

            if (right_index < len(self.heap) and 
                    self.heap[right_index] > self.heap[max_index]):
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
                       
    def remove(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return max_value


def find_kth_smallest(nums, k):
    max_heap = MaxHeap()
    # insert each number from nums into MaxHeap 
    for num in nums:
        max_heap.insert(num) 
    # smallest number - last node in MaxHeap
    # kth smallest number - kth element from the end of MaxHeap 
    for i in range(len(nums) - k+1):
        number = max_heap.remove()
    return number 


def stream_max(nums):
    max_heap = MaxHeap()
    result = [0] * len(nums)
    max_result = 0
    for i in range(len(nums)):
        max_heap.insert(nums[i])
        current_result = max_heap.remove() 
        if max_result == 0 or max_result < current_result:
            max_result = current_result
        result[i] = max_result
    return result  


print(stream_max([ 1,3,2,5,4]))


# Test cases
# nums = [[3,2,1,5,6,4], [6,5,4,3,2,1], [1,2,3,4,5,6], [3,2,3,1,2,4,5,5,6]]
ks = [2, 3, 4, 7]
expected_outputs = [2, 3, 4, 5]

