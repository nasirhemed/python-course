---
title: Course Review
separator: <next>
verticalSeparator: <subdown>
theme: solarized
progress: true
revealOptions:
    transition: 'fade'
---

## Intro to Python 
### Course Review
#### Nasir Hemed

<next>

## Review Session

- So we're almost done with the course!
- We will be reviewing the concepts we learned earlier
- Next steps and advancing further
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

<subdown>

<section>
<iframe src="https://froggi.es/mario/" style="position:fixed; top:0; left:0; bottom:0; right:0; width:100%; height:100%; border:none; margin:0; padding:0; overflow:hidden; z-index:999999;" >

<next>

## Data Types

- There are different types of data
    - `float`, `int`, `bool`, `str`
    - Each serve their different purpose

<subdown>

### Data Types Examples

```python
>>> "This is a string"
"This is a string"
>>> 0.0123 + 0.123
0.0253
>>> 4 + 5
9
>>> True and False
False
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

### Object Oriented Programming

- The focus of object-oriented programming is on creation of objects.
  - They contain both the data and functionality together
- Example of objects:
  - Turtle, string, List, ..., etc.

<subdown>

### User-Defined Data Types

- We can define our own objects/structures using classes
    - `class` allows us to define our own objects
    - We need to have an initializer
    - We can have attributes and methods within a class

<subdown>

### Class Example

```python
class Point:
  """ Point class represents and manipulates x, y coords. """


  def __init__(self):
    """Create a new point at the origin """

    self.x = 0
    self.y = 0

  def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

```

<subdown>

### Converting an instance to string

- Usually, we don't have a separate function to print a specific object 
	- For example, we just call
		- print(lst) for list
		- print(dict) for dictionary
- Right now, we defined a function `print_point` to just print a point 
- What happens when we call `print(pt)` ? 

<subdown>

- To fix this, we need to define a `__str__` method
	- When python sees this method to be defined, it will call this function instead

```python 
    class Point:
        # ...

        def __str__(self):    # All we have done is renamed the method
            return "({0}, {1})".format(self.x, self.y)
```

```python 
>>> p = Point(3, 4)
>>> print(p)
(3, 4)
```
<next>

## Class Composition 
- Sometimes we create multiple classes that we will end up using together 
- Consider a Blackjack Game 
	- Each card has a suit and a rank 
	- There is a deck of cards that we can shuffle, and distribute

<subdown>

### Anothe Example: Twitter

- We can have a class for each user
- Each user can post,like,retweet other tweets
- A user has followers (other users following them)
- A user can follow people

*We'll be doing an exercise on this ^*

<next>

### Inheritance

- One of the most common concepts in OOP is inheritance 
- Inheritance is the ability to define a new class that is a modified version of a class 
- The relationship is usually denoted as parent-child relationship 

<subdown>

### Example of Inheritance

- Let's say there was a class for Animal
  - Animal can sleep and make noises
- Let's say we now have a Dog and a Cat
  - They are both animals. They can sleep and make noise

<subdown>


```python
class Animal:
  def __init__(self):
    self.heart = 4

  def sleep(self):
    print("Sleeping: ZZZZZZ")

  def make_noise(self):
    print("animal is making noises")
```

```python
class Dog(Animal):
  def make_noise(self):
    print("Whoof Whoof")

class Cat(Animal):
  def make_noise(self):
    print("Meow Meow")
```

<next>

## Game Development

- The structure of games usually have a pattern
  - Poll for user input (pressing buttons/keyboard)
  - Process it (Move character)
  - Update the display 
  - Show it to the user 
  
<img data-src="https://gameprogrammingpatterns.com/images/game-loop-simple.png">


<subdown>

## Example of a blank game

```python
import pygame

def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surface_sz = 480   # Desired physical surface size, in pixels.

    # Create surface of (width, height), and its window.
    main_surface = pygame.display.set_mode((surface_sz, surface_sz))

    # Set up some data to describe a small rectangle and its color
    small_rect = (300, 200, 150, 90)
    some_color = (255, 0, 0)        # A color is a mix of (Red, Green, Blue)

    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop

        # Update your game objects and data structures here...

        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        main_surface.fill((0, 200, 255))

        # Overpaint a smaller rectangle on the main surface
        main_surface.fill(some_color, small_rect)

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()

    pygame.quit()     # Once we leave the loop, close the window.

main()
```

<subdown>

<iframe src="https://flappybird.io/" style="position:fixed; top:0; left:0; bottom:0; right:0; width:100%; height:100%; border:none; margin:0; padding:0; overflow:hidden; z-index:999999;" >

<next>

### Asynchronous vs Synchronous

- We talked about the types of functions in python
    - Synchronous worker have to complete entire job then proceed
    - Asynchronous worker can do other things while waiting
- Asynchronous is mostly used in web/file related works

<subdown>

### Example

```python
def synchronous_job(task):
    task.do_task_1()
    task.do_task_2()
    task.do_task_3()

    task.done = True
    return


async def asynchronous_job(task):
    await task.do_task_1()
    await task.do_task_2()
    await task.do_task_3()

    task.done = True
    return
```

<next>

### Decorators

- Decorators are design patterns that allow a user to add functionality to a function
- They are referred with the `@` symbol

```python
@discord.bot(name='ping')
async def ping(ctx):
    await ctx.send("pong")

```

<subdown>

### Example

```python
def my_decorator(func):
    def wrapper():
        print("I am about to call the function")
        func()
        print("I just called the function!")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

say_whee()
```
<next>

## Questions ?