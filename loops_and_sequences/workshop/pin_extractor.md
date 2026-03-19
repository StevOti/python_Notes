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
