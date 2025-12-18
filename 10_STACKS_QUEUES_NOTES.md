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

    

    
## 12.42 Stack using List 

my solution: 

```python 
class Stack:
    def __init__(self):
        self.stack_list = []
        self.height = 1 
```

## 12.43 Push 

my solution: 
```python
    def push(self, value):
       self.stack_list.append(value) 
```

## 12.44 Pop

my solution: 

```python 
    def pop(self):
        if self.peek() is not None:
            temp = self.peek() 
            del self.stack_list[-1]
            return temp
        
        return self.peek()
```

author's solution
```python 
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()
```

## 12.45 Reverse a string 

    push the letters of word to a stack 
    pop each letter (from the beginning)

my solution:

```python 

def reverse_string(str_val):
    str_stack = Stack()
    for letter in str_val:
        str_stack.push(letter)
    
    result_str = ""
    while not str_stack.is_empty():
        temp = str_stack.pop()
        result_str += temp 
    
    return result_str
    
```

## 12.61
    Balanced parantheses:
        open a paranthese and have a corresponding closing paranthese
    Balanced: "()" "(())" "()()"
    Not balanced: ")("

    Iterate through the input string
        - If we encounter opening paranthese, we push it to the stack 
            
        if stack is empty before reach to the end, paranthese are not balanced
        - If we encounter closing paranthese, we pop from a stack (opening paranthese)
    After the loop, is stack is empty? It means string had balanced parantheses

my solution: 

```python 
def is_balanced_parentheses(str_pars):
    par_stack = Stack()
    for char in str_pars:
        if char == '(':
            par_stack.push(char)
        elif char == ')':
            if par_stack.is_empty():
                return False
            par_stack.pop()
    
    return par_stack.is_empty()
```

## 12. 62 Sort Stack
    Sort the given stack of numbers 

    3   1
    1   2
    4   3
    2   4

    Create second stack 
    Create temp var = pop first item from a given stack
    peek var: points to top item in second stack 

    If the second stack is empty or peek number > temp, push to second stack 
        if temp > peek, push temp to second stack 
        if temp < peek, push peek to first stack
    
    if temp is empty, push items from second stack to first stack 

    