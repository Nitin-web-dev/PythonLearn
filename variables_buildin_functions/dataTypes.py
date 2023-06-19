# Data Types
# There are several data types in Python. To identify the data type we use the type built-in function. I would like to ask you to focus on understanding different data types very well. When it comes to programming, it is all about data types. I introduced data types at the very beginning and it comes again, because every topic is related to data types. We will cover data types in more detail in their respective sections.

# Checking Data types and Casting
# Check Data types: To check the data type of certain data/variable we use the type Example:
# # Different python data types

# # Let's declare variables with various data types

# first_name = 'Asabeneh'     # str
# last_name = 'Yetayeh'       # str
# country = 'Finland'         # str
# city= 'Helsinki'            # str
# age = 250                   # int, it is not my real age, don't worry about it

# # Printing out types
# print(type('Asabeneh'))     # str
# print(type(first_name))     # str
# print(type(10))             # int
# print(type(3.14))           # float
# print(type(1 + 1j))         # complex
# print(type(True))           # bool
# print(type([1, 2, 3, 4]))     # list
# print(type({'name':'Asabeneh','age':250, 'is_married':250}))    # dict
# print(type((1,2)))                                              # tuple
# print(type(zip([1,2],[3,4])))                                   # set
# Casting: Converting one data type to another data type. We use int(), float(), str(), list, set When we do arithmetic operations string numbers should be first converted to int or float otherwise it will return an error. If we concatenate a number with a string, the number should be first converted to a string. We will talk about concatenation in String section.

# Example:

# # int to float
# num_int = 10
# print('num_int',num_int)         # 10
# num_float = float(num_int)
# print('num_float:', num_float)   # 10.0

# # float to int
# gravity = 9.81
# print(int(gravity))             # 9

# # int to str
# num_int = 10
# print(num_int)                  # 10
# num_str = str(num_int)
# print(num_str)                  # '10'

# # str to int or float
# num_str = '10.6'
# print('num_int', int(num_str))      # 10
# print('num_float', float(num_str))  # 10.6

# # str to list
# first_name = 'Asabeneh'
# print(first_name)               # 'Asabeneh'
# first_name_to_list = list(first_name)
# print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']
# Numbers
# Number data types in Python:

# Integers: Integer(negative, zero and positive) numbers Example: ... -3, -2, -1, 0, 1, 2, 3 ...

# Floating Point Numbers(Decimal numbers) Example: ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...

# Complex Numbers Example: 1 + j, 2 + 4j, 1 - 1j

# full_moon You are awesome. You have just completed day 2 challenges and you are two steps ahead on your way to greatness. Now do some exercises for your brain and muscles.

