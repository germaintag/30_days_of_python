#Day 9: 30 days of python
#--------------------------------------------------------------------------------------------------
#Exercises: Level 1
#Question 1
user_age = int(input("Enter your age:"))
if user_age >= 18:
    print("You are old enough to learn to drive.")
else:
    print("you need "+ str(18 - user_age) +" more years to learn to drive." )
#Question 2 Must be completed

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
#Question 1
#Question 2
#Question 3
