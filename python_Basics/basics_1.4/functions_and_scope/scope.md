# What Is Scope in Python and How Does It Work?

In Python, **scope** determines the point at which you can access a variable. It controls the lifetime of a variable and how Python resolves names in different parts of your code.

To resolve variables correctly, Python follows the **LEGB rule**:

- **Local scope (L):** Variables defined in functions or classes
- **Enclosing scope (E):** Variables defined in enclosing or nested functions
- **Global scope (G):** Variables defined at the top level of a module or file
- **Built-in scope (B):** Reserved names in Python for predefined functions, modules, keywords, and objects

Python uses this order to resolve variable names in your program.

## Local Scope (L)

A variable declared inside a function or class can only be accessed within that function or class.

```python
def my_func():
	my_var = 10
	print(my_var)
```

In this case, `my_func` has its own local scope. Calling `my_func()` outputs `10`, but trying to print `my_var` outside the function causes a `NameError`:

```python
def my_func():
	my_var = 10  # Locally scoped to my_func
	print(my_var)

my_func()  # 10

print(my_var)  # NameError: name 'my_var' is not defined
```

## Enclosing Scope (E)

A nested function can access variables from its enclosing function.

```python
def outer_func():
	msg = 'Hello there!'

	def inner_func():
		print(msg)

	inner_func()

outer_func()  # Hello there!
```

Here, `inner_func` can access `msg` from `outer_func`.

However, outer functions cannot access variables defined only inside nested functions:

```python
def outer_func():
	msg = 'Hello there!'
	print(res)

	def inner_func():
		res = 'How are you?'
		print(msg)

	inner_func()

outer_func()  # NameError: name 'res' is not defined
```

That happens because `res` is local to `inner_func`, and `outer_func` tries to use it before it exists in its own scope.

One solution is to define `res` in the enclosing function and use `nonlocal` in the nested function:

```python
def outer_func():
	msg = 'Hello there!'
	res = ""  # Declare res in the enclosing scope

	def inner_func():
		nonlocal res  # Allow modification of an enclosing variable
		res = 'How are you?'
		print(msg)

	inner_func()
	print(res)

outer_func()

# Output:
# Hello there!
# How are you?
```

## Global Scope (G)

Variables declared outside functions/classes are global and can be accessed from anywhere in the module.

```python
my_var = 100

def show_var():
	print(my_var)

show_var()  # 100
print(my_var)  # 100
```

You can use `global` inside a function to make a variable globally accessible:

```python
my_var_1 = 7

def show_vars():
	global my_var_2
	my_var_2 = 10
	print(my_var_1)
	print(my_var_2)

show_vars()  # 7 10
print(my_var_2)  # 10
```

You can also use `global` to modify an existing global variable:

```python
my_var = 10

def change_var():
	global my_var
	my_var = 20

change_var()
print(my_var)  # 20
```

## Built-in Scope (B)

Built-in scope includes Python's built-in functions, modules, and keywords, which are available everywhere.

```python
print(str(45))  # '45'
print(type(3.14))  # <class 'float'>
print(isinstance(3, str))  # False
```

## Summary

- Scope controls where variables are accessible
- Python resolves names using **LEGB**: Local → Enclosing → Global → Built-in
- `nonlocal` is used to modify variables in enclosing scope
- `global` is used to create or modify global variables inside functions
