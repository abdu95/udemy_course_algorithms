class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None 
        self.prev = None 

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node 
        self.length = 1 
    
    def print_list(self):
        temp = self.head 
        while temp:
            print(temp.value)
            temp = temp.next 
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node 
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail 
            self.tail = new_node 
        self.length += 1
        
        return True 


    def pop(self):
        if self.length == 0:
            return None 
        temp = self.tail
        if self.length == 1:
            self.head = None 
            self.tail = None 
        else: 
            self.tail = self.tail.prev 
            self.tail.next = None 
            temp.prev = None 
        self.length -= 1
        return temp 

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node 
            self.tail = new_node 
        
        self.head.prev = new_node 
        new_node.next = self.head 
        self.head = new_node 
        self.length += 1 
        return True 

## 44 Pop first 

# This is my initial solution: 

    # def pop_first(self):
    #     if self.head is None: 
    #         return None 
        
    #     temp = self.head
    #     if self.length == 1:
    #         self.head = None 
    #         self.tail = None 
    #         return temp 
            
        
    #     self.head = self.head.next    
    #     self.head.prev = None 
    #     temp.next = None

    #     self.length -= 1
    #     return temp 




    def pop_first(self):
        if self.length == 0: 
            return None 
        
        temp = self.head
        if self.length == 1:
            self.head = None 
            self.tail = None 
        else: 
            self.head = self.head.next    
            self.head.prev = None 
            temp.next = None
        self.length -= 1
        return temp 
    
    def get(self, index):
        if index < 0 or index >= self.length: 
            return None 
        temp = self.head 
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next 
        else: 
            temp = self.tail 
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev 
        
        return temp 
    

## 46 Set 

# my initial solution 

    # def set_value(self, index, value): 
    #     if index < 0 or index >= self.length: 
    #         return None 
    #     temp = self.head 
    #     for _ in range(index): 
    #         temp = temp.next 
    #     temp.value = value
    #     return True 

    def set_value(self, index, value): 
        temp = self.get(index) 
        if temp: 
            temp.value = value 
            return True 
        return False 





## 47 Insert 

# my initial version, works only for inserting at the beginning

    # def insert(self, index, value):
    #     if index < 0 or index>= self.length:
    #         return None
    #     new_node = Node(value)
    #     temp = self.get(index)

    #     if index == 0:             
    #         new_node.prev = temp.prev 
    #         temp.prev = new_node
    #         new_node.next = temp 
    #         self.head = new_node 
    #     if index == self.length:
    #         new_node.next = temp.next 
    #         temp.next = new_node
    #         new_node.prev = temp 
    #         self.tail = new_node
 



    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next 

        new_node.prev = before 
        new_node.next = after
        before.next = new_node 
        after.prev = new_node 

        self.length += 1
        return True 


    ## 48 Remove 

# solution 1: using temp and prev 

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


# solution 2: using before and after 
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


# solution 3: using only temp

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


    def reverse(self):
        if not self.head or not self.head.next: 
            return 
        current = self.head 
        temp = None 

        while current:
            temp = current.prev 
            current.prev = current.next 
            current.next = temp 
            current = current.prev 


        temp = self.head 
        self.head = self.tail 
        self.tail = temp  


    def partition_list(self, x_val):
        if self.head is None:
            return self.head 
        less_head = Node(0)
        greater_head = Node(0)
        less_tail = less_head
        greater_tail = greater_head
        curr = self.head 
            
        while curr:
            next_node = curr.next 
            curr.next = None 
            if curr.value < x_val:
                less_tail.next = curr
                less_tail = curr 
            else:
                greater_tail.next = curr
                greater_tail = curr 
            curr = next_node  
        
        greater_tail.next = None 
        
        if less_head.next:
            less_tail.next = greater_head.next 
            self.head = less_head.next 
        else:
            self.head = greater_head.next 
        
        return self.head


    def reverse_between(self, start_index, end_index):
        if self.length <= 1 or start_index == end_index:
            return  
        
        dummy_head = Node(0)
        dummy_head.next = self.head 
        self.head.prev = dummy_head 
        
        prev = dummy_head 
        for i in range(start_index): 
            prev = prev.next 
        
        current = prev.next 
        
        for i in range(end_index - start_index):
            to_move = current.next 
            
            current.next = to_move.next 
            if to_move.next:
                to_move.next.prev = current
            
            to_move.next = prev.next 
            prev.next.prev = to_move 
            prev.next = to_move 
            to_move.prev = prev 
        
        self.head = dummy_head.next 
        self.head.prev = None



    def swap_pairs(self):
        if self.length == 1:
            return self.head 
        dummy = Node(0)
        dummy.next = self.head 
        prev = dummy
        
        while self.head and self.head.next:
            current = self.head
            after = current.next 
            # swap 
            prev.next = after 
            current.next = after.next 
            after.next = current 
            
            after.prev = prev 
            current.prev = after
            if current.next: 
                current.next.prev = current 
            self.head = current.next 
            prev = current

        self.head = dummy.next 
        if self.head: 
            self.head.prev = None 

        


# Test Cases
print("\nTest 1: Middle segment reversal")
dll1 = DoublyLinkedList(3)
for v in [8, 5, 10, 2, 1]:
    dll1.append(v)
print("BEFORE: ", end="")
dll1.print_list()
dll1.reverse_between(1, 4)
print("AFTER:  ", end="")
dll1.print_list()

print("\nTest 2: Full list reversal")
dll2 = DoublyLinkedList(1)
for v in [2, 3, 4, 5]:
    dll2.append(v)
print("BEFORE: ", end="")
dll2.print_list()
dll2.reverse_between(0, 4)
print("AFTER:  ", end="")
dll2.print_list()

print("\nTest 3: No-op on single node")
dll3 = DoublyLinkedList(9)
print("BEFORE: ", end="")
dll3.print_list()
dll3.reverse_between(0, 0)
print("AFTER:  ", end="")
dll3.print_list()

print("\nTest 4: Reversal with head involved")
dll4 = DoublyLinkedList(7)
for v in [8, 9]:
    dll4.append(v)
print("BEFORE: ", end="")
dll4.print_list()
dll4.reverse_between(0, 2)
print("AFTER:  ", end="")
dll4.print_list()
