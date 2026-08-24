# 1. Create a custom math module and import it in another file.

import mathmod
print("Two Numbers is 10,5")
print("Addition:", mathmod.add(10,5))
print("Subtraction:", mathmod.sub(10,5))
print("Multiplication:", mathmod.mul(10,5))
print("Division:", mathmod.div(10,5))

# 2. Create a module to perform string operations.

import strmod

text = input("Enter Something:")

print("Length of", text, "is", strmod.length(text))
print("Uppercase of", text, "is", strmod.upper(text))
print("Lowercase of", text, "is", strmod.lower(text))

# 3. Use random module to generate 5 random integers.

import random

def a():
    num=[]
    
    for i in range(5):
        numbers = random.randint(1,45)
        num.append(numbers)
    
    return num

print("Here are generated five random numbers:")
print(a())
    
# 4. Use datetime module to display current date and time.

import datetime

d1 = datetime.date.today()
t1 = datetime.datetime.now().time()
print("Today's date is",d1)
print("Current time is",t1)

# 5. Use math module to find factorial of a number.

import math
num = int(input("Enter a number:"))
print(num, "Factorial is", math.factorial(num))

# 6. Create a package shapes with modules for circle and rectangle.

from shape import cir
from shape import rec

r = int(input("Please enter the radius:"))

print("Area of circle is",cir.area(r))
print("Circumference of circle is",cir.circumference(r))

l = int(input("Please enter the length of rectangle:"))
w = int(input("Please enter the width of rectangle:"))

print("Area of rectangle is",rec.area(l,w))
print("Parimeter of rectangle is",rec.perimeter(l,w))

# 7. Import multiple functions from one module and use them.

from shape import mul

print("10 Square:", mul.square(10))
print("5 Square:", mul.square(5))
print("10 Cube:", mul.cube(10))
print("5 Cube:", mul.cube(5))
print("Remainder:", mul.remainder(10,5))
print("Average:", mul.average(10,5))
print("Maximum:", mul.maximum(10,5))
print("Minimum:", mul.minimum(10,5))

# 8. Write a program to shuffle a list using random module.

import random
num = list(input("Please enter list number:").split())
random.shuffle(num)
print("Here are the shuffled list:", num)

# 9. Write a program to calculate the difference between two dates.

import datetime

bdate = datetime.date(2005 , 2 , 17)
cdate = datetime.date.today()

diff = cdate - bdate
print("User birthdate :", bdate)
print("Current date :", cdate)
print("Difference between both date is", diff.days, "days")

# 10. Use os module to list files in a directory.

import os
f = os.listdir("D:\\python\\shape")
print("Here are the files name which are stored in shape folder:")
for file in f:
    print(file)