# 28 TREE TRAVERSAL 

## 106 Intro

Visit every node, put in list, return the list

```
      47
     /  \
   21    76
  /  \   / \
18   27 52 82
```

There are multiple ways to visit each node. 


1. Breadth-First Search (BFS)
    Visit nodes level by level (left → right)

    Instead of going deep, you go wide first.

We start from the root and move level by level.

✅ Level 0
47

✅ Level 1
21   76

✅ Level 2
18   27   52   82

🧾 Final BFS traversal 
47 → 21 → 76 → 18 → 27 → 52 → 82


2. Depth First Search
    Go as deep as possible first, then backtrack

Instead of going level by level (like BFS), you go down one path completely.

Types of DFS:
    Preorder (Root → Left → Right)
    Inorder (Left → Root → Right)
    Postorder (Left → Right → Root)

Step-by-step (Inorder):

Go left as much as possible → 18
Visit parent → 21
Go right → 27
Back to root → 47
Go right subtree:
    Left → 52
    Root → 76
    Right → 82


✅ Result: 18 → 21 → 27 → 47 → 52 → 76 → 82


## 107 Breadth First Search 
My quick summary: 
    BFS happens level-by-level, horizontally
    DFS happens depth-wise, vertically

Start from root. 
Visit nodes level by level 


```
      47
     /  \
   21    76
  /  \   / \
18   27 52 82
```


Create 2 lists: 
- queue: nodes
- results: all values of nodes 

BFS is a loop:
1. Take from front of queue 
2. Add to results
3. Push its children to queue
Loop runs as long as there are items in it

queue → We store here a NODE (not value)
        we keep track of which node to visit next
        start with root
results → nodes that we already visited
         (stores the traversal order)



✅ BFS Using queue + result
🔹 Initial State
queue  = [47]
results= []


🔹 Step-by-step
1️⃣ Take from queue → 47

Add to results 
Add children (21, 76) to queue

queue  = [21, 76]
results = [47]


2️⃣ Take → 21

Add to results 
Add children (18, 27) to queue

queue  = [76, 18, 27]
results = [47, 21]


3️⃣ Take → 76

Add to results 
Add children (52, 82) to queue

queue  = [18, 27, 52, 82]
results = [47, 21, 76]


4️⃣ Take → 18
18 has no children - therefore no nodes to add to queue
Simply add 18 to results 

queue  = [27, 52, 82]
results = [47, 21, 76, 18]


5️⃣ Take → 27
queue  = [52, 82]
results = [47, 21, 76, 18, 27]


6️⃣ Take → 52
queue  = [82]
results = [47, 21, 76, 18, 27, 52]


7️⃣ Take → 82
queue  = []
results = [47, 21, 76, 18, 27, 52, 82]


✅ Final Answer
BFS = [47, 21, 76, 18, 27, 52, 82]


## 109 Depth First Search 

Pre-order: Root → Left → Right
Post-Order: Left → Right → Root
In-Order: Left → Root → Right

Pre-Order

```
        47
       /  \
     21    76
    /  \   / \
  18   27 52 82
```

👉 Pre-order = Root → Left → Right
    Visit the node BEFORE its children

That’s why it’s called PRE-order:

You process the node FIRST (pre)
Then go explore left and right

🧠 Why the name “Pre-order”?
Think of it like timing:

Step | Action
✅ Pre (before) Visit node
Then Go left
Then Go right


🎨 Visual Explanation 
47   ✅ visit first (PRE!)
↓
21   ✅
↓
18   ✅ (leaf)
↩ backtrack
→ 27   ✅
↩ backtrack to 47
→ 76   ✅
↓
52   ✅
→ 82   ✅



🧠 How to “feel” Preorder
👉 At every node, ask:

Can I visit it now? → YES ✅
Then go left
Then go right


🔄 Compare with other DFS types


TypeRuleFirst thing you do
✅ PreorderRoot → Left → RightVisit immediately
InorderLeft → Root → RightVisit in the middle
PostorderLeft → Right → RootVisit last

💡 Quick Memory Trick

Pre-order → “Process NOW” ✅
Inorder → “Process in-between”
Postorder → “Process at the end”


🚀 Real Intuition (Super Important)
👉 Pre-order is used when:

You want to copy a tree
You want to serialize structure
You need parent before children


🎯 One-line summary

Pre-order DFS = visit node first, then explore left and right


## 110 DFS Code


```
        47
       /  \
     21    76
    /  \   / \
  18   27 52 82
```

call stack: 

| 18 | <- 18 gets popped from stack when there is no node on its left 
| 21 | 
| 47 | <- first we pass root to traverse. then its added to results 
|____|

 |    |   |    |   | 18 |     | 27 |    |    | |    | |    |            | 52 | |    |           | 82 | |    | |    | |    | 
 |    |   | 21 |   | 21 |     | 21 |    | 21 | |    | | 76 |            | 76 | | 76 |           | 76 | | 76 | |    | |    | 
 | 47 |   | 47 |   | 47 |     | 47 |    | 47 | | 47 | | 47 |            | 47 | | 47 |           | 47 | | 47 | | 47 | |    | 
 |____|   |____|   |____|     |____|    |____| |____| |____|            |____| |____|           |____| |____| |____| |____|
 [47]    [47, 21] [47,21,18]  [47,21,18, 27]          [47,21,18, 27, 76]  [47,21,18, 27, 76, 52] [47,21,18, 27, 76, 52, 82] 



```python 
def dfs_pre_order(self):
    results = []
    
    def traverse(current_node):
        results.append(current_node.value)
        if current_node.left is not None:
            traverse(current_node.left)
        if current_node.right is not None:
            traverse(current_node.right)

    traverse(self.root)
    return results 

```


## 111 DFS Post Order


Post-order
    process node AFTER exploring its children
    Left → Right → Root


Step            Action 
----            ------
First           Go left
Then            Go right
✅ Post (after) Visit node



```
        47
       /  \
     21    76
    /  \   / \
  18   27 52 82
```

47
↓
21
↓
18   ✅ leaf (no node in left & right) → process (add to list)
↩ backtrack
→ 27   ✅ (leaf → process)
↩ backtrack
21   ✅ (children done → process now)
↩ backtrack
→ 76
↓
52   ✅
→ 82   ✅
↩ backtrack
76   ✅
↩ backtrack
47   ✅


## 112 DFS Post Order Code


[18, 27, 21, 52, 82, 76, 47]

```python 
def dfs_post_order(self):
    results = []
    
    def traverse(current_node):
        if current_node.left is not None:
            traverse(current_node.left)
        if current_node.right is not None:
            traverse(current_node.right)
        results.append(current_node.value)

    traverse(self.root)
    return results 
```


## 113 DFS In order

```
        47
       /  \
     21    76
    /  \   / \
  18   27 52 82
```

[18 21 27 47 52 76 82]
added exactly as the numerical order 

Visit the node IN BETWEEN its children
    Left → Root → Right

Step            Action
----            ------
First           Go left
✅ In (middle)  Visit node
Then            Go right


47
↓
21
↓
18   ✅ (no left → process now)
↩ backtrack
21   ✅ (left done → process)
→ 27
   ✅ (process)
↩ backtrack to 47
47   ✅ (left subtree done → process)
→ 76
↓
52   ✅
↩
76   ✅
→ 82
   ✅


## 114 DFS In order code 

```python
def dfs_in_order(self):
    results = []

    def traverse(current_node):
        if current_node.left is not None:
            traverse(current_node.left)
        results.append(current_node.value)
        if current_node.right is not None:
            traverse(current_node.right)

    traverse(self.root)
    return results 

```
