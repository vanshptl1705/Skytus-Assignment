# 1 Write a program to print your name, age, and city in one line.

name = "Vansh Patel"
age = 21
city = "Billimora"
print("Name :", name , ", Age :", age , ", City :", city)

# 2 Take user input for two numbers and print their sum.

Number1 = int(input("Enter First Number ="))
Number2 = int(input("Enter Second Number ="))
Addition = Number1 + Number2
print("Addition of both number is", Addition)

# 3 Write a program to convert temperature from Celsius to Fahrenheit.
# Celsius To Fahrenheit Formula C>F : (C*9/5 +32 = F)

celsius = int(input("Enter the temprature in Celsius :"))
convert = (celsius*9/5+32)
print("Celsius:", celsius, "to Faherenheit:", convert)

# 4 Store your name in a variable and print it in uppercase.

namee = input("Enter your Name:")
print(namee.upper())

# 5 Ask the user for their birth year and calculate their current age.

BY = int(input("Enter Your Bornyear:"))
CY = 2026
Age = CY-BY
print("Your Current Age is:", Age)

# 6 Write a program to swap the values of two variables.

a = 36
b = 41

bag = a
a = b
b = bag

print("Value of a:" ,a)
print("Value of b:" ,b)

# 7 Create a program to calculate the area of a rectangle from user inputs.

length = int(input("Enter the value of Length:"))
width = int(input("Enter the value of Width:"))

rectangle = length*width

print("The area of rectangle is", rectangle)

# 8 Write a program to check if a number is positive or negative.

num = int(input("Enter the Number:"))

if num>0:
    print("This number is Positive")
else:
    print("This number is Negative")

# 9 Ask for two numbers and print their average.

num1 = int(input("Enter First value :"))
num2 = int(input("Enter Second value :"))

average = (num1 + num2) / 2

print("Average of both number is:" ,average)
