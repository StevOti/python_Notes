# How Do Functions Work in Python?

Functions are reusable pieces of code that run when you call them. Many programming languages come with built-in functions that make it easier to get started. Python is no exception, and we've already covered some built-in functions like `print()` in previous lessons.

## Built-in Functions

### `input()` Function

The `input()` function lets you prompt the user for input:

```python
name = input('What is your name?')  # User types "Kolade" and presses Enter
print('Hello', name)  # Output: Hello Kolade
```

### `int()` Function

The `int()` function converts a number, boolean, and a numeric string into an integer:

```python
print(int(3.14))   # 3
print(int('42'))   # 42
print(int(True))   # 1
print(int(False))  # 0
```

## Custom Functions

You can write your own custom functions using the `def` keyword, followed by the function name, a pair of parentheses, and a colon. Then on a new line, you write the code your function should run. The code the function runs is called the function's **body**.

### Simple Function Example

Here's an example of a custom function named `hello` that prints `Hello World`:

```python
def hello():
    print('Hello World')
```

To run the function, call it with its name followed by a pair of parentheses:

```python
hello()  # Output: Hello World
```

Notice the indentation before `print('Hello World')`. As in previous lessons, Python relies on indentation to determine which groups of statements belong together. These groups are called **code blocks**.

## Parameters and Arguments

Functions can accept values by using **parameters** and **arguments**.

- **Parameters** are placeholder variables in the function definition
- **Arguments** are the actual values you pass when calling the function

Here's a function with parameters:

```python
def calculate_sum(a, b):
    print(a + b)
```

The function `calculate_sum` has `a` and `b` as parameters. To call it and provide arguments:

```python
calculate_sum(3, 1)  # Output: 4
```

### Missing Arguments Error

If you call a function without the correct number of arguments, you'll get a `TypeError`:

```python
calculate_sum()
# TypeError: calculate_sum() missing 2 required positional arguments: 'a' and 'b'
```

## The `return` Keyword

Functions use the `return` keyword to exit the function and return a value. If you don't explicitly use `return`, Python will return `None` by default.

### Example Without `return`

```python
def calculate_sum(a, b):
    print(a + b)

my_sum = calculate_sum(3, 1)  # Output: 4
print(my_sum)  # Output: None
```

The function prints the sum but doesn't return it explicitly, so `my_sum` is `None`.

### Example With `return`

```python
def calculate_sum(a, b):
    return a + b

my_sum = calculate_sum(3, 1)
print(my_sum)  # Output: 4
```

Now the function returns the sum, which gets stored in `my_sum` and can be printed.

## Summary

- Built-in functions like `print()`, `input()`, and `int()` are already available in Python
- Write custom functions with `def`, followed by a name, parentheses, and a colon
- Use parameters to accept values into functions
- Pass arguments when calling a function
- Use `return` to send a value back from a function
- Python returns `None` if no explicit `return` statement is used
