# Employee Profile Generator Workshop

## Step 1

Strings are sequences of characters used to store text data. As you might recall from previous lessons, you can create a string by enclosing text inside either single (`'`) or double (`"`) quotes.

For example:

### Example Code

```python
greeting = 'Hello'
print(greeting)  # Output: Hello
```

Create a variable `first_name` which stores the string `John` and a variable `last_name` which stores the string `Doe`. Then print `first_name` and `last_name`.

## Step 2

In Python, you can combine strings using the `+` operator. This is called concatenation.

Here is an example:

### Example Code

```python
greeting = 'Hello' + 'World'
print(greeting)  # Output: HelloWorld
```

Create a variable `full_name` by concatenating `first_name` and `last_name`. Then print `full_name`.

## Step 3

If you concatenate two strings like `'John' + 'Doe'`, the result is `'JohnDoe'` with no space. To fix this, you need to concatenate a string containing a space (`' '`) between them.

Update your `full_name` variable so it concatenates `first_name`, a space, and `last_name`.

## Step 4

Next, create a variable `address` to store the employee's address. Assign it the string `123 Main Street`, and finally print `address`.

## Step 5

Now, your address seems incomplete. You also want to add the apartment number where the employee lives, so you should modify the variable.

When you want to add content to the end of an existing string variable, you can use the augmented assignment operator `+=`. This is shorter than writing `var = var + 'new text'`.

For example:

### Example Code

```python
greeting = 'Hello'
greeting += ' World'
print(greeting)  # Hello World
```

Remember that strings are immutable, therefore this operation does not change the original string. Instead it creates a new string and reassigns it to the variable.

Use the `+=` operator to add the string `, Apartment 4B` to your `address` variable.

## Step 6

The output in the terminal is getting crowded. Before you continue, it's time to clean it up.

Remove all the `print()` statements from your code.

## Step 7

Now create a variable named `employee_age` and assign it the integer `28`.

## Step 8

Now, you want to create a string that displays the employee's age.

Start by creating a variable `employee_info` and assign it the result of concatenating:

- the `full_name` variable.
- a string consisting of the characters `is` preceded and followed by a space.

## Step 9

Now try to concatenate `employee_age` to the end of your `employee_info` string.

Once you've done so, you'll see a `TypeError` in the terminal. In the next step, you'll work on fixing it.

## Step 10

As you can see Python raised a `TypeError: can only concatenate str (not "int") to str`. This happens because Python does not allow you to concatenate text (strings) and numbers (integers) directly.

To fix this, you must convert the number to a string first using the `str()` function, which returns the string version of an object:

### Example Code

```python
my_num = str(42)
print(type(my_num))  # <class 'str'>
```

Update your `employee_info` assignment to convert `employee_age` to a string using `str(employee_age)`.

## Step 11

Now complete the sentence by concatenating the string ` years old` to the end of `employee_info`. Remember to include a space at the beginning of your string.

Finally, print `employee_info`.

## Step 12

Now you're going to use the `str()` function one more time. Just like with age, you must convert any numeric variable to a string before concatenating it with other text.

Create a variable named `experience_years` and assign it the integer `5`.

Then, create a variable `experience_info`. Assign it a string formed by concatenating `'Experience: '`, the `experience_years` variable (converted to a string), and `' years'`. Print the result to the terminal.

## Step 13

Concatenating many strings using `+` and converting numbers using `str()` can get messy and hard to read.

Python 3.6 introduced f-strings to solve this. By adding the letter `f` before the opening quote, you can put variables and expressions inside replacement fields represented by curly braces `{}`.

For example:

### Example Code

```python
name = 'John'
print(f'Hello {name}')  # Output: Hello John
```

Create a variable `employee_card` and assign it an f-string that displays `Employee:` followed by a space and the value of the `full_name` variable.

## Step 14

Currently, `employee_card` only shows the employee's name. Now you're going to add more information to it.

Update the `employee_card` assignment to include the employee's age. The final string should look like this: `Employee: [name] | Age: [age]` with `[name]` replaced with the employee's name, and `[age]` replaced with the employee's age.

## Step 15

Now it's time to add the final details to the card.

Create a variable named `position` with the value of the string `Data Analyst` and a variable named `salary` with the value of the integer `75000`.

Then, update your `employee_card` f-string to include the position and salary. It should follow this exact format: `Employee: [full_name] | Age: [employee_age] | Position: [position] | Salary: $[salary]`. Replace the placeholders with the corresponding variables.

Finally, print `employee_card` to see the result.
