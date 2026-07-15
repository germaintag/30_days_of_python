#Day 3: 30 days of python
#--------------------------------------------------------------------------------------------------
#Question 1
age = 20
#--------------------------------------------------------------------------------------------------
#Question 2
height = 1.77
#--------------------------------------------------------------------------------------------------
#Question 3
complex_number = 20 + 1j
#--------------------------------------------------------------------------------------------------
#Question 4
base = int(input("Enter the base: "))
the_height = int(input("Enter the hight: "))
triangle_area = (0.5 * base * the_height)
print(" The area of the triangle is: ",triangle_area)
#--------------------------------------------------------------------------------------------------
#Question 5
a = int(input("Enter the side a: "))
b = int(input("Enter the side b: "))
c = int(input("Enter the side c: "))
perimeter = a + b + c
print(" The perimeter of the triangle is: ",perimeter)
#--------------------------------------------------------------------------------------------------
#Question 6
lenght = float(input("Enter the lenght: "))
width  = float(input("Enter the width: "))
area = (lenght * width)
perimeter = (2 * (lenght + width))
print(" The perimeter of the rectangle is: ",perimeter ,"and the area of the rectangle is: ",area)
#--------------------------------------------------------------------------------------------------
#Question 7
import math
cercle_radius = float(input("Enter the cercle radius: "))
pi = math.pi
area = pi * cercle_radius * cercle_radius
cercle_circumference = 2 * pi * cercle_radius
#--------------------------------------------------------------------------------------------------
#Question 8
# calculate the  slope, x-intercept and y-intercept of y = 2x -2
slope = 2
y_intercept = -2
x_intercept =  y_intercept / slope
#--------------------------------------------------------------------------------------------------
#Question 9
"""
Calculate the slope and Euclidean distance betwenn point (2, 2) and point (6,10)
#Slope is (m = y2-y1/x2-x1)
"""
slope_2 = (10 - 2)/(6 - 2)
euclidean_distance = math.sqrt(pow(6-2,2) + pow(10-2,2))
#--------------------------------------------------------------------------------------------------
#Question 10
#1 check if both slope are equal
are_equal = slope == slope_2
print("Are the slopes equal ?", are_equal)
#2 check if the first slope is greater than the second slope
is_first_slope_greater = slope > slope_2
print("Is the first slope greater than slope 9?", is_first_slope_greater)
#3 check if the second slope is greater than the first slope
is_second_slope_greater = slope < slope_2
print("Is the second slope greater than slope 8?", is_second_slope_greater)
#--------------------------------------------------------------------------------------------------
#Question 11
"""
Calculate the value of y (y = x^2 + 6x + 9).
Try to use different x values and figure out at what x value y is going to be 0.
"""
# Trial 1: If x is 0
x_test1 = 0
y_test1 = (x_test1 ** 2) + (6 * x_test1) + 9
print("If x is 0, y is:", y_test1)

# Trial 2: If x is 2
x_test2 = 2
y_test2 = (x_test2 ** 2) + (6 * x_test2) + 9
print("If x is 2, y is:", y_test2)

# Trial 3: If x is -3 (Our answer!)
x_test3 = -3
y_test3 = (x_test3 ** 2) + (6 * x_test3) + 9
print("If x is -3, y is:", y_test3)

# Comparison to prove that y is equal to 0 when x is -3
is_y_zero = (y_test3 == 0)
print("Is y equal to 0 when x is -3 ?", is_y_zero)
#--------------------------------------------------------------------------------------------------
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
#--------------------------------------------------------------------------------------------------
#Question 13
"""
Check if "on" is found in both 'python' and 'dragon'
"""
first_word = "python"
second_word = "dragon"
result = "on" in first_word and second_word == "dragon"
print(result)
#--------------------------------------------------------------------------------------------------
#Question 14
phrase = "I hope this course is not full of jargon."
the_result = "jargon" in phrase
print(the_result)
#--------------------------------------------------------------------------------------------------#--------------------------------------------------------------------------------------------------
#Question 15
"""
Check if 'on' is NOT in both 'dragon' and 'python'
"""
no_on_in_dragon = "on" not in "dragon"
no_on_in_python = "on" not in "python"
final_result = no_on_in_dragon and no_on_in_python
print("There is no 'on' in both dragon and python:", final_result)
#--------------------------------------------------------------------------------------------------
"""
Find the length of the text python and convert the value to float and convert it to string
"""
text_length = len("python")
print(text_length)
text_length_in_to_float = float(text_length)
text_length_in_to_string = str(text_length_in_to_float)
print(text_length_in_to_float)
print(text_length_in_to_string)
#--------------------------------------------------------------------------------------------------
#Question 17
"""
check if the number is divisible by 2
"""
le_nombre = int(input("Enter the number:"))
is_divisible = le_nombre % 2 == 0
print(is_divisible)
#--------------------------------------------------------------------------------------------------
#Question 18
"""
Check if the floor division of 7 by 3 is equal to the int converted value of 2.7
"""
floor_division = 7//3
number_0 = int(2.7)
print(floor_division is number_0)
#--------------------------------------------------------------------------------------------------
#Question 19
"""
Check if type of '10' is equal to type of 10
"""
the_compared = "on"
the_comparing_element =  10
print(the_compared is the_comparing_element)
#--------------------------------------------------------------------------------------------------
#Question 20
first_number = int(9.8)
second_number = 10
print( first_number is second_number )
#--------------------------------------------------------------------------------------------------
#Question 21
"""
Calculate the pay of the person based on hours worked and hourly rate.
"""
hours = int(input("Enter the hours: "))
rate_per_hour = float(input("Enter the rate per hours: "))
weekly_earning = hours * rate_per_hour
print("the weekly earning is :" ,weekly_earning)
#--------------------------------------------------------------------------------------------------
#Question 22
"""
Calculate the number of seconds a person can live.
"""
number_of_year_lived = int (input("Enter the number of years lived: "))
#31536000 correspond to the numbers of second in a  year
number_of_second_lived = number_of_year_lived * 31536000
print("You have lived for ",number_of_second_lived, " seconds")
#--------------------------------------------------------------------------------------------------
#Question 23
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

