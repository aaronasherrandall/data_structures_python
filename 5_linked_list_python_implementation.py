## Linked List implimentation from scracth
## We create our nodes using class with object
## This is how we create a node in python
class Node(object):

    ## Define init method to build constructor in python
    ## Pass in self and data
    ## We want to specify the data we want to store in this node
    ## We also store a reference to the next node
    ## Note: In the init method, self refers to the newly created object
    def __init__ (self, data):
        self.data = data
        self.nextNode = None

class Linkedlist(object):

    def __init__(self):
        ## First node
        ## Tree like structure
        self.head = None
        self.size = 0
    ## insert items at the beginning of the linked list
    ## O(1) - very fast
    def insertStart(self, data):

        ## increiment the size
        self.size = self.size + 1
        ## then we instantiate the new node
        newNode = Node(data)

        ## if the head is a null
        ## it will be the first item in the linked list
        if not self.head:
            ## initialize head to be new node
            self.head = newNode
        
        else:
            newNode.nextNode = self.head
            self.head = newNode

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

    ## O(1)
    def size(self):
        return self.size
    
    ## O(N) 
    def size2(self):
        actualNode = self.head
        size = 0

        while actualNode is not None:
            size+=1
            actualNode = actualNode.nextNode

        return size
    
    # insert item at end of the list
    # start at head and iterate through all of the items until we bump into a Null or "None" in Python
    # O(N)
    def insertEnd(self, data):

        self.size = self.size + 1
        newNode = Node(data)
        actualNode = self.head

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode

    def traverseList(self):

        actualNode = self.head

        while actualNode is not None:
            ## use %d since we know it will be an integer
            print("%d " % actualNode.data)
            actualNode = actualNode.nextNode

linkedlist = Linkedlist()

linkedlist.insertStart(12)
linkedlist.insertStart(122)
linkedlist.insertStart(3)
linkedlist.insertEnd(31)

linkedlist.traverseList()
# 3
# 122
# 12
# 31

# print(linkedlist.size)
# 4

linkedlist.remove(31)
linkedlist.remove(12)
linkedlist.remove(122)
linkedlist.remove(3)

# print(linkedlist.size)
# 0











