# What Are Special Methods and What Are They Used For?

Special methods in Python, also known as magic methods or dunder methods, are methods that start and end with double underscores (`__`).

The word dunder comes from double underscores.

You have probably used special methods already without noticing. Every time you write something like `3 + 4`, Python runs `3.__add__(4)` under the hood.

So while you can call special methods directly, you usually should not. Writing `3 + 4` is much clearer than calling `3.__add__(4)` yourself.

Apart from `__add__`, `__init__()` is another special method you will use often, because it initializes objects.

Other common special methods include `__len__()` and `__str__()`.

Think of special methods as the bridge between your code and Python's interpreter.

You do not usually call them directly. Python automatically calls them when certain actions happen.

These actions include:

- Arithmetic operations like addition, subtraction, multiplication, and division (`__add__()`, `__sub__()`, `__mul__()`, `__truediv__()`).
- String operations like concatenation, repetition, formatting, and conversion to text (`__add__()`, `__mul__()`, `__format__()`, `__str__()`, `__repr__()`).
- Comparison operations like equality, less-than, and greater-than (`__eq__()`, `__lt__()`, `__gt__()`).
- Iteration operations like creating iterators and moving through them (`__iter__()`, `__next__()`).

Built-in Python types like strings and numbers already implement many special methods.

But when you create your own classes, Python does not know how those operations should behave unless you define the special methods yourself.

That is where special methods help: they let you customize built-in behavior.

For example, suppose you want to get the number of pages in `Book` objects, compare books, and print a readable string. Without special methods:

```python
class Book:
	def __init__(self, title, pages):
		self.title = title
		self.pages = pages


book1 = Book('Built Wealth Like a Boss', 420)
book2 = Book('Be Your Own Start', 420)

print(len(book1))      # TypeError: object of type 'Book' has no len()
print(str(book1))      # <__main__.Book object at 0x...>
print(book1 == book2)  # False even though they have the same number of pages
```

In this example:

- `len(book1)` fails because Python does not know how to get length without `__len__()`.
- `str(book1)` prints the default object representation because `__str__()` is missing.
- `book1 == book2` is `False` because Python compares object identity by default, not content.

Here is how to define `__len__()`, `__str__()`, and `__eq__()` for the `Book` class:

```python
class Book:
	def __init__(self, title, pages):
		self.title = title
		self.pages = pages

	def __len__(self):
		return self.pages

	def __str__(self):
		return f"'{self.title}' has {self.pages} pages"

	def __eq__(self, other):
		return self.pages == other.pages


book1 = Book('Built Wealth Like a Boss', 420)
book2 = Book('Be Your Own Start', 420)

print(len(book1))      # 420
print(len(book2))      # 420
print(str(book1))      # 'Built Wealth Like a Boss' has 420 pages
print(str(book2))      # 'Be Your Own Start' has 420 pages
print(book1 == book2)  # True
```

Another example is a shopping cart.

You might want to:

- Add items
- Remove items
- Get number of items
- Loop through items
- Check if a specific item exists
- Access an item by index

Regular methods can handle add/remove, while special methods can support the built-in operations:

- `__len__()` to get number of items
- `__iter__()` to loop through items
- `__contains__()` to check membership with `in`
- `__getitem__()` to access items by index

Example `Cart` class:

```python
class Cart:
	def __init__(self):
		self.items = []

	def add(self, item):
		self.items.append(item)

	def remove(self, item):
		if item in self.items:
			self.items.remove(item)
		else:
			print(f'{item} is not in cart')

	def list_items(self):
		return self.items

	def __len__(self):
		return len(self.items)

	def __getitem__(self, index):
		return self.items[index]

	def __contains__(self, item):
		return item in self.items

	def __iter__(self):
		return iter(self.items)
```

Using the class:

```python
cart = Cart()
cart.add('Laptop')
cart.add('Wireless mouse')
cart.add('Ergo keyboard')
cart.add('Monitor')

for item in cart:
	print(item, end=' ')  # Laptop Wireless mouse Ergo keyboard Monitor

print(len(cart))          # 4
print(cart[3])            # Monitor

print('Monitor' in cart)  # True
print('banana' in cart)   # False

cart.remove('Ergo keyboard')
print(cart.list_items())  # ['Laptop', 'Wireless mouse', 'Monitor']

cart.remove('banana')     # banana is not in cart
```

These are practical ways special methods make your classes easier and more natural to use.
