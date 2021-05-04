---
title: Inheritance
separator: <next>
verticalSeparator: <subdown>
theme: solarized
progress: true
revealOptions:
    transition: 'fade'
---

## Intro to Python 
### Inheritance 
#### Nasir Hemed

<next>

## Inheritance 

- One of the most common concepts in OOP is inheritance 
- Inheritance is the ability to define a new class that is a modified version of a class 
- The relationship is usually denoted as parent-child relationship 

<subdown>

### Example of Inheritance 

- Let's say there was a class for Animal
  - Animal can sleep and make noises

```python
class Animal:
  def __init__(self):
    self.heart = 4

  def sleep(self):
    print("Sleeping: ZZZZZZ")

  def make_noise(self):
    print("animal is making noises")
```

<subdown>

### Example of Inheritance 
- Let's say we now have a Dog and a Cat
  - They are both animals. They can sleep and make noises 

```python
class Dog(Animal):
  def make_noise(self):
    print("Whoof Whoof")

class Cat(Animal):
  def make_noise(self):
    print("Meow Meow")
```

<subdown>

### Example of Inheritance

- So now if we define a cat and a dog, we get this:

```python
>>> a = Animal()
>>> c = Cat()
>>> d = Dog()
>>> a.make_noise()
"animal is making noises"
>>> d.make_noise()
"Whoof Whoof"
>>> c.make_noise()
"Meow Meow"
```

<next>
### Back to Cards 

- For any card game, we need to represent a hand of cards 
- A hand is kinda similar to a deck
- A hand is also different from a deck
  - We might need to compute whether we are winning
  - We might need to know what card we should play
- Thus, we will inheritance from Deck to make Hand class 

<subdown>

- A hand usually starts with empty cards
- We will use a name to indicate the name of the player

```python
class Hand(Deck):
  def __init__(self, name=""):
    self.cards = []
    self.name = name
```

<subdown>

- Unlike a Deck, we may need to add a card back to a Hand
  - We will have an `add` method 

```python
class Hand(Deck):
  ...
  def add(self, card):
    self.cards.append(card)
```

<next>

### Dealing Cards 
- Now that we have a Hand class, we want to deal cards from the `Deck` to the hands
  - Since this is usually what a Deck of cards do it makes sense to put it in the `Deck` class

```python
class Deck:
    ...
    def deal(self, hands, num_cards=999):
        num_hands = len(hands)
        for i in range(num_cards):
            if self.is_empty():
                break                    # Break if out of cards
            card = self.pop()            # Take the top card
            hand = hands[i % num_hands]  # Whose turn is next?
            hand.add(card)               # Add the card to the hand
```

<subdown>

- The first parameter is the hands (players) you will distribute the cards to
- The second parameter is the number of cards you will distribute in total 
  - Default is a big number because we will distribute all cards

<next>

### Printing a Hand

- Now let's say we want to print a Hand
- Luckily, the hand already inherits `__str__` from `Deck`

```python
>>> deck = Deck()
>>> deck.shuffle()
>>> hand = Hand("frank")
>>> deck.deal([hand], 5)
>>> print(hand)
2 of Spades
3 of Spades
4 of Spades
Ace of Hearts 
9 of Clubs
```


<next>

### Implementing Card Game 

- Now that we have a `Deck` and `Hand`, we can implement a game 
- Typically, before starting the game, you get a Deck of cards and shuffle them
  - So that is what we're gonna do

```python
class CardGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
```

- Now we can implement specific card game of our choice and add features
  - Blackjack, ..., etc. 

<next>

### Old Maid Game 

- Matching Game 
- Goal is to get rid of matching card from your hand 
  - Matching cards have same rank and colour
- Queen of Clubs removed so that Queen of Spades does not have a match 
- Players start trading cards when there is no more match
- Game ends when the last player only has one card left 

<next>

### Old Maid Hand 
- An Old Maid Hand requires some ability to find and remove matches 
- Everything else is the same as `Hand` however, so we can inherit from it 

```python
class OldMaidHand(Hand):
    def remove_matches(self):
        count = 0
        original_cards = self.cards[:]
        for card in original_cards:
            match = Card(3 - card.suit, card.rank)
            if match in self.cards:
                self.cards.remove(card)
                self.cards.remove(match)
                print("Hand {0}: {1} matches {2}"
                        .format(self.name, card, match))
                count += 1
        return count
```

<subdown>

### Example

```python
>>> game = CardGame()
>>> hand = OldMaidHand("frank")
>>> game.deck.deal([hand], 13)
>>> hand.remove_matches()
Hand frank: 7 of Spades matches 7 of Clubs
Hand frank: 8 of Spades matches 8 of Clubs
Hand frank: 10 of Diamonds matches 10 of Hearts
```

<next>

### Old Maid Game 

- Now we can focus on `OldMaidGame` class 
- We will inherit from `CardGame` class
- We will have a method `play` that starts this game 
  - It will remove Queen of Clubs
  - Deal the cards to the players 
  - Remove matches and start playing 

<subdown>

### Implementation

```python
class OldMaidGame(CardGame):
    def play(self, names):
        # Remove Queen of Clubs
        self.deck.remove(Card(0,12))

        # Make a hand for each player
        self.hands = []
        for name in names:
            self.hands.append(OldMaidHand(name))

        # Deal the cards
        self.deck.deal(self.hands)
        print("---------- Cards have been dealt")
        self.print_hands() # TODO: Implemented below

        # Remove initial matches
        matches = self.remove_all_matches() # TODO: Implemented below
        print("---------- Matches discarded, play begins")
        self.print_hands()

        # Play until all 50 cards are matched
        turn = 0
        num_hands = len(self.hands)
        while matches < 25:
            matches += self.play_one_turn(turn) # TODO: Implemented below
            turn = (turn + 1) % num_hands

        print("---------- Game is Over")
        self.print_hands()
```

<subdown>

### Removing matches 

```python
class OldMaidGame(CardGame):
    ...
    def remove_all_matches(self):
        count = 0
        for hand in self.hands:
            count += hand.remove_matches()
        return count
```

<subdown>

### Printing hands

```python
class OldMaidGame(CardGame):
    ...
    def print_hands(self):
        count = 0
        for hand in self.hands:
            print("=====")
            print("Hand {} contains".format(hand.name))
            print(hand)
            print("====")
```

<subdown>

### Player's turn to play 

- Idea is to find a neighbour and take a card from them
- Remove matches once you do that 


```python
class OldMaidGame(CardGame):
    ...
    def play_one_turn(self, i):
        if self.hands[i].is_empty():
            return 0
        neighbor = self.find_neighbor(i) # TODO: Implemented below
        picked_card = self.hands[neighbor].pop()
        self.hands[i].add(picked_card)
        print("Hand", self.hands[i].name, "picked", picked_card)
        count = self.hands[i].remove_matches()
        self.hands[i].shuffle()
        return count
```

<subdown>

### Picking a neighbor 

- The idea here is to find the player right next to you (to your left)
- Take a card from them if they have a card 

```python
class OldMaidGame(CardGame):
    ...
    def find_neighbor(self, i):
        num_hands = len(self.hands)
        for next in range(1,num_hands):
            neighbor = (i + next) % num_hands
            if not self.hands[neighbor].is_empty():
                return neighbor
        return None
```

<next>

### Final Product of Old Maid Game 

```python
>>> import cards
>>> game = cards.OldMaidGame()
>>> game.play(["Allen","Jeff","Chris"])
---------- Cards have been dealt
Hand Allen contains
King of Hearts
Jack of Clubs
Queen of Spades
King of Spades
10 of Diamonds

Hand Jeff contains
Queen of Hearts
Jack of Spades
Jack of Hearts
King of Diamonds
Queen of Diamonds

Hand Chris contains
Jack of Diamonds
King of Clubs
10 of Spades
10 of Hearts
10 of Clubs

Hand Jeff: Queen of Hearts matches Queen of Diamonds
Hand Chris: 10 of Spades matches 10 of Clubs
---------- Matches discarded, play begins
Hand Allen contains
King of Hearts
Jack of Clubs
Queen of Spades
King of Spades
10 of Diamonds

Hand Jeff contains
Jack of Spades
Jack of Hearts
King of Diamonds

Hand Chris contains
Jack of Diamonds
King of Clubs
10 of Hearts

Hand Allen picked King of Diamonds
Hand Allen: King of Hearts matches King of Diamonds
Hand Jeff picked 10 of Hearts
Hand Chris picked Jack of Clubs
Hand Allen picked Jack of Hearts
Hand Jeff picked Jack of Diamonds
Hand Chris picked Queen of Spades
Hand Allen picked Jack of Diamonds
Hand Allen: Jack of Hearts matches Jack of Diamonds
Hand Jeff picked King of Clubs
Hand Chris picked King of Spades
Hand Allen picked 10 of Hearts
Hand Allen: 10 of Diamonds matches 10 of Hearts
Hand Jeff picked Queen of Spades
Hand Chris picked Jack of Spades
Hand Chris: Jack of Clubs matches Jack of Spades
Hand Jeff picked King of Spades
Hand Jeff: King of Clubs matches King of Spades
---------- Game is Over
Hand Allen is empty

Hand Jeff contains
Queen of Spades

Hand Chris is empty
```

<next>

## Questions ?