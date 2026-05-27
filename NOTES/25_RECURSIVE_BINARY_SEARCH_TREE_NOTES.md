# Recursive Binary Search Tree 

## Contains

Contains method of Binary Search Tree (BST) using recursion

```python 
def __r_contains(self, current_node, value)

def r_contains(self, value):
    return self.__r_contains(self.root, value)
```

=> End user calls r_contains method
=> r_contains calls __r_contains

1. if BST is empty - return False
2. if value is same as we are looking, return True 


```python
def __r_contains(self, current_node, value)
    if current_node == None:
        return False
    if value == current_node.value:
        return True

```

3. if value exists, smaller than root (21)

```
   47
  /
21
```

current node: 47
current call stack:
| 47 |

we call function recursively by passing left child node and value (21)

current call stack:
| 21 |
| 47 |

```python
def __r_contains(self, current_node, value)
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

after function returns True, 21 is popped from call stack:
current active instance:
| 47 |

the previous result True is returned here:

if value < current_node.value:
    return True

now this return statement returns True to its caller - to **r_contains** method

def r_contains(self, value):
    return True

now this return statement returns True to its caller - original method call

my_tree.r_contains(21)


4. if value does not exist

call stack:
| 47 | 

```
    47
    /
None
```

call stack:
| 47 | 

if value < current_node.value:
    return self.__r_contains(current_node.left, value)

we recursively call function by passing left node of 41 - None

call stack:
| None |
| 47   | 


```python
def __r_contains(self, current_node, value)
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

call with None finished its work, popped from stack:
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


5. if value exists, higher than root (76)

```python
def __r_contains(self, current_node, value)
    if current_node == None:
        return False
    if value == current_node.value:
        return True
    if value < current_node.value:
        return self.__r_contains(current_node.left, value)
    if value > current_node.value:
        return self.__r_contains(current_node.right, value)
```