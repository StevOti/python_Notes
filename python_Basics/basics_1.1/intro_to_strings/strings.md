# What Are Strings and What Is String Immutability?

A **string** is a sequence of characters surrounded by either single or double quotation marks.

In some programming languages, single quotes and double quotes can behave differently. In Python, both are treated equally for strings.

## Basic string examples

### Example Code

```python
my_str_1 = 'Hello'
my_str_2 = "World"
```

## Multi-line strings

If you need a multi-line string, use triple quotes (single or double):

### Example Code

```python
my_str_3 = """Multiline
string"""
my_str_4 = '''Another
multiline
string'''
```

## Strings that contain quotes

If your string contains single or double quotation marks, you have two options.

### 1) Use the opposite type of quote

### Example Code

```python
msg = "It's a sunny day"
quote = 'She said, "Hello World!"'
```

### 2) Escape quotes with a backslash (`\`)

### Example Code

```python
msg = 'It\'s a sunny day'
quote = "She said, \"Hello!\""
```

## Checking whether text exists in a string (`in`)

Python provides the `in` operator to check whether one or more characters exist in a string.

### Example Code

```python
my_str = 'Hello world'

print('Hello' in my_str)  # True
print('hey' in my_str)    # False
print('hi' in my_str)     # False
print('e' in my_str)      # True
print('f' in my_str)      # False
```

## Getting string length with `len()`

Use the built-in `len()` function to get the number of characters in a string:

### Example Code

```python
my_str = 'Hello world'
print(len(my_str))  # 11
```

## String indexing

Each character in a string has a zero-based index:

- First character index: `0`
- Second character index: `1`
- and so on.

Access characters using square brackets:

### Example Code

```python
my_str = 'Hello world'

print(my_str[0])  # H
print(my_str[6])  # w
```

### Negative indexing

You can also access characters from the end of a string:

- `-1` is the last character
- `-2` is the second-to-last character

### Example Code

```python
my_str = 'Hello world'
print(my_str[-1])  # d
print(my_str[-2])  # l
```

## What is immutability?

Many languages classify data types as primitive or reference types. Python works differently: all data is treated as objects, and some objects are mutable while others are immutable.

An **immutable** data type cannot be changed after creation. You can reassign the variable to a new object, but you cannot modify the original object in place.

## String immutability in Python

Strings are immutable in Python.

You can reassign a variable to a new string:

### Example Code

```python
greeting = 'hi'
greeting = 'hello'
print(greeting)  # hello
```

But you cannot directly modify a character in an existing string:

### Example Code

```python
greeting = 'hi'
greeting[0] = 'H'  # TypeError: 'str' object does not support item assignment
```

## Other immutable Python data types

Other immutable data types include:

- `int`
- `float`
- `bool`
- `tuple`
- `range`
