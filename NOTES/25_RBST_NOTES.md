## 101 Delete 

```
     47
    /   \
  21    76
 / \    / \
18  27 52  82
```


To delete 27
1. start at root - 47 and traverse down the tree to 27
2. once we find node, delete it

CASES:
2.1. if its leaf node (last child), we simply delete it

```
   47
  /
21
```

2.2. if we need to delete node that is not leaf, that has opening on the left but has node on the right, we simply move them up 

```
    47
    /
  21
  / \
    22
```

2.3. if we need to delete node that is not leaf, that has node on the left and opening on the right we simply move them up

```
    47
    /
  21
  / \
20   
```


2.4. when we need to delete node  the node is not leaf and has nodes underneath it in both left and right sides


```
      47                 
    /     \               
  21       76              
 / \       / \
18 |27|  52  82
    /
   25
   /\
  24 26     


     47
    /   \
  21    76
 / \    / \
18  25 52  82
    /\
  24 26  
```

    we look at right node - with higher value
    we look at left bottom of that node - lower value - Node(X)
    We copy this value to a node that we want to delete
    now we have two nodes with same value - we delete Node(X)

```
     47
    /   \
  21     76
 / \     / \
18  |28| 52  82
   /   \
  25    29
 / \    / \
24 26  |28| 30

```


### CODE

```python 

def __delete_node(self, current_node, value):
    if current_node == None:
        return None
    if value < current_node.value:
        current_node.left = self.__delete_node(current_node.left, value)
    elif value > current_node.value:
        current_node.right = self.__delete_node(current_node.right, value)
    else:

    return current_node


def delete_node(self, value):
    self.root = self.__delete_node(self.root, value)
```


```
  47
  /
21 

```

delete 18 - does not exist in BST

| None | <- 18 < 21: so we call instance with node on left of 21 - which is None 
| 21   | <- since 18 is < 47 we call function recursively by passing 21 
| 47   | <- first root is passed
|______|

     \ None / - after returning None, None gets popped from call stack
None \ 21   / - None is returned to this call. 21 is already pointing to None
     \ 47   / - return current_node: current_node -> 21. 21 gets popped from stack 
              - current_node.left = self.delete() - this line called that instance
              - current_node.left = 21
              - return current_node - this is returned to calling function - delete_node()
              - this is when 47 gets popped from call stack 


### CODE for else

```python 
def __delete_node(self, current_node, value):
    if current_node == None:
        return None
    if value < current_node.value:
        current_node.left = self.__delete_node(current_node.left, value)
    elif value > current_node.value:
        current_node.right = self.__delete_node(current_node.right, value)
    else:
        # test if this is leaf node 
        # case 2.1
        if current_node.left == None and current_node.right == None:
            return None 
        # case 2.2
        elif current_node.left == None:
            current_node = current_node.right
        # case 2.3 
        elif current_node.right == None:
            current_node = current_node.left
        # case 2.4
        else:
            sub_tree_min = self.min_value(current_node.right)
            current_node.value = sub_tree_min
            current_node.right = self.__delete_node(current_node.right, sub_tree_min)

    return current_node

```

CASES: 
delete 21 

2.1. if we need to delete leaf node (last child), we simply delete it

```
   47
  /
21
```


| 21 | <- 21 < 47 so we call instance on 21
| 47 | <- first we call with root. then 21 returns None and gets popped from stack. 
        line that run that instance gets None: 
        current_node.left = None


delete 21
2.2. if we need to delete node that is not leaf, that has opening on the left but has node on the right, we simply move them up 

```
    47
    /\
  21
  /\
    22
```

| 21 | <- then call instance on current_node.left. 
        This is the value we want to remove (not more, not less, so we face ELSE)
        so we replace current_node |21| with a node on its right |22|
        then we return current_node - 21 gets popped from call stack 
        Node 21 has no node pointing to it - garbage collected.
| 47 | <- call instance on root
        21 is popped
        22 is returned to the line that called this instance:
        current_node.left = 22



2.3. if we need to delete node that is not leaf, that has node on the left and opening on the right we simply move them up

```
    47
    /
  21
  / \
20   
```


delete 21
2.4. when we need to delete node  the node is not leaf and has nodes underneath it in both left and right sides

- find the minimum value in a subtree of a node that is to be deleted 
- replace this with the value of a node that is to be deleted
- delete node with min value - for this we need to traverse to the right of the tree

```
       47
      /
   |21|
   / \
  20  25 
     / \
   |24| 26
```

## 104 Minimum Value

Find minimal value in subtree 
    pass a node (lets say root)
    and continuosly go to the left until you find min value - until you reach None 

```
        47
        /   \
    21     76
    / \     / \
 |18| 27  52  82
  /
None
```


```python 
def min_value(self, current_node):
    while current_node.left is not None:
        current_node = current_node.left 
    return current_node.value 
```

