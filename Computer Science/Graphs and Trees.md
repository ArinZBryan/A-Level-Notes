## Graphs
A graph is a network of nodes, connected via pointers. Each link between nodes is called an edge, and each node a vertex. A vertex may link to itself, or to another vertex that links to itself. A vertex may also be bi-directional or have a weight. It is because of this, that it is important to note the lack of a heirarchy / order (there are no root / parent / child nodes).

In a graph, there may be several unconnected subgraphs.

### Common Uses
- Navigation
- Data Transmission
- Links between web pages
- Mapping of social media

### Weights
The weight of an edge can be determined by several things. Of course this may be the distance between two points, or the desirability of some outcome. These weights can be changed by using heuristics, based on past experiences, or traversals of the graph.

### Adjacency Matrices
An adjacency matrix is a square matrix, where each element in the matrix is equal to the 'cost' associated with the vertex linking the vertices. An example matrix is shown below

![Ajacency Matrix](./Images/Graphs/Ajacency-Matrix.svg)

Note that the cells left empty correspond to the vertices that are not connected via an edge. Similarly, nodes not marked as connecting to themselves are denoted using a slash.

## Trees
A tree is a type of graph. In this case, nodes, known as leaves may not link to themselves. Such links are called branches in this case. There must be a 'head' node or 'root' node at the top of the tree, such that all other nodes are children directly or indirectly of this node. All links in this type of graph are one directional.

### Binary Trees
A Binary Tree is a type of tree, where there are only two or less child nodes per node. 
Generally, in this type of tree, the value held by each leaf is a number.

### Untyped Trees
An untyped tree is one where there are no limits on how many children each node may have. There is also no requirement on the type of data stored, or that it is in any way ordered.

### Tree Operations
#### Insertion of nodes
Inserting into a binary tree can be done in two major ways, the first, requires a node to act as a parent. This requires no further explanation, as it is just adding to an array. On the other hand, if the tree is ordered, then there is a procedure for inserting a node given a value for the node to have.
1. Start at the root node.
2. If the value is less than the node, move left. Else, move right.
3. If there are no children here, place the node here. Else, go back to step 2.

#### Deletion of nodes
Deleting from a binary tree involves traversing through the tree, using one of several searching methods, and comparing against the value to delete. If the node to delete has children, then there is a final procedure, to correct the tree.
1. Check the node's immediate children, pick the largest one which *could* act in the same way as the deleted node, and move it, and its children such that that is done.

#### Deletion of sub-trees
To delete a sub tree, first traverse through the tree using a depth first-search, deleting each node as you go.

#### Flattening trees
##### Preorder / Prefix
1. Add the parent node to the array
2. Run preorder algorithm on left sub-tree
3. Run preorder algorithm on right sub-tree 

##### Inorder / Infix
1. Run inorder algorithm on left sub tree
2. Add node to array
3. Run inorder algorithm on left sub tree if it exists, else recurse back up the tree

> This is the order in which traditional mathematics notation is written in.

##### Postorder / Postfix
1. Run postorder algorithm on the left sub-tree
2. Run postorder algorithm on the right sub-tree
3. Add node to array

> This is the order in which code is compiled to. It is also known as [Reverse Polish Notation](./The_Compilation_Toolchain.md).

## Traversals
### Breadth First
This type of traversal closely models the actions taken by Djikstra's algorithm. It is easily applicable to both graphs and trees. A breadth first traversal will use a queue to work, but generally, the route taken by the traversal will be what is asked for in a question.

### Depth First
This type of traversal is generally only used on on trees, rather than graphs, however, it can still be applied to graphs. A depth first traversal also uses a stack to store a '*trace*' of sorts. This will be what is asked for in exam questions. Below is the algorithm for a depth first traversal of a tree, starting at the *root node*:

1. Go as far as you can, going with the first node every time until you meet a dead end. Push this node on to the stack.
2. Backtrack to the last node with multiple unvisited children, and take the next child's route.
3. Repeat until the entire tree has been traversed.
4. Return the stack.

To make this algorithm work for undirected graphs takes only a small change to terminology: 
- There is no *root node*, so the node you start at is entirely arbitrary
- We use the term vertex instead of node
- Verticies have no defined children, and as such, we say neighbours instead of children.

This leaves us with a new algorithm that works for unordered graphs:

1. Go as far as you can, going with a random vertex every time until you meet a dead end. Push this vertex onto the stack.
2. Backtrack to the last vertex with multiple unvisited neigbours, and go to the next neighbour. 
3. Repeat until the entire graph has been traversed.
4. Return the stack.
