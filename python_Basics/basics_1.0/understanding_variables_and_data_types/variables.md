# Variables

## How do you declare variables in Python?

In Python, variables are like labeled boxes used to store and reference data.

To declare a variable, assign a value to a name using the assignment operator `=`:

```python
name = 'John Doe'
age = 25
```

In this example:

- `name` stores `'John Doe'`
- `age` stores `25`

Python does not require special keywords like `let`, `const`, or type declarations such as `char` or `int` when creating variables.

## Strings in Python

A **string** is a sequence of characters used to represent text.

Strings can be written with either single or double quotes:

```python
'Hello'
"Hello"
```

## Rules for naming variables in Python

When naming variables, follow these rules:

- Variable names must start with a letter or an underscore (`_`)
- Variable names cannot start with a number
- Variable names can only contain letters, numbers, and underscores
- Variable names are case-sensitive
- Variable names cannot use Python reserved keywords such as `if`, `class`, or `def`

### Example of an invalid variable name

```python
5variable_name = 5
```

This causes a `SyntaxError` because variable names cannot begin with a number.

## Python variable naming conventions

### 1. Use snake case

Python variables are usually written in **snake case**, where all letters are lowercase and words are separated with underscores:

```python
my_variable_name = 'freeCodeCamp'
```

### 2. Use descriptive names

Choose names that clearly explain what the variable stores:

```python
user_age = 30
```

This is better than vague or shortened names because it makes code easier to read and understand.

### 3. Avoid unclear single-letter names

Single-letter variable names usually do not communicate meaning well:

```python
x = 56  # Unclear variable name
```

Names like `i`, `j`, and `k` are acceptable in short loops, but in most cases, descriptive names are better.

## Comments in Python

Comments help explain code and improve readability.

A single-line comment starts with `#`:

```python
# This is a single-line comment
```

You can create multi-line comments by writing several single-line comments:

```python
# This is a
# multi-line
# comment
```

Comments are useful for:

- Explaining code
- Leaving reminders
- Clarifying why a line of code exists

However, comments should not be used as a replacement for clear variable names. Your variable names should already communicate their purpose.

## Key takeaways

- Variables are created by assigning a value with `=`
- Python does not require special declaration keywords
- Variable names must follow Python's naming rules
- Use **snake case** for variable names
- Prefer descriptive names over short or unclear ones
- Use comments to explain code, not to fix poor naming
