# 1 Check if a person is eligible to vote (age ≥ 18).

age = int(input("Enter your current Age:"))

if age >= 18:
    print("You are eligible for vote.")
else:
    print("You are not eligible for vote.")

# 2 Grade calculator based on marks: 90+ = A, 80+ = B, else C.

mark = int(input("Enter your total marks:"))

if mark >= 90:
    print("Grade-A")
elif mark >= 80:
    print("Grade-B")
else:
    print("Grade-C")

# 3 Simulate a traffic light: Red = Stop, Yellow = Wait, Green = Go.

light = (input("Enter the light colour:"))

if light == "red" or light == "Red":
    print("Light is Red Please Stop!!!")
elif light == "yellow" or light =="Yellow":
    print("Light is Yellow Please Wait!!!")
elif light == "green" or light=="Green":
    print("Light is Green you can Go now.")
else:
    print("Invalid Light Colour")   

# 4 ATM withdrawal check: sufficient balance or not.

balance = 4500
withdrawal = int(input("Please enter withdrawal amount:"))
if withdrawal <= balance:
    print("You have sufficient balance to withdraw money")
elif withdrawal>balance:
    print("You have not sufficient balance to withdraw money")

# 5 Check if a number is positive, negative, or zero.

no = int(input("Please enter the Number:"))
if no > 0:
    print("Entered number is positive")
elif no < 0:
    print("Entered number is negative")
elif no == 0:
    print("Entered number is Zero")
    

# 6 Check if a number lies within a given range.

nu = int(input("Guess the Number:"))

if nu>=18 and nu<=45:
    print("Congratulation, your number", nu, "is in the range between 18 & 45" )
else:
    print("Sorry, your number", nu, "is not in the range between 18 & 45" )

# 7 Username & password verification.

user = "Vansh" , "Vasu"
pas = 1234
u = input("Enter the Username:")
p = int(input("Enter your password:"))


if u in user and p == pas:
    print("Congratulation, Your Username and Password are Verified!!!")
elif u not in user and p != pas:
    print("Sorry, you enter wrong Username and Password!!!")
elif u not in user:
    print("Sorry, you enter wrong Username!!")
elif p != pas:
    print("Sorry, you enter wrong Password!!")
else:
    print("Something wrong!!")


# 8 Electricity bill calculator based on units consumed.

unit = int(input("Enter total number of unit you are used:"))
u1=unit*2
u2=unit*3
u3=unit*5
u4=unit*7

if unit>=0 and unit<=100:
    print("Your electicity bill is", u1)
elif unit>101 and unit<=200:
    print("Your electicity bill is", u2)
elif unit>200 and unit<=300:
    print("Your electicity bill is", u3)
elif unit>300:
    print("Your electicity bill is", u4)

# 9 Simple calculator (add, subtract, multiply, divide).

num1 = int(input("Enter the first number:"))
cal = input("Enter needed operation: + , - , * , / :")
num2 = int(input("Enter the Second number:"))
add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

if cal == "+":
    print("Addition of", num1,"+", num2, "=", add)
elif cal == "-":
    print("Subtraction of", num1,"-", num2, "=", sub)
elif cal == "*":
    print("Multiplication of", num1,"*", num2, "=", mul)
elif cal == "/":
    print("Division of", num1,"/", num2, "=", div)
else:
    print("Something wong!!!")

# 10 Check type of triangle (equilateral, isosceles, scalene).

fir = int(input("Enter the length of AB:"))
sec = int(input("Enter the length of BC:"))
thi =int(input("Enter the length of AC:"))

if fir == sec == thi:
    print("Type of triangle is equilateral")
elif fir == sec != thi or fir == thi != sec:
    print("Type of triangle is isosceles")
elif fir != sec != thi:
    print("Type of triangle is scalene")