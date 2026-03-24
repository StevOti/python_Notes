# Build a User Configuration Manager

In this lab, you will build a User Configuration Manager that allows users to manage their settings such as theme, language, and notifications.

You will implement functions to add, update, delete, and view user settings.

## Objective

Fulfill the user stories below and get all the tests to pass to complete the lab.

## User Stories

1. Define a function named `add_setting` with two parameters:
	- A dictionary of settings.
	- A tuple containing a key-value pair.

2. `add_setting` should:
	- Convert the key and value to lowercase.
	- If the key exists, return:
	  `Setting '[key]' already exists! Cannot add a new setting with this name.`
	- If the key does not exist, add the key-value pair and return:
	  `Setting '[key]' added with value '[value]' successfully!`

3. Define a function named `update_setting` with two parameters:
	- A dictionary of settings.
	- A tuple containing a key-value pair.

4. `update_setting` should:
	- Convert the key and value to lowercase.
	- If the key exists, update the value and return:
	  `Setting '[key]' updated to '[value]' successfully!`
	- If the key does not exist, return:
	  `Setting '[key]' does not exist! Cannot update a non-existing setting.`

5. Define a function named `delete_setting` with two parameters:
	- A dictionary of settings.
	- A key.

6. `delete_setting` should:
	- Convert the key to lowercase.
	- If the key exists, delete it and return:
	  `Setting '[key]' deleted successfully!`
	- If the key does not exist, return:
	  `Setting not found!`

7. Define a function named `view_settings` with one parameter:
	- A dictionary of settings.

8. `view_settings` should:
	- Return `No settings available.` if the dictionary is empty.
	- Otherwise return a formatted string that starts with:
	  `Current User Settings:`
	  followed by each key-value pair on a new line.
	- Each key should be capitalized.
	- The returned string should end with a newline character.

## Expected Example Output for `view_settings`

```text
Current User Settings:
Theme: dark
Notifications: enabled
Volume: high
```

## Testing Requirement

Create a dictionary named `test_settings` and add some user preference values to it.
