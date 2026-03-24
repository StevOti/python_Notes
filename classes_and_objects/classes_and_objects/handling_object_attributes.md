# How to Handle Object Attributes Dynamically?

In a previous lesson, you learned about attributes being the variables that belong to an object. That means they hold data that describes the state or behavior of the object.

For example, a car would normally have a brand and model. The brand and model could be attributes for a `Car` class:

```python
class Car:
	def __init__(self, brand, model):
		self.brand = brand
		self.model = model


my_car = Car('Lamborghini', 'Gallardo')
print(my_car.brand)  # Lamborghini
print(my_car.model)  # Gallardo
```

But sometimes, you might not know which attributes you need until your program is running. Imagine you are writing a script that receives attribute names from a user or a configuration file. Those are not attributes you can hardcode ahead of time.

That is where handling attributes dynamically comes in. This way, you can access, modify, check, or even delete attributes using their names as variables, not as fixed names in your code. This gives your program flexibility to respond to different data or user input on the fly.

Python gives you four handy built-in functions to dynamically work with object attributes:

- `getattr()`
- `setattr()`
- `hasattr()`
- `delattr()`

They let you access, create, check, and remove attributes using variable names.

## getattr()

`getattr()` makes it possible to read an attribute from an object when you do not know its name until runtime.

If the attribute does not exist, it raises an `AttributeError`, unless you provide a default value.

Syntax:

```python
getattr(object, attribute_name, default_value)
```

Example:

```python
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age


person = Person('John Doe', 30)

print(getattr(person, 'name'))            # John Doe
print(getattr(person, 'age'))             # 30
print(getattr(person, 'city', 'Milano'))  # Milano
```

In this example, `Milano` is returned because `city` does not exist.

The real power of `getattr()` appears when the attribute name comes from a variable, such as user input or a file:

```python
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age


person = Person('John Doe', 30)

attr_name = input('Enter the attribute you want to see: ')
print(getattr(person, attr_name, 'Attribute not found'))
```

If the user enters `name`, they see `John Doe`. If they enter `age`, they see `30`. If they enter something unknown like `email`, they see `Attribute not found`.

## dir()

You may also want to inspect all attributes an object has, not just the ones you already know.

The built-in `dir()` function returns a list of all attribute names on the object.

```python
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age


person = Person('John Doe', 30)

# Loop through all attributes with dir()
for attr in dir(person):
	# Ignore dunder methods and regular methods
	if not attr.startswith('__') and not callable(getattr(person, attr)):
		value = getattr(person, attr)
		print(f'{attr}: {value}')

# Output
# age: 30
# name: John Doe
```

## setattr()

`setattr()` lets you create a new attribute or update an existing one dynamically.

Syntax:

```python
setattr(object, attribute_name, value)
```

Example setting configuration values at runtime:

```python
class Configuration:
	pass


# Data loaded at runtime (for example, from config or env files)
settings_data = {
	'server_url': 'https://api.example.com',
	'timeout_sec': 30,
	'max_retries': 5,
}

config_obj = Configuration()

# Dynamically set attributes
for attr_name, attr_value in settings_data.items():
	setattr(config_obj, attr_name, attr_value)

print(config_obj.server_url)   # https://api.example.com
print(config_obj.timeout_sec)  # 30
```

## hasattr()

Before using or deleting an attribute, it is a good practice to check if it exists.

`hasattr()` checks whether an attribute exists and returns `True` or `False`.

Syntax:

```python
hasattr(object, attribute_name)
```

Example:

```python
class Product:
	def __init__(self, name, price):
		self.name = name
		self.price = price


product_a = Product('T-Shirt', 25)

required_attributes = ['name', 'price', 'inventory_id']

for attr in required_attributes:
	if not hasattr(product_a, attr):
		print(f"ERROR: Product is missing the required attribute: '{attr}'")
	else:
		print(f'{attr}: {getattr(product_a, attr)}')

# Output:
# name: T-Shirt
# price: 25
# ERROR: Product is missing the required attribute: 'inventory_id'
```

The error output occurs because `inventory_id` is missing from the `Product` instance.

## delattr()

`delattr()` lets you remove an attribute dynamically.

Syntax:

```python
delattr(object, attribute_name)
```

Example cleanup of sensitive and temporary attributes:

```python
class UserSession:
	def __init__(self, user_id, token):
		self.user_id = user_id
		self.auth_token = token  # sensitive
		self.temp_counter = 0    # temporary


session = UserSession(101, 'a1b2c3d4e5')

# Attributes to remove before saving
attributes_to_clean = ['auth_token', 'temp_counter']

for attr in attributes_to_clean:
	if hasattr(session, attr):
		delattr(session, attr)
		print(f'Removed attribute: {attr}')

print('\nFinal attributes remaining:')

for attr in dir(session):
	if not attr.startswith('__') and not callable(getattr(session, attr)):
		print(f' - {attr}: {getattr(session, attr)}')

# Output:
# Removed attribute: auth_token
# Removed attribute: temp_counter
#
# Final attributes remaining:
#  - user_id: 101
```

And that is how you can handle object attributes dynamically in Python.
