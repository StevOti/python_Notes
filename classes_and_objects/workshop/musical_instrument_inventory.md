## Step 1

In this workshop, you'll get some practice with Python's classes and objects by building a musical instrument inventory.

To define a class in Python, use the `class` keyword followed by the class name and a colon.

```python
class ClassName:
	# class contents go here
```

Remember that in Python, class names typically use PascalCase, which means each word starts with an uppercase letter with no spaces between words.

Start by creating a class called `MusicalInstrument`. Add `pass` as the body of the class for now.

## Step 2

Methods are functions defined inside a class that can perform actions using the class's data. Here is how you create methods:

```python
def method_name(parameter1, parameter2, ...):
	# Method contents will go here
```

In Python, the `__init__` method is a special method known as the initializer method, which is called when you create a new instance of the class.

Inside your `MusicalInstrument` class, add an `__init__` method with three parameters: `self`, `name`, and `instrument_type`.

The `self` parameter is a standard way to refer to the instance of the class and is required as the first parameter for all instance methods in a class.
