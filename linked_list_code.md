# Section 5
## Exercise 3

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
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)
```

# Section 4
## 22

Append:
New Node's next attribute = None
- last item point to new Node
- tail points to the new Node
edge:
- if no item in the LL (length = 0), head & tail points to the New Node


```python
def append(self, value):
    new_node = Node(value)
    new_node.next = None
    # if self.length = 0:
    if self.head is None:
        self.head = new_node
        self.tail = new_node
    else: 
        self.tail.next = new_node
        self.tail = new_node
    # forgot this
    self.length += 1
    return True
    
```

```python 
def pop(self):
    # find node that is pointing to last node
    # then make tail point to that node

    if self.head is None:
        return None
    elif self.head = self.tail:
        return self.head
    else:
        pop_elem = self.tail
        temp = self.head
        while temp is None:
            if temp.next == self.tail:
                self.tail = temp
    
    return pop_elem
```