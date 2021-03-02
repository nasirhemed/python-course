---
title: Loops
separator: <next>
verticalSeparator: <subdown>
theme: solarized
progress: true
revealOptions:
    transition: 'fade'
---

## Intro to Python 
### Strings
#### Nasir Hemed
<next>

## Agenda

<next> 

## Strings

<next>

### Strings

- Datatypes so far:
  - int
  - float
  - bool (boolean)
  - str (string)

- Strings are different from int, float and bool

- A string is a collection of characters

<next>

### String Operations

Remember that strings are not numbers!

But python uses `+` and `*` for a different purpose

<subdown>

```python
>>> "Hello" + " World" # Concatenation
"Hello World"
>>> "pew" * 3 # Concatenation 3 times
"pewpewpew"
```

`+` only works when both are str

`*` only works when one of them is `int`  

```python
>>> "Hello" + 3 # Error
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> "uh" * "oh!" # Error
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
```

<next>

### String methods

When we were playing around with turtle, we noticed that the turtle could do things:

```python
t = turtle.Turtle()
t.forward(100) # Move forward
t.right(100) # Turn right
```

<subdown>

In a similar manner, string has way we can do things about it:

```python
>>> ss = "Hello Word"
>>> tt = ss.upper()
>>> tt
"HELLO WORLD"
```

- `upper` is a method that converts the string into uppercase

- There are also other methods such as `lower`, `capitalize` , and so on...

<subdown>

Note that methods are different from functions!

```
ss = "Hello"
tt = ss.upper() # This is a method

print(tt) # This is a function.
```

- `ss.upper()` is like saying:
  - "ss, give me the upper case"

- But we cannot do `upper(ss)`

<subdown>

Listing all the methods:

```python
>>> ss = "Hello World"
>>> ss. # Press tab
ss.capitalize(    ss.isalpha(       ss.ljust(         ss.split(
ss.casefold(      ss.isascii(       ss.lower(         ss.splitlines(
ss.center(        ss.isdecimal(     ss.lstrip(        ss.startswith(
ss.count(         ss.isdigit(       ss.maketrans(     ss.strip(
ss.encode(        ss.isidentifier(  ss.partition(     ss.swapcase(
ss.endswith(      ss.islower(       ss.replace(       ss.title(
ss.expandtabs(    ss.isnumeric(     ss.rfind(         ss.translate(
ss.find(          ss.isprintable(   ss.rindex(        ss.upper(
ss.format(        ss.isspace(       ss.rjust(         ss.zfill(
ss.format_map(    ss.istitle(       ss.rpartition(    
ss.index(         ss.isupper(       ss.rsplit(        
ss.isalnum(       ss.join(          ss.rstrip(   
```

<next> 

### String as a collection

- Strings are just characters put together

```python
"ABCDE" 
# This is a list of characters 
# they are 'A', 'B', 'C', 'D'
```

<subdown>

- Sometimes we may want to analyze a letter.
  - We do this with indexing

```python
name = "Albert"
first_character = name[0]
print(first_character) # Will print 'A'
```

- Note that we start from 0! 
- Computers start counting from 0 onwards

<next> 

### Length

The `len` function, when applied to a string, calculates the number of characters in a string

```python
>>> fruit = "Banana"
>>> len(fruit)
6
>>> len("Water Melon")
11
```
<subdown>

Let's say we wanted to get the last charater of a string

```python
fruit = "Banana" 
sz = len(fruit) # sz will be 6
last = fruit[sz] # Will fruit[6] work ? 
# Hint: Computers start counting from 0
```

The 6th character is out of bounds so we will get an error

<subdown>

One trick in python to get the last character is `fruit[-1]`

```python
>>> fruit = "Banana" 
>>> fruit[-1]
'a'
```
<next>

### Slices

- Sometimes, we want to play with parts of the string. 
- For example the first 3 characters

```python
>>> s = "Bananas are nutritious"
>>> print(s[0:8])
'Bananas'
>>> print(s[9:14])
'are'
>>> print(s[15:25])
'nutritious'
```
<subdown>

Visualization of slices:

```python
fruit = "banana"
How python sees it:

			 +---+---+---+---+---+---+
	fruit -> | b | a | n | a | n | a |
			 +---+---+---+---+---+---+
			 0   1   2   3   4   5   6	
```

<subdown>

Omitting the numbers:

```python
fruit = "banana"
fruit[3:] # From index 3 till the end
'ana'
fruit[:3] # From the beginning up to 3rd character
"ban"
```

<next>

### String Comparison

We can use equality to check if two strings are the same

```python
>>> "banana" == "banana"
True
>>> " banana" == "banana"
False
```

<subdown> 

We can also compare using `<` and `>` and this will do a lexicographic comparison

```python
>>> "abcd" < "efgh"
True
>>> "abca" < "abcb"
True
```

<next>


### Loops

A lot of times, we may need to process one character at a time in a string. There are two ways to do this:

<subdown>

### While Loops

```python
ix = 0
while ix < len(fruit):
	letter = fruit[ix]
	print(letter)
	ix += 1
```

- This while loop will allow us to process each character at a time. 

- Loop condition is `ix < len(fruit)` so when ix becomes equal to the length of the string, the condition becomes False and we exit the loop.

<subdown>

### For Loops

```python
for letter in fruit:
	print(letter)
```

The above is exactly equivalent to our while loop we wrote. Pretty neat!

<subdown>

**Examples**

```python
prefixes = "JKLMNOPQ"
suffix = "ack"

for p in prefixes:
	print(p + suffix)
```
<next>

### Immutable
- Remember that strings are just a collection of characters.
- Can you change the second character to be something else?

```python
s = "Hello"
s[0] = "J" # This will give me an error
```

Unfortunately, you cannot

<next>

### `in` and `not in`

To check if a character or substring is in the text, we use `in` operator

```python
>>> "a" in "a"
True
>>> "apple" in "apple"
True
>>> "" in "a"
True
>>> "" in "apple"
True
```

<next>

### Format Strings

Sometimes, we want to have a format so that we can use the string multiple times

```txt
Automated message to send to all students:
"""
Hello FIRST LAST,
How are you ?
"""

Replace FIRST LAST with student names for every student

```

<subdown>

Python has multiple ways to use format strings. One of them is a format method:

```python
s1 = "His name is {0}!".format("Arthur")
print(s1)

name = "Alice"
age = 10
s2 = "I am {1} and I am {0} years old.".format(age, name)
print(s2)

n1 = 4
n2 = 5
s3 = "2**10 = {0} and {1} * {2} = {3:f}".format(2**10, n1, n2, n1 * n2)
print(s3)
```

<subdown>

#### Examples:

```python
letter = """
Dear {0} {1}.
 {0}, I have an interesting money-making proposition for you!
 If you deposit $10 million into my bank account, I can
 double your money ...
"""

print(letter.format("Paris", "Hilton"))
print(letter.format("Bill", "Gates"))
```

<next>

## Questions ?