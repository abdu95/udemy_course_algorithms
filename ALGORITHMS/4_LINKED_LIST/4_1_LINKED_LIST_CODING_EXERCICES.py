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
    

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    
    def pop(self):
        if self.head is None:
            return None
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node 
        else:
            new_node.next = self.head 
            self.head = new_node 
        
        self.length += 1 
        return True
    
    def pop_first(self):
        # return first item - item to which head is pointing to 
        # now head should point to item to which removed item was pointing to
        
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
        if index >= self.length or index < 0:
            return None 
        i = 0
        result = self.head
        while i < index:
            result = result.next
            i += 1

        return result 
    
    def set_value(self, index, value):
        result = self.get(index)
        if result:
            result.value = value
            return True

        return False 
    
    # def insert(self, index, value):
        # if index >= self.length or index < 0:
        #     return False
        # if index == [0]:
        #     return self.prepend(value)
        # if index == self.length:
        #     return self.append(value)
        # new_node = Node(value)
        # pre = self.head
        # temp = self.head 
        # # insert a node at given index
        # while temp.next:
        #     pre = temp 
        #     temp = temp.next 
        # pre.next = new_node
        # new_node.next = temp 
        # self.length += 1
        
        # return True
        
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index -1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        
        return True


    # def remove(self, index):
    #     node_to_remove = self.get(index)
    #     if index == 0:
    #         self.head = self.get(1)
    #     temp_pre = self.get(index -1)
    #     if temp_pre and node_to_remove:
    #         temp_pre.next = node_to_remove.next
    #         node_to_remove.next = None
    #         self.length -= 1
    #     return node_to_remove

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None 
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
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


   