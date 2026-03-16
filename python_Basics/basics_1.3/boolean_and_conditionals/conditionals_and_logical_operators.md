# Conditionals and Logical Operators in Python

Conditional statements (or conditionals) let you control the flow of your program based on whether certain conditions are `True` or `False`.

Before writing conditionals, you need to understand **comparison operators**. These operators compare values and return a boolean result.

In Python, booleans can only be:

- `True`
- `False`

## Comparison Operators

| Operator | Name | Description |
|---|---|---|
| `==` | Equal | Checks if two values are equal |
| `!=` | Not equal | Checks if two values are not equal |
| `>` | Greater than | Checks if the value on the left is greater than the value on the right |
| `<` | Less than | Checks if the value on the left is less than the value on the right |
| `>=` | Greater than or equal | Checks if the value on the left is greater than or equal to the value on the right |
| `<=` | Less than or equal | Checks if the value on the left is less than or equal to the value on the right |

### Examples

```python
print(3 > 4)   # False
print(3 < 4)   # True
print(3 == 4)  # False
print(4 == 4)  # True
print(3 != 4)  # True
print(3 >= 4)  # False
print(3 <= 4)  # True
```

These operators are used inside conditionals to run code depending on whether an expression is `True` or `False`.

## The `if` Statement

The most basic conditional in Python is `if`.

```python
if condition:
	pass  # Code to execute if condition is True
```

- `if` starts the statement.
- `condition` is an expression that evaluates to `True` or `False`.
- A colon (`:`) follows the condition.
- The body must be indented to form a code block.

The `pass` keyword is a placeholder that does nothing. It is useful when an empty code block is not allowed.

### Example

```python
age = 18

if age >= 18:
	print('You are an adult')  # You are an adult
```

The code inside the `if` block runs only when the condition is `True`.

## Indentation in Python

In Python, indentation defines code blocks. Unlike languages that use braces, Python requires indentation for block structure.

This causes an error because the block is not indented:

```python
age = 18

if age >= 18:
print('You are an adult')
# IndentationError: expected an indented block after 'if' statement on line 3
```

Use consistent indentation. Python style guidelines recommend **four spaces** per indentation level.

## `if...else`

If you want one action for `True` and another for `False`, use `else`.

```python
if condition:
	pass  # Code to execute if condition is True
else:
	pass  # Code to execute if condition is False
```

### Example

```python
age = 12

if age >= 18:
	print('You are an adult')
else:
	print('You are not an adult yet')  # You are not an adult yet
```

You cannot place statements between the `if` block and `else`.

```python
age = 12

if age >= 18:
	print('You are an adult')
print('Almost there!')
else:
	print('You are not an adult yet')
# SyntaxError: invalid syntax
```

## `if...elif...else`

To handle multiple conditions, use `elif`.

```python
if condition1:
	pass  # Runs if condition1 is True
elif condition2:
	pass  # Runs if condition1 is False and condition2 is True
else:
	pass  # Runs if all conditions are False
```

### Example

```python
age = 12

if age >= 18:
	print('You are an adult')
elif age >= 13:
	print('You are a teenager')
else:
	print('You are a child')  # You are a child
```

You can use as many `elif` blocks as needed:

```python
age = 2

if age >= 65:
	print('You are a senior citizen')
elif age >= 30:
	print('You are an adult in your prime')
elif age >= 18:
	print('You are a young adult')
elif age >= 13:
	print('You are a teenager')
elif age >= 3:
	print('You are a young child')
else:
	print('You are a toddler or an infant')  # You are a toddler or an infant
```

## Summary

Now you know how to:

- Compare values using comparison operators
- Use `if` to run code when a condition is true
- Use `else` for an alternative path
- Use `elif` to check multiple conditions

These tools are the foundation for writing programs that make decisions based on logic and input.
