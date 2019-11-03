# Linked List implimentation from scracth

To create nodes in python, we use ```class``` with object

```Python
class Node(object):
```

We then define ```init``` method to build our constructor in python
We pass in self and data
We want to specify the data we want to store in this node **and** store a reference to the next node

```Python
    def __init__ (self, data):
        self.data = data
        self.nextNode = None
```
- Note: In the init method, self refers to the newly created object

Next, we create a class for our linked list:
```Python
class Linkedlist(object):
```

We use the init method again for our constructor
```Python
    def __init__(self):
        ## First node
        ## Tree like structure
        self.head = None
        self.size = 0
 ```
Next, we define our method for inserting items at the **beginning** of the linked list
This takes **O(1)** time complexity - very fast!

```Python
    def insertStart(self, data):

        ## increiment the size of the linked list
        self.size = self.size + 1
        ## then we instantiate the new node
        newNode = Node(data)

        ## If the head is a null, it will be the first item in the linked list
        if not self.head:
            ## initialize head to be new node
            self.head = newNode
        ## Otherwise, 
        else:
            newNode.nextNode = self.head
            self.head = newNode
```

Next, we can define out method for removing items from the linked list

```Python
    def remove(self, data):

        if self.head is None:
            return

        self.size = self.size -1

        currentNode = self.head
        previousNode = None

        while currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.nextNode

        if previousNode is None:
            self.head = currentNode.nextNode
        else:
            previousNode.nextNode = currentNode.nextNode
```

Here, we can define a method for checking the size of the linked list:
```Python    
    ## O(1)
    def size(self):
        return self.size
```

```Python    
    ## O(N) 
    def size2(self):
        actualNode = self.head
        size = 0

        while actualNode is not None:
            size+=1
            actualNode = actualNode.nextNode

        return size
 ```
    
Next, we can define out method for inserting items at **end** of the linked list
With this, we start at head and iterate through all of the items until we bump into a Null or "None" in Python:
This takes **O(N)** time complexity - very slow!

```Python
    def insertEnd(self, data):

        self.size = self.size + 1
        newNode = Node(data)
        actualNode = self.head

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode
```

And, here is our method for traversing the linked list:

```Python
    def traverseList(self):

        actualNode = self.head

        while actualNode is not None:
            ## use %d since we know it will be an integer
            print("%d " % actualNode.data)
            actualNode = actualNode.nextNode
```

We can test our linked list below:

```Python
linkedlist = Linkedlist()

linkedlist.insertStart(12)
linkedlist.insertStart(122)
linkedlist.insertStart(3)
linkedlist.insertEnd(31)

linkedlist.traverseList()
```

Output

```
3
122
12
31
```

We can also check the size of our list:
```Python
print(linkedlist.size)
```

Output:
```
4
```

To remove items, we can use our method we created and then print the size to check:

```Python
linkedlist.remove(31)
linkedlist.remove(12)
linkedlist.remove(122)
linkedlist.remove(3)
print(linkedlist.size)
```

Output:
```
0
```











