# Dictionaries and Sets Review

## Dictionaries

### Dictionaries
Dictionaries are built-in data structures that store collections of key-value pairs. Keys need to be immutable data types.

```python
dictionary = {
	key1: value1,
	key2: value2
}
```

### `dict()` Constructor
The `dict()` constructor is an alternative way to build a dictionary by passing a list of tuples.

```python
pizza = dict([
	('name', 'Margherita Pizza'),
	('price', 8.9),
	('calories_per_slice', 250),
	('toppings', ['mozzarella', 'basil'])
])
```

### Bracket Notation
To access the value of a key-value pair, use bracket notation.

```python
dictionary[key]
```

## Common Dictionary Methods

### `get()` Method
Retrieves the value associated with a key, optionally with a default value.

```python
dictionary.get(key, default)
```

### `keys()` and `values()` Methods
Return view objects with all keys or all values in the dictionary.

```python
pizza = {
	'name': 'Margherita Pizza',
	'price': 8.9,
	'calories_per_slice': 250
}

pizza.keys()
# dict_keys(['name', 'price', 'calories_per_slice'])

pizza.values()
# dict_values(['Margherita Pizza', 8.9, 250])
```

### `items()` Method
Returns a view object with all key-value pairs.

```python
pizza.items()
# dict_items([('name', 'Margherita Pizza'), ('price', 8.9), ('calories_per_slice', 250)])
```

### `clear()` Method
Removes all key-value pairs from the dictionary.

```python
pizza.clear()
```

### `pop()` Method
Removes the key-value pair with the given key and returns its value.

```python
pizza.pop('price', 10)
pizza.pop('total_price')  # KeyError
```

### `popitem()` Method
In Python 3.7+, removes the last inserted key-value pair.

```python
pizza.popitem()
```

### `update()` Method
Updates dictionary entries from another dictionary.

```python
pizza.update({'price': 15, 'total_time': 25})
```

## Looping Over a Dictionary

### Iterating Over Values

```python
products = {
	'Laptop': 990,
	'Smartphone': 600,
	'Tablet': 250,
	'Headphones': 70,
}

for price in products.values():
	print(price)

# 990
# 600
# 250
# 70
```

### Iterating Over Keys

```python
for product in products.keys():
	print(product)

# Or

for product in products:
	print(product)

# Laptop
# Smartphone
# Tablet
# Headphones
```

### Iterating Over Key-Value Pairs

```python
for product in products.items():
	print(product)

# ('Laptop', 990)
# ('Smartphone', 600)
# ('Tablet', 250)
# ('Headphones', 70)
```

```python
for product, price in products.items():
	print(product, price)

# Laptop 990
# Smartphone 600
# Tablet 250
# Headphones 70
```

### `enumerate()` Function
Use `enumerate()` to keep track of a counter while iterating.

```python
for index, product in enumerate(products.items()):
	print(index, product)

# 0 ('Laptop', 990)
# 1 ('Smartphone', 600)
# 2 ('Tablet', 250)
# 3 ('Headphones', 70)
```

```python
for index, product in enumerate(products.items(), 1):
	print(index, product)

# 1 ('Laptop', 990)
# 2 ('Smartphone', 600)
# 3 ('Tablet', 250)
# 4 ('Headphones', 70)
```

## Sets

### Sets
Sets are built-in data structures that do not allow duplicate values. Sets are mutable and unordered. Elements must be immutable types.

### Defining a Set

```python
my_set = {1, 2, 3, 4, 5}
```

### Defining an Empty Set

```python
set()  # Set
{}     # Dictionary
```

## Common Set Methods

### `add()` Method

```python
my_set.add(6)
```

### `remove()` and `discard()` Methods

```python
my_set.remove(4)
my_set.discard(4)
```

### `clear()` Method

```python
my_set.clear()
```

## Mathematical Set Operations

### `issubset()` and `issuperset()` Methods

```python
my_set = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 5}

print(your_set.issubset(my_set))    # True
print(my_set.issuperset(your_set))  # True
```

### `isdisjoint()` Method

```python
my_set = {1, 2, 3}
your_set = {4, 5, 6}

print(my_set.isdisjoint(your_set))  # True
```

### Union Operator (`|`)

```python
my_set = {1, 2, 3}
your_set = {4, 5, 6}

my_set | your_set  # {1, 2, 3, 4, 5, 6}
```

### Intersection Operator (`&`)

```python
my_set = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 6}

my_set & your_set  # {2, 3, 4}
```

### Difference Operator (`-`)

```python
my_set = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 6}

my_set - your_set  # {1, 5}
```

### Symmetric Difference Operator (`^`)

```python
my_set = {1, 2, 3, 4, 5}
your_set = {2, 3, 4, 6}

my_set ^ your_set  # {1, 5, 6}
```

### `in` Operator

```python
print(5 in my_set)  # True
```

## Python Standard Library

### Python Standard Library
A library gives you pre-written and reusable code (functions, classes, and data structures). Python has an extensive standard library with built-in modules such as `math`, `random`, `re`, and `datetime`.

## Import Statement

### Import Statement
To access built-in module elements, use `import` statements, usually at the top of the file.

### Basic Import Statement

```python
import module_name
```

Call module members with dot notation:

```python
module_name.function_name()
```

```python
import math

math.sqrt(36)
```

### Importing a Module with a Different Name

```python
import module_name as module_alias
```

```python
import math as m
m.sqrt(36)
```

### Importing Specific Elements

```python
from module_name import name1, name2
```

```python
from math import radians, sin, cos

angle_degrees = 40
angle_radians = radians(angle_degrees)

sine_value = sin(angle_radians)
cos_value = cos(angle_radians)

print(sine_value)  # 0.6427876096865393
print(cos_value)   # 0.766044443118978
```

You can also alias imported names:

```python
from module_name import name1 as alias1, name2 as alias2
```

### Import Statement with Asterisk (`*`)

```python
from module_name import *
```

```python
from math import *
print(sqrt(36))  # 6.0
```

This is generally discouraged because it can cause namespace collisions.

## `if __name__ == '__main__'`

### `__name__` Variable
`__name__` is a special built-in variable.

- If a file is executed directly, `__name__ == '__main__'`.
- If a file is imported, `__name__` is set to the module name.

```python
if __name__ == '__main__':
	# Code
```

