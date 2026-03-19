# Loops and Sequences Review

## Python Lists

### Introduction
In Python, the list data type is an ordered sequence of elements that can be composed of strings, numbers or even other lists. Lists are mutable and zero based indexed.

```python
cities = ['Los Angeles', 'London', 'Tokyo']
```

### Accessing Elements in a List
To access an element from the `cities` list, you can reference its index number in the sequence:

```python
cities = ['Los Angeles', 'London', 'Tokyo']
cities[0] # Los Angeles
```

### Accessing Elements Using Negative Indexing
To access the last element of any list, you can use `-1` as the index number:

```python
cities = ['Los Angeles', 'London', 'Tokyo']
cities[-1] # Tokyo
```

Negative indexing is used to access elements starting from the end of the list instead of the beginning at index `0`.

### Creating Lists Using the `list()` Constructor
Lists can also be created using the `list()` constructor. The `list()` constructor is used to convert an iterable into a list:

```python
developer = 'Jessica'

print(list(developer))
# Result: ['J', 'e', 's', 's', 'i', 'c', 'a']
```

### Finding the Length of a List
You can use the `len()` function to get the length of a list:

```python
numbers = [1, 2, 3, 4, 5]
len(numbers) # 5
```

### List Mutability
Lists are mutable, meaning you can update any element in the list as long as you pass in a valid index number. To update lists at a particular index, you can assign a new value to that index:

```python
programming_languages = ['Python', 'Java', 'C++', 'Rust']
programming_languages[0] = 'JavaScript'
print(programming_languages) # ['JavaScript', 'Java', 'C++', 'Rust']
```

### Index Out of Range Error
If you pass in an index (either positive or negative) that is out of bounds for the list, then you will receive an `IndexError`:

```python
programming_languages = ['Python', 'Java', 'C++', 'Rust']
programming_languages[10] = 'JavaScript'

"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list assignment index out of range
"""
```

### Removing Elements from a List
Elements can be removed from a list using the `del` keyword:

```python
developer = ['Jane Doe', 23, 'Python Developer']
del developer[1]
print(developer) # ['Jane Doe', 'Python Developer']
```

### Checking if an Element Exists in a List
The `in` keyword can be used to check if an element exists in a list:

```python
programming_languages = ['Python', 'Java', 'C++', 'Rust']

'Rust' in programming_languages # True
'JavaScript' in programming_languages # False
```

### Nesting Lists
Lists can be nested inside other lists:

```python
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
```

To access the nested list, use index `2`:

```python
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
developer[2] # ['Python', 'Rust', 'C++']
```

To access the second language in that nested list:

```python
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
developer[2][1] # Rust
```

### Unpacking Values from a List
Unpacking values from a list assigns values to variables:

```python
developer = ['Alice', 34, 'Rust Developer']
name, age, job = developer
```

If the number of variables on the left side of the assignment operator doesn't match the total number of items in the list, then you will receive a `ValueError`.

### Collecting Remaining Items From a List
Use `*` to collect the rest of the items:

```python
developer = ['Alice', 34, 'Rust Developer']
name, *rest = developer
```

### Slicing Lists
Slicing accesses a portion of a list with `:`:

```python
desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie']
desserts[1:3] # ['Cookies', 'Ice Cream']
```

### Step Intervals
You can specify a step interval:

```python
numbers = [1, 2, 3, 4, 5, 6]
numbers[1::2] # [2, 4, 6]
```

## List Methods

### `append()`
Used to add an item to the end of the list:

```python
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
print(numbers) # [1, 2, 3, 4, 5, 6]
```

### Appending Lists
`append()` can add a whole list as one item:

```python
numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]

numbers.append(even_numbers)
print(numbers) # [1, 2, 3, 4, 5, [6, 8, 10]]
```

### `extend()`
Used to add multiple items to the end of a list:

```python
numbers = [1, 2, 3, 4, 5]
even_numbers = [6, 8, 10]

numbers.extend(even_numbers)
print(numbers) # [1, 2, 3, 4, 5, 6, 8, 10]
```

### `insert()`
Used to insert an item at a specific index:

```python
numbers = [1, 2, 3, 4, 5]
numbers.insert(2, 2.5)

print(numbers) # [1, 2, 2.5, 3, 4, 5]
```

### `remove()`
Removes the first occurrence of a value:

```python
numbers = [1, 2, 3, 4, 5, 5, 5]
numbers.remove(5)

print(numbers) # [1, 2, 3, 4, 5, 5]
```

### `pop()`
Removes and returns an item by index:

```python
numbers = [1, 2, 3, 4, 5]
numbers.pop(1) # The number 2 is returned
```

If no index is provided, it removes the last item:

```python
numbers = [1, 2, 3, 4, 5]
numbers.pop() # The number 5 is returned
```

### `clear()`
Removes all items:

```python
numbers = [1, 2, 3, 4, 5]
numbers.clear()

print(numbers) # []
```

### `sort()`
Sorts a list in place:

```python
numbers = [19, 2, 35, 1, 67, 41]
numbers.sort()

print(numbers) # [1, 2, 19, 35, 41, 67]
```

### `sorted()`
Returns a new sorted list:

```python
numbers = [19, 2, 35, 1, 67, 41]
sorted_numbers = sorted(numbers)

print(sorted_numbers) # [1, 2, 19, 35, 41, 67]
print(numbers) # [19, 2, 35, 1, 67, 41]
```

### `reverse()`
Reverses list order:

```python
numbers = [6, 5, 4, 3, 2, 1]
numbers.reverse()

print(numbers) # [1, 2, 3, 4, 5, 6]
```

### `index()`
Finds first index of a value:

```python
programming_languages = ['Rust', 'Java', 'Python', 'C++']
programming_languages.index('Java') # 1
```

If the value is not found, `index()` raises a `ValueError`.

## Tuples in Python

### Definition
A tuple is a Python data type used to create an ordered sequence of values. Tuples can contain a mixed set of data types:

```python
developer = ('Alice', 34, 'Rust Developer')
```

Tuples are immutable, meaning elements cannot be changed once created. Trying to update one raises a `TypeError`:

```python
programming_languages = ('Python', 'Java', 'C++', 'Rust')
programming_languages[0] = 'JavaScript'

"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: "tuple" object does not support item assignment
"""
```

### Accessing Elements from a Tuple

```python
developer = ('Alice', 34, 'Rust Developer')
developer[1] # 34
```

Negative indexing:

```python
numbers = (1, 2, 3, 4, 5)
numbers[-2] # 4
```

Out of range index raises `IndexError`:

```python
numbers = (1, 2, 3, 4, 5)
numbers[7]

"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: tuple index out of range
"""
```

### Creating Tuples with `tuple()`
You can pass strings, lists, and tuples to `tuple()`:

```python
developer = 'Jessica'

print(tuple(developer))
# Result: ('J', 'e', 's', 's', 'i', 'c', 'a')
```

### Verifying Items in a Tuple

```python
programming_languages = ('Python', 'Java', 'C++', 'Rust')

'Rust' in programming_languages # True
'JavaScript' in programming_languages # False
```

### Unpacking Tuples

```python
developer = ('Alice', 34, 'Rust Developer')
name, age, job = developer
```

Collect remaining elements:

```python
developer = ('Alice', 34, 'Rust Developer')
name, *rest = developer
```

### Slicing Tuples

```python
desserts = ('cake', 'pie', 'cookies', 'ice cream')
desserts[1:3] # ('pie', 'cookies')
```

### Removing Items from Tuples
Removing items raises `TypeError` because tuples are immutable:

```python
developer = ('Jane Doe', 23, 'Python Developer')
del developer[1]

"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: "tuple" object doesn't support item deletion
"""
```

### When to Use Tuple vs List
Use a list for dynamic, changeable collections. Use a tuple for fixed, immutable collections.

## Common Tuple Methods

### `count()`
Counts occurrences:

```python
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.count('Rust') # 2
```

If item is absent:

```python
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.count('JavaScript') # 0
```

No argument to `count()` raises `TypeError`.

### `index()`
Finds first index of an item:

```python
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust')
programming_languages.index('Java') # 1
```

If item is missing, `ValueError` is raised.

Optional start index:

```python
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
programming_languages.index('Python', 3) # 5
```

Optional start and end index:

```python
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python', 'JavaScript', 'Python')
programming_languages.index('Python', 2, 5) # 2
```

### `sorted()`
Sorts an iterable and returns a new list:

```python
numbers = (13, 2, 78, 3, 45, 67, 18, 7)
sorted(numbers) # [2, 3, 7, 13, 18, 45, 67, 78]
```

Custom sorting with `key`:

```python
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')
sorted(programming_languages, key=len)

# Result
# ['C++', 'Rust', 'Java', 'Rust', 'Python', 'Python']
```

Reverse sorting with `reverse=True`:

```python
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python')

print(sorted(programming_languages, reverse=True))

# Result
# ['Rust', 'Rust', 'Python', 'Python', 'Java', 'C++']
```

## Loops in Python

### Definition
Loops are used to repeat a block of code for a set number of times.

### `for` Loop
Iterates over sequences (list, tuple, string):

```python
programming_languages = ['Rust', 'Java', 'Python', 'C++']

for language in programming_languages:
	print(language)

"""
Result

Rust
Java
Python
C++
"""
```

Looping over a string:

```python
for char in 'code':
	print(char)

"""
Result

c
o
d
e
"""
```

Nested `for` loops:

```python
categories = ['Fruit', 'Vegetable']
foods = ['Apple', 'Carrot', 'Banana']

for category in categories:
	for food in foods:
		print(category, food)

"""
Result

Fruit Apple
Fruit Carrot
Fruit Banana
Vegetable Apple
Vegetable Carrot
Vegetable Banana
"""
```

### `while` Loop
Repeats until condition is `False`:

```python
secret_number = 3
guess = 0

while guess != secret_number:
	guess = int(input('Guess the number (1-5): '))
	if guess != secret_number:
		print('Wrong! Try again.')

print('You got it!')
```

### `break` and `continue`
`break` exits loop immediately:

```python
developer_names = ['Jess', 'Naomi', 'Tom']

for developer in developer_names:
	if developer == 'Naomi':
		break
	print(developer)
```

`continue` skips current iteration:

```python
developer_names = ['Jess', 'Naomi', 'Tom']

for developer in developer_names:
	if developer == 'Naomi':
		continue
	print(developer)
```

Loop `else` runs only if no `break` occurs:

```python
words = ['sky', 'apple', 'rhythm', 'fly', 'orange']

for word in words:
	for letter in word:
		if letter.lower() in 'aeiou':
			print(f"'{word}' contains the vowel '{letter}'")
			break
	else:
		print(f"'{word}' has no vowels")
```

## Ranges and Their Use in Loops

### `range()`
Used to generate a sequence of integers:

```python
range(start, stop, step)
```

`stop` is required and non-inclusive:

```python
for num in range(3):
	print(num)
```

Default `start` is `0`, default step is `1`. Example with step `2`:

```python
for num in range(2, 11, 2):
	print(num)
```

No arguments causes `TypeError`.

`range()` only accepts integers, not floats:

```python
ERROR!
Traceback (most recent call last):
  File "<main.py>", line 1, in <module>
TypeError: 'float' object cannot be interpreted as an integer
```

Negative step for descending sequence:

```python
for num in range(40, 0, -10):
	print(num)
```

Use with `list()`:

```python
numbers = list(range(2, 11, 2))
print(numbers) # [2, 4, 6, 8, 10]
```

## `enumerate()` and `zip()` Functions

### `enumerate()`
Iterates with index + value:

```python
languages = ['Spanish', 'English', 'Russian', 'Chinese']

for index, language in enumerate(languages):
	print(f'Index {index} and language {language}')

# Result
# Index 0 and language Spanish
# Index 1 and language English
# Index 2 and language Russian
# Index 3 and language Chinese
```

Outside a loop:

```python
languages = ['Spanish', 'English', 'Russian', 'Chinese']

print(list(enumerate(languages)))
# [(0, 'Spanish'), (1, 'English'), (2, 'Russian'), (3, 'Chinese')]
```

It also accepts an optional `start` argument.

### `zip()`
Iterates over multiple iterables in parallel:

```python
developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

for name, id in zip(developers, ids):
	print(f'Name: {name}')
	print(f'ID: {id}')
```

## List Comprehensions

### Definition
List comprehension creates a new list in one line by combining loop and condition inside square brackets.

```python
even_numbers = [num for num in range(21) if num % 2 == 0]
print(even_numbers)
```

## Iterable Functions

### `filter()`
Filters elements based on a condition:

```python
words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

def is_long_word(word):
	return len(word) > 4

long_words = list(filter(is_long_word, words))
print(long_words) # ['mountain', 'river', 'cloud']
```

### `map()`
Applies a function to every item:

```python
celsius = [0, 10, 20, 30, 40]

def to_fahrenheit(temp):
	return (temp * 9/5) + 32

fahrenheit = list(map(to_fahrenheit, celsius))
print(fahrenheit) # [32.0, 50.0, 68.0, 86.0, 104.0]
```

### `sum()`
Sums values in an iterable:

```python
numbers = [5, 10, 15, 20]
total = sum(numbers)
print(total) # Result: 50
```

Optional `start` positional argument:

```python
numbers = [5, 10, 15, 20]
total = sum(numbers, 10) # positional argument
print(total) # 60
```

Optional `start` keyword argument:

```python
numbers = [5, 10, 15, 20]
total = sum(numbers, start=10) # keyword argument
print(total) # 60
```

## Lambda Functions

### Definition
A lambda function in Python is a concise anonymous function.

Lambda functions are often used as arguments to other functions:

```python
numbers = [1, 2, 3, 4, 5]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]
```

Best practices:
- Avoid assigning lambda functions to variables.
- Keep lambda expressions simple and readable.
- Prefer lambdas for short, one-off expressions.
