# 25 Recursive Binary Search Tree 

## 99 Contains

Contains method of Binary Search Tree (BST) using recursion

```python 
def __r_contains(self, current_node, value)

def r_contains(self, value):
    return self.__r_contains(self.root, value)
```

=> End user calls r_contains method
=> r_contains calls __r_contains

1. CASE: when BST is empty - return False
    root => None

2. CASE: when value is same as we are looking - return True 
    root => 47


```python
def __r_contains(self, current_node, value)
    if current_node == None:
        return False
    if value == current_node.value:
        return True

```

3. CASE when value exists but smaller than root (21)

```
   47
  /
21
```

current node: 47
current call stack:
    | 47 |
      21 

we call function recursively by passing left child node and value (21)

current call stack:
    | 21 | <-- active instance
      21
    | 47 |
      21  

```python
def __r_contains(self, current_node, value):
    if current_node == None:
        return False
    if value == current_node.value:
        return True
    if value < current_node.value:
        return self.__r_contains(current_node.left, value)
```

after we call by passing current nodes left node and value(21), we stop at this condition because value is the same:

if value == current_node.value:
    return True

function call returns True to this instance: 

    | 21 | <-- 21 is popped from call stack:
      21
    | 47 | <-- active instance
      21  


after function returns True, 21 is popped from call stack

active instance - 47

in this instance, we stopped here: 

    if value < current_node.value:
        return self.__r_contains(current_node.left, value)

now because the result of __r_contains() was True, this return statement returns True to its caller - to **r_contains** method 
(and pops 47 from stack)

def r_contains(self, value):
    return True

now this return statement returns True to its caller - original method call

my_tree.r_contains(21)



4. CASE when value does not exist - looking for 21

call stack:
| 47 | 

21 < 47  So this statement apply: 

if value < current_node.value:
    return self.__r_contains(current_node.left, value)

we recursively call function by passing left node of 41 - None

```
    47
    /
None
```


call stack:
    | None | <-- active instance of call stack
    | 47   | 


```python
def __r_contains(self, current_node, value):
    if current_node == None:
        return False
    if value == current_node.value:
        return True
    if value < current_node.value:
        return self.__r_contains(current_node.left, value)
```


Because we called function calling None, we stop at this condition and return False:

if current_node == None:
    return False

call with None finished its work, None popped from stack:
    | 47 |

=> False is passed to caller:
if value < current_node.value:
    return False

=> False is passed to caller:
def r_contains(self, value):
    return False

47 popped from stack

=> False is passed to original method call 
my_tree.r_contains(21)


5. CASE when value exists, higher than root (76)

```python
def __r_contains(self, current_node, value):
    if current_node == None:
        return False
    if value == current_node.value:
        return True
    if value < current_node.value:
        return self.__r_contains(current_node.left, value)
    if value > current_node.value:
        return self.__r_contains(current_node.right, value)
```


## 100 Insert 

user calls r_insert() :

```python
def r_insert(self, value):
    if self.root == None:
        self.root = Node(value)
    self.__r_insert(self.root, value)
```

r_insert() calls __r_insert():

```python 
def __r_insert(self, current_node, value):
    # base case
    if current_node = None:
        return Node(value)
    if value < current_node.value:
        current_node.left = self.__r_insert(current_node.left, value)
    if value > current_node.value:
        current_node.right = self.__r_insert(current_node.right, value)
    return current_node
```



```
        47
        /
    21
    /
    None
```


| None | <- when we reach base case, Node(18) is returned, assigned as left node 
| 21   | <- when function called recursively, left root passed to function call
| 47   | <- first pass, current_node was root 



```
        47
        /
      21
     /
   18
```

18 - | 21 | <- None popped from stack, 18 returned to this instance
            18 assigned as left node
21 - | 47 | <- return current_node returns 21 and 21 gets popped from stack. 
            current_node.left = 21: 47 continues pointing to 21
            at last, 47 is also gets popped from stack


Binary search tree cannot contain duplicates
    if we try to insert 21:
        code does not meet any condition (value is not None, not less or greater than root)
        so it returns current_node - 21. 
        so 47 root keeps pointing to 21

