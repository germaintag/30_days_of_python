#Day 3: 30 days of python
#Question 1
age = 20

#Question 2
height = 1.77

#Question 3
complex_number = 20 + 1j

#Question 4
base = int(input("Enter the base: "))
the_height = int(input("Enter the hight: "))
triangle_area = (0.5 * base * the_height)
print(" The area of the triangle is: ",triangle_area)

#Question 5
a = int(input("Enter the side a: "))
b = int(input("Enter the side b: "))
c = int(input("Enter the side c: "))
perimeter = a + b + c
print(" The perimeter of the triangle is: ",perimeter)

#Question 6
lenght = float(input("Enter the lenght: "))
width  = float(input("Enter the width: "))
area = (lenght * width)
perimeter = (2 * (lenght + width))
print(" The perimeter of the rectangle is: ",perimeter ,"and the area of the rectangle is: ",area)

#Question 7
import math
cercle_radius = float(input("Enter the cercle radius: "))
pi = math.pi
area = pi * cercle_radius * cercle_radius
cercle_circumference = 2 * pi * cercle_radius
#Question 8
# calculate the  slope, x-intercept and y-intercept of y = 2x -2
slope = 2
y_intercept = -2
x_intercept =  y_intercept / slope
#Question 9
"""
Calculate the slope and Euclidean distance betwenn point (2, 2) and point (6,10)
#Slope is (m = y2-y1/x2-x1)
"""
slope_2 = (10 - 2)/(6 - 2)
euclidean_distance = math.sqrt(pow(6-2,2) + pow(10-2,2))
#Question 10
#Question 11
#Question 12
"""
Calculate the length of the words "python" and "dragon",then make a falsy comparison to check if their lengths are different.
"""
first_word = "python"
second_word = "dragon"
#calcul of lenght
length_python = len(first_word)
length_dragon = len(second_word)
print("the lenght of the word pyton is :",len(first_word))
print("the lenght of the word dragon is :",len(second_word))
# Comparaison falsy : check if their lenght are different
falsy_comparison = length_python != length_dragon
print(falsy_comparison)
#Question 21
"""
Calculate the pay of the person based on hours worked and hourly rate.
"""
hours = int(input("Enter the hours: "))
rate_per_hour = float(input("Enter the rate per hours: "))
weekly_earning = hours * rate_per_hour
print("the weekly earning is :" ,weekly_earning)
#Question 22
"""
Calculate the number of seconds a person can live.
"""
number_of_year_lived = int (input("Enter the number of years lived: "))
#31536000 correspond to the numbers of second in a  year
number_of_second_lived = number_of_year_lived * 31536000
print("You have lived for ",number_of_second_lived, " seconds")
#Question 22
"""
Python script that displays the following table
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
"""
line1 = [1, 1, 1, 1, 1]
line2 = [2, 1, 2, 4, 8]
line3 = [3, 1, 3, 9, 27]
line4 = [4, 1, 4, 16, 64]
line5 = [5, 1, 5, 25, 125]
# Displays every lines
print(line1)
print(line2)
print(line3)
print(line4)
print(line5)





































