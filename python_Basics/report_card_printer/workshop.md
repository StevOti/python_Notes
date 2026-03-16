# Report Card Printer Workshop

## Step 1

In this workshop, you will practice Python data types by building a simple report card printer.

As you learned in previous lessons, variables are assigned in this way:

### Example Code

```python
greeting = 'Hello World'
```

In the example above, the variable `greeting` has the value of a string, which is a sequence of characters surrounded by quotes.

Create a variable called `name` and assign it the string `Alice`. Remember to surround the value with either single or double quotes as shown in the example.

**Important:** Python uses indentation (the spaces at the beginning of a line) to organize code. For this workshop, make sure there are no extra spaces at the start of each line of code. Adding extra spaces will cause an `IndentationError` and prevent your code from running.

## Step 2

You can print the value of a variable using the `print()` function.

### Example Code

```python
greeting = 'Hello World'
print(greeting)  # Output: Hello World
```

You will learn more about functions in upcoming lessons. For now, know that a function is a reusable block of code that can be called (or invoked) to run its code, and arguments can be passed to it.

In the example above, `print(greeting)` is a function call, and `greeting` is the argument of the function.

Refer to the example and print the `name` variable. Check the output in the terminal.

## Step 3

You should now see the student name printed in the terminal.

Python provides a function named `type()` that you can use to check the type of a value.

### Example Code

```python
platform = 'freeCodeCamp'
print(type(platform))  # Output: <class 'str'>
```

In the example above, the output `<class 'str'>` means that the variable passed to the `type()` function is a string.

Use the `type()` function with `name` as its argument and print the output like the example. Check the output in the terminal that shows `name` is of the type `str` (string).

## Step 4

The report card should also show whether the student is currently enrolled. This can be represented using a boolean value.

Boolean values represent a yes-or-no condition, and they are often used to make decisions in code. There are only two boolean values: `True` and `False`.

Declare a variable named `is_student` and assign it the value `True`.

## Step 5

The `print()` function can display more than one value at a time. Separate values with a comma (`,`) to print them on the same line.

### Example Code

```python
subject = 'Python'
print(subject, type(subject))  # Output: Python <class 'str'>
```

Print both `is_student` and `type(is_student)` on the same line using a comma `,` as shown in the example.

Then, check the output in the terminal that shows the value of `is_student` and its type as `bool`.

## Step 6

The student name should follow the same format as the other details.

Remove the earlier outputs of the `name` variable. Then, print `name` and `type(name)` together on one line separated by a comma, like the previous step.

## Step 7

Now you need to add the student's age to the report card. For that you'll use an integer, one of the numeric data types in Python.

Declare a variable named `age` and assign it the integer value `20`.

Then, print the value and data type of `age` together separated by a comma. Check the output in the terminal that shows the value of `age` and its type as `int` (integer).

## Step 8

Now, add the student's score.

Declare a variable named `score` and assign it the value `80.5`.

Although both `age` and `score` are numbers, they may not be the same kind. Python provides a function called `isinstance()` to check this.

### Example Code

```python
x = 10
print(isinstance(x, int))  # Output: True
```

Use `isinstance()` to check whether `score` is an `int`, and print the result to the terminal as shown in the example above.
