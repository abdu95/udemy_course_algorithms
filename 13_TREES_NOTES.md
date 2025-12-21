

# 13 Trees 

## 13.64 Trees Intro

    LinkedList is a form of a tree that does not fork
    
    Binary tree is a tree in which each node has at most two children

  4 
 /  \    
3    23

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

4: Parent, 3,23 Child nodes. They share same parent - siblings. Child nodes can be parent nodes too. 
  4 
 /  \    
3    23

Every node can have only one parent. 
4 has two parents - not a tree. 
3   23
 \  /
  4

Leaf - nodes that does not have children (12  17  14 27)
      4 
    /  \
   3    23
  / \   / \ 
12  17  14 27