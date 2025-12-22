

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

- Full tree: points to 0 or 2 nodes
- Perfect tree: any level in the tree that has any nodes is completely filled all the way across
- Complete tree: fill tree from left to right with no gaps 

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