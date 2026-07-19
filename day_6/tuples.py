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
# Correction : On utilise len(siblings) pour compter le total des frères et sœurs, et on l'affiche avec print()
print(len(siblings))
#--------------------------------------------------------------------------------------------------
#Question 5
"""Modify the siblings tuple and add the name of your father and mother and assign it to family_members"""
parents = ("rihanna", "asap")
family_members = siblings + parents
print(family_members)