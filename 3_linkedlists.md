# data_structures_python
Data Structures in Python

# Linked Lists 

Linked lists are composed of nodes and references / pointers which point from one node to the other.

The last node in a linked list always points to a null:

![Screenshot](linked_lists.png)

A single node:

 | Data | 
| ------------- | 
| Reference  |


- contains data -> integer, double or custom object
- contains a reference pointing to the next node in the linked list

The below is pseudo code illustrates a node below:
```
class Node {

  data
  Node nextNode
  ...
 }
 ```
- Each node is composed of a data and a reference/link to the next node in the sequence
- Simple and very common data structure
- They can be used to implement several other common data types: stacks, queues
- Simple linked lists by themselves **do not allow for random access to the data** //
so we can use indecies: getitem(int index)
- Many basic operations such as obtaining the last node of the list, finding a node that contains certain data or locating the place where the node should be inserted require sequential scanning of most of all of the list elements.
 
