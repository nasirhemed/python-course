---
title: Dictionaries
separator: <next>
verticalSeparator: <subdown>
theme: solarized
progress: true
revealOptions:
    transition: 'fade'
---

## Intro to Python 
### Modules
#### Nasir Hemed
<next>


# Dictionaries

<next>

## Compound Data Types

- Recall compound data types
  - Lists
  - Strings
  - Tuples

But what do they have in common ?

<subdown>

- There is order
- They are sequence types
  -  Use index to access value they contain

```python

l = [1,2,3]
s = "123"
t = (1, 2, 3)

s[1]
t[1]
l[1]
```

<next>

## What are dictionaries ?

- Dictionaries are compound datatypes 
  - Mapping data type
  - Map **keys** to **values**


- key1 → [1,2,4,5]
- key2 → "string"
- key3 → "anything"


<subdown>

To create a dictionary in python, we use the curly braces to define one

```python
>>> eng2sp = {} # Create a dictionary named eng2sp
>>> eng2sp["one"] = "uno" # key is one, value is uno
>>> eng2sp["two"] = "dos" # key is two, value is dos
>>> eng2sp
{"two": "dos", "one": "uno"}
```

<subdown>

Another way we can create dictionary is with the following:

```python
>>> eng2sp = {"one": "uno", "two": "dos", "three": "tres"}
>>> eng2sp
{"two": "dos", "one": "uno"}
```

<subdown>

To access a value for a certain key, we use "indexing". But this time instead of specifying the position, we specify the "key"

```python
>>> eng2sp = {"one": "uno", "two": "dos", "three": "tres"}
>>> eng2sp["one"]
"uno"
```

<next>

## Dictionary operations

- Just like lists, dictionaries have operations
  - Add
  - Delete
  - Update

<subdown>

Let's say we have a dictionary that has a stock of fruits


```python
>>> inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}
>>> print(inventory)
{'pears': 217, 'apples': 430, 'oranges': 525, 'bananas': 312}
```


### Add
Let's say we want to add a new type of fruit. We want to add strawberries

```python
>>> inventory["strawberries"] = 50
>>> print(inventory)
{'pears': 217, 'apples': 430, 'oranges': 525, 'bananas': 312, 'strawberry': 50}

```

<subdown>

### Update 

Let's say someone buys some fruits. Now we have to update it

```python
# Someone bought 100 apples
>>> inventory["apples"] = inventory["apples"] - 100
>>> print(inventory)
{'pears': 217, 'apples': 330, 'oranges': 525, 'bananas': 312}
```

Notice that updating this is quite similar to updating elements in the list. This is becuase dictionaries are mutable

<subdown>

### Delete

Let's say someone bought all the pears. So no we are no longer selling pears. 

To delete a key:value pair, we use the `del` keyword

```python
>>> del inventory["pears"]
>>> print(inventory)
{'apples': 330, 'oranges': 525, 'bananas': 312}
```

<subdown>

Let's say we got new shipment of bananas

```python
>>> inventory["bananas"] += 200
>>> print(inventory)
{'pears': 0, 'apples': 330, 'oranges': 525, 'bananas': 512}
```

<subdown>

The `len` function checks how many key:value pairs are there in the dictionary. So we can use it to check how many types of fruits we are selling

```python
>>> len(inventory)
4
```

<subdown>

## Dictionary Methods

- Dictionaries have a lot of useful methods. 

<subdown>

### `keys` method

The `keys` method returns a "collection" of the keys that were defined in the dictionary. We can use it to loop throguh the elements of the dictionary  

```python
for k in eng2sp.keys():   # The order of the k's is not defined
   print("Got key", k, "which maps to value", eng2sp[k])

ks = list(eng2sp.keys())
print(ks)
```

Not that the order of the keys do not matter. Since dictionary is not a sequence of elements

<subdown>

### `values` method

The `values` method returns a collection of values

```python
>>> list(eng2sp.values())
['tres', 'dos', 'uno']
```

<subdown>

### `items` method

The `items` method returns a tuple where both key and value are there

```python
>>> list(eng2sp.items())
[('three', 'tres'), ('two', 'dos'), ('one', 'uno')]
```

We can use the items method for our loops as well

```python
for (k,v) in eng2sp.items():
    print("Got",k,"that maps to",v)
```

<subdown>

### `in` and `not in`
To check if a key is inside the dictionary, we use `in` and `not in`

```python
>>> "one" in eng2sp
True
>>> "six" in eng2sp
False
>>> "tres" in eng2sp    # Note that 'in' tests keys, not values.
False
```

<subdown>

This can be useful if we want to avoid errors

```python
>>> eng2esp["dog"]
Traceback (most recent call last):
  ...
KeyError: 'dog'
```

```python
if "dog" in eng2esp:
	print(eng2esp["dog"])

```

<next>

## Aliasing and Copying

Recall what we discussed about mutability (lists and strings)

We are able to change values inside the list but we have to be careful about assigning

```python
a = [1,2,3,4]
b = a
a[0] = 3
b # What is the value of b ?
```

<subdown>

Dictionaries are mutlable too. So we need to be careful whenever we assign again.

```python
>>> opposites = {"up": "down", "right": "wrong", "yes": "no"}
>>> alias = opposites
>>> alias["right"] = "left"
>>> opposites
{"up": "down", "right": "left", "yes": "no"}
```

<subdown> 

To fix this: 

```python
>>> opposites = {"up": "down", "right": "wrong", "yes": "no"}
>>> alias = opposites.copy()
>>> alias["right"] = "left"
>>> opposites
{"up": "down", "right": "wrong", "yes": "no"}
```

<next>

## Counting the number of letters

We can use dictionaries to count the occurrences of letters in a string. Consider the following problem:

Count the number of occurences of letter "e"

```python
count = 0
for letter in word:
	if letter == "e":
		count += 1

return count
```

<subdown>

What if we want to count the occurrences of all letters? We need some table for that right ? We can use a dictionary!

```python
>>> letter_counts = {}
>>> for letter in "Mississippi":
...     letter_counts[letter] = letter_counts.get(letter, 0) + 1
...
>>> letter_counts
{'M': 1, 's': 4, 'p': 2, 'i': 4}
```

<next>

## Questions ?