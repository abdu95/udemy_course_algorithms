
partition: 86, 725 

## 51 Partition list 

similar to single linked 
    prev pointers should also be attached with next pointers  

Edge case:
    before combining less part and greater part, greater part can be empty 

for single linked list 
```python 
    def partition_list(self, x_val):
        if self.head is None:
            return self.head 
        less_head = Node(0)
        greater_head = Node(0)
        less_tail = less_head
        greater_tail = greater_head
        curr = self.head 
            
        while curr: 
            nxt = curr.next 
            curr.next = None 
            if curr.value < x_val:
                less_tail.next = curr
                less_tail = curr 
            else:
                greater_tail.next = curr
                greater_tail = curr 
            curr = nxt   
        
        greater_tail.next = None 
        
        if less_head.next:
            less_tail.next = greater_head.next 
            self.head = less_head.next 
        else:
            self.head = greater_head.next 
        
        return self.head
```

for doubly linked list 
```python 

    def partition_list(self, x_val):
        if self.head is None:
            return self.head 
        less_head = Node(0)
        greater_head = Node(0)
        less_tail = less_head
        greater_tail = greater_head
        curr = self.head 
            
        while curr:
            nxt = curr.next 
            curr.next = None 
            curr.prev = None 
            if curr.value < x_val:
                less_tail.next = curr
                # connect previous 
                curr.prev = less_tail
                less_tail = curr 
            else:
                greater_tail.next = curr
                # connect previous 
                curr.prev = greater_tail 
                greater_tail = curr 
            curr = nxt  
        

        # merge
        if less_head.next and greater_head.next:
            less_tail.next = greater_head.next
            greater_head.next.prev = less_tail
            self.head = less_head.next
            self.head.prev = None     # new head must have prev=None
            # ensure final tail terminates
            greater_tail.next = None
        elif less_head.next:  # only less part exists
            self.head = less_head.next
            self.head.prev = None
            less_tail.next = None
        else:  # only greater part exists
            self.head = greater_head.next
            if self.head:
                self.head.prev = None
                greater_tail.next = None

        return self.head

    
```

## 34 Reverse Between for Doubly Linked List 