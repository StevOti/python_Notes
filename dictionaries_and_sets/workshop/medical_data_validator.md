# Medical Data Validator Workshop

## Step 1
Declare a variable named `medical_records` and assign it an empty list.

```python
medical_records = []
```

## Step 2
As you learned in previous lessons, a dictionary is a data structure that holds key-value pairs, where keys are immutable data types (such as strings) and unique within a dictionary:

```python
person = {
    'name': 'John',
    'age': 33
}
```

The `medical_records` list will store dictionaries, each of them representing a patient. Add a dictionary with a key `patient_id` and value of the string `P1001` to the `medical_records` list.

## Step 3
Add a key `age` with the value of the integer `34` and a key `gender` with the value of the string `Female` to your dictionary.

## Step 4
Complete the dictionary by adding the following three key-value pairs:

- A key `diagnosis` with the value `Hypertension`
- A key `medications` with the value of the list `['Lisinopril']`
- A key `last_visit_id` with the value `V2301`

## Step 5
Following the same structure used in the previous steps, the `medical_records` list has been filled up with other patients' data.

Create a function named `validate` with a single parameter `data`.

Within the function, declare a variable named `is_sequence` and assign it a call to `isinstance`. Pass in `data` as the first argument and a tuple containing `list` and `tuple` as the second argument.

## Step 6
Create an if statement. For its condition, use the `not` operator to negate `is_sequence`.

Within the if statement, print `Invalid format: expected a list or tuple.` and return `False`.

## Step 7
Right after your if statement, declare a variable named `is_invalid` and set it to `False`.

## Step 8
As you learned in a previous lesson, the `enumerate` function allows to keep track of the index while looping over an iterable:

```python
person = {'name': 'John', 'age': 33}

for index, item in enumerate(person):
    print(index, item)

# 0 name
# 1 age
```

Create a for loop that iterates over `data`. Use the `enumerate` function to get both the index and the item in `data` at each iteration. Use `index` and `dictionary` as iteration variables.

For now use `pass` to fill the loop body.

## Step 9
Inside your for loop, if the item in `dictionary` is not an instance of `dict`, print `Invalid format: expected a dictionary at position <index>.` (where `<index>` should be replaced by the current index) and set `is_invalid` to `True`.

## Step 10
After your for loop, still inside the `validate` function, create an if statement. If `is_invalid` is `True`, return `False`.

## Step 11
After the if statement, print the string `Valid format.`. Then return `True`.

## Step 12
At the bottom of your code, call the `validate` function with `medical_records` as the argument. You should see `Valid format.` printed to the terminal.

## Step 13
To test the first if statement of your function, turn `medical_records` into a string. You should see `Invalid format: expected a list or tuple.` printed to the terminal.

## Step 14
Now turn `medical_records` back to a list/tuple of dictionaries.

## Step 15
To test the second conditional statement, add two items of your choice that are not dictionaries at the end of the `medical_records` list. You should see two validation messages printed to the terminal.

## Step 16
Now that you tested the validation for this part, remove the last two items from the `medical_records` list.

## Step 17
As you learned in a previous lesson, a set is an unordered collection of unique elements:

```python
integers = set([3, 5, 1, 2, 1, 3, 4])
print(integers) # {1, 2, 3, 4, 5}
```

You're going to use a set to ensure that each dictionary does not contain extra or misspelled keys.

Inside the `validate` function, use the `set()` constructor to create a set from the following list of keys that each dictionary should have: `['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id']`. Assign the set to a variable named `key_set`.

## Step 18
The `keys()` method returns a view object containing all the keys from a dictionary:

```python
person = {
   'name': 'John',
   'age': 33
}

print(person.keys()) # dict_keys(['name, 'age'])
```

Inside your for loop, after the first if statement, create an if statement that runs when the set of keys from the current dictionary is different from `key_set`.

Within the new if statement, print `Invalid format: <dictionary> at position <index> has missing and/or invalid keys.` (where `<dictionary>` and `<index>` should be replaced by the dictionary and index at the current iteration) and set `is_invalid` to `True`.

## Step 19
To test that everything is working correctly, comment out the `age` key from the first dictionary in `medical_records`.

You should see a validation message appear in the terminal.

## Step 20
Now restore the line `'age': 34,`.

## Step 21
Now you are going to make the validation more granular. Create a function named `find_invalid_records` to find invalid values in a dictionary. Give it the following parameters: `patient_id`, `age`, `gender`, `diagnosis`, `medications`, `last_visit_id`.

Inside your new function, create an empty dictionary named `constraints`. Then, return `constraints` from your new function.

## Step 22
The `**` operator can be used to unpack the elements in a dictionary and pass them as keyword arguments in a function call:

```python
def sum(a, b, c):
    return a + b + c
nums = {'a': 2, 'b': 4, 'c': 1}

print(sum(**nums)) # 7
```

In the example above, `sum(**nums)` is equivalent to `sum(a=2, b=4, c=1)`.

At the bottom of your code, print the result of calling the `find_invalid_records` function. For its arguments, use the `**` operator to unpack `medical_records[0]`.

## Step 23
The `constraints` dictionary will contain each key you should expect to have in the data to validate. The value associated to each of them will indicate the result of the validation.

Add the key `patient_id` to the `constraints` dictionary. For its value, use a call to `isinstance` passing in `patient_id` and `str` as the arguments.

## Step 24
As you wrote in the previous step, `patient_id` should be a string. You want to check that it also has a specific pattern though.

For that, you are going to use a regular expression. Therefore, at the top of your code, use the `import` keyword to import the `re` module.

## Step 25
A regular expression, or regex, is a pattern used to match a sequence of characters in text. The `search` function from the `re` module takes a regex pattern and a string as its arguments.

It returns a corresponding match object if the pattern produces a match. Otherwise it returns `None`.

```python
import re

greeting = "Hello there!"
print(re.search('Hi', greeting)) # None
print(re.search('Hello', greeting)) # <re.Match object; span=(0, 5), match='Hello'>
```

Call `re.search` with the string `p` as the first argument and `patient_id` as the second argument. Use the `and` operator to add the function call as a second expression to the value of your `patient_id` key.

## Step 26
Now you can see `{'patient_id': None}` printed to the terminal because the lowercase `p` does not match `P1001` and the `and` operator returns the first falsy value of the expression.

You want to ensure that the patient ID starts with the letter `p`, but it can be either lowercase or uppercase. To modify the matching behavior of regular expressions, you can use flags. For example, `re.search` accepts a third argument to specify any flags:

```python
import re

greeting = "Hello there!"
print(re.search('hello', greeting)) # None

print(re.search('hello', greeting, re.IGNORECASE))
# <re.Match object; span=(0, 5), match='Hello'>
```

Add `re.IGNORECASE` as the third argument to your `re.search` call. This will make your regex search case insensitive.

After that, you'll see `None` replaced by the match object `<re.Match object; span=(0, 1), match='P'>`, where `match` indicates the match and `span` indicates its location in the string.

## Step 27
Regular expressions can contain special sequences consisting in a backslash (`\`) followed by a character. These sequences have a special meaning. For example, `\d` matches a decimal digit.

```python
import re

book = "Fahrenheit 451"
print(re.search('\\d', book))
# <re.Match object; span=(11, 12), match='4'>
```

After the letter `p`, `patient_id` should have a series of numbers. So, modify your regex pattern to have the character `p` followed by the special sequence `\d`.

## Step 28
Quantifiers are used in regular expressions to specify how many times a character can be repeated. For example, the `+` character matches the previous character one or more times:

```python
import re

book = "Fahrenheit 451"
print(re.search('\\d', book))
# <re.Match object; span=(11, 12), match='4'>

print(re.search('\\d+', book))
# <re.Match object; span=(11, 14), match='451'>
```

So append a `+` quantifier to your regex pattern to match one or more digits.

## Step 29
Now that your regex matches the letter `p` followed by one or more digits, one last thing you need to check is that no extra characters are found in the string.

To do that you can make use of another function from the `re` module. The `fullmatch` function returns a match object when the regex pattern matches the entire string and `None` otherwise.

```python
import re

book = "Fahrenheit 451"
print(re.fullmatch('\\d+', book)) #None

print(re.fullmatch('Fahrenheit \\d+', book))
# <re.Match object; span=(0, 14), match='Fahrenheit 451'>
```

Replace the `search` call with a `fullmatch` call keeping the same arguments.

## Step 30
Next, you want to verify that `age` is an integer. So add another key `age` to the `constraints` dictionary. For its value, call `isinstance` passing `age` and `int` as its arguments.

## Step 31
`age` should not only be an integer, it should be a positive integer greater than or equal to `18`.

Using the `and` operator, add a second expression to the value of the `age` key to check that.

## Step 32
Add another key `gender` to the `constraints` dictionary. Following the format of the expression you wrote in the previous steps, verify that `gender` is a string. Then, use the `and` operator to check that the lowercase `gender` is in `('male', 'female')`.
