# What Are Some Common String Methods?

Python provides many built-in string methods that make working with text straightforward. Here are the most common ones.

## `upper()`

Returns a new string with all characters converted to uppercase.

```python
my_str = 'hello world'

uppercase_my_str = my_str.upper()
print(uppercase_my_str)  # HELLO WORLD
```

## `lower()`

Returns a new string with all characters converted to lowercase.

```python
my_str = 'Hello World'

lowercase_my_str = my_str.lower()
print(lowercase_my_str)  # hello world
```

## `strip()`

Returns a new string with leading and trailing characters removed. Without an argument, it removes whitespace.

```python
my_str = '  hello world  '

trimmed_my_str = my_str.strip()
print(trimmed_my_str)  # hello world
```

## `replace(old, new)`

Returns a new string with all occurrences of `old` replaced by `new`.

```python
my_str = 'hello world'

replaced_my_str = my_str.replace('hello', 'hi')
print(replaced_my_str)  # hi world
```

## `split(separator)`

Splits a string on a specified separator and returns a list. If no separator is given, it splits on whitespace.

```python
my_str = 'hello world'

split_words = my_str.split()
print(split_words)  # ['hello', 'world']
```

## `join(iterable)`

Joins elements of an iterable into a single string using a separator.

```python
my_list = ['hello', 'world']

joined_my_str = ' '.join(my_list)
print(joined_my_str)  # hello world
```

## `startswith(prefix)`

Returns `True` if the string starts with the given prefix, otherwise `False`.

```python
my_str = 'hello world'

starts_with_hello = my_str.startswith('hello')
print(starts_with_hello)  # True
```

## `endswith(suffix)`

Returns `True` if the string ends with the given suffix, otherwise `False`.

```python
my_str = 'hello world'

ends_with_world = my_str.endswith('world')
print(ends_with_world)  # True
```

## `find(substring)`

Returns the index of the first occurrence of `substring`, or `-1` if not found.

```python
my_str = 'hello world'

world_index = my_str.find('world')
print(world_index)  # 6
```

## `count(substring)`

Returns the number of times a substring appears in the string.

```python
my_str = 'hello world'

o_count = my_str.count('o')
print(o_count)  # 2
```

## `capitalize()`

Returns a new string with the first character capitalized and all others lowercased.

```python
my_str = 'hello world'

capitalized_my_str = my_str.capitalize()
print(capitalized_my_str)  # Hello world
```

## `isupper()`

Returns `True` if all letters in the string are uppercase, otherwise `False`.

```python
my_str = 'hello world'

is_all_upper = my_str.isupper()
print(is_all_upper)  # False
```

## `islower()`

Returns `True` if all letters in the string are lowercase, otherwise `False`.

```python
my_str = 'hello world'

is_all_lower = my_str.islower()
print(is_all_lower)  # True
```

## `title()`

Returns a new string with the first letter of each word capitalized.

```python
my_str = 'hello world'

title_case_my_str = my_str.title()
print(title_case_my_str)  # Hello World
```
