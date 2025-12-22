class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value = None):
        if value is None: 
            self.head = None 
            self.tail = None 
            self.length = 0 
        else: 
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1


    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1 
        
    
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
    
    def prepend(self, value):
        new_node = Node(value)

        new_node.next = self.head
        self.length += 1
        if self.length == 1:
            self.tail = new_node
        self.head = new_node
        return True 

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None 
        self.length -= 1
        if self.length == 0:
            self.tail = None 
        return temp  
    

    def get(self, index):
        if index < 0 or index > self.length:
            return None
        temp = self.head
        i = 0
        while i < index:
            temp = temp.next 
            i+=1  
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value 
            return True
        return False 

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

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None 
        if index == 0: 
            return self.pop_first()
        if index == self.length:
            return self.pop()
        
        pre = self.get(index - 1)
        temp = pre.next 
        pre.next = temp.next 
        temp.next = None 
        self.length -= 1
        return temp 

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

## 32 
    def find_middle_node(self):
        fast = self.head
        slow = self.head 
        while fast is not None and fast is not self.tail : 
            fast = fast.next.next 
            slow = slow.next
        return slow 
    
## 33
    def has_loop(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
            if slow is fast: 
                return True
            
        return False


# 35
    def remove_duplicates(self):
        current = self.head 
        while current:
            runner = current 

            # whenever code reaches runner.next = None, it exits the loop
            # and new iteration for current starts 
            while runner.next:
                if runner.next.value == current.value: 
                    runner.next = runner.next.next
                    self.length -= 1 
                else: 
                    runner = runner.next 
            current = current.next 

# 36
    def binary_to_decimal(self):
        result = 0
        current = self.head
        while current:
            result = result*2 + current.value                
            current = current.next 
        return result

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.length = 0

#  4.37 Partition list 

    """
        A linked list and x value is given
        partition list into two 
        nodes with value < x goes to left list 
        nodes with value >= x goes to right list 
        connect two lists 
        (maintain initial order of nodes)

        3 - 8 - 5 - 10 - 2 - 1 
        => 
        3 - 2 - 1 - 8 - 5 - 10

    LOGIC: 
        add dummy nodes dummy1 =0, dummy2 = 0
        prev1 & prev2 points to dummy nodes
        loop through linked list
            if node's value is < x, add node to prev1 Linked List
                point prev1 to new node  
            if node's value is >= x, add to prev2 Linked List 
                point prev2 to new node 
        
        connect lists: prev1.next connects to node dummy2 is pointing to 
        head should point to first node - node that dummy1 is pointing to
    """


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

    """
    TASK: 
        start_index and end_index range is given
        swap the position of nodes in this range: 
        1st with 3rd, 2nd with 4th, ...

    prev => current => to_move 
    
    - if LL has one node, return None 
    - create dummy_node
    - dummy node points to head 
    => create prev, it points to dummy node 
    - iterate prev start_index many times 
    => now create current, it points to prev.next 
    - iterate x many times: end_index - start_index 
        => create to_move, it points to current.next 
        - set current's next to to_move's next 
        - set to_move's next to prev's next 
        prev's next points to to_move
    - head points to dummy's next 
    - return head 
    """

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
    
## 39  Swap pairs 

    # create dummy node
    # prev = points to dummy node
    # current = prev.next 
    # after = current.next  
    # swap current & after 

    # prev = current 

    def swap_pairs(self):
        if self.length == 1:
            return self.head 
        dummy = Node(0)
        dummy.next = self.head 
        prev = dummy
        
        
        while prev.next and prev.next.next:
            current = prev.next 
            after = current.next 
            # swap 
            prev.next = after 
            current.next = after.next 
            after.next = current 
            prev = current 

        self.head = dummy.next 
        


# 34. LL: Find Kth Node from End
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



# Function to convert linked list to Python list
def linkedlist_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result

# Function to test partition_list
def test_partition_list():
    test_cases_passed = 0
    
    print("-----------------------")
    
    # Test 1: Normal Case
    print("Test 1: Normal Case")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(3)
    ll.append(1)
    ll.append(4)
    ll.append(2)
    ll.append(5)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 2, 3, 4, 5]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 2: All Equal Values
    print("Test 2: All Equal Values")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(3)
    ll.append(3)
    ll.append(3)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [3, 3, 3]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 3: Single Element
    print("Test 3: Single Element")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(1)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 4: Already Sorted
    print("Test 4: Already Sorted")
    x = 2
    print(f"x = {x}")
    ll = LinkedList(1)
    ll.append(2)
    ll.append(3)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 2, 3]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 5: Reverse Sorted
    print("Test 5: Reverse Sorted")
    x = 2
    print(f"x = {x}")
    ll = LinkedList(3)
    ll.append(2)
    ll.append(1)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 3, 2]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 6: All Smaller Values
    print("Test 6: All Smaller Values")
    x = 2
    print(f"x = {x}")
    ll = LinkedList(1)
    ll.append(1)
    ll.append(1)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [1, 1, 1]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Test 7: Single Element, Equal to Partition
    print("Test 7: Single Element, Equal to Partition")
    x = 3
    print(f"x = {x}")
    ll = LinkedList(3)
    print("Before:", linkedlist_to_list(ll.head))
    ll.partition_list(x)
    print("After:", linkedlist_to_list(ll.head))
    if linkedlist_to_list(ll.head) == [3]:
        print("PASS")
        test_cases_passed += 1
    else:
        print("FAIL")
        
    print("-----------------------")
    
    # Summary
    print(f"{test_cases_passed} out of 7 tests passed.")


# Run the test function
test_partition_list()
      