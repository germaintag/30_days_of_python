#Day 6: 30 days of python
#--------------------------------------------------------------------------------------------------
#Exercises: Level 1
#--------------------------------------------------------------------------------------------------
#Question 1
"""Create an empty tuple"""
empty_tuple = ()
#--------------------------------------------------------------------------------------------------
#Question 2
"""Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)"""
brother_tuple = ("john", "callum")
sister_tuple = ("snow", "djodjoklidjo")
#--------------------------------------------------------------------------------------------------
#Question 3
"""Join brothers and sisters tuples and assign it to siblings"""
siblings = brother_tuple + sister_tuple
#--------------------------------------------------------------------------------------------------
#Question 4
"""How many siblings do you have?"""
print(len(siblings))
#--------------------------------------------------------------------------------------------------
#Question 5
"""Modify the siblings tuple and add the name of your father and mother and assign it to family_members"""
parents = ("rihanna", "asap")
family_members = siblings + parents
#--------------------------------------------------------------------------------------------------
#Exercises: Level 2
#--------------------------------------------------------------------------------------------------
# Question 1
# Unpacking: Using * to capture all siblings, while assigning the last two values to father and mother
*siblings, father, mother = family_members
#--------------------------------------------------------------------------------------------------
# Question 2
# Creating separate tuples for each category and joining them together using the + operator
fruits = ("mango", "orange")
vegetables = ("laitue", "choux", "aubergine")
animal_products = ("meat", "milk")
food_stuff_tp = fruits + vegetables + animal_products
#--------------------------------------------------------------------------------------------------
# Question 3
# Converting the tuple to a list so it becomes mutable (easier to modify if needed)
food_stuff_tp = list(food_stuff_tp)
# ------------------------------------------------------------------------------------------------
# Question 4
# Finding the middle item by calculating the center index with integer division (//)
middle_index = len(food_stuff_tp) // 2
# Extracting the item at the middle index
middle_item = food_stuff_tp[middle_index]
print(middle_item)
# -------------------------------------------------------------------------------------------------
# Question 5
# Slicing the list: getting the first 3 elements, then getting elements from index 4 to the end
first_three_items = food_stuff_tp[:3]
last_three_items = food_stuff_tp[4:]
# -------------------------------------------------------------------------------------------------
# Question 6
# Completely removing the variable from memory using del
del food_stuff_tp
# -------------------------------------------------------------------------------------------------
# Question 7
# Checking if specific elements exist inside the tuple using the 'in' keyword
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)