#Day 5: 30 days of python
#--------------------------------------------------------------------------------------------------
#Exercises: Level 1
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
#--------------------------------------------------------------------------------------------------
#Exercises: Level 2
#--------------------------------------------------------------------------------------------------
#Question 1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age = ages[0]
max_age = ages[-1]
ages.append(min_age)
ages.append(max_age)
#Find the median age
ages.sort()
middle_index = len(ages) // 2
the_median_age = (ages[middle_index - 1]  +  ages[middle_index])/2
#Find the average age (sum of all items divided by their number )
average_age = sum(ages)/len(ages)
#Find the range of the ages (max minus min)
max_age = max(ages)
min_age = min(ages)
age_range = max_age - min_age
#Compare the value of (min - average) and (max - average), use abs() method
# Calculate the two distances
distance_min = abs(min(ages) - average_age)
distance_max = abs(max(ages) - average_age)

# Print both results to compare them
print("Distance min-average:", distance_min)
print("Distance max-average:", distance_max)
#--------------------------------------------------------------------------------------------------
#Question 2
countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo, Democratic Republic of the', 'Congo, Republic of the', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor (Timor-Leste)', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Macedonia', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']
middle_index = len(countries) // 2
middle_item = countries[middle_index]
print(middle_item)
#--------------------------------------------------------------------------------------------------
#Question 3
countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Central African Republic', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo, Democratic Republic of the', 'Congo, Republic of the', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor (Timor-Leste)', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Macedonia', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']
middle_index = len(countries) // 2
first_country_list = countries[:middle_index]
second_country_list = countries[middle_index:]
#Question 4
china, russia, usa, *scandic = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
