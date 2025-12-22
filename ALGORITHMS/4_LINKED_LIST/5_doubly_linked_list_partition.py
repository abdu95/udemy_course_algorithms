class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def print_list(self):
        output = []
        current_node = self.head
        while current_node is not None:
            output.append(str(current_node.value))
            current_node = current_node.next
        print(" <-> ".join(output))
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        self.length += 1
        return True

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

        
    def partition_list(self, x_val):
        if self.head is None:
            return self.head 
        less_head = Node(0)
        greater_head = Node(0)
        less_tail = less_head
        greater_tail = greater_head
        curr = self.head 
            
        while curr:
            if curr.value < x_val:
                less_tail.next = curr
                curr.prev = less_tail
                less_tail = curr 
            else:
                greater_tail.next = curr
                curr.prev = greater_tail 
                greater_tail = curr 
            curr = curr.next 
        
        less_tail.next = greater_head.next 
        if greater_head.next:
            greater_head.next.prev = less_tail 
        greater_tail.next = None 

        self.head = less_head.next 
        self.head.prev = None  


    def reverse_between(self, start_index, end_index):
        if self.length <= 1:
            return None 
        dummy_head = Node(0)
        dummy_head.next = self.head 
        prev = dummy_head 
        for i in range(start_index): 
            prev = prev.next 
        
        current = prev.next 
        
        for i in range(end_index - start_index):
            to_move = current.next 
            current.next = to_move.next 
            to_move.next = prev.next 
            prev.next = to_move 
        
        self.head = dummy_head.next 
        
        return self.head 
  
    
    

    
# -------------------------------
# Test Cases:
# -------------------------------

print("\nTest Case 1: Partition around 5")
dll1 = DoublyLinkedList(3)
dll1.append(8)
dll1.append(5)
dll1.append(10)
dll1.append(2)
dll1.append(1)
print("BEFORE: ", end="")
dll1.print_list()
dll1.partition_list(5)
print("AFTER:  ", end="")
dll1.print_list()

print("\nTest Case 2: All nodes less than x")
dll2 = DoublyLinkedList(1)
dll2.append(2)
dll2.append(3)
print("BEFORE: ", end="")
dll2.print_list()
dll2.partition_list(5)
print("AFTER:  ", end="")
dll2.print_list()

print("\nTest Case 3: All nodes greater than x")
dll3 = DoublyLinkedList(6)
dll3.append(7)
dll3.append(8)
print("BEFORE: ", end="")
dll3.print_list()
dll3.partition_list(5)
print("AFTER:  ", end="")
dll3.print_list()

print("\nTest Case 4: Empty list")
dll4 = DoublyLinkedList(1)
dll4.make_empty()
print("BEFORE: ", end="")
dll4.print_list()
dll4.partition_list(5)
print("AFTER:  ", end="")
dll4.print_list()

print("\nTest Case 5: Single node")
dll5 = DoublyLinkedList(1)
print("BEFORE: ", end="")
dll5.print_list()
dll5.partition_list(5)
print("AFTER:  ", end="")
dll5.print_list()

