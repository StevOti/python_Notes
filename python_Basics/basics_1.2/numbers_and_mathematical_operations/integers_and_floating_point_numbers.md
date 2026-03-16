# How Do You Work With Integers and Floating Point Numbers?

Integers and floats are the primary numeric data types in Python. You can use them to store numbers and perform mathematical operations.

This lesson covers:

- what integers and floats are
- arithmetic operations with both
- mixed operations between ints and floats
- modulo, floor division, and exponentiation
- numeric type conversion with `int()` and `float()`
- useful built-in functions like `round()`, `abs()`, and `pow()`

## Integers (`int`)

Integers are whole numbers (positive, negative, or zero) with no decimal point.

```python
my_int_1 = 56
my_int_2 = -4

print(type(my_int_1))  # <class 'int'>
print(type(my_int_2))  # <class 'int'>
```

### Integer arithmetic

#### Addition

```python
my_int_1 = 56
my_int_2 = 12

sum_ints = my_int_1 + my_int_2
print('Integer Addition:', sum_ints)  # Integer Addition: 68
```

#### Subtraction

```python
my_int_1 = 56
my_int_2 = 12

diff_ints = my_int_1 - my_int_2
print('Integer Subtraction:', diff_ints)  # Integer Subtraction: 44
```

#### Multiplication

```python
my_int_1 = 12
my_int_2 = 4

product_ints = my_int_1 * my_int_2
print('Integer Multiplication:', product_ints)  # Integer Multiplication: 48
```

#### Division

```python
my_int_1 = 56
my_int_2 = 12

div_ints = my_int_1 / my_int_2
print('Integer Division:', div_ints)  # Integer Division: 4.666666666666667
```

## Floating-point numbers (`float`)

Floats are numbers with decimal points, such as `3.14`, `-0.5`, and `0.0`.

```python
my_float_1 = -12.0
my_float_2 = 4.9

print(type(my_float_1))  # <class 'float'>
print(type(my_float_2))  # <class 'float'>
```

### Float arithmetic

#### Addition

```python
my_float_1 = 5.4
my_float_2 = 12.0

float_addition = my_float_1 + my_float_2
print('Float Addition:', float_addition)  # Float Addition: 17.4
```

#### Subtraction

```python
my_float_1 = 5.4
my_float_2 = 12.0

float_subtraction = my_float_2 - my_float_1
print('Float Subtraction:', float_subtraction)  # Float Subtraction: 6.6
```

#### Multiplication

```python
my_float_1 = 5.4
my_float_2 = 12.0

float_multiplication = my_float_2 * my_float_1
print('Float Multiplication:', float_multiplication)  # Float Multiplication: 64.80000000000001
```

#### Division

```python
my_float_1 = 5.4
my_float_2 = 12.0

float_division = my_float_2 / my_float_1
print('Float Division:', float_division)  # Float Division: 2.222222222222222
```

## Mixing integers and floats

When an operation mixes an `int` and a `float`, Python returns a `float`.

```python
my_int = 56
my_float = 5.4

sum_int_and_float = my_int + my_float

print(sum_int_and_float)        # 61.4
print(type(sum_int_and_float))  # <class 'float'>
```

This behavior applies to subtraction, multiplication, and division too.

## Additional arithmetic operators

### Modulo (`%`)

Returns the remainder of division.

```python
my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

mod_ints = my_int_1 % my_int_2
mod_floats = my_float_2 % my_float_1

print('Integer Modulo:', mod_ints)  # Integer Modulo: 8
print('Float Modulo:', mod_floats)  # Float Modulo: 1.1999999999999993
```

### Floor division (`//`)

Divides numbers and returns the greatest integer less than or equal to the result.

```python
my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

floor_div_ints = my_int_1 // my_int_2
floor_div_floats = my_float_2 // my_float_1

print('Integer Floor Division:', floor_div_ints)  # Integer Floor Division: 4
print('Float Floor Division:', floor_div_floats)  # Float Floor Division: 2.0
```

### Exponentiation (`**`)

Raises a base number to a power.

```python
my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

exp_ints = my_int_1 ** my_int_2
exp_floats = my_float_1 ** my_float_2

print('Integer Exponentiation:', exp_ints)    # Integer Exponentiation: 951166013805414055936
print('Float Exponentiation:', exp_floats)    # Float Exponentiation: 614787626.1765089
```

## Why float results can look odd

Sometimes float arithmetic produces more decimal digits than expected:

```python
print(0.1 + 0.2)  # 0.30000000000000004
```

This happens because many decimal fractions cannot be represented exactly in binary, so Python stores close approximations, which can introduce small rounding errors.

## Type conversion with `float()` and `int()`

### `float()`

Converts a number (or valid numeric string) to a float.

```python
my_int_1 = 56
my_float_1 = float(my_int_1)

print(my_float_1)        # 56.0
print(type(my_float_1))  # <class 'float'>
```

### `int()`

Converts a number (or valid integer string) to an integer.

```python
my_float = 12.92563
my_int = int(my_float)

print(my_int)        # 12
print(type(my_int))  # <class 'int'>
```

## Converting strings to numbers

```python
my_str_int = '45'
my_str_float = '7.8'

converted_int = int(my_str_int)
converted_float = float(my_str_float)

print(converted_int, type(converted_int))      # 45 <class 'int'>
print(converted_float, type(converted_float))  # 7.8 <class 'float'>
```

## Common numeric built-in functions

### `round()`

Rounds a number. By default, it rounds to the nearest integer.

```python
my_int_1 = 4.798
my_int_2 = 4.253

rounded_int_1 = round(my_int_1)
rounded_int_2 = round(my_int_2, 1)

print(rounded_int_1)  # 5
print(rounded_int_2)  # 4.3
```

### `abs()`

Returns the absolute value.

```python
num = -15

absolute_value = abs(num)
print(absolute_value)  # 15
```

### `pow()`

Raises a number to a power, or performs modular exponentiation.

```python
result_1 = pow(2, 3)      # Equivalent to 2 ** 3
print(result_1)           # 8

result_2 = pow(2, 3, 5)   # (2 ** 3) % 5
print(result_2)           # 3
```
