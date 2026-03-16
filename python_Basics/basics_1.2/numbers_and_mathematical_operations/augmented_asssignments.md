# How Do Augmented Assignments Work?

Augmented assignment combines a binary operation with assignment in a single step.

It takes a variable, applies an operation with another value, then stores the result back into the same variable.

## Basic syntax

```python
variable <operator>= value
```

Equivalent expanded form:

```python
variable = variable <operator> value
```

## Example: addition assignment

With augmented assignment:

```python
my_var = 10
my_var += 5

print(my_var)  # 15
```

Without augmented assignment:

```python
my_var = 10
my_var = my_var + 5

print(my_var)  # 15
```

Augmented assignment is concise and reduces repetition, which can also reduce typo-related mistakes.

## Common augmented assignment operators

### Subtraction assignment (`-=`)

Subtracts the right operand from the left variable.

```python
count = 14
count -= 3

print(count)  # 11
```

### Multiplication assignment (`*=`)

Multiplies the left variable by the right operand.

```python
product = 65
product *= 7

print(product)  # 455
```

### Division assignment (`/=`)

Divides the left variable by the right operand.

```python
price = 100
price /= 4

print(price)  # 25.0
```

### Floor division assignment (`//=`)

Floor-divides the left variable by the right operand.

```python
total_pages = 23
total_pages //= 5

print(total_pages)  # 4
```

### Modulo assignment (`%=`)

Stores the remainder of left divided by right.

```python
bits = 35
bits %= 2

print(bits)  # 1
```

### Exponentiation assignment (`**=`)

Raises the left variable to the power of the right operand.

```python
power = 2
power **= 3

print(power)  # 8
```

## Augmented assignment with strings

Some augmented assignment operators work with strings.

### String concatenation with `+=`

```python
greet = 'Hello'
greet += ' World'

print(greet)  # Hello World
```

### String repetition with `*=`

```python
greet = 'Hello'
greet *= 3

print(greet)  # HelloHelloHello
```

Other operators like `-=` and `/=` are not supported for strings and raise `TypeError`:

```python
greet = 'Hello'
greet -= ' World'

print(greet)  # TypeError: unsupported operand type(s) for -=: 'str' and 'str'
```

```python
greet = 'Hello'
greet /= 'World'

print(greet)  # TypeError: unsupported operand type(s) for /=: 'str' and 'str'
```

## About increment and decrement operators in Python

Python does not support C-style increment and decrement operators (`++` and `--`).

Instead of `x++`, use:

```python
x += 1
```

Writing `++x` in Python does not increment `x`; it applies unary plus multiple times:

```python
my_var = 5

print(+my_var)   # 5
print(++my_var)  # 5
print(+++my_var) # 5

my_var += 1

print(my_var)  # 6
```
