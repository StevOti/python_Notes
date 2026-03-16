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

## Step 10
In Python, the `and` operator is used to check if multiple conditions are true. Here's how you can use it to combine two conditions in an `if` statement:

```python
if condition1 and condition2:
	# Code to execute if all conditions are True
```

The membership discount should only apply to members if their age is greater than or equal to `21`.

Update the condition of the `if is_member:` line by using the `and` operator to combine the existing condition with another condition checking if `age` is greater than or equal to `21`.

## Step 11
Now change the value of the `is_member` variable to `False` as the user is not a member.

After that, you will see that the `discount` value now remains `0`, because both conditions must be satisfied for the discount to apply.

## Step 12
Now create a variable named `extra_charges` and set it to `0`. This will represent extra charges to apply to the movie ticket on weekends.

Then, create an `if` statement to check if `is_weekend` is truthy. Inside the body of `if` statement, update the `extra_charges` value to `2` and print `Extra charges will be applied` in the terminal.

## Step 13
Now, add an `else` clause to your `if` statement and print `No extra charges will be applied` inside the `else` body. This will print the message only when the extra charges condition is false.

Then, below the `else` clause, use the `print()` call to display a message that shows `Extra charges:` followed by the updated value of `extra_charges` and check the output in the terminal.

## Step 14
In Python, the `or` operator is used to check whether at least one of two conditions is true. Here's how you can use it in an `if` statement:

```python
if condition1 or condition2:
	# Code to execute if any condition is True
```

Extra charges should also apply if the show is in the evening. Update the condition of the `if is_weekend:` line by using the `or` operator to combine the existing condition with a second condition checking if `show_time` is equal to the string `Evening`.

## Step 15
Now you will check if the user satisfies the conditions to book a movie ticket. Users with age `21` or above can always book tickets without any restrictions.

Create an `if` statement to check if `age` is greater than or equal to `21`. Inside the body of the `if` statement, print `Ticket booking condition satisfied` to the terminal.

Then, add an `else` clause to your `if` statement and print `Ticket booking failed due to restrictions` inside the `else` body.

## Step 16
Users between `18` and `21` can book tickets, but only when the `show_time` is not `Evening`.

Update the condition of the `if age >= 21:` line. Use the `and` operator to build an expression checking if `age` is greater than or equal to `18` and `show_time` is not `Evening`. Then use the `or` operator to combine that expression with the existing condition. Do not create new variables.

## Step 17
There is one more exception to the booking rules. Users between `18` and `21` can book evening shows if they are members.

When multiple logical operators are used in an `if` statement, conditions joined with `and` are evaluated before conditions joined with `or`. Parentheses `()` are used in Python to group conditions and control the order in which they are evaluated.

```python
if condition1 and (condition2 or condition3):
	# Code to execute if conditions evaluate to True
else:
	# Code to execute if conditions evaluate to False
```

Update the condition of the `if age >= 21 or age >= 18 and show_time != 'Evening':` line to add another condition using the `or` operator to check if `is_member` is truthy. Use parentheses `()` to group the `show_time != 'Evening'` and `is_member` conditions together as shown in the above example.

## Step 18
In Python, an `if` statement can also be placed inside the body of another `if` statement. This is called a nested `if` statement.

A nested `if` statement allows you to check an additional condition only after the first condition has already been satisfied. The inner `if` statement will run only if the outer `if` condition is true.

```python
if condition1:
	# Code to execute if condition1 is True
	if condition2:
		# Code to execute if both conditions are True
```

Now you will calculate service charges based on the type of seat the user has selected.

Inside the body of the last `if` statement, below the `print('Ticket booking condition satisfied')` line, create a variable named `service_charges` and set it to `0`. Make sure to indent your code by four spaces to keep it inside the outer `if` statement body.

Then, create a nested `if` statement to check if `seat_type` is equal to `Premium`. Inside the body of the nested `if` statement, update the `service_charges` value to `5`.

## Step 19
Still inside the body of the outer `if` statement, add an `else` clause to the nested `if seat_type == 'Premium':` statement and update the `service_charges` value to `1` inside the `else` body. Make sure to keep the `else` indented by four spaces to stay inside the outer `if` statement body.
