def merge(list1, list2):
    combined = []
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j+=1 

    while i < len(list1):
        combined.append(list1[i])
        i += 1

    while j < len(list2):
        combined.append(list2[j])
        j += 1

    return combined



def merge_sort(my_list):
    # base case 
    if len(my_list) == 1:
        return my_list
    # mid point to split in half
    mid_index = int(len(my_list)/2)
    # recursion
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])

    return merge(left, right)


"""
Merge Two Sorted LL ( ** Interview Question)

The merge method takes in another LinkedList as an input and merges it with the current LinkedList.
The elements in both lists are assumed to be in ascending order.

Parameters: other_list (LinkedList): the other LinkedList to merge with the current list
Return Value: This method does not return a value, but it modifies the current LinkedList to contain the merged list.
Detailed Steps:

Initialize Helper Nodes:

Create a "dummy" node that acts as a starting point, and give it a value of 0.

Create another node called "current" and set it to point to this dummy node. We'll use "current" to keep track of where we are in the new merged list.

Merge Loop:

This loop will go through each node in both the list we're working on (self.head) and the list we're merging into it (other_head).

For each pair of nodes (one from each list), compare their values.

Take the node with the smaller value and attach it to the "current" node.

Move both the "current" node and the list head that had the smaller value to their respective next nodes.

Check for Remaining Nodes:

After the loop, it's possible that one list still has nodes while the other doesn't.

If that's the case, take the remaining nodes from the list that isn't empty and attach them to "current".

Update Head, Tail, and Length:

Once you're done with the merging, the "dummy" node will still be at the start. Update the head of the list to point to the node that comes immediately after this dummy node.

Also, make sure to update the tail node to be the last node in the new, merged list.

Finally, update the length of the list to account for the nodes from both original lists.


"""

def merge(self, other_list):
    other_head = other_list.head 
    dummy = Node(0)
    current = dummy
    
    while self.head is not None and other_head is not None:
        if self.head.value < other_head.value:
            current.next = self.head
            self.head = self.head.next 
        else: 
            current.next = other_head
            other_head = other_head.next 
        current = current.next 
    
    if self.head is not None:
        current.next = self.head 
    else:
        current.next = other_head
        self.tail = other_list.tail 
    
    self.head = dummy.next 
    self.length += other_list.length
