
# Section 4: Linked Lists

## 4.16 LL intro

    LL has head & tail 
    Each node points to the next one
    Last node points to None

## 4.17 Big of LL

Time complexity for each LL operations

    Append - add node to the end = O(1)
        make last item point to new item
        make tail point to new item 
    Pop - remove node from the end = O(N)
        tail should point to element one before the last item
        start iterating from head, through LL until we find that element
    Prepend - add node to the beginning = O(1)
        make next property of new node point to the node that head is pointing to
        make head point to the new node 
    Pop first - remove node from the beginning = O(1)
        make head point to the next node after the first node (head = head.next)
        remove first node 
    Insert - add node to the middle - X node = O(N) 
        iterate through LL to find X node
        new node should point to next node of the X node
        X node should point to new node 
    Remove - remove node from the middle = O(N)

    Lookup by value = O(N)
    Lookup by index = O(N)


List 
    removing from or adding to the end = O(1)
LL  
    removing from or adding to the beginning = O(1) 


## 4.18 Under the hood 

NODE has value & pointer (.next)

Node = Dict
    7 -> 4

```python
    head = {"value": 7, 
    "next": {
         "value": 4   
         "next": None
        }}
```

## 4.19 Constructor

    all 4 methods create new node.    so we create class Node for this 

```python 
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node 
        self.length = 1



my_linked_list = LinkedList(4)

print('Head:', my_linked_list.head.value)
```

## 4. 21 Print 

    temp is not None = until we reach the end of the LL 

```python
def print_list(self):
    temp = self.head
    while temp is not None:
        print(temp.value)
        temp = temp.next 
``` 

## 4.22 LL: Append

    New Node's next attribute = None
        make last item of LL point to new Node
        make tail point to the new Node
    edge case:
        if no item in the LL (length = 0), head & tail points to the New Node

```python
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # point last node to new node 
            self.tail.next = new_node
            # move tail to point to new node 
            self.tail = new_node
        self.length += 1 
```

## 4.23 Pop 

    Edge cases: 
        no nodes in LL
        one node in LL

    Pop - remove node from the end = O(N)
        start iterating from head, through LL until we find a node before last node
        point tail to that node

    
    pre & temp 
        they point to head
        iterate until temp.next is not None
        when temp.next is None - end reached, set tail = pre 
        self.tail.next = None
        return temp (popped node)

```python
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head 
        pre = self.head

        #   start iterating from head, through LL until we find a node before last node
        while temp.next is not None:
            pre = temp  
            temp = temp.next

        # point tail to that node
        self.tail = pre
        self.tail.next = None 
        self.length -= 1 
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

```

~Two-pointer technique
~Fast and Slow Pointer approach
~Floyd’s Cycle Detection Algorithm 





## 4. 25: Prepend
add item to the beginning of the list 

- create new node with a given value
- new node points to what head is pointing to 
- head now points to new node 

if empty list: 
- both head & tail points to new node


```python
    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.length += 1
        if self.length == 1:
            self.tail = new_node
        self.head = new_node
        
```

## 4.26 Pop first 

    - point head to a node that first node is pointing to
    - first node points to None

Edge cases
    one item in the LL
    no items in the LL

my attempt. It passed for empty LL and LL with single node 
```python 
    def pop_first(self):
        if self.length == 0:
            self.head = None 
            self.tail = None 
            return None
        elif self.length == 1:
            temp = self.head
            self.head = None 
            self.tail = None 
            self.length -= 1
            return temp 
        else: 
            temp = self.head
            self.head = self.head.next
            self.length -= 1
            return temp  
```


## 4.27 Get (lookup by index)

Solved without looking at hints Yaaayy!!

```python 
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        i = 0
        while i < index:
            temp = temp.next 
            i+=1  
        return temp
```


## 4.28 Set 

- go to index and change value

Solved without looking at hints Yaaayy!!

```python
    def set_value(self, index, value):
        if index < 0 or index > self.length or self.length == 0:
            return None
        temp = self.head 
        i = 0
        while i < index:
            temp = temp.next 
            i+=1 
        temp.value = value 
        return True

```

## 4.29 Insert 

- new_node should point to the node at the given index 


I thought well the part about getting node previous to the node at the given index 

```python 
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False 
        if index == 0: 
            return self.prepend(value) 
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next  
        temp.next = new_node 
        self.length += 1 
        return True
```

## 4.30 Remove 

- remove item at the given index

Solved without looking at hints Yaaayy!!

```python
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None 
        if index == 0: 
            return self.pop_first()
        if index == self.length:
            return self.pop()
        
        
        node_previous = self.get(index-1)
        temp = node_previous.next
        node_previous.next = node_previous.next.next 
        temp.next = None 
        self.length -= 1 
        return temp 
        
```

## 4.31
    REVERSE 
    all reverse does is it switches node pointers from right to the left - from next to previous 


        3 steps to switch head & tail: 
            temp var to hold a head 
            head = tail 
            tail = temp 
        2 vars as a pointer
            after points to temp.next 
            before = None
        4 steps loop but only one step does REVERSE: 7
            6 switch after pointer to the next node
            7 switch temp pointer to prev node 
            8 move before forward (before = temp)
            9 move temp forward (temp = after)  


```python
    def reverse(self):
        temp = self.head
        self.head = self.tail 
        self.tail = temp 
        after = temp.next 
        before = None
        for _ in range(self.length):
            after = temp.next 
            temp.next = before
            before = temp 
            temp = after 

```

## 4.32 Find middle nodes 

    Task: find the middle node
    3 constraints:
        no LL length is given 
        no counter variable allowed
        iterate through LL only once  

    Slow and Fast pointers
        in each iteration, fast moves 2 nodes, slow moves 1 node 
     
    end condition for LL with odd numbers is when fast points to tail 
    end condition for LL with even numbers is when fast points to None, its when slow points to first node in the second half of LL 

Solved without looking at hints Yaaayy!!

```python
    def find_middle_node(self):
        fast = self.head
        slow = self.head 
        while fast is not None and fast is not self.tail : 
            fast = fast.next.next 
            slow = slow.next
        return slow 
```

<!-- 21 June 2025 -->
- Big O graph for all cases


## 4.33 Has loop
Floyd's cycle-finding algorithm

```python
    def has_loop(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
            if slow is fast: 
                return True
            
        return False
```

## 4.34 kth node from end 

This was my initial solution but its not allowed to use length
 
```python
def find_kth_from_end(ll, k):       
    temp = ll.head
    i = 1 
    while i <= ll.length - k: 
        temp = temp.next 
        i += 1 
    return  temp 
```

Hint:
    for - We'll advance the fast pointer first to create a gap of k nodes between slow and fast.
    while - At this stage, we continue moving both pointers at the same speed. By the time the fast pointer reaches the end of the list, the slow pointer will have advanced by the length of the list minus k nodes. This positions the slow pointer at the kth node from the end.

```python
def find_kth_from_end(ll, k):       
    slow = ll.head
    fast = ll.head 
    # We'll advance the fast pointer first to create a gap of k nodes between slow and fast
    for i in range(k):
        if fast is None:
            return None 
        fast = fast.next 
    # 
    while fast:
        slow = slow.next 
        fast = fast.next 
    return slow

```


<!-- 15 August 2025 -->
## 35 Remove duplicates
    loop - current: iterates until it reaches the end of LL - length of LL
        nested loop - runner: for each iteration of current, it iterates starting from current until LL end
    initially they are both pointing to LinkedList head
        current = self.head
        runner = self.head
    runner var checks if next node is equal to current node
        if runner.next != current:
            runner = runner.next 
        else:
            temp = runner.next.next  
            runner.next = None
            runner.next = temp 
            self.length -= 1

        if equals, we get next pointer of next node, we make the node that runner is now pointing to so that it points to next of the next. the next of runner points to None. runner continues iterating until it reaches the end of LL  or finds another duplicate
    now current points to next node.     runner points to next node of current.  
    runner starts iterating again 

LOGIC using nested loops - O(N^2):
    current & runner nodes
    runner checks if next node is equal to current node
    if equals, sets node pointer to next.next node 

LOGIC using set - O(N)





4 December 

## 4.36 Binary to decimal

I figured out almost all code using video except this part:
    result = result*2 + current.value                


```python
    def binary_to_decimal(self):
        result = 0
        current = self.head
        while current:
            result = result*2 + current.value                
            current = current.next 
        return result
```

## 38 Reverse between 

    prev => current => to_move 

    *dummy node - points to beginning  
    *prev node - points to dummy node 

    Loop until prev reaches the start_index 
    *current - points to prev.next 
    Loop K times: until we iterate through items that need to be reversed 
        K = end_index - start_index 
        *to_move = current.next 
        current.next points to to_move.next 
        to_move.next points to prev.next  
        prev.next points to to_move 

    point head to a node dummy node is pointing to  
    
    


## 39 Swap pairs 

This is my initial code. It passed tests for single and empty 

```
  def swap_pairs(self):
        if self.length == 1:
            return self.head 
        dummy = Node(0)
        dummy.next = self.head 
        
        prev = dummy
        
        while prev.next and prev.next.next:
            current = prev.next 
            prev = prev.next 

            after = current.next 
            current.next = after.next 
            
        
        self.head = dummy.next 
        
```