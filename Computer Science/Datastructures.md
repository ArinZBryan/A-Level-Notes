## Stacks
A stack is a manipulation of an already existing data structure (usually an array, but sometimes a list). Stacks
operate on a first in / last out principle.

#### Algorithm for adding (pushing) to the stack
>- Check to see if the stack is full (not commonly done)
>- If stack is full, raise error
>- Increment the stack pointer
>- Insert data to location pointed to by stack pointer

#### Algorithm for removing (popping) from the Stack
>- Check to see if the stack is empty
>- If stack is empty, raise error
>- Copy item at stack pointer to elsewhere in memory
>- Decrement stack pointer

The stack is most commonly used to implement hierarchical scope for variables.

## Queues
A Queue is another manipulation of existing data structures (usually an array, but sometimes a list). Queues operate on the principle of first in / first out.

The use two pointers, the head and the tail. Items are added at the tail and removed from the head.

They are commonly used in OS scheduler algorithms, the handling of data packets and breadth first searches.

#### Algorithm for adding to the Queue
>- Check to see if queue is full
>- if queue is full, throw error
>- insert item at location pointed to by tail pointer
>- Increment tail pointer

#### Algorithm for removing from the queue
>- Check to see if queue is full
>- if queue is empty, throw error
>- copy data pointed to by head pointer to memory
>- increment head pointer  

## Linked Lists
A versatile data structure, that is dynamically typed (sometimes), and has a non-fixed length during program execution.

A linked list is made of nodes, a node contains an element of the list, and a pointer to the next node. Sometimes a pointer to the last node is included
Along with arrays, this is the only data structure that exists 'for real'

Serial access - refers to the saving of data in the order in which it appears/is used/is generated.

Each item only exists in locality only.

Linked lists are found in:
- the file structure (sort of)
- Image viewers (a list of image pointers + images in a list)


We have to be able to traverse a linked list as part of the A-level.

We also need to know how to add and remove items from the linked list.

Algorithm for iterating through a linked list
```c++
linked_list = new linked_list(...)
endIndex = ...
int i = 0;
struct node n = &linked_list
while (i != endIndex) {
    n = &n::next_node
    i++;
}
return n::data
```
Algorithm for adding to the end of a linked list
>- allocate memory for the data, and save the pointer
>- get length of data
>- make new node from data and length of data
>- traverse to the end node of the linked list.
>- update its `next_node` property to the pointer to the new node

## Dictionaries
A dictionary consists of key-value pairs, for example: 
` "key1" : "value1"`, where, to access the value, the dictionary must be accessed via the use of the key. In the previous example, the key and value were of the same type, however, this is not required. The value can generally take any `type`, `class` or `struct`. In some cases, the key can be of a range of types. It is very uncommon to find keys of types other than in `int` or `string`. To use a datatype other than `int`, it must first be hashed, and the integer value used as the key. In this case the formal name of the data structure is not a '*dictionary*', but a '*hash map*'.

### Hash Maps
Hashmaps require a hashing function that produces no overlap, i.e.. no two keys may result in the same hash. If they do, then the entire thing breaks. This hashed value is then used as an index from the base pointer to the dictionary. This does mean that not all spaces in the continuous memory allocated for this data structure will be filled: a hash map is not memory efficient. 

A hash map may use a specialised hashing algorithm that uses a specific part of the data or does some specific maths to get a pointer from it. This allows programmers who know their dataset to optimise their hashmap for the specific application.