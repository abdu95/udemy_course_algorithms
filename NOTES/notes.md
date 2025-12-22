
## 37 Partition list 

x = 5
    3 - 8 - 5 - 10 - 2 - 1 
    3 - 2 - 1 - 8 - 5 - 10

Nodes < 5: left side, Nodes >= 5: right side 
Keep initial order 

create dummy nodes with value 0: less_head & greater_head 
create variables to point to these nodes: less_tail, greater_tail

iterate through list
    if current node value < x, add current as next node to less_tail 
        move less_tail to current
    else, add current as next node to greater_tail
        move greater_tail to current  

connect less & greater
    less_tail.next = greater_head.next 
head should point to less_head (or greater_head)

## 6.39 Swap pairs 

    create dummy node
    prev = points to dummy node
    current = prev.next 
    after = current.next  
    swap current & after 

    prev = current 





section   | coding | interview ex  
S&Q       | 8      | 4
Trees     | 7      | 1
HasTables | 8 | 11
Graph | 8 | 
Heaps | 7 | 2
Recursion | 3+7 | 2
BST | 9 | 2
Basic sorts | 8 | 3
Merge sort | 6 | 1
Quick sort | 5 | 
Dynamic programming | 5 | 7


## 44 Pop first 

This is my initial solution: 

```python 
    def pop_first(self):
        if self.head is None: 
            return None 
        
        temp = self.head
        if self.length == 1:
            self.head = None 
            self.tail = None 
            return temp 
            
        
        self.head = self.head.next    
        self.head.prev = None 
        temp.next = None

        self.length -= 1
        return temp 

```


## 46 Set 

my initial solution 

```python 
    def set_value(self, index, value): 
        if index < 0 or index >= self.length: 
            return None 
        temp = self.head 
        for _ in range(index): 
            temp = temp.next 
        temp.value = value
        return True 
```

## 47 Insert 

my initial version, works only for inserting at the beginning
```
    def insert(self, index, value):
        if index < 0 or index>= self.length:
            return None
        new_node = Node(value)
        temp = self.get(index)

        if index == 0:             
            new_node.prev = temp.prev 
            temp.prev = new_node
            new_node.next = temp 
            self.head = new_node 
        if index == self.length:
            new_node.next = temp.next 
            temp.next = new_node
            new_node.prev = temp 
            self.tail = new_node
 
```

## 48 Remove 

solution 1: using temp and prev 

```python
    def remove(self, index):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop()
        
        prev = self.get(index - 1)
        temp = prev.next 

        prev.next = temp.next 
        temp.prev = None 
        temp.next = None 
        
        self.length -= 1
        return temp

```

solution 2: using before and after 
```python 
    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        
        temp = self.get(index)
        before = temp.prev
        after = temp.next  
        before.next = after 
        after.prev = before

        temp.prev = None 
        temp.next = None 

        self.length -= 1
        return temp

```

solution 3: using only temp
```
    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        
        temp = self.get(index)
        temp.next.prev = temp.prev 
        temp.prev.next = temp.next 
        temp.prev = None 
        temp.next = None 

        self.length -= 1
        return temp

```

## 49 Palindrome checker 

my solution 
no need for is_palindrome, redundant code for odd and even 

```python 
    def is_palindrome(self):
        is_palindrome = False
        if self.length == 0 or self.length == 1:
            return True
    
        forward = self.head 
        backward = self.tail 
        
        if self.length % 2 == 0: 
            while forward.next == backward and backward.prev == forward: 
                if forward.value == backward.value:
                    is_palindrome = True 
                forward = forward.next 
                backward = backward.prev  
        else: 
            while forward.next != backward.prev: 
                if forward.value == backward.value:
                    is_palindrome = True 
                forward = forward.next 
                backward = backward.prev  
        
        return is_palindrome

```


simpler code: 

```python 
    def is_palindrome(self):
        if self.length <= 1:
            return True
            
        forward = self.head 
        backward = self.tail 
        for i in range(self.length // 2):
            if forward.value != backward.value:
                return False
            forward = forward.next 
            backward = backward.prev  
        return True

        
```



    