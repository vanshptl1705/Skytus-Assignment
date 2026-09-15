# 1 Print numbers from 1 to 10.

for i in range(1, 11):
    print(i)

# 2 Display multiplication table for a given number.

a = int(input("Enter the number:"))

for i in range(1 , 11):
    print(a, "*", i, "=", a*i)

# 3 Find factorial of a number.

num = int(input("Enter a number:"))
factorial = 1

for i in range(1, num+1):
    factorial = factorial * i

print(num, "Factorial is", factorial)

# 4 Generate the first N Fibonacci numbers.

num = int(input("Enter a number:"))
n1 = 0
n2 = 1
print("Generating fibonacci numbers :")
for i in range(num):
    print(n1, end=" ,")
    n1 , n2=n2 , n1+n2

print()

# 5 Check if a number is prime.

n = int(input("Enter a number:"))
no = 0 

for i in range(1,n+1):
    if n % i == 0:
        no = no+1

if no == 2:
    print(n, "is prime number.")
else:
    print(n, "is not a prime number.")

# 6 Reverse a number (e.g., 123 → 321).

num = input("Enter a number:")
reverse = ""
for i in num:
    reverse = i + reverse

print(reverse)

# 7 Count digits in a number.

try:
    num = (input("Enter a number:"))
    for i in num:
        if not i.isdigit():
            raise ValueError
    print(len(num))

except ValueError:
    print("Please Enter any Digit!!!")

# 8 Find sum of even numbers between 1–100.

number = 0
for i in range(1,101):
    if i % 2 == 0:
        number = number + i

print("sum of even numbers between 1 to 100 is", number)       

# 9 Print a pyramid pattern.

num = int(input("Enter a number:"))

for i in range(1 , num+1):
    print(" " * (num-i) + "* " * i)

# 10 Find all divisors of a number.

num = int(input("Enter a number:"))
print("Divisors of", num, "are:")
    
for i in range(1,num):
    if num % i == 0:
        print(i)