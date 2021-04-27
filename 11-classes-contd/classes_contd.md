---
title: OOP Continued
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

### Object Oriented Programming 

- Last time, we had a small intro to classes 
- Today, we will pick up on what we left last time and continue 

<next>

### Rectangles

- Recall our `Point` class we discussed 
- Let's say we wanted to create a rectangle located somewhere at `(x, y)`
	- There are many ways of representing a Rectangle 
	- We will use corner and size to represent the rectangle

<subdown>

### Rectangle Class 

```python
class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return  "({0}, {1}, {2})"
                  .format(self.corner, self.width, self.height)
```
<subdown>

### Examples

```python
>>> box = Rectangle(Point(0, 0), 100, 200)
>>> bomb = Rectangle(Point(100, 80), 5, 10)    # In my video game
>>> print(box)
box: ((0, 0), 100, 200)
>>> print(bomb)
bomb: ((100, 80), 5, 10)
```

<next>

### Objects are Mutable

- We can change the state of an object by making an assignment to one of its attributes

```python
box.width += 50
box.height += 100
```
<subdown>

- But it's usually better to provide a method to do this

```python
class Rectangle:
    # ...

    def grow(self, delta_width, delta_height):
        """ Grow (or shrink) this object by the deltas """
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        """ Move this object by the deltas """
        self.corner.x += dx
        self.corner.y += dy
```

<subdown>

```python
>>> r = Rectangle(Point(10,5), 100, 50)
>>> print(r)
((10, 5), 100, 50)
>>> r.grow(25, -10)
>>> print(r)
((10, 5), 125, 40)
>>> r.move(-10, 10)
print(r)
((0, 15), 125, 40)
```
<next>

### Sameness 
- Since objects are mutable, what will happen if I do this ?

```python
>>> a = Point(3, 4)
>>> b = a 
>>> a.x = 20
>>> b.x 
# What will be the output
```

<subdown>

- Another way to think of this is for example if we say Bob and Alice have the same car 
	- Then it means they have the same make, same model 
	- But they are two cars so they are different cars 

<subdown>

- `is` allows us to check if two objects refer to one `reference`

```python
>>> p1 = Point(3, 4)
>>> p2 = Point(3, 4)
>>> p1 is p2 
False
>>> p3 = p1 
>>> p1 is p3
True
```

<next>

## Class Composition 
- Sometimes we create multiple classes that we will end up using together 
- Consider a Blackjack Game 
	- Each card has a suit and a rank 
	- There is a deck of cards that we can shuffle, and distribute

<subdown>

### Card Object 

- Let's go over the cards used in a blackjack game
	- 52 Cards
		- 4 suits 
			- 13 ranks

<subdown>

```
### Ranks ###
Spades   -->  3
Hearts   -->  2
Diamonds -->  1
Clubs    -->  0
```

```
### Cards ###
Numeric --> 1 - 10
Jack --> 11
Queen --> 12
King --> 13
```

<subdown>

- Thus, we have the following class for `Card`

```python
class Card:
    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank
```

<next>

### Attributes and Representation

- Now we need to represent a card. 
- We can use lists/dictionary for this

```python
class Card:
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return (self.ranks[self.rank] + " of " + self.suits[self.suit])
```

<subdown>

### Examples 

```python
>>> card1 = Card(1, 11)
>>> print(card1)
Jack of Diamonds
...
>>> card2 = Card(1, 3)
>>> print(card2)
3 of Diamonds
>>> print(card2.suits[1])
Diamonds
```

<next>
### Comparing Cards 
- Each card has a value now
	- So we need to compare the cards

```python
def cmp(self, other):
    # Check the suits
    if self.suit > other.suit: return 1
    if self.suit < other.suit: return -1
    # Suits are the same... check ranks
    if self.rank > other.rank: return 1
    if self.rank < other.rank: return -1
    # Ranks are the same... it's a tie
    return 0
```

<subdown>

- Now let us use `cmp` to define `<`, `>`, `==`, ... for the card class 

```python
def __eq__(self, other):
    return self.cmp(other) == 0

def __le__(self, other):
    return self.cmp(other) <= 0

def __ge__(self, other):
    return self.cmp(other) >= 0

def __gt__(self, other):
    return self.cmp(other) > 0

def __lt__(self, other):
    return self.cmp(other) < 0

def __ne__(self, other):
    return self.cmp(other) != 0
```

<subdown>

### Examples 

```python
>>> card1 = Card(1, 11)
>>> card2 = Card(1, 3)
>>> card3 = Card(1, 11)
>>> card1 < card2
False
>>> card1 == card3
True
```

<next>

### Deck of Cards 

- Now that we have a card, we have to put them together 
- We usually put them in a Deck

```python
class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))
```

<subdown>

### Printing a deck

- We may want to print the deck
- But this is a list of cards 

```python 
class Deck:
    ...
    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + str(self.cards[i]) + "\n"
        return s
```

<<subdown>

### Shuffling the Deck 

- When we play with cards, we usually shuffle the cards
- Let's implement shuffling 

```python 
class Deck:
    ...
    def shuffle(self):
        import random
        random.shuffle(self.cards)
```

<subdown>

### Dealing Cards 
- Of course, once there are player, we distribute the cards
- Let's implement dealing cards 

```python
class Deck:
    ...
    def deal(self):
		return self.cards.pop() 
```

<subdown>

### Checking for Empty 

- Will dealing cards always work ?
- What if the deck is empty ?
- We need to check if there are cards left 

```python
class Deck:
    ...
    def is_empty(self):
		return self.cards == [] 
```

<next> 

## Questions ?
