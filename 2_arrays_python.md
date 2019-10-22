# Arrays: Python Implementation

Python does not have a native array data sctucture.
However, it does have the **list**, which is much more general and can be used as a multidimensional array.
The **list** in Python is an ordered collection of items which can be of any data type.

See the list of numbers below:
```Python
numbers = [10, 20, 30, 40, 50]
```
We can perform **random indexing** on the above list, which has a time complexity of **O(1)**. This will get items we **know the index for**.

```Python
print(numbers[4])
50
```

We can also iterate through the list and update the item in the **1*** index as such:
```Python
numbers[1] = 200
print(numbers[1])
200
```

To iterate through a given 1 dimensional array we can use a **for loop**:
```Python
for num in numbers:
    print(num)
10
200
30
40
50
```

Since python allows for lists to contain multiple data types, we can update the second item to a string:
```Python
numbers[1] = 'Adam'
numbers
[10, 'Adam', 30, 40, 50]
```

**We are not able to store multiple data types in Java or C++ as we can in Python.**

The below works the same as the for loop above:
```Python
for i in range (len(numbers)):
    print(numbers[i])
10
Adam
30
40
50
```

Use the **semicolun operator** to print out just the first two items in list:
```Python
print(numbers[0:2])
[10, 'Adam']
```

Just placing a single semicolun will print out all items of the list:
```Python
print(numbers[:])
[10, 'Adam', 30, 40, 50]
```

Print out all but the last item:
```Python
print(numbers[:-1])
[10, 'Adam', 30, 40]
```

# Find the maximum

#### # O(N) search running time / linear time complexity

```Python
numbers = [10, 20, 300, 40, 50]

maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num
            
print(maximum)
300
```

#### Notes:

Binary Search Trees have O(logN) time complexity
Associative Arrays such as dictionaries have 0(1) time complexity - constant time complexity
