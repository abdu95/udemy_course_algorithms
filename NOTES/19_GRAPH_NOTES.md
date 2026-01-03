# Graphs

## Intro

    Vertex (node)
    Edge (connection)

```
          82
          ^
       /  ||
    44 <= 76
```

*Weighted and unweighted edges*

Graph can have weighted edges (google maps, networking protocol)

Road 43 <= 76 has a lot of traffic. 
82 <= 76: cost 15 

44 <= 76: cost 3
82 <= 44: cost 2

82 <= 44 <= 76 cost = 5


*Bidirectional relationship*

Facebook friend

You <=> Friend 
Your Friend is connected to you and you are connected to your friend. 

*Directional relationship*

You => Celebrity
You follow a Celebrity. Celebrity does not follow you back.  


*Graph <= Tree <= LinkedList*

LinkedList is a form of a tree, but they point to only one node.
Tree is a form of graph, but each node can point out two other nodes. 


## Adjacency Matrix 

```
       A
    /    \
   E      B
    \     /
    D <-> C
```

```
   A B C D E
A  0 1 0 0 1
B  1 0 1 0 0
C  0 1 0 1 0
D  0 0 1 0 1
E  1 0 0 1 0
```

- 1: has edges with vertex
- 0: has not edge with a vertex 

If edges are weighted, we write weight in the matrix instead of 1.

Vertex has no edge with itself. That's why it has 45 degree line of zeros.
In such bidirectional matrix, you will always have a mirror image on each side of the 45 degree line. 

- Horizontal: vertex
- Vertical: the items it has an edge with


## Adjacency List


```
       A
    /    \
   E      B
    \     /
    D <-> C
```

Adjacecny list holds all of the edges that each vertex has with other vertices. 

```
{
    'A': ['B', 'E'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['C', 'E'],
    'E': ['A', 'D']
}
```


## Graph Big O

Space complexity

Adjaceny matrix: has to store all of the vertices it is not connected to (zeros) 

- Adjaceny matrix
    O(|V|^2) - number of vertices squared
- Adjacency list
    O(|V| + |E|) - number of vertices plus number of edges 


*Adding a vertex* 
- with Adjacency List 
    just add new vertex to dictionary - 'F': [] 
    {'F': []}
    O(1)
- with Adjacency Matrix
    adding a new row, adding a new column - rewriting the entire matrix
    O(|V|^2)

*Adding an edge* 

F <=> B
add an edge between F and B

- with Adjacency List - O(1)
```    
{
        'B': ['F']
        'F': ['B']
}
```

- with Adjacency Matrix - O(1)

add 1: row B, column F
add 1: row F, column B

```
   B F
B  0 1 
F  1 0
```

*Removing an edge*

- with Adjacency List - O(|E|) - number of edges

    go to vertex B , iterate through all edges to find necessary edge, remove it 

    go to vertex F , iterate through all edges to find necessary edge, remove it 

- with Adjacency Matrix - O(1)

set 0: row B, column F
set 0: row F, column B


*Removing a vertex*

- from Adjacency List - O(|V| + |E|)
        
        remove vertex F from dictionary 
        iterate over each vertex and iterate over each edge: remove edge with F

- from Adjacency Matrix - O(|V|^2)

    rewriting the entire matrix

        remove column F
        remove row F


| Adjacency Matrix 

In the example of Facebook, there are billions of profiles. Billion edges - billion columns and billion rows. For each cell, we have to record 1 & 0. 

But in Adjacency List, we dont have to store the zeros. 


Finding a vertex - O(1)


## Add vertex 

prevent duplicate vertex name - first check if key exists

```python
class Graph:
    def __init__(self):
        self.adj_list = {}


    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
```


## Add edge 

Add edge means create a connection. In code its adding a vertex to a list of edges
First check if both vertices exist

```python
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():    
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True 
        return False
```


## Remove edge

```python
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():    
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
            return True 
        return False
```

Edge case: new vertex is added which has no edge with other vertices. When we try remove edge between this new vertex and other vertex, we are trying to remove edge that is not in the list - ValueError is thrown 

```
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():    
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True 
        return False
```


## Remove vertex 

Remove vertex includes removing an edge that a vertex has with all other nodes 

Bidirectional graphs has efficiency. 
We want to delete D.
In the list of edges of D we can see an edge with another vertex - A, A also has an edge with D. 
So we should iterate over edges of A, find D and remove it from the list. We should repeat this for other vertices with which D has an edge.
At the end we delete D vertex from dictionary. 
This is efficient as we iterate through only the vertices that are mentioned in the edge list of D. 


```
{
    'A': ['B', 'C', 'D'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['A', 'B', 'C']
}
```


```
{
    'A': ['B', 'C'],
    'B': ['A'],
    'C': ['A'],
}
```