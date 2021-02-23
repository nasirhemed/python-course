---
title: Loops
separator: ---
verticalSeparator: --
theme: solarized
progress: true
revealOptions:
    transition: 'fade'
---
## Intro to Python 
### Loops
#### Nasir Hemed
---

## Agenda

- [Course Updates](#/2)
- [Loops and Iteration](#/3)
  - [Motivation](#/4)
  - [While Loops](#/7)
  - [Abbreviated Assignments](#/10)
  - [Break Statements](#/11)
--- 

## Course Updates
- [Google Classroom](#)
  - Make sure you submit your exercises!

---
## Loops and Iteration

---

## Motivation

We often use computers to do repeated tasks.

- Alarm at 8 AM everyday
- Turning on the computer
- Logging in and out

Repeated exectuion of statements is called iteration.

Python has ways to allow you to write iterations

---

### Assignment

Recall variables and assigning variables. We know that in python, we can any variable and assign values to them multiple times

```python
a = 3
a = 5
a = 7
print(a) # Final value will be 7
```

--

Note that `=` is completely different from `==` 

`=` is used in assignment of variables like `a = "hello"` but `==` is a statement/expression used to check for equality whether `a == b`

Equality is symmetric: i.e `a == "hello"` is the same as saying `"hello" == a` 

However, assignment is not!

--

Consider the following however: 

```python
a = 5
b = a # Here we assign b to be whatever a was
a = 3 # Here we assign a to be b
print(b) # However, the value of b will be the original value
```
---

### Updating Variables

This means that we ware able to use already defined variables.

```python
# This program will not work because a is defined later
*b = a + 1 # Python will see this as (?) + 1 and will give error
a = 5
```

```python
# This program will work because a is already defined
a = 5
b = a + 1 # Python will see this as (5) + 1 since a = 5
```
--

Thus, consider this: 

```python
n = 5
n = n + 1 # Python will see this as (5) + 1
print(n) # Therefore, n will be 6
```

---

## While loops

--

### If statements

```python
if bool_expr:
	...
	...
```

- `...` will be executed
  - only if `bool_expr` is True
- `...` will be executed once 

--

Replacing `if` with `while`

```python
while bool_expr
	...
```
- In English
  - `...` will execute "while" `bool_expr` is True

---

### Example

```python
def sum_to(n):
	"""
	Return the sum of 1 + 2 + 3 + ... + n
	
	Arguments:
	n : int
	"""
	
	total_sum = 0
	current_number = 1
	while current_number <= n:
		total = total + current_number
		current_number = current_number + 1
	
	return total_sum
```

--

### What does the above function do ?

In English:
- Start from 1
- Keep track of total
- While the current number is <= n:
  - Keep adding current number to total 
  - Update current number + 1

--

More formally, this is what python sees:

- Evaluate the condition: `current_number <= n`
- If the condition is `False`:
  - Move on to `return total_sum`
- If the condition is `True`:
  - Go inside the body

---

### Doing Something `n` Times

So now let's say we want to do something n times. How would we do it?
- Have a counter and initialize to 1 
- Do a while loop condition 
    - `while counter <= n:` 
- Do what you want to do in your while loop 
- Update counter by 1
    - `counter = counter + 1`

--
The code: 

```python
counter = 1
n = 5 # I want to do something 5 times
while counter <= n:
	print("I am doing something")
	counter = counter + 1
```

--

In computer science, we always start numbers from 0. So the updated code will be:

```python
counter = 0
n = 5 # I want to do something 5 times
while counter < n:
	print("I am doing something")
	counter = counter + 1
```

---

### Abbreviated Assignments

Python gives us a nice way to increment numbers

```python
>>> count = 0
>>> count += 1
>>> count
1
>>> count += 10
>>> count
11
```

--

There are similar abbreviations for `-=`, `*=`, `/=`, `//=` and `%=`:


```python
>>> n = 2
>>> n *= 5
>>> n
10
>>> n -= 4
>>> n
6
>>> n //= 2
>>> n
3
>>> n %= 2
>>> n
1
```

---

## Break!

--

The `break` statement is used to tell python to exit out of the loop immediately without checking conditions

```python
counter = 0
n = 5
while True: #This will execute forever if we don't do something
	if counter >= 5:
		break
	print("I am doing something")
```
---

## Questions? 