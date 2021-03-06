# data_structures_python
Data Structures in Python

# Data Structures: Intro

## Why do we use Data Structures?

Data can be stored in computer memory in many different ways. With the utilization of data structures, we can influence the way the computer stores and retrieves data from any location in its memory. This allows the computer to perform different applications and tasks more efficiently.

Data structures ensure than running time will be faster for the algorithm they are applied to.

A good example is how Facebook uses data structures. More than 1 billion customers are present on Facebook at any given time. At this scale of big data, the difference between merge sort or bubble sort for sorting algorithms and the corresponding utilization of specific data structures will make a vast difference in the speed at which calculations can be made and how we can manipulate the data.

## Dijkstra Algorithm

- Without a proper data structure ( heap / priority queue ) the running time would be quadratic **O(N<sup>2</sup>)**

*We would like to find the shortest path in the graph where the number of edges is equal to the **n**, while the time complexity of this algorithm will be **O(N<sup>2</sup>)***

- Priority queue approach makes sure the running time will be far better **O(N<sup>*</sup>logN)**

*If we have a large dataset, i.e. n = huge number, it becomes more important to use **O(N<sup>*</sup>logN)** algorithm instead of **O(N<sup>2</sup>)**

## Spanning Trees

- We can boost up the algorithm with the help of priority queues as well

- So the running time of the algorithms are determined by the data structures we use

# Abstract Data Type

- This is the model ( logical description ) for a certain data structure
  - Similar to a supertype in programming ( so an interface in Java) 
    -  *Subtyping (also subtype polymorphism or inclusion polymorphism) is a form of type polymorphism in which a subtype is a datatype that is related to another datatype (the supertype) by some notion of substitutability, meaning that program elements, typically subroutines or functions, written to operate on elements of the supertype can also operate on elements of the subtype*
    - *If S is a subtype of T, the subtyping relation is often written S <: T, to mean that any term of type S can be safely used in a context where a term of type T is expected* (https://en.wikipedia.org/wiki/Subtyping)
- We define what methods / functions the data structure will have - defining the basic behavior
- IMPORTANT: it is just the model. The ADT (Abstract Data Type) does not specify the concrete implementation of the programming language
- "This is what the user knows"
- Example: **stack → push() pop() peek()**
  - ADT will *define* these behaviors
  
  # Data Structures
  - The concrete implemntation, the actual representation of the data
  - The aim is to be able to store and retrieve data in an efficient manner
  - What we want: to be able to insert / find items in **O(1)** time complexity and to be able to retrieve items in **O(1)** as well
  - Example: arrays, linked lists, binary trees etc.
  
| Abstract Data Types  | Data Sctructures |
| ------------- | ------------- |
| Stack  | array, linked list  |
| Queue  | array, linked list  |
| Priority Queue  | heap  |
| Dictionary / hashmap | array  |

ADT and DS are not independant from each other. ADT are the specifications, and every ADT has an underlying DS that will impliment the behavior specified by the ADT.





