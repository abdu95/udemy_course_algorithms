17 Dec 2025 - started Stacks 

# Section 10 Stacks & Queue

## 10.52 Intro
    Stacks - LIFO: Last In First Out
    adding item = pushing item on top of existing one 
    last item on top 
    we can get only the last item that was pushed
    Example: 
        browser tabs 
        back button - pop tab off of a stack 

    Implement stack using list 
        add & remove from same side (top) 
        add & remove from the end (top) = O(1)
        add & remove from the beginning = O(N)

        3 7
        2 23
        1 3
        0 11
    
    Implement stack using LinkedList 
        None - terminated end - should not be in top, it should be in bottom
        pop first - remove first item  
        push - prepend
        head = top (no tail because we add & remove only from top)

## 10.53 Stack Constructor

```python
class Node():
    def __init__(self, value):
        self.value = value 
        self.next = None 

class Stack():
    def __init__(self, value):
        new_node = Node(value)
        self.top = None 
        self.height = 1

```


## 10.54 Push 
    similar to LinkedList prepend 
    edge case: add to empty stack 

    new_node points to top 
    top points to new_node

```python 
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node 
        else:
            new_node.next = self.top 
            self.top = new_node 
        self.height += 1 
```

## 10.55 Pop 
    Pop - remove top node 
    edge case: pop from empty stack 


```python 
    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None 
        self.height -= 1
        return temp  

```

## 10.56 Queue

    Queue - FIFO: First In First Out 
    Enque - add items to queue
    Deque - remove items from queue

    Implementing queue using list:
        Removing and adding to end = O(1)
        Removing and adding from beginning = O(N)

    Implementing queue using Linked List: 
        Removing from end = O(N), adding to end = O(1)
        Removing from beginning = O(1) and adding to beginning = O(1)

        Since removing from end = O(N), dont deque from end 
        FIFO: Enque to end, Deque from beginning 
            adding to end = O(1), removing from beginning = O(1)
        head = first, tail = last 

## 10.57 Constructor 

```python 
class Node():
    def __init__(self, value):
        self.value = value 
        self.next = None 

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
    
    def print_queue(self):
        temp = self.first 
        while temp is not None:
            print(temp.value)
            temp = temp.next 
```

## 10.58 Enqueu 
    Enqueu 
        add item to end of the queue - append
        edge case: add to empty queue - first and last points to new_node 

```python
    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node 
            self.last = new_node
        
        self.length += 1
```

## 10.59 Dequeue
    Dequeue 
        remove item from the beginning, return it
        edge cases: if one item in the queue, or none

```python 

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None 
            self.last = None 
        else:
            self.first = self.first.next
            temp.next = None 
        
        self.length -= 1
        return temp  
```

    

    



