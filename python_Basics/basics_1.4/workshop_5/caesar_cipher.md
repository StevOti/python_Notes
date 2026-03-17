# Caesar Cipher Workshop

## Step 1
As you may recall from previous lessons, in Python, you declare a variable by writing the variable name on the left side of the assignment operator (`=`) and the value to assign on the right side:

```python
variable_name = value
```

Create a variable called `shift` and assign the value `5` to your new variable.

## Step 2
In previous lessons, you learned about different data types you can store in a variable. You just assigned an integer value. Now you need to assign a string, which is a sequence of characters enclosed by either single or double quotes:

```python
string_1 = 'I am a string'
string_2 = "I am also a string"
```

Declare another variable called `alphabet` and assign the string `abcdefghijklmnopqrstuvwxyz` to this variable.

## Step 3
In this workshop, you are going to build a Caesar cipher. This is one of the simplest techniques to encrypt text, which consists of substituting each letter of the plain text with the letter found at a fixed number of positions down the alphabet. For example, with a shift of `5`, `a` would be replaced by `f`, `b` by `g` and so on.

To implement this cipher, you'll need to create a new version of your alphabet that starts at the position indicated by the shift. As you learned in a previous lesson, you can extract part of a string using string slicing:

```python
fcc = 'freeCodeCamp'
print(fcc[8:])  # Camp
```

Create a variable named `shifted_alphabet` and use the slicing syntax to assign it the portion of `alphabet` that starts at the index of `shift`. Then, call the built-in `print()` function to print `shifted_alphabet` on the terminal and look at the result.

## Step 4
As you can see from the output, the shifted alphabet starts at the letter `f` because `shift` has the value `5`. But now the first five letters of the alphabet – `a`, `b`, `c`, `d` and `e` – are missing from the shifted alphabet, so you'll need to add them at the end of the shifted alphabet.

The `+` operator is used to combine two or more strings together in a process called concatenation like this:

```python
greeting = 'Hello' + ' ' + 'World'
print(greeting)  # Hello World
```

Modify the existing assignment of the `shifted_alphabet` variable: use the slicing syntax to extract the missing first portion of `alphabet` and concatenate it to `alphabet[shift:]`.

As a reminder, `sentence[start:stop]` returns the characters of `sentence` from position `start` (included) to `stop` (excluded).
