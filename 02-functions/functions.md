---
title: Data Types, Functions and Booleans
separator: ---
verticalSeparator: --
theme: solarized
progress: true
revealOptions:
    transition: 'fade'
---
## Intro to Python 
### Data Types, Functions and Booleans
#### Nasir Hemed
---

## Agenda

- [Course Updates](#/2)
- [Data Types](#/3)
- [Functions](#/9)
- [Booleans and Conditionals](#/17)

--- 

## Course Updates
- [Google Classroom](#)
- Syllabus and Marking updated
- Assignment to be released next week

---

## Data Types
---

### Values and Data Types

`type(...)` function tells you what type of data it is in python
- `type(3)`
- `type(3.2)`
- `type("string")`

--

### Values and Data Types

What will be the outcome of the following: 

- `type("17")`
  - Is this an integer, float or string?

---

### Type Converter Functions

There may be times where we need to convert data from one type to another
- Taking a number from user
- Rounding up number to be integer


--
Here's an example: 


```python
a = "18" # This seems to be an int but it is a string

print("The type of a is ", type(a))

# Can we convert a to be integer
```


--

Each data type has its own function that you can convert:

```python
>>> int("18") # Converts to integer
18
>>> int("3.14") # Converts to decimal
3
>>> int("60 million") 
Traceback (most recent call last):
File "<interactive input>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '60 million'
```

```python
>>> float(17)
17.0
>>> float("123.45")
123.45
```

```python
>>> str(17)
'17'
>>> str(123.45)
'123.45'
```

---

### Operation on Strings

Why do we need to convert "123" to int ?

```python
message = "This is a message"
message + 123 # Error
message * 345 # Error
message / 90 # Error
"90" + 20 # Error: Notice that "90" is a string
```

--

### String Operations
Strings do have operations + and * but they are not math related
```python
message1 = "This is a message."
message2 = " This is another message"
# Adding the above two will concatenate the strings
message3 = message1 + message2 
five_a = "a" * 5 # Result is "aaaaa"
```

---
### Input Function

Whenever we write programs, we will try to get input from user.
- Logging in an application
- Playing games
- Calculator

--

In python, we can take user input by using the `input` function

```python
name = input("What is your name?")
print("Hi ", name)
print("The type of name is ", type(name))
```

The type of `name` is `str`. Which means if we take input for calculation, we have to convert it to its type

---

### Putting Everyhing Together

--
Here's a program that calculates the area of a square

```python
# This program calculates the area of a square
# Area of a square = side * side
side = input("What is the length of the side: ")
# Convert the side into a number. 
side = float(side)
area = side * side
print("The area of the square is ", area)
```

---

## Functions

---

### What are functions ?
- Function is a sequence of expressions in a block.
- It takes in input and returns/does something for you
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
- All the expressions in the function are indented
--

### Back to Turtles!

--

### Creating Rectangles

```python
def draw_rectangle(t, w, h):
	"""
	Make a turtle t draw a rectangle of size sz
	
	Arguments:
	t: This is the turtle that you created (t = turtle.Turtle())
	w: This is the width of the rectangle you want to draw
	h: This is the height of the rectangle you want to draw
	"""
	for i in range(2):
		t.forward(w)
		t.left(90)
		t.forward(h)
		t.left(90)
```

---

### Functions calling other functions

Let's create a function that draws a square
- A square is a rectangle
  - width is equal to height

```python
def draw_square(t, sz):
    """
	Make a turtle t draw a rectangle of size sz
	
	Arguments:
	t: This is the turtle that you created (t = turtle.Turtle())
	sz: This is the size of the rectangle you want to draw
	"""
	# A square is just a rectangle with height = width
	draw_rectangle(t, sz, sz) 
```

---

### Flow of Execution

It is important to define your functions before calling them!

```python
# This will fail because you called it before defining
draw_rectangle(t, 30, 40)

def draw_rectangle(t, w, h):
	... # Code omitted
```

---

### Arguments in Functions
Most functions require arguments to generalize things.

In math, we define $f$ as $f(x)$ = "something with $x$"

- $f(x) = x^2$
- $f(x) = x + 3$
- $f(x) = 3$
    - $x$ doesn't really do much here

--

### Python Functions
```python
>>> abs(5)
5
>>> abs(-5)
5
```
```python
>>> pow(2, 3)
8
>>> pow(6, 2)
36
```
```python
>>> max(3,4,1023)
1023
>>> max(3, 5, 1023 * 0)
5
```

We're getting a value when we call these functions

---

### Return Statement

`draw_rectangle` we didn't give any "value" back

- It did something for us 
  - But we did not store any value

--

Whereas functions like `abs` give us a value
```python
n = abs(-3) # n is equal to -3
a = input("Write something and I will store it to a: ")
```

--

`return` allows us to "give back" that value

```python
def square(x):
	return x * x # return expression

def calculate_tax(price):
	final_price = price * 1.13
	return final_price

a = square(2) # a will become 4
new_price = calculate_tax(100) # new_price will be 113
```

--
### Return vs Print
- `return` is very different from `print`.
- `print` just displays something on the screen
- `return` will actually give back something

```python
def print_square(x):
    print(x * x) 
    # Nothing will be returned
```

---

### Local Variables

Variables defined inside a function are only accessible in that function!

```python
def calculate_tax(price):
    final_price = price * 1.13
    return final_price

print(final_price) # This will fail!
```

---

## Back to Turtles!

--
Initialization functions

```python
def make_window(colr, ttle):
    """
    Set up the window with background color and title.
    Returns the new window.
    """
    w = turtle.Screen()
    w.bgcolor(colr)
    w.title(ttle)
    return w

def make_turtle(colr, sz):
    """
      Set up a turtle with the given color and pensize.
      Returns the new turtle.
    """
    t = turtle.Turtle()
    t.color(colr)
    t.pensize(sz)
    return t

wn = make_window("lightgreen", "Tess and Alex dancing")
tess = make_turtle("hotpink", 5)
alex = make_turtle("black", 1)
dave = make_turtle("yellow", 2)
```

---

## Booleans and Conditionals

---

### Boolean Values and Expressions
We have another datatype. `True` and `False`

These are called Booleans (or bool in python)

```python
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>

```

--

They are usually used in expressions to see if something is True of False

```python
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

--

Operators for boolean expressions


```python
x == y               # Produce True if ... x is equal to y
x != y               # ... x is not equal to y
x > y                # ... x is greater than y
x < y                # ... x is less than y
x >= y               # ... x is greater than or equal to y
x <= y               # ... x is less than or equal to y
```

Booleans can also be assigned

```python 
>>> a = 5 > 2
>>> a
True
```
---
### Logical Operators

Sometimes, we need a complicated logic. For Example 

- $f(x) = x^2$
  - Find x that is bigger than 0 <b style="color: coral;">**and**</b> $f(x) = 4$
    - Does $x = -2$ work ? 
    - How about $x = 2$ ?

--

### Logical Operators

**and** / **or**

<style>
.container{
    display: flex;
}
.col{
    flex: 1;
}


.col table td {
    text-align: center;
}
</style>

<div class="container">

<div class="col">
 <table border="1" class="docutils">
<colgroup>
<col width="20%">
<col width="20%">
<col width="60%">
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">a</th>
<th class="head">b</th>
<th class="head">a and b</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td>F</td>
<td>F</td>
<td>F</td>
</tr>
<tr class="row-odd"><td>F</td>
<td>T</td>
<td>F</td>
</tr>
<tr class="row-even"><td>T</td>
<td>F</td>
<td>F</td>
</tr>
<tr class="row-odd"><td>T</td>
<td>T</td>
<td>T</td>
</tr>
</tbody>
</table>

<section>
  <pre><code class="language-python hljs" data-trim data-noescape>
    >>> False and False
    False
    >>> False and True
    False
    >>> True and False
    False
    >>> True and True
    True
  </code></pre>
</section>
</div>

<div class="col">
<table border="1" class="docutils">
<colgroup>
<col width="20%">
<col width="20%">
<col width="60%">
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">a</th>
<th class="head">b</th>
<th class="head">a or b</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td>F</td>
<td>F</td>
<td>F</td>
</tr>
<tr class="row-odd"><td>F</td>
<td>T</td>
<td>T</td>
</tr>
<tr class="row-even"><td>T</td>
<td>F</td>
<td>T</td>
</tr>
<tr class="row-odd"><td>T</td>
<td>T</td>
<td>T</td>
</tr>
</tbody>
</table>

<section>
  <pre><code class="language-python hljs" data-trim data-noescape>
    >>> False or False
    False
    >>> False or True
    True
    >>> True or False
    True
    >>> True or True
    True
  </code></pre>
</section>
</div>

</div>

--

### Logical Operators

**not**

<style>
.container{
    display: flex;
}
.col{
    flex: 1;
}
</style>

<div class="container">

<div class="col">
<table border="1" class="docutils">
<colgroup>
<col width="33%">
<col width="67%">
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">a</th>
<th class="head">not a</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td>F</td>
<td>T</td>
</tr>
<tr class="row-odd"><td>T</td>
<td>F</td>
</tr>
</tbody>
</table>

</div>
<section>
  <pre><code class="language-python hljs" data-trim data-noescape>
    >>> False or False
    False
    >>> False or True
    True
    >>> True or False
    True
    >>> True or True
    True
  </code></pre>
</section>


</div>

```python
>>> not True
False
>>> not False
True
```

---
### Conditional Execution

So now we come to the purpose of logic

```python
if boolean_expression:
    # Code will be executed only if the statement is True
	do something 
	...
else:
    # If the statement is not True, then we will execute here
	do the other thing 



### Example

if 3 > 2:
	print("I am in if case")
else:
	print("I am in else case")

if 3 < 2:
	print("I am in if case")
else:
	print("I am in else case")

```

--
### Chained Conditionals
If you have multiple conditions

- `if something`
- `elif something_else` (else if something_else)
- `elif ...`
- `else`
```python
if x < y:
	# Do something
elif x > y:
	# Do something
else:
	# Do something
```

--

### Examples


```python
def divide(a, b):
	if b != 0:
		return a / b
	else:
		print("ERROR: YOU CANNOT DIVIDE BY 0!")

def calculate_tax(price):
	if price < 0:
		print("Error: Price cannot be negative")
	else:
		final_price = price * 1.13
		return final_price
```

---

### Return within condition
Whenever you reach a return statement, you will exit the function

```python
def function(x):
	return x * x
	x = 4 # This will not be executed 
	return x # This will not be executed
```

--

Avoiding else by using return
```python
def function(x):
	if x == 0: # We cannot accept x to be zero
		print("x cannot be zero")
		return 
	# From here on, we know that x can never be 0
	return 1 / x
```

---

## Questions ?