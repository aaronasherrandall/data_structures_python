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

## Advantages
- Linked lists are dynamic data structures ( arrays are not )
- It can be allocated the needed memory at run-time
- Very efficient if we want to manipulate the first elements
- Easy implementation
- Can store items with different sizes: an array assumes every element to be exactly the same
- It's easier for a linked list to grow organically. An array's size needs to be known ahead of time, or re-created when it needs to grow.

## Disadvantages
- Waste memory because of the references ( reference is required in each node )
- Nodes in a linked list must be read in order from the beginning as linked list have sequential access ( array items can be reached via indexes **O(1)** time complexity
- Difficulties arise in linked lists when it comes to reverse traversing. Singly linked lists are extremely difficult to navigate backwards.
- Soulution: doubly linked lists -> easier to read, but memory is wasted in allocating space for a back pointer.

# Operations

## insertion

Inserting items at the beginning of the linked list: very simple, we just have to update the references -> **O(1)** time complexity

```
linkedList.insertAtStart(-5);
```

![Screenshot](array_insertion.png)

