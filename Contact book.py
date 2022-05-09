#Contact book(list) as global variable
contacts =[]


def add_contact():
    """Function for adding a contact
    Return contacts"""

    contact_list = []
    input_name = input("""Enter Givenname and Surname: """)
    input_phone = input("""Enter Phone Number: """)
    input_email = input("""Enter Email Address: """)
    input_birthday = input("""Enter Birthday: """)

    contact_list.append(input_name)
    contact_list.append(input_phone)
    contact_list.append(input_email)
    contact_list.append(input_birthday)
    contacts.append(contact_list)
    return contacts
    

def search_contact():
    """Function for searching a contact
    If search information was found return the right contact
    If search information was not found return 'Contact doesn't exist'"""

    search_info = input('''"Enter Name" or "Phone Number" or "Email Address" or "Birthday" of the contact: ''')
    search_info = search_info.lower()
    i = 0
    search_list = []
    while i < len(contacts):
        search_list = contacts[i]
        for element in search_list:
            if element.lower() == search_info:
                print("\nContact has been found:\n")
                return contacts[i]
        i += 1
    print("")
    return "Contact doesn't exist"


def edit_contact():
    """Function for editing or deleting a contact
    If contact was not found return 'Contact doesn't exist'
    Otherwise let the user choose either to delete or edit the contact"""

    edit_list = search_contact()
    if edit_list == "Contact doesn't exist":
        return "Contact doesn't exist"
    else:
        print(f"{edit_list}\n")
        index_number = contacts.index(edit_list)
        edit_info = input("""Enter the number to edit the information of one of the following categories, enter '4' for deleting the contact or '5' to exit the program.

 0) Name 
 1) Phone Number
 2) Email Address
 3) Birthday
 4) Delete Contact

 5) Quit Editing

""")
        if edit_info == "4":
            contacts.pop(int(index_number))
            print("Contact has been deleted:\n")
            return contacts
        if edit_info == "5":
            return "No editing completed"
        try:
            edit_list.pop(int(edit_info))
            edit_list.insert(int(edit_info), input("""Enter new information: """))
            contacts[index_number]= edit_list
            print("\nContact has been edited:\n")
            return contacts[index_number]
        except: 
            print("Input wrong try again\n")
            return edit_contact()


def ask_order():
    """Ask the user which feature they want to choose:

    1. Add another contact
    2. Search and read a contact
    3. Edit or delete a contact
    4. Show entire contact book

    and accordingly call the right function.

    Except the user quit the contact book"""

    order = input("""Please choose what for features you want to use for your contact book.
Enter the number for the feature:

1) Add another contact
2) Search and read a contact
3) Edit or delete a contact
4) Show entire contact book

5) Quit contact book

""")
    if order == "1":
        add_contact()
        contacts.sort()
    elif order == "2":
        print(search_contact())
    elif order == "3":
        print(edit_contact())
        contacts.sort()
    elif order == "4":
        print(contacts)
    elif order == "5":
        return order
    else: 
        print("Input wrong try again\n")
        return ask_order()


def user_interface():
    """The Unser Interface:
    Ask user to enter at least 5 records to its contact book and let they choose to:

    1. Add another contact
    2. Search and read a contact
    3. Edit or delete a contact
    4. Show entire contact book

    Until the user quit the contact book"""

    print("""Please enter at least 5 records to your contact book.
Enter following information for each contact:""")
    for i in range (1,6):
        print(f"""
Contact {i}:
""")
        add_contact()
        contacts.sort()
    print(f"""
Your current contact book sorted alphabetically:

{contacts}
""")
    
    while True:
        order_1 = ask_order()
        if order_1 == "5":
            break
        order_2 = input("""
Do you want to continue or quit the contact book?
Enter the number:

1) Continue
2) Quit Contact Book

""")
        if order_2 == "2":
            break
        elif order_2 != "1":
            print("Input wrong try again\n")


def test_data():
    """Test 1: Show Contact list with two contacts
    Please enter for the test two contacts with the following information:

    1st Contact: ['Gianluca Cannone', '0176 84078863', 'gc22299@essex.ac.uk', '03.10.1995']
    2nd Contact: ['Arron Fox', '0151 81743283', 'arron.fox@gmail.com', '04.12.1990']
    
    Test 2: Sort contact list alphabetically and show contact list

    Test 3: Search contact "Gianluca Cannone" by entering any information of the contact and show the contact
    
    Test 4: Edit email address from contact "Gianluca Cannone" to gianluca.cannone@gmail.com and show the contact
    The user will be asked to enter the following input:

    Input 1: Gianluca Cannone
    Input 2: 2
    Input 3: gianluca.cannone@gmail.com
    
    Test 5: Show the entire contact list"""
    
    #Test 1: Adding contacts with the right data
    global contacts
    print("""Please enter for the test two contacts with the following information:

1st Contact: [Gianluca Cannone, 0176 84078863, gc22299@essex.ac.uk, 03.10.1995]
2nd Contact: [Arron Fox, 0151 81743283, arron.fox@gmail.com, 04.12.1990]""")
    test_list = [['Gianluca Cannone', '0176 84078863', 'gc22299@essex.ac.uk', '03.10.1995'], ['Arron Fox', '0151 81743283', 'arron.fox@gmail.com', '04.12.1990']]
    for i in range(1,3):
        print(f"""
Contact {i}:
""")
        add_contact()
    print(f"\n{contacts}")
    if test_list == contacts:
        print(f"Contact list output is {True}\n")
    else:
        print(f"Contact list output is {False}\n")
    
    #Test 2: Sorting contact list 
    test_list.sort() 
    contacts.sort()
    print(contacts)
    if test_list == contacts:
        print(f"Contact list is sorted alphabetically, thus output is {True}\n")
    else:
        print(f"Contact list is sorted wrong, thus output is {False}\n")

    #Test 3: Searching contact "Gianluca Cannone"
    test_search_contact = ['Gianluca Cannone', '0176 84078863', 'gc22299@essex.ac.uk', '03.10.1995'] 
    search_list = search_contact()
    print(search_list)
    if test_search_contact == search_list:
        print(f"Contact is 'Gianluca Cannone', thus output is {True}\n")
    else:
        print(f"Contact is wrong, thus output is {False}\n")
    
    #Test 4: Editing email address from contact "Gianluca Cannone" to gianluca.cannone@gmail.com
    print("""Edit email address from contact "Gianluca Cannone" to gianluca.cannone@gmail.com
You will be asked to enter following information:
    
Input 1: Enter for example the name "Gianluca Cannone" to search the contact
Input 2: Enter the number "2" to edit the email address
Input 3: Enter new email address "gianluca.cannone@gmail.com"
""")
    test_edit_contact = ['Gianluca Cannone', '0176 84078863', 'gianluca.cannone@gmail.com', '03.10.1995']
    edit_email_contact = edit_contact()
    print(edit_email_contact)
    if test_edit_contact == edit_email_contact:
         print(f"Contact 'Gianluca Cannone' has new email: 'gianluca.cannone@gmail.com', thus output is {True}\n")
    else:
        print(f"Email address is not gianluca.cannone@gmail.com, thus output is {False}\n")
    
    #Test 5: Showing entire contact list
    test_entire_contact = [['Arron Fox', '0151 81743283', 'arron.fox@gmail.com', '04.12.1990'], ['Gianluca Cannone', '0176 84078863', 'gianluca.cannone@gmail.com', '03.10.1995']]
    print(contacts)
    if test_entire_contact == contacts:
        print(f"Contact list Output is {True}\n")
    else:
        print(f"Contact list Output is {False}\n")

    #Clearing contact book
    contacts = []
    return contacts


def start_contact_book():
    """Function for starting the contact book
    Ask user either to start a data test or with the contact book and adding its first contacts"""

    print("Welcome to your contact book. Feel free to start a data test or start adding your first contacts.\n")
    order = input("""Enter '1' to start the data test or enter '2' to start with your contact book: 

1) Data Test
2) Contact Book

""")
    if order == '1':
        test_data()
        return start_contact_book()
    elif order == '2':
        user_interface()
        return
    else: 
        print("Input is wrong, try again\n")
        return start_contact_book()

start_contact_book()