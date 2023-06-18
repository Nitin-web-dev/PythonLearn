# Variables
# Variables store data in a computer memory. Mnemonic variables are recommended to use in many programming languages. A mnemonic variable is a variable name that can be easily remembered and associated. A variable refers to a memory address in which data is stored. Number at the beginning, special character, hyphen are not allowed when naming a variable. A variable can have a short name (like x, y, z), but a more descriptive name (firstname, lastname, age, country) is highly recommended.

# Python Variable Name Rules

# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME) are different variables)
# Let us se valid variable names

# firstname
# lastname
# age
# country
# city
# first_name
# last_name
# capital_city
# _if # if we want to use reserved word as a variable
# year_2021
# year2021
# current_year_2021
# birth_year
# num1
# num2
# Invalid variables names

# first-name
# first@name
# first$name
# num-1
# 1num
# We will use standard Python variable naming style which has been adopted by many Python developers. Python developers use snake case(snake_case) variable naming convention. We use underscore character after each word for a variable containing more than one word(eg. first_name, last_name, engine_rotation_speed). The example below is an example of standard naming of variables, underscore is required when the variable name is more than one word.

# When we assign a certain data type to a variable, it is called variable declaration. For instance in the example below my first name is assigned to a variable first_name. The equal sign is an assignment operator. Assigning means storing data in the variable. The equal sign in Python is not equality as in Mathematics.

# Example:

# # Variables in Python
# first_name = 'Asabeneh'
# last_name = 'Yetayeh'
# country = 'Finland'
# city = 'Helsinki'
# age = 250
# is_married = True
# skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
# person_info = {
#    'firstname':'Asabeneh',
#    'lastname':'Yetayeh',
#    'country':'Finland',
#    'city':'Helsinki'
#    }



# to get the length 
# print(len('Hello, World!')) # it takes only one argument


# Declaring Multiple Variable in a Line
# Multiple variables can also be declared in one line:

# Example:

# first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

# print(first_name, last_name, country, age, is_married)
# print('First name:', first_name)
# print('Last name: ', last_name)
# print('Country: ', country)
# print('Age: ', age)
# print('Married: ', is_married)



# Getting user input using the input() built-in function. Let us assign the data we get from a user into first_name and age variables. Example:

# first_name = input('What is your name: ')
# age = input('How old are you? ')

# print(first_name)
# print(age)