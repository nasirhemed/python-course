---
title: Modules
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

# Modules

<next>

## What are modules ?

- A module is a file containing python code and is intended for use in other python programs. 
- We have used libraries such as turtle, random, string and even in your assignment!

<next>

### Random Numbers

We often want to use random numbers in programs. Examples

- Flip a coin
- Roll a dice
- Shuffle cards
- To simulate a new world (minecraft)
- Encryption/Decryption

Most libraries provide a module to deal with randomness. In python, we use the `random` module

<subdown>

```python
import random

# Create a black box object that generates random numbers
rng = random.Random()

dice_throw = rng.randrange(1,7)   # Return an int, one of 1,2,3,4,5,6
delay_in_seconds = rng.random() * 5.0
```

`randrange` method generates an integer between its lower and upper bounds

The `random` method returns a floating value between 0 and 1. In other words, the value for x is s.t  $0 \le x < 1$

<subdown>

We can also `shuffle` a list. This can be used to shuffle items such as cards, ... , etc.

```python
import random
lst = [1,2,3,4,5,6]
random.shuffle(lst)
```

<subdown>

#### Testing Randomness

- Using random makes it hard to test
- Sometimes we want to make sure that our programs work
- Use `seed` in random

### Examples

<subdown>

Simulating throwing a die n times

```python
import random
def throw_die(num):
	rng = random.Random()
	result = []
	for i in range(num):
		result.append(rng.randrange(1, 7))

	return result
```

<subdown>

Simulating shuffling a deck of cards

```python
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'reverse', '+4', '+2', 'stop']
rng = rng.Random()
rng.shuffle(cards)
cards
```

<subdown>

Choose a random card

```python
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'reverse', '+4', '+2', 'stop']
rng = rng.Random()
card = rng.choice(cards)
card
```

<next>

### Time Module

- We want fast and efficient programs
- But how do we know a program is fast ?
  - We time how long it takes to run!
  - One way of doing this is using the `time` module

<subdown>

The `time` module has a function called `time()` that returns the current time in seconds. 

So the idea here is:

```python
start = time.time()
# Run your function
end = time.time()
time_take = end - start
```
<subdown>


### Example:

```python
import time

def do_my_sum(xs):
    sum = 0
    for v in xs:
        sum += v
    return sum

sz = 10000000        # Lets have 10 million elements in the list
testdata = range(sz)

t0 = time.clock()
my_result = do_my_sum(testdata)
t1 = time.clock()
print("my_result    = {0} (time taken = {1:.4f} seconds)"
        .format(my_result, t1-t0))

t2 = time.clock()
their_result = sum(testdata)
t3 = time.clock()
print("their_result = {0} (time taken = {1:.4f} seconds)"
        .format(their_result, t3-t2))
```
<next>

### Other modules

There are a ton of other modules we can play with. Each has their own purpose. Some examples include:

- math
- request
- sys
- turtle

<next> 

### Creating your own modules

- How do we create our own modules ?
- Sometimes we have multiple files of code
  - How do we use code from another file ?

All we need to do to create our own modules is to save our file with a `.py` extension.

<subdown>

For example, if we have a file called `[seqtools.py](http://seqtools.py)` and we have a function:

```python
def remove_at(pos, seq):
    return seq[:pos] + seq[pos+1:]
```

<subdown>

We can use this by importing

```python
>>> import seqtools
>>> s = "A string!"
>>> seqtools.remove_at(4, s)
'A sting!'
```

<next>

### Ways of importing files

There are three different ways of importing files

<subdown>

#### Just use `import`

```python
import math
x = math.sqrt(10)
```

Here, we import the entire math module. Sometimes, all we need is just one function not all the functions. For this, we can use the second method

<subdown>

#### `from ... import ...`

```python
from math import sqrt   # Import all the identifiers from math,
                     #   adding them to the current namespace.
x = sqrt(10)         # Use them without qualification.
```

<subdown>

#### `import ... as ...`

Sometimes, we can import a module under a different name. For example if the module name is too long, we can use this

```python
import math as m
x = m.sqrt(10)
```

<next>

## Questions ?