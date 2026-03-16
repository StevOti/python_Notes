# What Are Common Data Types in Python and How Do You Get the Type of a Variable?

Before working with Python variables, it's important to understand **data types**.

A data type describes the kind of value a variable holds, such as a number, text, or a collection of items. Programming languages use data types to know how to store and work with information.

## Python and dynamic typing

Python is a **dynamically typed** language (similar to JavaScript). This means you do not explicitly declare the type of a variable.

Python determines the type from the value you assign:

```python
name = 'John Doe'  # Python knows this is a string
age = 25           # Python knows this is an integer
```

This is different from **statically typed** languages like C#, Java, and C++, where you declare the type:

```text
string name = 'John Doe'
int age = 25
```

Dynamic typing makes coding fast and flexible, but type errors are often found only at runtime.

## Runtime vs compile-time type errors

- In Python, type-related mistakes are usually discovered when the program is **running**.
- In compiled languages, many type errors are caught during the **compile step** before execution.

Key idea:

- Python often reveals type errors when execution reaches the problematic line.
- Compiled languages often catch type errors before the program starts.

## Common data types in Python

### 1) Integer (`int`)

Whole numbers without decimals.

```python
my_integer_var = 10
print('Integer:', my_integer_var)  # Integer: 10
```

### 2) Float (`float`)

Numbers with decimal points.

```python
my_float_var = 4.50
print('Float:', my_float_var)  # Float: 4.5
```

### 3) String (`str`)

Text enclosed in single or double quotes.

```python
my_string_var = 'hello'
print('String:', my_string_var)  # String: hello
```

### 4) Boolean (`bool`)

Represents `True` or `False`.

```python
my_boolean_var = True
print('Boolean:', my_boolean_var)  # Boolean: True
```

### 5) Set (`set`)

Unordered collection of unique elements.

```python
my_set_var = {7, 'hello', 8.5}
print('Set:', my_set_var)  # Example output: {7, 'hello', 8.5}
```

### 6) Dictionary (`dict`)

Collection of key-value pairs.

```python
my_dictionary_var = {'name': 'Alice', 'age': 25}
print('Dictionary:', my_dictionary_var)  # {'name': 'Alice', 'age': 25}
```

### 7) Tuple (`tuple`)

Immutable ordered collection.

```python
my_tuple_var = (7, 'hello', 8.5)
print('Tuple:', my_tuple_var)  # (7, 'hello', 8.5)
```

### 8) Range (`range`)

Sequence of numbers, often used in loops.

```python
my_range_var = range(5)
print('Range:', my_range_var)  # range(0, 5)
```

### 9) List (`list`)

Ordered collection that can store different types.

```python
my_list = [22, 'Hello world', 3.14, True]
print(my_list)  # [22, 'Hello world', 3.14, True]
```

### 10) None (`NoneType`)

Special value representing the absence of a value.

```python
my_none_var = None
print('None:', my_none_var)  # None: None
```

## How to get the type of a variable with `type()`

Use `type()` to inspect a variable's data type:

```python
my_var_1 = 'Hello world'
my_var_2 = 21

print(type(my_var_1))  # <class 'str'>
print(type(my_var_2))  # <class 'int'>
```

## Type outputs for all examples

```python
my_integer_var = 10
print(type(my_integer_var))  # <class 'int'>

my_float_var = 4.50
print(type(my_float_var))  # <class 'float'>

my_string_var = 'hello'
print(type(my_string_var))  # <class 'str'>

my_boolean_var = True
print(type(my_boolean_var))  # <class 'bool'>

my_set_var = {7, 'hello', 8.5}
print(type(my_set_var))  # <class 'set'>

my_dictionary_var = {'name': 'Alice', 'age': 25}
print(type(my_dictionary_var))  # <class 'dict'>

my_tuple_var = (7, 'hello', 8.5)
print(type(my_tuple_var))  # <class 'tuple'>

my_range_var = range(5)
print(type(my_range_var))  # <class 'range'>

my_list = [22, 'Hello world', 3.14, True]
print(type(my_list))  # <class 'list'>

my_none_var = None
print(type(my_none_var))  # <class 'NoneType'>
```

## Checking types with `isinstance()`

The built-in `isinstance()` function checks whether a value matches a specific type. It returns `True` or `False`.

```python
isinstance('Hello world', str)   # True
isinstance(True, bool)           # True
isinstance(42, int)              # True
isinstance('John Doe', int)      # False
```

## Key takeaway

Python supports many data types and infers them automatically from assigned values. Use `type()` to inspect a value's type and `isinstance()` to test whether a value matches a specific type.
