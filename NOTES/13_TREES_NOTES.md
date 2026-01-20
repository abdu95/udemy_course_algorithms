

# 13 Trees 

## 13.64 Trees Intro

    LinkedList is a form of a tree that does not fork
    
    Binary tree is a tree in which each node has at most two children

```
  4 
 /  \    
3    23
```

```json
{
    "value":4,
    "left": {
        "value": 3,
        "left":None,
        "right": None
        },
    "right" {
        "value": 23,
        "left":None,
        "right":None
        }
}
```

- Full tree
  points to 0 or 2 nodes
  Every non leaf has two children and all the leaves are on the same level

- Perfect tree: any level in the tree that has any nodes is completely filled all the way across
- Complete tree: 
  
  Every non leaf has two children except for the last row 

  All levels are completely filled except possibly the last level,
and the last level is filled from left to right with no gaps.

- Parent (4) 
- child nodes (3,23). 
  They share same parent - siblings. Child nodes can be parent nodes too. 

```
  4 
 /  \    
3    23
```

Every node can have only one parent. 
4 has two parents - not a tree. 

```
3   23
 \  /
  4
```

Leaf - nodes that does not have children (12  17  14 27)

```
      4 
    /  \
   3    23
  / \   / \ 
12  17  14 27
```

## 13.65 Binary Search Tree

There is a node X. A new Y node will be added to right side of the node (if Y > X) or the left side (if Y < X)
    
- All nodes below the root node (47) and to the right are greater than root node
- All nodes below the root node (47) and to the left are less than root node

```
     47
   /    \
  21      76
 /  \    /  \
18  27  52  82
```

My notes: 

- Binary tree
  A tree that can have at most two children 

- Binary search tree
  A type of binary tree with an ordering property: for every node, all values in its left subtree are smaller, and all values in its right subtree are larger

Key Differences

- Structure: Binary trees have no ordering requirement; BSTs must maintain sorted order.

- Search efficiency: In a binary tree, you might need to check every node (O(n) time). In a balanced BST, search is O(log n) because you can eliminate half the remaining nodes at each step.

- Use cases: Binary trees are good for representing hierarchies. BSTs are designed for efficient searching, insertion, and deletion of sorted data.

- Insertion: Binary trees can insert anywhere. BSTs must insert in the correct position to maintain the ordering property.

So every BST is a binary tree, but not every binary tree is a BST. The ordering constraint is what makes BSTs particularly useful for operations like searching and finding min/max values.



## 13.66 BST: Big O


Number of nodes = 1 = 2^1 - 1

```
 47
/  \
```

Number of nodes = 2^2-1
```
 47
/  \
21  76
```

Number of nodes = 2^3-1

```
   47
  /  \
  21  76
  /  \  / \
 18  27 52  82 
```

1 is insignificant. 2^3-1 approximately 2^3 nodes

LOOKUP 

How many steps it takes to find 76?

Number of nodes = 2^2-1
Steps it takes = 2
```
 47
/  \
21  76
```


REMOVE 

Iterate through tree, find 76, remove 
Steps it takes = 2
```
 47
/  \
21  76
```


ADD 

Iterate through tree, find index, add 
Steps it takes = 2
```
 47
/  \
21  76
```

| BST: LOOKUP, REMOVE, INSERT - O(log N)

O (log N) - very efficient 

O(1) > O (log N) > O(N)


O (log N) - divide & conquer

In a balanced BST, each comparison splits the remaining elements in half.

In the example we used perfect tree. Perfect tree gives best possible scenario. Best possible scenario is measured using Omega. 

But Big O describes the worst-case scenario. 

WORST CASE SCENARIO

If tree never forks (node does not split into branches), it is essentialy a linked list. 
Finding 91 is O(N)

Technically Big O of binary search tree is O(N), not O(log N) 

```
47 
  \
  76
    \ 
     82
      \
      91
```

Summary:

- Ω(1) for best case -  The element is at the root
- O(log N) for worst case in a balanced tree.
- O(N) for worst case in an unbalanced tree.



| Linked List: LOOKUP - O(N), REMOVE - O(N), INSERT O(1)

- Choose BST for LOOKUP, REMOVE
- Choose LinkedList for INSERT 

Use case: in situations where INSERT is done frequently, LinkedList is better 



### NOTE: 

2^x = 16 can be written as log2 16 =x. This shows in what x power of 2 the result will be 16. 
In a balanced BST, each comparison splits the remaining elements in half.
1. What does log⁡N\log NlogN mean in BST context?

In a balanced BST, each comparison splits the remaining elements in half.
If you start with NNN elements, after:

1 comparison → N/2N/2N/2 remain
2 comparisons → N/4N/4N/4 remain
3 comparisons → N/8N/8N/8 remain


After kkk comparisons, remaining elements = N/2kN / 2^kN/2k.


2. When do we stop?
We stop when there’s 1 element left:
```
N/2^k = 1

Solve for kkk:

N = 2^k => k = log_2 N
```

So log⁡2N tells us how many times we can divide N by 2 before reaching 1.
That’s exactly the number of steps in a binary search or BST lookup.
If N=16N = 16N=16, then:

log_2 16 = 4log2​16=4
So at most 4 comparisons to find an element in a balanced BST with 16 nodes.

So shortly, the main question is how many steps lookup takes? Or more clearly, when do I stop? 
I stop when N /2^k = 1. And what is such k? in other words, k = log2 N 

So basically you give me N, I give k (I tell you when to stop = how many steps algorithm will take)



## 13.67 Constructor 

```python
class Node:
    def __init__(self, value):
        self.value = value 
        self.left = None 
        self.right = None 

```

Each node have something pointing to it, except for root node.


```
     47
   /    \
  21      76
 /  \    /  \
18  27  52  82
```

```python
class BinarySearchTree:
    def __init__(self, value):
        new_node = Node(value)
        self.root = new_node
```


But you can also create tree where root is None - empty tree. 

```python
class BinarySearchTree:
    def __init__(self):
        self.root = None
```


## 13.68 BST: Insert 

  The main idea is to compare new_node to temp (current node). If new_node < temp, go to the left side of the node. If new_node > temp, go to the right side of the node. 
  Then after we go left or right, we check if there is a node on that side. If there is no node, we insert there. If there is a node, we do comparison again.  
  Edge case I: if root == None 
  Edge case II: if new_node == temp 

  create new_node
  if root == None then root = new_node 
  temp = self.root 
  while loop
    if new_node == temp return False
    if new_node < temp then left, else right 
    if None insert new_node else move to next 





Insert 

Create New Node

The code new_node = Node(value) creates a new node with the value you want to insert.

Is the Tree Empty?

The line if self.root is None: checks if the tree is empty.

If it's empty, self.root = new_node makes the new node the root of the tree.

Start at Root

temp = self.root sets a temporary variable, temp, to the root so we can start there.

Loop Until Spot Found

while(True): makes a loop that will keep going until it finds the right spot for the new node.

Duplicate Check

if new_node.value == temp.value: checks for duplicate values.

If a duplicate is found, it exits by returning False.

Should We Go Left?

if new_node.value < temp.value: checks if the new value is less than the current node's value.

Insert to the Left

if temp.left is None: checks if the left child spot is empty.

If so, temp.left = new_node puts the new node there.

Move Left and Continue

temp = temp.left means, if the left spot isn't empty, move left and continue looking.

Or Should We Go Right?

If the new node's value is greater, the code moves to the else: part.

Insert to the Right

if temp.right is None: checks if the right child spot is empty.

If so, temp.right = new_node puts the new node there.

Move Right and Continue

temp = temp.right means, if the right spot isn't empty, move right and continue looking.


## 13.70 BST: Contains

  if root == None return False
  temp = self.root 
  while temp is not None 
    if < left 
    elif > right 
    else = return True
  return False