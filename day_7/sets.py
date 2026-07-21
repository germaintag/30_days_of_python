#Day 7: 30 days of python
#-----------------------------------------------------------------------------------------------
#exercice level 1
#-----------------------------------------------------------------------------------------------
# Setup data
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Question 1
# Getting the number of elements in the set with len()
print("the length of it_companies is: ", len(it_companies))

#Question 2
# Adding a single item to the set using .add()
it_companies.add('Twitter')

#Question 3
# Adding multiple items at once using .update() with a list
it_companies.update(["huawei","nothing"])

#Question 4
# Removing an item with .remove() (raises KeyError if item doesn't exist)
it_companies.remove("Google")

#Question 5
"""What is the difference between remove and discard?"""
# Note: .remove() throws an error if the item is missing,
# while .discard() does nothing and won't crash the code.
#-----------------------------------------------------------------------------------------------
#exercice level 2
#Question 1
#Returns a new set with items from both sets.
print(A.union(B))
#-----------------------------------------------------------------------------------------------
#Question 2
#Gets common elements between both sets
print(A.intersection(B))
#-----------------------------------------------------------------------------------------------
#Question 3
#Checks if all elements of A are inside B (returns True or False)
print(A.issubset(B))
#-----------------------------------------------------------------------------------------------
#Question 4
#Checks if A and B have NO common elements (returns False here)
print(A.isdisjoint(B))
#-----------------------------------------------------------------------------------------------
#Question 5
#Joining sets both ways
a_union_b = A.union(B)
b_union_a = B.union(A)
#-----------------------------------------------------------------------------------------------
#Question 6
#Symmetric difference gets elements that are in A or B, but not in both
print(A.symmetric_difference(B))
#-----------------------------------------------------------------------------------------------
#Question 7
# Deleting variables completely from memory
del A
del B
del it_companies
#-----------------------------------------------------------------------------------------------
#Question 1
#Converting list to set automatically removes duplicate values
st = set(age)
#Comparing lengths
print("the length of the list is: ", len(age))
print("the length of the set is: ", len(st))
# Note: The list is bigger (length 8 vs 5) because it contains duplicate ages.
#-----------------------------------------------------------------------------------------------
#Question 2
"""Explain the difference between the following data types: string, list, tuple and set"""
#String: Text data enclosed in quotes. It is ordered, indexable, but immutable.

#List:Ordered collection of items. Mutable and allows duplicates.

#Tuple:Ordered collection of items. Immutable (cannot be changed after creation) and allows duplicates.

#Set:Unordered collection of unique items. Mutable, but doesn't allow duplicates or indexing.

#-----------------------------------------------------------------------------------------------
#Question 3
# Splitting sentence into words, converting to set to extract unique words
phrase = "I am a teacher and I love to inspire and teach people"
phrase_first_version = phrase.split()
st = set(phrase_first_version)
print(st)
print("the length of the set is: ", len(st))