#Day 8: 30 days of python
#-----------------------------------------------------------------------------------------------
#Question 1 & 2
# Creating an empty dictionary and adding key-value pairs for a dog
dog = {
    'name': "barabas",
    'color':"brown",
    'breed':"akplévou",
    'legs':4,
    'age':2,
}
#-----------------------------------------------------------------------------------------------
#Question 3
# Creating a student dictionary with various data types (strings, int, list)
student = {
    'first_name': "Emmanuel",
    'last_name':"trump",
    'gender':"masculin",
    'country': "Allemagne",
    'age':46,
    'marital status':"married",
    'skills':["python","c++","sql"],
    'city':"toulouse",
    'adress':"45 rue de totsi",
}
#-----------------------------------------------------------------------------------------------
#Question 4
# len() on a dict counts the total number of key-value pairs
print(len(student))
#-----------------------------------------------------------------------------------------------
#Question 5
# Accessing the 'skills' key to get length of list and check data type
print(type(student['skills']))
#-----------------------------------------------------------------------------------------------
#Question 6
"""Modify the skills values by adding one or two skills"""
student['skills'].append("java")
#-----------------------------------------------------------------------------------------------
#Question 7
# Get the dictionary keys as a list
keys = student.keys()
print(keys)
#-----------------------------------------------------------------------------------------------
#Question 8
# Get the dictionary values as a list
values = student.values()
print(values)
#-----------------------------------------------------------------------------------------------
#Question 9
# .items() extracts (key, value) tuples, list() turns it into a list of tuples
peer = student.items()
list_of_tuples = list(peer)
#-----------------------------------------------------------------------------------------------
#Question 10
"""Delete one of the items in the dictionary"""
student.pop('age')
print(student)
#-----------------------------------------------------------------------------------------------
#Question 11
# Delete the dictionaries
del dog
del student
