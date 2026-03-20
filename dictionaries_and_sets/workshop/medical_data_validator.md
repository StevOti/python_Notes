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
