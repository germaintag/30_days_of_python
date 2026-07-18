#Day 5: 30 days of python
#--------------------------------------------------------------------------------------------------
#Question 1
"""Declare an empty list"""
empty_list = []

#--------------------------------------------------------------------------------------------------
#Question 2
"""Declare a list with more than 5 items"""
the_list = [1, 2, 3, 4, 5, 6]

#--------------------------------------------------------------------------------------------------
#Question 3
"""Find the length of your list"""
print(len(the_list))

#--------------------------------------------------------------------------------------------------
#Question 4
"""Get the first item, the middle item and the last item of the list"""
first_item = the_list[0]
print(first_item)

middle_index = len(the_list) // 2
middle_item = the_list[middle_index]
print(middle_item)

last_item = the_list[-1]
print(last_item)

#--------------------------------------------------------------------------------------------------
#Question 5
"""Declare a list called mixed_data_types, put your(name, age, height, marital status, address)"""
mixed_data_types = ["Emmanuel", 36, "single", "55 Rue du Faubourg Saint-Honoré, 75008 Paris"]

#--------------------------------------------------------------------------------------------------
#Question 6
"""Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon."""
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

#--------------------------------------------------------------------------------------------------
#Question 7
"""Print the list using print()"""
print(it_companies)

#--------------------------------------------------------------------------------------------------
#Question 8
"""Print the number of companies in the list"""
number = len(it_companies)
print("we have ", number, " company")

#--------------------------------------------------------------------------------------------------
#Question 9
"""Print the first, middle and last company"""
first_item = it_companies[0]
print(first_item)

middle_index = len(it_companies) // 2
middle_item = it_companies[middle_index]
print(middle_item)

last_item = it_companies[-1]
print(last_item)

#--------------------------------------------------------------------------------------------------
#Question 10
"""Print the list after modifying one of the companies"""
it_companies[0] = "Meta"  # On modifie le premier élément
print(it_companies)

#--------------------------------------------------------------------------------------------------
#Question 11
"""Add an IT company to it_companies"""
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.append("IT company")
print(it_companies)

#--------------------------------------------------------------------------------------------------
#Question 12
"""Insert an IT company in the middle of the companies list"""
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
middle_index = len(it_companies) // 2
it_companies.insert(middle_index, "IT company")
print(it_companies)

#--------------------------------------------------------------------------------------------------
#Question 13
"""Change one of the it_companies names to uppercase (IBM excluded!)"""
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
string = "Facebook"
it_companies.remove("Facebook")
it_companies.insert(0, string.upper())
print(it_companies)

#--------------------------------------------------------------------------------------------------
#Question 14
"""Join the it_companies with a string '#;  '"""
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
# Correction : Pour joindre proprement des éléments avec un séparateur, on utilise .join()
result = '#;  '.join(it_companies)
print(result)

#--------------------------------------------------------------------------------------------------
#Question 15
"""Check if a certain company exists in the it_companies list."""
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
does_exist = "Facebook" in it_companies
print(does_exist)

#--------------------------------------------------------------------------------------------------
#Question 16
"""Sort the list using sort() method"""
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.sort()
print(it_companies)

#--------------------------------------------------------------------------------------------------
#Question 17
"""Reverse the list in descending order using reverse() or sort(reverse=True) method"""
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.sort(reverse=True)
print(it_companies)

#--------------------------------------------------------------------------------------------------
#Question 18
"""Slice out the first 3 companies from the list"""
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies[:3])

#--------------------------------------------------------------------------------------------------
#Question 19
"""Slice out the last 3 companies from the list"""
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies[-3:])

#--------------------------------------------------------------------------------------------------
#Question 20
"""Slice out the middle IT company or companies from the list"""
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
middle_index = len(it_companies) // 2
print(it_companies[middle_index : middle_index + 1])

#--------------------------------------------------------------------------------------------------
#Question 21
"""Remove the first IT company from the list"""
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.pop(0)  # Ou it_companies.remove(it_companies[0])
print(it_companies)

#--------------------------------------------------------------------------------------------------
#Question 22
"""Remove the middle IT company or companies from the list"""
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
middle_index = len(it_companies) // 2
it_companies.remove(it_companies[middle_index])
print(it_companies)

#--------------------------------------------------------------------------------------------------
#Question 23
"""Remove the last IT company from the list"""
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.remove(it_companies[-1])
print(it_companies)

#--------------------------------------------------------------------------------------------------
#Question 24
"""Remove all IT companies from the list"""
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.clear()
print(it_companies)

#--------------------------------------------------------------------------------------------------
#Question 25
"""Destroy the IT companies list"""
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
del it_companies

#--------------------------------------------------------------------------------------------------
#Question 26
"""Join the following lists"""
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
front_end_and_back_end = front_end + back_end
print(front_end_and_back_end)

#--------------------------------------------------------------------------------------------------
#Question 27
"""After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux."""
full_stack = front_end_and_back_end.copy()
# Insertion of Python et SQL just after 'Redux'
redux_index = full_stack.index('Redux')
full_stack.insert(redux_index + 1, "Python")
full_stack.insert(redux_index + 2, "SQL")
print(full_stack)