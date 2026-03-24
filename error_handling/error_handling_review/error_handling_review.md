# Error Handling Review

## Common Errors in Python

### SyntaxError

The error Python raises when your code does not follow syntax rules.

For example, the code below leads to a syntax error because the closing parenthesis is missing:

```python
print("Hello there"
# SyntaxError: '(' was never closed
```

### NameError

Python raises a `NameError` when you try to access a variable or function you have not defined.

For instance:

```python
print(username)
# NameError: name 'username' is not defined
```

### TypeError

This error happens when you perform an operation on incompatible data types.

For example, adding a string to a number raises a type error:

```python
"Age: " + 20
# TypeError: can only concatenate str (not "int") to str
```

### IndexError

You get an `IndexError` when you access an index that does not exist in a sequence like a list, tuple, or string.

Example:

```python
greet = "hello world"
print(greet[12])
# IndexError: string index out of range
```

### AttributeError

Python raises this error when you try to use a method or property that does not exist for an object type.

Example:

```python
"hello".append("!")
# AttributeError: 'str' object has no attribute 'append'
```

## Good Debugging Techniques in Python

### Using the print Function

Inserting `print()` statements in different parts of your code helps you inspect variable values and follow execution flow.

### Using Python's Built-in Debugger (pdb)

Python provides the `pdb` module in the standard library. You can call `set_trace()` to pause execution and inspect your program interactively.

### Leveraging IDE Debugging Tools

Many IDEs and editors, like PyCharm and VS Code, offer debugging tools with breakpoints, step execution, and variable inspection.

## Exception Handling

### try...except

Use `try` for code that may raise an exception and `except` to handle specific exceptions.

```python
try:
	print(22 / 0)
except ZeroDivisionError:
	print("You can't divide by zero!")
	# You can't divide by zero!
```

You can chain multiple `except` blocks to handle different exceptions:

```python
try:
	number = int(input('Enter a number: '))
	print(22 / number)
except ZeroDivisionError:
	print('You cannot divide by zero!')
	# Prints when you enter 0
except ValueError:
	print('Please enter a valid number!')
	# Prints when you enter a string
```

### else and finally

If no exception occurs, the `else` block runs. The `finally` block always runs.

```python
try:
	result = 100 / 4
except ZeroDivisionError:
	print('You cannot divide by zero!')
else:
	print(f'Result is {result}')
	# Result is 25.0
finally:
	print('Execution complete!')
	# Execution complete!
```

### Exception Object

Use `as` to capture the exception object and access the error message.

```python
try:
	value = int('This will raise an error')
except ValueError as e:
	print(f'Caught an error: {e}')
	# Caught an error: invalid literal for int() with base 10: 'This will raise an error'
```

### The raise Statement

Use `raise` to manually throw exceptions when a condition is met.

```python
def divide(a, b):
	if b == 0:
		raise ZeroDivisionError('You cannot divide by zero')
	return a / b
```

## Exception Signaling

The `raise` statement is useful for custom exceptions with custom messages.

```python
class InvalidCredentialsError(Exception):
	def __init__(self, message='Invalid username or password'):
		self.message = message
		super().__init__(self.message)


def login(username, password):
	stored_username = 'admin'
	stored_password = 'password123'

	if username != stored_username or password != stored_password:
		raise InvalidCredentialsError()

	return f'Welcome, {username}!'
```

Here is how you can use `login` with `InvalidCredentialsError`:

```python
# Failed login attempt
try:
	message = login('user', 'wrongpassword')
except InvalidCredentialsError as e:
	print(f'Login failed: {e}')
else:
	print(message)


# Successful login attempt
try:
	message = login('admin', 'password123')
except InvalidCredentialsError as e:
	# This block is not executed because the login was successful
	print(f'Login failed: {e}')
else:
	# The else block runs if the try block completes without an exception
	print(message)
```

The `raise` statement can also be used with `from` to chain exceptions and preserve error context:

```python
def parse_config(filename):
	try:
		with open(filename, 'r') as file:
			data = file.read()
			return int(data)
	except FileNotFoundError:
		raise ValueError('Configuration file is missing') from None
	except ValueError as e:
		raise ValueError('Invalid configuration format') from e


config = parse_config('config.txt')
```
