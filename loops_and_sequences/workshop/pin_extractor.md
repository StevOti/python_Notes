# Pin Extractor Workshop

## Step 1
In this workshop you will create a pin extractor, the pin digits are hidden in each line of a poem.

Start by creating a function called `pin_extractor` with a parameter `poem`. An empty function gives an error, so add `pass` inside the function momentarily to make it valid.

## Step 2
You will need a variable to hold the secret code while you decode it, so remove `pass` and create a variable called `secret_code` inside the function and assign to it an empty string.

## Step 3
While you work on the function it would be useful to have a function call for debugging purposes, so create a `poem` variable, outside the function, that contains this poem:

```python
Stars and the moon
shine in the sky
white and bright
until the end of the night
```

You can use a multi-line string for that.

And then, call the function with the `poem` variable as argument.

## Step 4
Now that you have added a function call you can see any error created inside the function in the terminal, and you can always use `print` to see the value of things.

There is a digit of the pin hidden in every line, so inside the function use the `split` method to divide the string in a list of lines. Split the lines on the newline character (`\n`), and assign the resulting list to a variable called `lines`.

## Step 5
You need to work on each line independently: create a loop over `lines` that uses `line` as loop variable. Inside the loop, `print(line)`.

## Step 6
The nth digit of the pin is hidden as the length of the nth word in the nth line.

To find the length of the nth word, the next step is to separate the line of the poem into a list of words: inside the loop, create a variable `words` and assign to it the value of `line` split into words using the `split` method.

Then, add a `print` call with `words` as its argument.

## Step 7
As you learned in a previous lesson, the `enumerate` function allows to keep track of the index while looping over an iterable:

```python
fruits = ['apple', 'plum', 'bananas']

for index, item in enumerate(fruits):
	print(index, item)

# 0 apple
# 1 plum
# 2 bananas
```

The nth digit of the secret code comes from the nth word of the nth line, so you need to know what is the number of each line.

Change the loop so that it iterates on `enumerate(lines)`, and add another loop variable before `line` named `line_index`.

Also, update the `print` call to `print(line_index, line)`.
