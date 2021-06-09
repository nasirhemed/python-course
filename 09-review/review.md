---
title: Review
separator: <next>
verticalSeparator: <subdown>
theme: solarized
progress: true
revealOptions:
    transition: 'fade'
---

## Intro to Python 
### Review
#### Nasir Hemed

<next>

## Review Session

- So we're halfway through the course!
- We will be reviewing the concepts we learned earlier
- Next sessions: Classes, OOP, Pygame, Game Project

<next>

## What is Computer Programming

- Series of instructions
    - Like a Recipe or Manual
    - Using a language that is clear and concise

Computers are kinda dumb. But at least they are obedient

<subdown>

<section>
<iframe src="https://vanillawebprojects.com/projects/hangman/" style="position:fixed; top:0; left:0; bottom:0; right:0; width:100%; height:100%; border:none; margin:0; padding:0; overflow:hidden; z-index:999999;">
    Your browser doesn't support iframes
</iframe>
</section>

<next>

## Data Types

- There are different types of data
    - `float`, `int`, `bool`, `str`
    - Each serve their different purpose

<subdown>

### Python as Calculator (Gone Wrong)

```python
>>> 0.1 + 0.2 
0.30000000000000004
>>> 1 + 0.00000000000000000000000001
1.0
>>> 1.01 - 0.99
0.020000000000000018
```

<next>

## Variables

```python
x = 2 
x += 5
x = 3

# Final value of x is ?
```

<next>

## Functions

- Function is a sequence of expressions in a block.
- It takes in input and returns/does something for you

<subdown>

### Default Functions

- `print` function lets your print to the console
- `input` lets us ask a user something
- `int()`, `str()`, `float()` lets us convert from one type to another

<subdown>

### User Defined Functions

- We can define our own functions

```python
# Syntax for a function
def function_name(args): # <- Header for the function
  """
  Here, we are explaining what the function does 
  so that other people can know what it does and how 
  to use it
  """
  ... # expression to write
  ... # expression
  ... # expression
```

<subdown>

### Return vs Print
- `return` is very different from `print`.
- `print` just displays something on the screen
- `return` will actually give back something

```python
def print_square(x):
    print(x * x) 
    # Nothing will be returned
```

<next>

### Booleans

- `bool` is a datatype that is basically either `True` or `False`

```python
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>

>>> 5 > 2
True
>>> 3 < 0
False
>>> 5 == (3 + 2) 
True
>>> j = "hel"
>>> j + "lo" == "hello"
True
```

<subdown>

### Conditions

* Conditions allows us to execute code if a certain condition is met

```python
if boolean_expression:
    # Code will be executed only if the statement is True
    do something 
    ...
else:
    # If the statement is not True, then we will execute here
    do the other thing 
```
<subdown>

### Example 

```python
if 3 > 2:
    print("I will not execute")
else:
    print("I will execute because 3 is bigger than 2")

if 3 < 2:
    print("I will execute because 3 is less than 2")
else:
    print("I will not execute")
```

<next>

## While Loops

- While loops allow us to repeat the code until the condition is no longer satisfied

```python
counter = 1
while counter < 10:
  print(counter)
  counter += 1
```

<next>

## For Loops
- For loops are similar to while loops except we don't have to worry about updating the counter

```python
for i in range(10):
  print(i)
```

<next>

## Strings

- A string is a collection of characters
- Allows us to put text

```python
>>> name = "John Wick"
>>> name.upper()
"JOHN WICK"
>>> name.replace("W", "N")
"John Nick"
```

<subdown>

### Strings as a collection

```python
>>> name[0]
'J'
>>> len(name)
9
>>> name[0:4]
"John"
```

<subdown>

### Strings are Immutable

- Remember that strings are just a collection of characters.
- Can you change the second character to be something else?

```python
s = "Hello"
s[0] = "J" # This will give me an error
```

Unfortunately, you cannot

<next>

## Lists

- Lists are an ordered collection of elements
  - Elements can be anything
  - `int`, `str`, `float`, etc.

```python
>>> points = [10, 20, 30, 40, 50] # List of 5 integers
>>> food_items = ["tuna", "apple", "cherry"] # list of 3 strings
>>> len(food_items)
3
>>> food_items.pop()
"cherry"
>>> food_items
["tuna", "apple"]
```

<subdown>

### Lists are Mutable

- Unlike strings, we can change elements of lists
```python
>>> fruit = ["banana", "apple", "quince"]
>>> fruit[0] = "pear"
>>> fruit[2] = "orange"
>>> fruit
['pear', 'apple', 'orange']
```

<subdown>

### Object and Reference


- When we assign a variable to a list
  -  What is actually happening in the background ?
```python
>>> a = [1, 2, 3]
# Python creates [1, 2, 3] somewhere in memory 
# and gives you back the location in memory
>>> id(a)
1987213982341
```

<subdown>

### Aliasing can be dangerous!

- If we assign one variable to another
  -  Both variables refer to the same object:


```python
>>> a = [1, 2, 3]
>>> b = a
>>> a is b
True
>>> id(a)
801928310123
>>> id(b)
801928310123
```

<next>

## Tuples

- Tuples are very similar to lists 
- They allow us to group data
- They are immutable however
- Can be used to define multiple vars for a single record

```python
>>> paris = ("Paris", "Hilton", 1981)
>>> john = ("John", "Wick", 1964)

>>> first, last, dob = paris
>>> first
"Paris"
>>> last
"Hilton"
>>> dob
1981
```

<next>

## Dictionaries

- Dictionaries are compound datatypes 
  - Mapping data type
  - Map **keys** to **values**


- key1 → [1,2,4,5]
- key2 → "string"
- key3 → "anything"

<subdown>

### Examples 


```python
>>> eng2sp = {} # Create a dictionary named eng2sp
>>> eng2sp["one"] = "uno" # key is one, value is uno
>>> eng2sp["two"] = "dos" # key is two, value is dos
>>> eng2sp
{"two": "dos", "one": "uno"}
```
<next>

## Files

- Files reside in the disk which is far and slow to get
  - Open file
  - Do something (Read/Write)
  - Close the file

```python
myfile = open("test.txt", "w")
myfile.write("My first file written from Python\n")
myfile.write("---------------------------------\n")
myfile.write("Hello, world!\n")
myfile.close()
```

<subdown>

### Using with
- We always have to open and close file
  - Very annoying!
  - We may forget
- We don't have to worry about this if we use the with transaction


```python
with open("somefile.txt", 'w') as f:
    content = f.read()
    # Do something with content
    # Once done you don't need to worry about closing

f # You will get an error here. The variable f is only used within that scope
```

<next>

## Modules

- A module is a file containing python code and is intended for use in other python programs.
- We have used libraries such as turtle, random, string, ...etc

<subdown>

- We import modules by using the `import` statement
  - `import turtle` imports everything from turtle
  - `from random import randint` imports only one thing

<next>

## Questions ?