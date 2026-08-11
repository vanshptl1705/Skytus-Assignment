# 1 Calculate the remainder of two numbers.

n1 = int(input("Enter First Number :"))
n2 = int(input("Enter Second Number :"))

remainder = n1 % n2
print("The Remainder is:", remainder)

# 2 Check if a number is even or odd.

z = int(input("Enter the Number :"))

if z%2==0:
    print(z, "is Even Number")
else:
    print(z, "is Odd Number")  


# 3 Compare two numbers and print the larger one.

n11 = int(input("Enter First Number :"))
n12 = int(input("Enter Second Number :"))

if n11>n12:
    print(n11, "is Larger Number")
else:
    print(n12, "is Larger Number")

# 4 Write a program to calculate the square and cube of a number.

z1 = int(input("Enter the Number:"))

square = z1 ** 2
cube = z1 ** 3

print(z1, "Square is", square)
print(z1, "Cube is", cube)

# 5 Check if two entered numbers are equal.

n13 = int(input("Enter First Number :"))
n14 = int(input("Enter Second Number :"))

if n13 is n14:
    print("Both numbers are equal")
else:
    print("Both numbers are not equal")

# 6 Take two numbers and print True if both are positive, else False.

n15 = int(input("Enter First Number :"))
n16 = int(input("Enter Second Number :"))
l = ("Both number are Positive is")

if n15>0 and n16>0:
    print(l, "True")
else:
    print(l, "False")

# 7 Write a program to convert float to integer.

float = 10.37
i1 = int(float)
print(i1)

# 8 Take a number as string, convert it into int, and multiply by 10.

num = ("25")
inte = int(num)
res = inte * 10
print(res)

 # 9 Write a program that uses & or operators to check multiple conditions.

power = int(input("Enter remainder Power of player:"))
life = int(input("Enter remainder Life of player:"))
special_power = int(input("Enter remainder Special_Power of player:"))

if (power>=40 and life>1) or special_power>= 80:
    print("Player are ready to go Next Level")
else:
    print("Game Over")

 # 10 Divide two numbers and print the quotient and remainder separately.
 
n17 = int(input("Enter First Number :"))
n18 = int(input("Enter Second Number :"))

quo = n17 // n18
rem = n17 % n18

print("quotient is", quo)
print("remainder is", rem)