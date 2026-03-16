# What Are String Concatenation and String Interpolation?

When working with strings, combining different pieces of text is a very common task.

## String concatenation with `+`

In Python, you can combine multiple strings with the plus (`+`) operator. This process is called **string concatenation**.

### Example Code

```python
my_str_1 = 'Hello'
my_str_2 = "World"

str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str)  # Hello World
```

## Concatenating strings with non-strings

Concatenation with `+` only works when all parts are strings.

If you try to concatenate a string and a number directly, Python raises a `TypeError`.

### Example Code

```python
name = 'John Doe'
age = 26

name_and_age = name + age
print(name_and_age)  # TypeError: can only concatenate str (not "int") to str
```

This happens because Python does not automatically convert integers (or other non-string types) to strings during concatenation.

## Fix with `str()` conversion

Use the built-in `str()` function to convert a value to its string representation.

### Example Code

```python
name = 'John Doe'
age = 26

name_and_age = name + str(age)
print(name_and_age)  # John Doe26
```

`str()` returns a string version of the value without modifying the original object.

## Concatenation with `+=`

You can also use the augmented assignment operator `+=`, which combines concatenation and assignment in one step.

### Example Code

```python
name = 'John Doe'
age = 26

name_and_age = name
name_and_age += str(age)

print(name_and_age)  # John Doe26
```

## String interpolation with f-strings

Inserting variables and expressions into a string is called **string interpolation**.

Python supports this with **f-strings** (formatted string literals).

- Start the string with `f` (or `F`)
- Put variables/expressions inside curly braces `{}`

### Example Code

```python
name = 'John Doe'
age = 26
name_and_age = f'My name is {name} and I am {age} years old'
print(name_and_age)  # My name is John Doe and I am 26 years old

num1 = 5
num2 = 10
print(f'The sum of {num1} and {num2} is {num1 + num2}')
# The sum of 5 and 10 is 15
```

With f-strings, values like `age`, `num1`, and `num2` are converted to strings automatically during interpolation.
