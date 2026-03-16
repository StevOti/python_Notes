# Truthy and Falsy Values, Boolean Operators, and Short-Circuiting

In the previous lesson, you learned how comparison operators and conditional statements control program flow.

As your logic gets more complex, nested conditionals can become hard to read. For example:

```python
is_citizen = True
age = 25

if is_citizen:
	if age >= 18:
		print('You are eligible to vote')  # You are eligible to vote
else:
	print('You are not eligible to vote')
```

To write cleaner logic, Python provides the boolean operators `and`, `or`, and `not`.

## Truthy and Falsy Values

In Python, every value has an inherent boolean meaning when used in a logical context.

- **Truthy values** evaluate to `True`
- **Falsy values** evaluate to `False`

Common falsy values include:

- `None`
- `False`
- `0` (integer)
- `0.0` (float)
- `""` (empty string)

Most other values, including non-zero numbers and non-empty strings, are truthy.

### Checking Truthiness with `bool()`

Use `bool()` to explicitly convert a value to `True` or `False`.

```python
print(bool(False))   # False
print(bool(0))       # False
print(bool(''))      # False

print(bool(True))    # True
print(bool(1))       # True
print(bool('Hello')) # True
```

## Boolean Operators

Python has three boolean operators:

- `and`
- `or`
- `not`

These operators help combine or invert conditions for more expressive decision-making.

## The `and` Operator

`and` returns the first operand if it is falsy; otherwise, it returns the second operand.

An `and` expression is truthy only if **both operands** are truthy.

```python
is_citizen = True
age = 25

print(is_citizen and age)  # 25
```

In this case, `is_citizen` is truthy, so Python returns `age`.

### `and` in a Conditional

```python
is_citizen = True
age = 25

if is_citizen and age >= 18:
	print('You are eligible to vote')  # You are eligible to vote
else:
	print('You are not eligible to vote')
```

Both conditions are true, so the `if` block executes.

## The `or` Operator

`or` returns the first operand if it is truthy; otherwise, it returns the second operand.

An `or` expression is truthy if **at least one operand** is truthy.

```python
age = 19
is_employed = False

print(age or is_employed)  # 19
```

Since `age` is truthy, Python returns it immediately.

### `or` in a Conditional

```python
age = 19
is_student = True

if age < 18 or is_student:
	print('You are eligible for a student discount')  # You are eligible for a student discount
else:
	print('You are not eligible for a student discount')
```

`age < 18` is false, but `is_student` is true, so the condition is true overall.

## The `not` Operator

`not` takes one operand and flips its truth value.

- Truthy becomes `False`
- Falsy becomes `True`

Unlike `and` and `or`, `not` always returns a boolean (`True` or `False`).

```python
print(not '')       # True
print(not 'Hello')  # False
print(not 0)        # True
print(not 1)        # False
print(not False)    # True
print(not True)     # False
```

### `not` in a Conditional

```python
is_admin = False

if not is_admin:
	print('Access denied for non-administrators.')  # Access denied for non-administrators.
else:
	print('Welcome, Administrator!')
```

Because `is_admin` is `False`, `not is_admin` becomes `True`, so the first message is printed.

## Short-Circuiting

Both `and` and `or` use short-circuit evaluation:

- Python evaluates operands from left to right
- It stops as soon as the final result is known

For `and`:

- If the left side is falsy, Python stops and returns it

For `or`:

- If the left side is truthy, Python stops and returns it

This behavior can make code faster and avoid unnecessary checks.

## Summary

You now understand:

- Truthy and falsy values
- How to check truthiness with `bool()`
- How `and`, `or`, and `not` work
- How short-circuiting affects expression evaluation

These concepts help you write cleaner, more flexible, and more readable conditional logic.
