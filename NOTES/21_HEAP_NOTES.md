# Heaps 

## Heap: Intro

Heap: Uyum

- Heap - Complete Binary Tree: filled from left to right with no gaps
- In heap, you can have duplicates
- Order of nodes does not matter: lower value does not have to be on left


A heap has two strict rules:

- Shape rule (Complete Binary Tree)

    Filled level by level.
    Left to right.
    No gaps.

- Order rule

    Max-heap: parent ≥ children:
        highest value on top, any node has a value that is higher than or equal to its descendents 
    
    Min-heap: parent ≤ children:
        lowest value on top, any node has a value that is lower than equal to its descendents 

Because of these rules:

    Heap is not sorted.
    You only know that the root is min or max.
    That's why heap is not efficient for searching.
    It is efficient for tracking the top item and removing it. 
    Very efficient for priority queues.



```
       99
    /     \
  72       61
 /  \     / \
58  55  27  18
```


- Height of tree is logN

Height of tree with 8 nodes => log 2 of 8 = 3




```
       99
    /     \
  72       61
 /  \     / \
58  55  27  18
```

We store heap tree in a list and not create a Node class. 
Starting from 1 is easier for calculating the position.


```
    99  72  61  58  55  27  18  
0   1   2   3   4   5   6   7   
```

*Find the children of 99:*

    left child = 2 * parent_index
             2 = 2 * 1 

    right_child = 2 * parent_index + 1

*Find the parent of 27 & 18:*

    parent_index = left child // 2
    6 // 2 = 3
    parent_index = right child // 2
    7 // 2 = 3


### Questions 
1. difference between heap vs. tree 
Tree (general)
    Can have any shape.
    No strict rule about ordering.
    Parent and children can hold any values.
Example use: file systems, org charts.

Think of a tree as a free-form forest 🌳

Heap (special kind of tree)

A heap has two strict rules:

Shape rule (Complete Binary Tree)

Filled level by level.

Left to right.

No gaps.

Order rule

Max-heap: parent ≥ children

Min-heap: parent ≤ children

Because of these rules:

Heap is not sorted.

You only know that the root is min or max.

Very efficient for priority queues.

Think of a heap as a tree with military discipline 🪖


2. when inserting a node to heap, we should compare it to parent. what if there is left node, should we compare new node to left node and then to parent node or only to parent node?

Short answer: only compare with the parent ✅

Why?

When you insert into a heap:

You must insert at the next free position (to keep completeness).

That position is a leaf.

Leaves have no children yet.

So there is no left or right child to compare with.

What happens next?

You do heapify-up (bubble-up):

Compare new node with its parent.

If heap property is violated:

Swap with parent.

Repeat until:

Property is satisfied, or

You reach the root.

You never compare sideways. Only upward.

Sideways comparisons belong to sorting, not heaps 🚫


3. when inserting a node to heap, we should compare it to parent node. To find parent node, we divide current position to 2. why dividing to 2 helps to find the position of parent node?  
    Because in heap nodes are stored in array in order. First parent is stored, followed by its 2 child nodes. That's why when we divide the position into 2, we get position two steps back - the postiion of the parent. 

Sideways comparisons belong to sorting, not heaps 🚫

After you said this, I remembered that in a binary search tree, left node should be lower than right node. So in heap, we compare new node to parent node not to left or right node because heap has no such requirement as in binary search tree?
Yes
    BST orders values horizontally and vertically.
    Heap orders values only vertically.


## Heap: Insert 

Insert 100 to a heap 

```
       99
      / \
    72   61
  /
58
```

We start by inserting a new node to next open space. The reason is the tree needs to remain complete. 

```
       99
      / \
    72   61
  /  \
58   100
```

Now we need to **bubble up new node to appropriate spot**. 
- We start by comapring it to its parent - 72. 100 > 72. We swap.  

```
       99
      / \
   100   61
  /  \
58   72
```

- 100 > 99. We swap

```
    100
    / \
   99   61
  /  \
58   72


    100 99  61  58  72
0   1   2   3   4   5   
```


Bubble up - moving new node to top with while loop

While loop stops in 2 conditions:
- if new node reaches top of heap
- if new node is less than top node 


## Heap: Helper methods 


```
```




## Heap: Remove

Remove consists of 3 operations: 
1. Remove node from top 
2. Bring last node to top
Temporarily bring last node to top so that remaining nodes stay connected 
3. Sink down 
Now **sink down the top node to appropriate spot** - below the node that is greater than this top node 
