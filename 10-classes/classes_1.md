---
title: OOP Intro
separator: <next>
verticalSeparator: <subdown>
theme: solarized
progress: true
revealOptions:
    transition: 'fade'
---

## Intro to Python 
### Object Oriented Programming
#### Nasir Hemed
<next>

### What is Object Oriented Programming ?
- Up to now, we have been using discussing about data structures
  - We discussed about lists, strings, tuples, dictionary, ... , etc.
- But what if we now want to create our own type of structure ?
  - This is where Object Oriented Programming comes in handy!

<subdown>

- The focus of object-oriented programming is on creation of objects.
  - They contain both the data and functionality together
- Example of objects:
  - Turtle, string, List, ..., etc.

<next>

## User-Defined data types

- Let us create a new type of data.
  - We would like to create a Point object that will tell us the location in 2D
  - A point consists of two numbers that are treated as a single object.
  - For example: (0, 0), (5, 0), (x, y)

<subdown>

- We would also like to do some of the following things in a Point
  - Calculate distance from the origin
  - Calculate distance between two points
  - Finding the midpoint between two points
  - And other point related stuff

<subdown>

- We use Classes to define objects in Python

```python
class Point:
  """ Point class represents and manipulates x, y coords. """


  def __init__(self):
    """Create a new point at the origin """

    self.x = 0
    self.y = 0

```

<subdown>

- Every class has an **initializer** method called `__init__`.
  - This is something that will be automatically called whenever a new object is defined
  - The `self` parameter is set to refer to the object itself

<subdown>

- So no we can define a point and access its x and y coordinates

```python 

p = Point()
q = Point()

print(p.x, p.y, q.x, q.y)
```

- The above is familiar to how we used to define Turtle

```python
from turtle import Turtle

tess = Turtle()
alex = Turtle()
```

<next>

## Attributes

- If we think about objects, they usually have attributes and methods
	- For example, our point has two atttributes
		- x and y 
- We can access attributes using dot notation

```python 
>>> p.x = 3
>>> p.y = 5
>>> p.x
3
>>> p.y
5
```

<subdown>

- In other words, `p.x` basically means
	- "Go to the object `p` and get the value of x"
	- If the attribute "x" does not exist, we get an error

<next>

## Custom Initializer

- When we define points, they don't always belong in the origin
	- For example, if we want to have (5, 7), the way to currently do this is

```python
p = Point()
p.x = 5
p.y = 7
```

<subdown>

- We can improve our initializer function

```python 
class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

# Other statements outside the class continue below here.
```
- And now we have:

```python 
>>> p = Point(4, 2)
>>> q = Point(6, 3)
>>> r = Point()       # r represents the origin (0, 0)
>>> print(p.x, q.y, r.x)
4 3 0
```

<next>

## Methods 
- Now let's add some functionality of the points 
	- Let's say we want to calculate distance from the origin 
	- This is where methods come in handy

- A **method** behaves like a function but is only for a specific instance
	- For example, `tess.right(90)` in turtle
	- They are accessed with a dot notation

<subdown>

- Let's add a method to calculate distance from origin
```python 
class Point:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
```

<subdown>

- Let's try using the method 

```python 
>>> p = Point(3, 4)
>>> p.x
3
>>> p.y
4
>>> p.distance_from_origin()
5.0
>>> q = Point(5, 12)
>>> q.x
5
>>> q.y
12
>>> q.distance_from_origin()
13.0
```

<next>

## Instances as arguments and parameters 

- If we use our normal functions, then we can still pass our defined objects as parameters and play with them

```python 
def print_point(pt):
	print("({}, {})".format(pt.x, pt.y))
```


```python 
>>> p = Point(3, 4)
>>> print_point(p)
(3, 4)
```

<next>

## Converting an instance to a string 

- Usually, we don't have a separate function to print a specific object 
	- For example, we just call
		- print(lst) for list
		- print(dict) for dictionary
- Right now, we defined a function `print_point` to just print a point 
- What happens when we call `print(pt)` ? 

```python 
>>> p = Point(3, 4)
>>> print(p)
'<__main__.Point object at 0x01F9AA10>'
```

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

## Returning instance values 

- Let's say we want to calculate the midpoint 
	- Let's do it using functions

```python 
def midpoint(p1, p2):
    """ Return the midpoint of points p1 and p2 """
    mx = (p1.x + p2.x)/2
    my = (p1.y + p2.y)/2
    return Point(mx, my)	
```
- The function creates and returns a new `Point` object 

```python 
>>> p = Point(3, 4)
>>> q = Point(5, 12)
>>> r = midpoint(p, q)
>>> r
(4.0, 8.0)
```

<subdown>

- We can also do this using methods with classes 



```python 
class Point:
   # ...

   def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)
```
- So now we can use it like this 


```python 
>>> p = Point(3, 4)
>>> q = Point(5, 12)
>>> r = p.halfway(q)
>>> r
(4.0, 8.0)
```

<next>

## Questions ?
