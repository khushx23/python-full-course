# LIST

- Lists are ordered collection of data items.
- They store multiple items in a single variable.
- List items are separated by commas and enclosed within square brackets [].
- Lists are changeable meaning we can alter them after creation.

## List Indexes - 

Each item/element in a list has its own unique index. This index can be used to access any particular item from the list. The first item has index [0], second item has index [1], third item has index [2] and so on.

colors = ["Red", "Green", "Blue", "Yellow", "Green"]

          [0]      [1]     [2]      [3]      [4]

### Check for item:
We can check if a given item is present in the list. This is done using the in keyword.
```python
`colors = ["Red", "Green", "Blue", "Yellow", "Green"]
if "Yellow" in colors:
    print("Yellow is present.")
else:
    print("Yellow is absent.")`
```
output - Yellow is present.

## Range of Index:
You can print a range of list items by specifying where do you want to start, where do you want to end and if you want to skip elements in between the range. 

Syntax:

List[start : end : jumpIndex]

**Note**: jump Index is optional. We will see this in given examples.

```python
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])	#using positive indexes
print(animals[-7:-2])	#using negative indexes

```
OUTPUT- 

```python
['mouse', 'pig', 'horse', 'donkey']
['bat', 'mouse', 'pig', 'horse', 'donkey']

```
Here, we provide index of the element from where we want to start and the index of the element till which we want to print the values.

**Note**: The element of the end index provided will not be included. 

 ## ADD LIST ITEMS:
There are three methods to add items to list: append(), insert() and extend()

**append():**
This method appends items to the end of the existing list.

syntax: list(name).append(element)  #the element that is to be added

**insert():**
This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.
 syntax : list(name).insert(idx,ele)  #( the index at which the item is to be added , element)

 **extend():**
This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.
```python
#add a list to a list
colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)
print(colors)
```

## Remove List Items:
There are various methods to remove items from the list: pop(), remove(), del(), clear().

**pop():**
This method removes the last item of the list if no index is provided. If an index is provided, then it removes item at that specified index.

syntax: list(name).pop(i)  # i is the index at which the element is to be removed


**remove():**

This method removes specific item from the list.

syntax: list(name).remove(element)  #name of the element that is to be removed

## Change List Items:
Changing items from list is easier, you just have to specify the index where you want to replace the item with existing item.

```python
names = ["Harry", "Sarah", "Nadia", "Oleg", "Steve"]
names[2] = "Millie"
print(names)
```

```python
['Harry', 'Sarah', 'Millie', 'Oleg', 'Steve']
```
 