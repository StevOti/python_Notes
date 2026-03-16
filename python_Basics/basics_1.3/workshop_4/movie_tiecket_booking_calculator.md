# Movie Ticket Booking Calculator Workshop

## Step 1
In this workshop, you will practice how to use booleans and conditional statements in Python by building a movie ticket booking calculator.

Begin by declaring variables that store information about the user and the movie show.

As you learned in previous lessons, variables are assigned using the assignment operator (`=`) this way:

```python
# Assigns the value 10 to variable x
x = 10
```

Create a variable named `base_price` to store the base price of the movie ticket and set its value to `15`. Create another variable named `age` to store the user's age and set its value to `21`.

## Step 2
Now you need to store some string values about the movie ticket. You can store strings in Python this way:

```python
name = 'Alice'
```

Create a variable named `seat_type` to store the type of seat the user has selected and set its value to the string `Gold`. Create another variable named `show_time` to store the show time of the movie and set its value to the string `Evening`.

Remember to surround both values with either single or double quotes.

## Step 3
As you learned in previous lessons, in Python, an `if` statement can be used to run code depending on if a condition is true.

An `if` statement consists of the `if` keyword, followed by a condition and a colon. The code to run when the condition is true, which must be indented, is called the body of the `if` statement.

```python
if condition:
	# Code to execute if condition is True
```

In this step, you will check if the user is eligible to book a movie ticket based on their age.

Create an `if` statement to check if `age` is greater than `17`. Inside the body of the `if` statement, print `User is eligible to book a ticket.` This will print the message only when the user's age is greater than `17`.

Remember to indent the body of the `if` statement and surround the message with single or double quotes inside the `print()` call.

## Step 4
Now you will check whether the user is allowed to book an evening show based on their age.

Create an `if` statement to check if `age` is greater than or equal to `21`. Inside the body of the `if` statement, print `User is eligible for Evening shows.`

## Step 5
In the previous step, you checked a condition using an `if` statement. The `else` clause is used to handle the case when the condition is false. Here's the syntax of an `if...else` statement:

```python
if condition:
	# Code to execute if condition is True
else:
	# Code to execute if condition is False
```

Now, add an `else` clause to your `if` statement and print `User is not eligible for Evening shows` inside the `else` body. This will print only when the condition in the `if` statement is false.

## Step 6
Some information can only be true or false. As you have learned in previous lessons, this can be represented using boolean values.

Create a variable named `is_member` to indicate whether the user is a member and set its value to `True`.

Below the `is_member` variable create another variable named `is_weekend` to indicate whether the movie show is on a weekend and set its value to `False`. Do not surround the value with quotes.

## Step 7
The user qualifies for a membership discount if they are a member.

Create a variable named `discount` and set its value to `0`. This will store the discount the user gets on the movie ticket.

## Step 8
In Python, `if` conditions don't have to compare values explicitly to `True` or `False`. Instead, they rely on the truthiness of values. Truthy values evaluate to `True` in a boolean context, such as the condition of an `if` statement. These include non-zero numbers, non-empty strings, and the boolean value `True`.

```python
if value:
	print('value is truthy')
```

Create an `if` statement to check if `is_member` is truthy. Inside the body of the `if` statement, update the `discount` value to `3` and print `User qualifies for membership discount` to the terminal.

## Step 9
You should also handle the case when the user does not qualify for a membership discount.

Add an `else` clause to your `if` statement and print `User does not qualify for membership discount` inside the `else` body.

You can print a message followed by a variable like this:

```python
print('Total:', total)
```

You also want to display the updated value of `discount`. Below the `if...else` statement, use the `print()` call to display a message that shows `Discount:` followed by the updated value of `discount`. Then, check the output in the terminal.
