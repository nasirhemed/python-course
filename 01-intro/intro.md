layout: true
class: nord-light, typo, typo-selection 

---
class: nord-light, center, middle
# Intro to Python
## Course Intro + Programming
#### Nasir Hemed

---
# Agenda

- [Computer Programming](#computer-programming)
- [About this Course](#course)
- [Let's get started with programming](#programming)
- [Data Types](#data-types)
- [Variables](#variables)
- [Swapping Problem](#swapping-problem)

---

class: nord-light
name: computer-programming

# What is Computer Programming?

--

- Series of Instructions 
  - Like a recipe or manual

--

- Why not just use English Instructions?
  - Computers are dumb
  - There are only limited set of instructions

--

- Language that is clear and concise

Computers are kinda dumb. But at least they are obedient

---

# What can programming do ?

There are a lot of things that programming can do. 

- Solve problems
- Create applications
- Make life easier 
- Games, poetry, animation
- And much more!

*This course will serve as a building block to understanding how computers work*

---

# Programming Examples

## Algorithms + Animation

- A* Search Algorithm
<div class="wrap"> 
<iframe class="frame" src="https://jakedeichert.github.io/wasm-astar/">

<div>

---

# Programming Examples

## Someone to help you out

- Machine Learning Text Generator

<div class="wrap"> 
<iframe class="frame" height="600px" src="https://bellard.org/textsynth/">

<div>


---

name: course

# About this Course

**Questions or Comments?** Let me know!

**Prerequisites**: Little or no programming experience assumed.

### Goals
- How to make computer solve problems
- Programming in Python
- Designing programs and application

---

# Course Logistics

## Course Delivery
- First hour: Lecture content and slides
- Second hour: In class excercises and lab

---

# Grading + Assignments
- Excercises
  - Attendance
  - In class excercises
- Assignments
  - 4 Assignments
  - Due dates TBD
- Tests
  - Two Term tests: Midterm and Final
---
# Important Links

## Links we will be referring to

- [Course Website](https://nasirhemed.github.io/python-course/)
    - Lecture Slides
    - Additional Notes
- [Google Classroom](https://classroom.google.com/c/MjYyNTU1MDYyMDU1)
  - Announcements
  - Grades
  - Assignemnts
- [Wing IDE](https://wingware.com/)
  - Install python editing software
  - Run code
- and other links...

---
name: programming
# Let's get started with programming

```python
print("Hello World!")
```

- Printing things out: `print("Hello World")`
  - You can use either single ('hello') or double quotes ("hello")
  - `print('hmm "this is interesting"')`
  - `print("my name's Nasir")`

---
# What is Print ?

- Print is a function 
  - You call it by specifying arguments
- `print("Hello World")`
  - Here, `"Hello World"` is an argument
- `print("arg1", " arg2", "arg3")`
  - Here, the values that are passed in the print function are 
    - "arg1"
    - "arg2"
    - "arg3"

---
name: data-types
# Data Types

- Python can use different types of data
  - They can be integers (int), decimals (float)
  - They can be text (strings) like the ones we printed before
  - They can be booleans (True, False)

---

# Python as a Calculator

- We can use python as a calculator
  - Use the shell to enter calculator commands

```python 
>>> 9 + 1 # Addition
10
>>> 9 - 1 # Subtraction 
8
>>> 9 * 10 # Multiplication
90
>>> 9**3 # Exponentiation
729
>>> 9 / 4 # Division
2.25
>>> 9 // 4 # Integer Divsion
2
>>> 9 % 4 # Remainder
1
```
  <!-- - Operators used:
    - \+ (addition)
    - \- (subtraction)
    - \* (multiplication)
    - \*\* (exponentiation)
    - / (division) and // (integer division)
    - % (remainder)
  - e.g: 9 + 10 in the shell gives 21   -->


---
name: variables
# Variables

Variables are like math variables.  

- E.g: In math, we say "let x = 5 or suppose x = 5"
  - then x + 4 will be 9
- Python is very similar
  - However, the values can change as much as we want it to
  - we can say `x = 1` at one point and then `x = 5` at another point


---
 
# Assigning Variables

## Assignment statement
If we want to create a variable in python, we do it like so
```python
variable = value
```
---

# Examples
```python
x = 5 
x = 2 + 3
```

Once we assign a variable, we can use that later. But the value represented will be the last assigned value.

--
Steps the computer takes:
- Evaluate the expression on the right-hand side to get a result
- Store that result in memory and refer to it as "x"

---
# Quiz

What is the value of x after the execution of this code?

--
```python
x = 37
x = x - 2
x = 20
```
--

1. 39
2. 22
3. 35
4. 20
5. 18

---

# Quiz Result

The answer is 20. But why?

--

- `x = 37`
  -  Assigns x to become 37  
--

- `x = x - 2`
  -  Evaluating the right hand becomes 37 - 2 which is 35
--

- `x = 20`
  -  x is assigned to 20


--

- What happens to 37 and 35?  
--

  - Well they are just dumped out and forgotten

---
# Naming Conventions

- You can use any length of names and letters to name a variable
- We usually use meaningful names for variables
  - `name = "Nasir"`
  - `course = "Intro to Python"`
  - `students = 5`


--
Sometimes, variable names can have more than one word
```python
thisisavariable = "hard to know what it says"
thisIsAVariable = "This is camelCase"
tHiSIsAVaRIaBLe = "This is madness"
this_is_a_variable = "That's the way I like to see"
```
---
class: nord-dark, center, middle
name: swapping-problem

# Swapping Problem

---
# Swapping Problem
Here's an interesting problem.

My favourite game is zelda  

John's favourite game is mario

So I write in python:
```python 
nasir_fave_game = 'mario'
john_fave_game = 'zelda'
```

Yikes! I made a mistake.

How can I fix this?

---
# Swapping Problem

What I originally wrote:
```python 
nasir_fave_game = 'mario'
john_fave_game = 'zelda'
```

My fix:
```python 
nasir_fave_game = john_fave_game
john_fave_game = nasir_fave_game
```
Will this work ? 

---
# Swapping Problem

The solution to this would involve a temporary variable.
```python 
nasir_fave_game = 'mario'
john_fave_game = 'zelda'
```

Swapping these two:
```python
*temp = nasir_fave_game
nasir_fave_game = john_fave_game
*john_fave_game = temp
```
