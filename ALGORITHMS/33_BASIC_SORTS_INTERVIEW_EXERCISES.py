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

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1



    def bubble_sort(self):
        if self.head is None and self.tail is None:
            return  
        
        sorted_until = None 

        while sorted_until != self.head.next:
            current_node = self.head
            while current_node.next != sorted_until:
                next_node = current_node.next 
                if current_node.value > next_node.value:
                    current_node.value, next_node.value = next_node.value, current_node.value 
                
                current_node = current_node.next 
                
            sorted_until = current_node


    def selection_sort(self):
        if self.head is None:
            return  
        
        current_node = self.head

        while current_node is not None:
            temp = current_node.next 
            smallest = current_node 


            while temp is not None:

                if temp.value < smallest.value:
                    smallest = temp 
                temp = temp.next 
                    
            current_node.value, smallest.value = smallest.value, current_node.value
            current_node = current_node.next 


    def insertion_sort(self):
        if self.head is None or self.tail is None:
            return
        
        sorted_head = self.head 
        unsorted_head = self.head.next 
        sorted_head.next = None 

        while unsorted_head is not None:
            current = unsorted_head
            unsorted_head = unsorted_head.next
            
            if current.value < sorted_head.value:
                current.next = sorted_head
                sorted_head = current
            else:
                search_pointer = sorted_head
            
                # inner loop within unsorted part:
                while search_pointer.next is not None and current.value > search_pointer.next.value:
                    search_pointer = search_pointer.next 
                
                current.next = search_pointer.next 
                search_pointer.next = current 
                
        self.head = sorted_head
        temp = self.head
        while temp.next is not None:
            temp = temp.next 
        self.tail = temp 


"""
Method Description:

If the length of the linked list is less than 2, the method returns and the list is assumed to be already sorted.

The first element of the linked list is treated as the sorted part of the list, and the second element is treated as the unsorted part of the list.

The first element of the sorted part of the list is then disconnected from the rest of the list, creating a new linked list with only one element.

The method then iterates through each remaining node in the unsorted part of the list.

For each node in the unsorted part of the list, the method determines its correct position in the sorted part of the list by comparing its value with the values of the other nodes in the sorted part of the list.

Once the correct position has been found, the node is inserted into the sorted part of the list at the appropriate position.

After all the nodes in the unsorted part of the list have been inserted into the sorted part of the list, the head and tail pointers of the linked list are updated to reflect the new order of the nodes in the list.
"""


""" 
Here's how it works:



First, the function checks if the length of the linked list is less than 2. If it is, then the list is already sorted, and the function returns.

Next, the function sets the sorted_list_head pointer to the head of the linked list, and the unsorted_list_head pointer to the next node after the head.

The sorted_list_head pointer is then disconnected from the rest of the list by setting its next attribute to None.

The function enters a loop where it iterates through each remaining node in the unsorted part of the list. For each node:

    The node is temporarily saved in the current variable, and the unsorted_list_head pointer is moved to the next node.

    If the current node is smaller than the first node in the sorted part of the list (i.e., the sorted_list_head node), then the current node becomes the new sorted_list_head node.

    Otherwise, the function searches through the sorted part of the list to find the correct position to insert the current node. The search is done using the search_pointer variable, which initially points to the sorted_list_head node. The search_pointer variable is moved along the sorted part of the list until it reaches the last node that is smaller than the current node, or until it reaches the end of the sorted part of the list. Once the correct position is found, the current node is inserted into the sorted part of the list.

Finally, the head and tail attributes of the linked list are updated to reflect the new order of the nodes in the list. This is done by setting the head attribute to the new sorted_list_head node, and by iterating through the list to find the new tail node.

"""        


my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.bubble_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    Linked List Before Sort:
    4
    2
    6
    5
    1
    3

    Sorted Linked List:
    1
    2
    3
    4
    5
    6

"""

