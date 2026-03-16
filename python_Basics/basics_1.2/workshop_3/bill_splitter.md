# Bill Splitter Workshop

## Step 1

In this workshop, you will practice working with numbers and mathematical operations to build a bill splitter. This tool will calculate how much each person owes after adding meal costs and a tip.

To start, you need a way to keep track of the total amount as costs are added. In Python, you can use a variable to store an integer (a whole number) that changes over time.

For example, you might write:

```python
my_number = 2
```

Create a variable named `running_total` and assign it the value `0`.

## Step 2

Next, you need to account for the number of people sharing the bill. Store this value in a variable, as you did in the previous step.

Create a variable named `num_of_friends` and assign it the value of `4`. This will be used later in the workshop to calculate the final split.

## Step 3

Each course has a cost. You need to store these amounts in variables to use them later. Since these amounts include cents, you will use the `float` type, which is used to represent decimal numbers.

Here's an example of a variable with a float value:

### Example Code

```python
change = 2.35
```

Create four variables: `appetizers` set to `37.89`, `main_courses` set to `57.34`, `desserts` set to `39.39`, and `drinks` set to `64.21`.
## Step 4
Now that you have stored the individual costs, you can calculate the total. In Python, you use the addition operator `+` to sum values together.

The `+=` operator adds a value to an existing variable and updates it at the same time. For example:

```python
total = 10
total += 2 + 2 + 1
print(total)  # total is now 15
```

Use the `+=` operator once to add `appetizers`, `main_courses`, `desserts`, and `drinks` to `running_total`.

Finally, use `print()` to display the string `Total bill so far:` followed by a space and the value of `running_total`.

> **Note:** You might notice that the output has more decimal digits than expected. As you learned in a previous lesson, this happens because numbers are stored in binary, and many decimal values cannot be represented exactly in this format, which leads to rounding errors.