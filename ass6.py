# # 1. Function to check if a number is prime.

def prime(num):
    count = 0
    
    for i in range (1, num+1):
        if num % i == 0:
            count = count + 1
        
    if count == 2:
        print(num, "is a Prime Number")
    else:
        print(num, "is not Prime Number")
    
number = int(input("Enter any Number :"))
prime(number)

# 2. Function to reverse a string.

def reverse(n):
    return n[::-1]

text=input("Enter Text:")
print(reverse(text))

# 3. Function to find factorial.

def factorial(n):
    fac = 1
    if n<1:
        return False
    for i in range(1,n+1):
        fac = i * fac
    return fac

num=int(input("enter the number:"))
print(num, "Factorial is",factorial(num))

# 4. Function to calculate simple interest.

def si(p,r,i):
    si = p*r*i/100
    return si

user1 = int(input("Enter the Principal:"))
user2 = int(input("Enter the Rate:"))
user3 = int(input("Enter the Time:"))

print("Total simple intrest is",si(user1,user2,user3))

# 5. Function to check if a word is palindrome.

def palindrome(n):
    a =n[::-1]
    if a == n:
        print("word is palindrome")
    elif a != n:
        print("word is not palindrome")

word = input("Enter a Word:")
palindrome(word)

# 6. Function to count vowels in a string.

def vowel(n):
    v="aeiou"
    count=0
    for i in n:
        if i in v:
            count=count+1
    return count

word = input("Enter a Word:")
print("Total number of vowels is",vowel(word))
 
# 7. Function to merge two lists.

def merge(a,b):
    c = []
    c = a + b
    return c

user1 = list(input("Enter List-1 :").split())
user2 = list(input("Enter List-2 :").split())

print(merge(user1,user2))

# 8. Function to find GCD of two numbers.

def g(a,b):
    gcd=0
    
    for i in range (1,min(a,b)+1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd

user1 = int(input("Enter first Number :"))
user2 = int(input("Enter second number :"))

print(g(user1,user2))

# 9. Function to find area of rectangle.

def rec(l,w):
    area = l*w
    return area

len = int(input("Enter Length:"))
wid = int(input("Enter Width:"))

print("Area of Rectangle is",rec(len,wid))

# 10. Function to check Armstrong number

def arm(n):
    count = 0
    
    for i in str(n):
        count = count + int(i) ** 3
        
    if count == n:
        return "Armstrong number"
    else:
        return "Not a Armstrong number"
        
num = int(input("Enter the number:"))
print(num, "Number is", arm(num))
        