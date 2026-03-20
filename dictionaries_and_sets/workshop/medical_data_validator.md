# Medical Data Validator Workshop

In this workshop, you'll validate a set of medical data to ensure that it complies with a set of rules.

## Step 1: Create an Empty List for Medical Records

Declare a variable named `medical_records` and assign it an empty list. In the following steps, you are going to use it to store your medical data.

```python
medical_records = []
```

**What you're doing:** You're initializing an empty list that will hold medical record dictionaries. This list will serve as the foundation for storing and validating patient data throughout this workshop.

## Step 2: Add a Patient Dictionary to the Medical Records

As you learned in previous lessons, a **dictionary** is a data structure that holds key-value pairs, where keys are immutable data types (such as strings) and unique within a dictionary.

**Example Code:**

```python
person = {
    'name': 'John',
    'age': 33
}
```

The `medical_records` list will store dictionaries, each of them representing a patient. Add a dictionary with a key `patient_id` and value of the string `P1001` to the `medical_records` list.

```python
medical_records = []
medical_records.append({'patient_id': 'P1001'})
```

**What you're doing:** You're creating a dictionary with a `patient_id` key and appending it to the `medical_records` list. This dictionary will serve as the first patient record. As you progress through this workshop, you'll add more fields to represent complete patient information.

## Step 3: Add Age and Gender to the Patient Dictionary

Add a key `age` with the value of the integer `34` and a key `gender` with the value of the string `Female` to your dictionary. Don't forget the comma between the key-value pairs.

```python
medical_records = []
medical_records.append({'patient_id': 'P1001', 'age': 34, 'gender': 'Female'})
```

**What you're doing:** You're expanding the patient dictionary to include multiple fields. Now the dictionary has three key-value pairs: `patient_id`, `age`, and `gender`. This demonstrates how dictionaries can store diverse types of data (strings, integers) in a single structure, making them ideal for representing complex objects like patient records.

## Step 4: Complete the Dictionary with Diagnosis, Medications, and Last Visit ID

Complete the dictionary by adding the following three key-value pairs:

- A key `diagnosis` with the value `Hypertension`
- A key `medications` with the value of the list `['Lisinopril']`
- A key `last_visit_id` with the value `V2301`

```python
medical_records = []
medical_records.append({
    'patient_id': 'P1001',
    'age': 34,
    'gender': 'Female',
    'diagnosis': 'Hypertension',
    'medications': ['Lisinopril'],
    'last_visit_id': 'V2301'
})
```

**What you're doing:** You're creating a comprehensive patient record dictionary that includes not just demographic information but also medical details. Notice that the `medications` value is a list, which allows storing multiple medications for a single patient. This demonstrates how dictionaries can contain various data types, including lists, making them flexible for representing complex data structures.

## Step 5: Create a Validate Function with Type Checking

Following the same structure you used in the previous steps, the `medical_records` list has been filled up for you with other patients' data. Feel free to take a look at it.

Next you'll start to write the function to validate the data set. Create a function named `validate` with a single parameter `data`.

You want to ensure that your data is either a list or a tuple. Therefore, within the `validate` function, declare a variable named `is_sequence` and assign it a call to `isinstance`. Pass in `data` as the first argument and a tuple containing `list` and `tuple` as the second argument.

```python
def validate(data):
    is_sequence = isinstance(data, (list, tuple))
```

**What you're doing:** You're creating the foundation of a validation function that will check whether the input is a sequence type (list or tuple). The `isinstance()` function checks if an object is an instance of a class or tuple of classes. By passing `(list, tuple)` as the second argument, you're allowing the function to accept either lists or tuples as valid input. This variable will be used in subsequent steps to determine whether validation should proceed.

## Step 6: Add Validation Check for Sequence Type

Create an if statement. For its condition, use the `not` operator to negate `is_sequence`. Within the if statement, print `Invalid format: expected a list or tuple.` and return `False`.

```python
def validate(data):
    is_sequence = isinstance(data, (list, tuple))
    if not is_sequence:
        print("Invalid format: expected a list or tuple.")
        return False
```

**What you're doing:** You're adding error handling to the `validate()` function. The `if not is_sequence:` condition checks if the data is NOT a sequence type. If it's not valid, the function prints an error message and returns `False`, signaling that validation failed. This is the first validation rule: the input must be a list or tuple.

## Step 7: Declare an Invalid Flag Variable

Right after your if statement, declare a variable named `is_invalid` and set it to `False`. Later on, you'll use it as a flag to run a conditional statement.

```python
def validate(data):
    is_sequence = isinstance(data, (list, tuple))
    if not is_sequence:
        print("Invalid format: expected a list or tuple.")
        return False
    is_invalid = False
```

**What you're doing:** You're creating a flag variable that will track whether any validation errors are found. By initializing it to `False`, you're starting with the assumption that the data is valid. As you add more validation checks in the following steps, you'll set this flag to `True` if any validation rule is violated.

## Step 8: Loop Through Data with `enumerate()`

As you learned in a previous lesson, the `enumerate` function allows to keep track of the index while looping over an iterable:

**Example Code**

```python
person = {'name': 'John', 'age': 33}

for index, item in enumerate(person):
    print(index, item)

# 0 name
# 1 age
```

Create a `for` loop that iterates over `data`. Use the `enumerate` function to get both the index and the item in `data` at each iteration. Use `index` and `dictionary` as iteration variables.

For now use `pass` to fill the loop body.

```python
def validate(data):
    is_sequence = isinstance(data, (list, tuple))
    if not is_sequence:
        print("Invalid format: expected a list or tuple.")
        return False
    is_invalid = False

    for index, dictionary in enumerate(data):
        pass
```

**What you're doing:** You're setting up iteration over each patient record while keeping track of both the position (`index`) and the record itself (`dictionary`). Using `pass` keeps the loop syntactically complete for now, so you can add validation rules in the next steps.

## Step 9: Validate That Each Item Is a Dictionary

You are checking if the data passed to your function is a list or a tuple. You still need to ensure that each item in the sequence is a dictionary.

Inside your `for` loop, if the item in `dictionary` is not an instance of `dict`, print `Invalid format: expected a dictionary at position <index>.` (where `<index>` should be replaced by the current index) and set `is_invalid` to `True`.

```python
def validate(data):
    is_sequence = isinstance(data, (list, tuple))
    if not is_sequence:
        print("Invalid format: expected a list or tuple.")
        return False
    is_invalid = False

    for index, dictionary in enumerate(data):
        if not isinstance(dictionary, dict):
            print(f"Invalid format: expected a dictionary at position {index}.")
            is_invalid = True
```

**What you're doing:** You're adding item-level validation to make sure every element in `data` is a dictionary. If a non-dictionary item appears, the function reports exactly where it happened using the current `index` and flips `is_invalid` to `True` so you can handle invalid data after the loop.

## Step 10: Return `False` If Invalid Data Was Found

After your `for` loop, still inside the `validate` function, create an `if` statement. If `is_invalid` is `True`, return `False`.

```python
def validate(data):
    is_sequence = isinstance(data, (list, tuple))
    if not is_sequence:
        print("Invalid format: expected a list or tuple.")
        return False
    is_invalid = False

    for index, dictionary in enumerate(data):
        if not isinstance(dictionary, dict):
            print(f"Invalid format: expected a dictionary at position {index}.")
            is_invalid = True

    if is_invalid:
        return False
```

**What you're doing:** You're adding a final check after iterating through all records. If any invalid item was detected during the loop, `is_invalid` will be `True`, and the function returns `False` to signal failed validation.

## Step 11: Print Success Message and Return `True`

After the `if` statement, print the string `Valid format.`. Then return `True`.

```python
def validate(data):
    is_sequence = isinstance(data, (list, tuple))
    if not is_sequence:
        print("Invalid format: expected a list or tuple.")
        return False
    is_invalid = False

    for index, dictionary in enumerate(data):
        if not isinstance(dictionary, dict):
            print(f"Invalid format: expected a dictionary at position {index}.")
            is_invalid = True

    if is_invalid:
        return False

    print("Valid format.")
    return True
```

**What you're doing:** You're completing the validation flow with a success path. If no invalid records were found, the function prints `Valid format.` and returns `True`, clearly indicating that the dataset passed all current validation rules.

## Step 12: Call `validate()` with `medical_records`

At the bottom of your code, call the `validate` function with `medical_records` as the argument. You should see `Valid format.` printed to the terminal.

```python
def validate(data):
    is_sequence = isinstance(data, (list, tuple))
    if not is_sequence:
        print("Invalid format: expected a list or tuple.")
        return False
    is_invalid = False

    for index, dictionary in enumerate(data):
        if not isinstance(dictionary, dict):
            print(f"Invalid format: expected a dictionary at position {index}.")
            is_invalid = True

    if is_invalid:
        return False

    print("Valid format.")
    return True

validate(medical_records)
```

**What you're doing:** You're executing your validation logic by calling `validate(medical_records)` after the function definition. Since `medical_records` contains valid dictionary records at this point, the function reaches the success path and prints `Valid format.`.

## Step 13: Test the First `if` Statement with Invalid Sequence Type

To test the first `if` statement of your function, turn `medical_records` into a string. You should see `Invalid format: expected a list or tuple.` printed to the terminal.

```python
def validate(data):
    is_sequence = isinstance(data, (list, tuple))
    if not is_sequence:
        print("Invalid format: expected a list or tuple.")
        return False
    is_invalid = False

    for index, dictionary in enumerate(data):
        if not isinstance(dictionary, dict):
            print(f"Invalid format: expected a dictionary at position {index}.")
            is_invalid = True

    if is_invalid:
        return False

    print("Valid format.")
    return True

medical_records = str(medical_records)
validate(medical_records)
```

**What you're doing:** You're intentionally passing invalid input to test your guard clause. Since `medical_records` is converted to a string, it is no longer a list or tuple, so the first validation check fails and the function prints `Invalid format: expected a list or tuple.`.

## Step 14: Turn `medical_records` Back into a List/Tuple of Dictionaries

Now turn `medical_records` back to a list/tuple of dictionaries.

```python
def validate(data):
    is_sequence = isinstance(data, (list, tuple))
    if not is_sequence:
        print("Invalid format: expected a list or tuple.")
        return False
    is_invalid = False

    for index, dictionary in enumerate(data):
        if not isinstance(dictionary, dict):
            print(f"Invalid format: expected a dictionary at position {index}.")
            is_invalid = True

    if is_invalid:
        return False

    print("Valid format.")
    return True

medical_records = [
    {
        'patient_id': 'P1001',
        'age': 34,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'last_visit_id': 'V2301'
    }
]

validate(medical_records)
```

**What you're doing:** You're restoring `medical_records` to a valid sequence type (a list) where each item is a dictionary. This satisfies your current validation rules again, so the function can print `Valid format.`.

## Step 15: Test the Dictionary Check with Invalid Items

To test the second conditional statement, add two items of your choice that are not dictionaries at the end of the `medical_records` list. You should see two validation messages printed to the terminal.

```python
def validate(data):
    is_sequence = isinstance(data, (list, tuple))
    if not is_sequence:
        print("Invalid format: expected a list or tuple.")
        return False
    is_invalid = False

    for index, dictionary in enumerate(data):
        if not isinstance(dictionary, dict):
            print(f"Invalid format: expected a dictionary at position {index}.")
            is_invalid = True

    if is_invalid:
        return False

    print("Valid format.")
    return True

medical_records = [
    {
        'patient_id': 'P1001',
        'age': 34,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'last_visit_id': 'V2301'
    }
]

medical_records.append("invalid record")
medical_records.append(404)

validate(medical_records)
```

**What you're doing:** You're intentionally adding two invalid items that are not dictionaries, so the loop-level type check fails twice. The function prints one message per invalid position, which confirms your second validation condition is working correctly.

## Step 16: Remove the Last Two Invalid Items

Now that you tested the validation for this part, remove the last two items from the `medical_records` list.

```python
def validate(data):
    is_sequence = isinstance(data, (list, tuple))
    if not is_sequence:
        print("Invalid format: expected a list or tuple.")
        return False
    is_invalid = False

    for index, dictionary in enumerate(data):
        if not isinstance(dictionary, dict):
            print(f"Invalid format: expected a dictionary at position {index}.")
            is_invalid = True

    if is_invalid:
        return False

    print("Valid format.")
    return True

medical_records = [
    {
        'patient_id': 'P1001',
        'age': 34,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'last_visit_id': 'V2301'
    }
]

medical_records.append("invalid record")
medical_records.append(404)

medical_records.pop()
medical_records.pop()

validate(medical_records)
```

**What you're doing:** You're cleaning up the test data by removing the two non-dictionary values that were intentionally appended. After popping them off, `medical_records` is back to a valid list of dictionaries for the next steps.

## Step 17: Define the Required Dictionary Keys with a Set

As you learned in a previous lesson, a set is an unordered collection of unique elements:

**Example Code**

```python
integers = set([3, 5, 1, 2, 1, 3, 4])
print(integers) # {1, 2, 3, 4, 5}
```

You're going to use a set to ensure that each dictionary does not contain extra or misspelled keys.

Inside the `validate` function, use the `set()` constructor to create a set from the following list of keys that each dictionary should have: `['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id']`. Assign the set to a variable named `key_set`.

```python
def validate(data):
    is_sequence = isinstance(data, (list, tuple))
    if not is_sequence:
        print("Invalid format: expected a list or tuple.")
        return False
    is_invalid = False
    key_set = set(['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id'])

    for index, dictionary in enumerate(data):
        if not isinstance(dictionary, dict):
            print(f"Invalid format: expected a dictionary at position {index}.")
            is_invalid = True

    if is_invalid:
        return False

    print("Valid format.")
    return True

medical_records = [
    {
        'patient_id': 'P1001',
        'age': 34,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'last_visit_id': 'V2301'
    }
]

medical_records.append("invalid record")
medical_records.append(404)

medical_records.pop()
medical_records.pop()

validate(medical_records)
```

**What you're doing:** You're defining a single source of truth for valid dictionary keys. By storing required field names in `key_set`, you'll be able to compare each record's keys against this expected set in the next steps and catch extra, missing, or misspelled keys.

## Step 18: Validate Dictionary Keys with `keys()` and `set()`

The `keys()` method returns a view object containing all the keys from a dictionary:

**Example Code**

```python
person = {
   'name': 'John',
   'age': 33
}

print(person.keys()) # dict_keys(['name, 'age'])
```

Inside your `for` loop, after the first `if` statement, create an `if` statement that runs when the set of keys from the current dictionary is different from `key_set`. This is to ensure that no missing or invalid keys are present in the dictionary.

Within the new `if` statement, print `Invalid format: <dictionary> at position <index> has missing and/or invalid keys.` (where `<dictionary>` and `<index>` should be replaced by the dictionary and index at the current iteration) and set `is_invalid` to `True`.

```python
def validate(data):
    is_sequence = isinstance(data, (list, tuple))
    if not is_sequence:
        print("Invalid format: expected a list or tuple.")
        return False
    is_invalid = False
    key_set = set(['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id'])

    for index, dictionary in enumerate(data):
        if not isinstance(dictionary, dict):
            print(f"Invalid format: expected a dictionary at position {index}.")
            is_invalid = True
        if set(dictionary.keys()) != key_set:
            print(f"Invalid format: {dictionary} at position {index} has missing and/or invalid keys.")
            is_invalid = True

    if is_invalid:
        return False

    print("Valid format.")
    return True

medical_records = [
    {
        'patient_id': 'P1001',
        'age': 34,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'last_visit_id': 'V2301'
    }
]

medical_records.append("invalid record")
medical_records.append(404)

medical_records.pop()
medical_records.pop()

validate(medical_records)
```

**What you're doing:** You're adding structural validation for each record by comparing its keys to `key_set`. If any dictionary has missing, extra, or misspelled fields, the function prints a detailed message with the record content and position, and marks the overall dataset as invalid.

## Step 19: Test Missing-Key Validation by Commenting Out `age`

To test that everything is working correctly, try to comment out the `age` key from the first dictionary in `medical_records`.

You should see a validation message appear in the terminal.

```python
def validate(data):
    is_sequence = isinstance(data, (list, tuple))
    if not is_sequence:
        print("Invalid format: expected a list or tuple.")
        return False
    is_invalid = False
    key_set = set(['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id'])

    for index, dictionary in enumerate(data):
        if not isinstance(dictionary, dict):
            print(f"Invalid format: expected a dictionary at position {index}.")
            is_invalid = True
        if set(dictionary.keys()) != key_set:
            print(f"Invalid format: {dictionary} at position {index} has missing and/or invalid keys.")
            is_invalid = True

    if is_invalid:
        return False

    print("Valid format.")
    return True

medical_records = [
    {
        'patient_id': 'P1001',
        # 'age': 34,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'last_visit_id': 'V2301'
    }
]

medical_records.append("invalid record")
medical_records.append(404)

medical_records.pop()
medical_records.pop()

validate(medical_records)
```

**What you're doing:** You're intentionally removing a required field (`age`) from the first record to test the key-set comparison rule. Since the dictionary keys no longer match `key_set`, the function prints the missing/invalid keys validation message.
