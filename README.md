# Contact Book

The contact book is a python project without any external libraries. 
It is for this purpose to create a contact list where the user can:

1. Add a contact
2. Show and read a contact
3. Edit and update a contact
4. Delete a created contact

Furthermore, it is sorted alphabetically by the name, like an actual contact book.

## Description

This project has a text-based user interface design for creating a contact book. It also includes a data test and functions like a tutorial for the user. It will be discussed again later. For any modification to the contact book, a global variable list "contacts" was assigned as an empty list. In other words, the variable list "contacts" is the contact book. This list is associated with each function and can be modified by the user.

If the user wants to add a new contact, the function "add_contact" will execute this feature. The function "add_contact" will let the user add a contact step by step in a user-friendly manner. First, the user will be asked to enter the name, phone number, email address and birthday to create a simple contact. Then, the function appends the created contact automatically to the list "contacts".

For showing and reading a contact, the user has to find the data of the desired contact. For this purpose, the function "search_contact" was created. The user will be asked to enter one of the contact criteria: name, phone number, email address, or birthday. If the user input is wrong, the user will be notified that the contact does not exist. On the other hand, if the input is correct, the function will print the right contact for the user.

The function "edit_contact" was created for editing and updating any contact in the contact list. Firstly, it includes the search function to find the desired contact to update the right contact. After the user has found the contact, they will be asked to choose which criteria should be updated. Accordingly, the user can enter the new information and the function print the modified contact for the user. Also, the user can quit the feature before editing if they have found the wrong contact.

In order to understand the "ask_order" function, it needs to describe the "user_interface" firstly. The "user_interface" function is responsible for the user-friendly interface. The function includes all upper declared functions and starts to ask the user to add at least five records to the contact list. After that, the user can choose which feature of the primary project purpose they want to use for their contact book. Finally, the prompt will appear each time the user has used one of the functions.
For this reason, the "ask_order" function was created. Principally as long the user does not quit the contact book, the function "ask_order" will ask the user if they want to add, read, edit or delete a contact. Furthermore, for sorting the contact alphabetically by name, both functions will automatically sort the contact after the user adds and edits a contact.

Ultimately the "start_contact_book" function will let the user choose if they want to start a data test or add the first contacts to their contact book. Firstly, it will welcome the user to their contact book, and if the user chooses to start with the data test, it will appear again until they begin to open the contact book. Finally, the "test_data" function is responsible for the test data user interface. It will lead the user through five tests and check if the declared outputs are correct. Also, the user will get a first introduction to their contact book and how the user interface is designed.

## Getting Started

### Dependencies

This python project does not have any external libraries. However, starting this program will only require a Python 3 version.

### Installing

The latest version of python can be installed on the website: https://www.python.org/downloads/.

### Executing program

Executing this python project requires only running the file on the python platform. A welcome prompt will lead the user through this project until they quit the contact book by command. Then, the user needs to rerun the file to repeat the project.

## Help

Every function contains helper information. The command "help(function_name)" will display the function's information.

## Authors

Gianluca Cannone - https://github.com/gicanon

## License

Copyright (c) [2022] [Gianluca Cannone]

Permission is hereby granted, free of charge, to any person obtaining a copy of the project without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the project, and to permit persons to whom the project is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of this project.

THE PROJECT IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE PROJECT OR THE USE OR OTHER DEALINGS IN THE PROJECT.
