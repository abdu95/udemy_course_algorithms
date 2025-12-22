# LEETCODE PROBLEMS 

# Template:
    # TOPIC
    # DATE
    # LEETCODE PROBLEM ID
    # STATUS: SOLVED


# LINKED LISTS
 
# 28 Nov 2025 


# ID-876. Middle of the Linked List
# Status: Solved 

# tail is not given. Instead of tail, in while loop I used this condition: 
#   and fast.next:

def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    fast = head
    slow = head 
    while fast is not None and fast.next:
        fast = fast.next.next
        slow = slow.next 
    return slow

# ID-141 Linked List Cycle 
# Status: Solved 
# 

class Solution(object):
    def hasCycle(self, head):
        slow = head
        fast = head 
        if head is None:
            return False
        while fast and fast.next:
                 
            slow = slow.next 
            fast = fast.next.next
            if slow is fast:
                return True  
               
        return False 
        


        
# ID-19. Remove Nth Node From End of List

class Solution(object):
    def removeNthFromEnd(self, head, n):
        slow = fast = head 
        if head.next is None:
            return None

        for _ in range(n):
            if fast is None:
                head = None 
            fast = fast.next 
        
        pre = None
        while fast:
            pre = slow
            slow = slow.next 
            fast = fast.next 
        if pre:
            pre.next = slow.next 
            slow.next = None 
        else:
            head = head.next
         
        return head 

# ID-206. Reverse Linked List
# Status: SOLVED 

# Since tail is not given, I used temp var only (chatGPT helped)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head 
        before = None 
        while temp:
            after = temp.next 
            temp.next = before 
            before = temp 
            temp = after 
        return before 
        






# 83. Remove Duplicates from Sorted List
    def deleteDuplicates(self, head):
        current = head 
        while current: 
            runner = current
            while runner.next: 
                if runner.next.val == current.val: 
                    runner.next = runner.next.next
                else:
                    runner = runner.next 
            current = current.next 
        return head 
    


# 1290. Convert Binary Number in a Linked List to Integer
class Solution(object):
    def getDecimalValue(self, head):
        result = 0
        current = head
        while current:
            result = result*2 + current.val                
            current = current.next 
        return result
    

# 86. Partition List 

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        less_head = ListNode(0)
        greater_head = ListNode(0)
        less_tail = less_head
        greater_tail = greater_head 

        curr = head 
        while curr: 
            next_node = curr.next 
            curr.next = None  
            if curr.val < x: 
                less_tail.next = curr
                less_tail = curr
            else:
                greater_tail.next = curr 
                greater_tail = curr
            
            curr = next_node
        
        # if less_head is not empty
        if less_head.next:
            less_tail.next = greater_head.next
            head = less_head.next  
        else: 
            head = greater_head.next 

        return head
        