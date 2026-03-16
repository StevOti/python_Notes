# What Is String Slicing and How Does It Work?

In a previous lesson, you learned how each character in a string can be identified by its index (starting from zero) and accessed using bracket notation:

```python
my_str = "Hello world"

print(my_str[0])   # H
print(my_str[6])   # w
print(my_str[-1])  # d
```

## What is string slicing?

String slicing lets you extract a portion of a string using a start and stop index.

### Basic syntax

```python
string[start:stop]
```

The `stop` index is **non-inclusive**, meaning the character at that index is not included in the result.

### Example Code

```python
my_str = 'Hello world'
print(my_str[1:4])  # ell
```

This extracts characters from index `1` up to, but not including, index `4`.

## Omitting start or stop

You can omit either index and Python will use sensible defaults.

### Omit the start index (defaults to `0`)

```python
my_str = 'Hello world'
print(my_str[:7])  # Hello w
```

### Omit the stop index (defaults to end of string)

```python
my_str = 'Hello world'
print(my_str[8:])  # rld
```

### Omit both (extracts the full string)

```python
my_str = 'Hello world'
print(my_str[:])  # Hello world
```

## Slicing does not modify the original string

```python
my_str = 'Hello world'
print(my_str[8:])  # rld
print(my_str)      # Hello world
```

The original string remains unchanged because strings are immutable.

## The step parameter

There is also an optional third parameter — **step** — which specifies the increment between each index in the slice.

### Syntax

```python
string[start:stop:step]
```

### Example Code

```python
my_str = 'Hello world'
print(my_str[0:11:2])  # Hlowrd
```

This starts at index `0`, stops before `11`, and picks every second character.

## Reversing a string with step `-1`

Setting step to `-1` while leaving start and stop blank reverses the string:

```python
my_str = 'Hello world'
print(my_str[::-1])  # dlrow olleH
```
