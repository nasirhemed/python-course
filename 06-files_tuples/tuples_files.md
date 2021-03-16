---
title: Tuples and Files
separator: <next>
verticalSeparator: <subdown>
theme: solarized
progress: true
revealOptions:
    transition: 'fade'
---

## Intro to Python 
### Tuples and Files
#### Nasir Hemed
<next>

## Agenda

<next> 

## Tuples

<next>

## What are tuples

Tuples are very similar to lists. They allow use to grop data:

```python
>>> paris = ("Paris Hilton", 1981)
>>> john = ("John", "Wick", 1964, "John Wick 4", 2022, "Actor", "Belarus")
```

<subdown>

Tuples are useful for representing "records"

Information related to each other

```python

>>> paris = ("Paris Hilton", 1981) # Name, DOB
>>> 
>>> #        fname, lname, dob, movie, release, role, birthplace
>>> john = ("John", "Wick", 1964, "John Wick 4", 2022, "Actor", "Belarus")
```

<subdown>

Tuples are like lists. We can index, slice, ... etc.
```python
>>> john = ("John", "Wick", 1964, "John Wick 4", 2022, "Actor", "Belarus")
>>> len(john)
7
>>> john[0]
"John"
>>> john[0:3]
("John", "Wick", 1964)
>>> for val in john:
    print(val)
"John"
"Wick"
1964
"John Wick 4"
2022
"Actor"
"Belarus"
```

<subdown>

Tuples are not like lists however. They are immutable
```python
>>> john[0] = "Bohn"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

<next>

Tuples are very powerful because they allow us to define multiple variables for a single record:

```python
>>> john = ("John", "Wick", 1964, "John Wick 4", 2022, "Actor", "Belarus")
>>> (name, surname, b_year, movie, m_year, profession, b_place) = john
```

<subdown>

In tuple unpacking, the values on the right are 'unpacked' into variables on the right:

```python
>>> b = ("Bob", 19, "CS")
>>> (name, age, studies) = b    # tuple unpacking
>>> name
'Bob'
>>> age
19
>>> studies
'CS'
```

<subdown>

If we don't have enough variables that support the length of the tuple, then the last variable is a tuple containing the rest:

```python
>>> b = ("Bob", 19, "CS")
>>> (name, rest) = b    # tuple unpacking
>>> name
'Bob'
>>> rest
(19, "CS")
```

<next>

## Tuples as return values

Note that functions return only one value. What if we want to return multiple values ? We can use tuples!

```python
def f(r):
		""" Return (circumference, area) of a circle of radius r """
    c = 2 * math.pi * r
    a = math.pi * r * r
    return (c, a)
```

<next>

# Files

<next>

## Types of Storage

<subdown>

- Cache
  - Super duper fast
  - Very small memory
    - 800Kb, 3Mb, 8Mb  
  - Mostly handled by OS

<subdown>

- RAM
  - Super fast
  - Big but not thaat big memory
    - 8GB, 16GB, 32GB
  - Not permanent

<subdown>

- Disk/Main Storage
  - Very biiig memory
    - 256GB, 500GB, 1TB
  - Very Slow
  - Permanent Storage

<next>

## About Files
- Working with files is like working with books
  - You open the book
  - Read/Write in it
  - Close the book when you are done

<subdown>

- The same happens with files
  - Open the file
  - Read/Write in it
  - Close the file when you are done

<next>


How do we write to files: Here's an example:

```python
myfile = open("test.txt", "w")
myfile.write("My first file written from Python\n")
myfile.write("---------------------------------\n")
myfile.write("Hello, world!\n")
myfile.close()
```

<subdown>

### Open

- `open` function 
  - First argument is the name of the file
  - Second argument is used to specify if you want to read or write
    - `'w'` vs `'r'` vs `'a'`

<subdown>

- `close` function
  - Once we are done we close the file 

<next>

## Appending Files

- If a file already exists
  -  We can open the file with `open(file, 'a')`
  -  We can add new lines at the end of the file.

```python
myfile = open("test.txt", "w")
myfile.write("My first file written from Python\n")
myfile.write("---------------------------------\n")
myfile.write("Hello, world!\n")
myfile.close()

# ^ Previous code
oldfile = open("test.txt", "a")
oldfile.write("I am adding more lines to this file\n")
oldfile.close()
```

<next>

## Reading a file

How do we read from files: Here's an example using a while loop:

```python
mynewhandle = open("test.txt", "r")
while True:                            # Keep reading forever
    theline = mynewhandle.readline()   # Try to read next line
    if len(theline) == 0:              # If there are no more lines
        break                          #     leave the loop

    # Now process the line we've just read
    print(theline, end="")

mynewhandle.close()
```
<subdown> 

We can also use a for loop

```python
mynewhandle = open("test.txt", "r")
for line in mynewhandle:
	print(line)

mynewhandle.close()
```

<next>

## Turning a file into a list of lines

Sometimes, we may want to read everything from the file and turn it into a list of lines. 
- For example
  - Reorder lines
  - Sort them.
  - Change the nth line

<subdown>

So we can do this by calling `f.readlines()`

```python
f = open("friends.txt", "r")
xs = f.readlines()
f.close()

xs.sort()

g = open("sortedfriends.txt", "w")
for v in xs:
    g.write(v)
g.close()
```

<next>

## Reading all of the file as a string

What we can also do is we can read all the lines and store it inside a string

```python
f = open("somefile.txt")
content = f.read()
f.close()

words = content.split()
print("There are {0} words in the file.".format(len(words)))

```


<next>

## Files as a transaction

- We always have to open and close file
  - Very annoying!
  - We may forget
- We don't have to worry about this if we use the `with` transaction

```python
with open("somefile.txt", 'w') as f:
	content = f.read()
	# Do something with content
	# Once done you don't need to worry about closing

f # You will get an error here. The variable f is only used within that scope
```

<next>

## Questions ?