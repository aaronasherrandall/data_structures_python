# Arrays: Python Implimentation

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

We can also iterate through the list as such:
```Python
numbers[1] = 200
print(numbers[1])
200
```
