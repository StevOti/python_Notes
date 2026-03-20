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
