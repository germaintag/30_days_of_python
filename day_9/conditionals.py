#Day 9: 30 days of python
#--------------------------------------------------------------------------------------------------
#Exercises: Level 1
#--------------------------------------------------------------------------------------------------
#Question 1
#--------------------------------------------------------------------------------------------------
user_age = int(input("Enter your age:"))
if user_age >= 18:
    print("You are old enough to learn to drive.")
else:
    print("you need "+ str(18 - user_age) +" more years to learn to drive." )
#--------------------------------------------------------------------------------------------------
#Question 2 Must be completed
#--------------------------------------------------------------------------------------------------
#Question 3
a = int (input("Enter the first number:"))
b = int (input("Enter the second number:"))
if a > b :
    print( a , "is greater than b")
elif a < b :
    print( a , "is less than b")
else:
    print( a , "is equal to b")
#--------------------------------------------------------------------------------------------------
#Exercises: Level 2
#--------------------------------------------------------------------------------------------------
#Question 1: code which gives grade to students according to theirs scores
score = int(input("Enter you score: "))
if 0 <= score <= 59:
    print("Your grade is F")
elif 60 <= score <= 69:
    print("Your grade is D")
elif 70 <= score <= 79:
    print("Your grade is C")
elif 80 <= score <= 89:
    print("Your grade is B")
elif 90 <= score <= 100:
    print("Your grade is A")
#--------------------------------------------------------------------------------------------------
#Question 2
month = str(input("Enter your month:"))
if month == "September"or month == "October" or month == "November":
    print("the season is Autumn.")
elif month == "December"or month == "January" or month == "February":
    print("the season is winter.")
elif month == "March"or month == "Avril" or month == "May":
    print("the season is spring.")
elif month == "June"or month == "July" or month == "August":
    print("the season is summer.")
#--------------------------------------------------------------------------------------------------
#Question 3
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = str(input("Enter the new fruit:"))
if new_fruit in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(new_fruit)
print(fruits)
#--------------------------------------------------------------------------------------------------
#Exercises: Level 3
#--------------------------------------------------------------------------------------------------
person = {
        'first_name': 'Asabeneh',
        'last_name': 'Yetayeh',
        'age': 250,
        'country': 'Finland',
        'is_married': True,
        'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
        'address': {
            'street': 'Space street',
            'zipcode': '02210'
        }
    }
#Question 1
#Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if "skills" in person:
    middle_index = len(person["skills"]) // 2
    print(person["skills"][middle_index])
# --------------------------------------------------------------------------------------------------
#Question 2
#Check if the person dictionary has skills key and 'Python' as skill.
if "skills" in person:
    if "Python" in person["skills"]:
        print("The personn has python in his/her skills")
#--------------------------------------------------------------------------------------------------
#Question 3
#If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title')
skills = person['skills']
if len(skills) == 2 and 'JavaScript' in skills and 'React' in skills:
    print('He is a front end developer')
elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
    print('He is a backend developer')
elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
    print('He is a fullstack developer')
else:
    print('unknown title')
#--------------------------------------------------------------------------------------------------
#Question 4
#If the person is married and if he lives in Finland, print the information in the following format:  Asabeneh Yetayeh lives in Finland. He is married.
if person['is_married'] and person['country'] == 'Finland':
    print("Asabeneh Yetayeh lives in Finland. He is married.")