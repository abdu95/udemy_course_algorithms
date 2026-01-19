# Recursion

A function that calls itself until it doesn't 

Example: opening a gift box

```
- function returns ball or another box 

open_gift_box()
    => if ball, stop
    => if box - open_gift_box()
        => if ball, stop
        => if box - open_gift_box() 
```

```python 
def open_gift_box():
    if ball:            # <-- Base case 
        return ball
    open_gift_box()     # <-- function calls itself 
```

- The process of opening each new box is the same 
- Each time we open a box, we make the problem smaller 


**Base case** - case when the function stops calling itself 

**Recursive case** - case when the function needs to call itself 


```python 
# recursive call without a base case causes a stack overflow
def open_gift_box():
    open_gift_box() 
```

- Base case should be a condition that has to be true at some point. 
- Base case should return (terminate)

