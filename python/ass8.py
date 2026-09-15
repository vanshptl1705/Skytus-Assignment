# 1. Write a program to handle division by zero error.

u1 = int(input("Enter the Number:"))
u2= int(input("Enter the divisible number:"))
try:
    u = u1 / u2
    print(u1, "divisible by",u2 ,"is",u)
except:
    if u2 == 0:
        print("Error: Cannot divide by zero.")
        
# 2. Write a program to handle invalid integer input.

u1 = input("Enter the Number:")
try:
    print(int(u1))
except ValueError:
    print("Error; you enter invalid integer input")

# 3. Write a program to open a file and handle the "file not found" error.

try:
    f=open(input("File-name:"),"r")
    print(f.read())
    f.close()
        
except FileNotFoundError:
    print("Sorry,File are not found!!!")
    
# 4. Write a program to demonstrate multiple exception blocks.

try:
    u1 = int(input("Enter the Number:"))
    u2= int(input("Enter the divisible number:"))
    print("Answer is ", u1/u2)
except ValueError:
    print("Error:Please enter proper Value")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# 5. Write a program to use finally for resource cleanup.

file = False

try:
    f=open(input("File-name:"),"r")
    print(f.read())
    file = True
        
except FileNotFoundError:
    print("Error:File are not found!!!")
    
finally:
    if file == True:
        print("\n","The File is Executed Successfully...")
    else:
        print("\n","The File is not Executed...")

# 6. Write a program to create a custom exception for invalid age (<18).

class ia(Exception):
    pass

try:
    a = int(input("Enter your current age:"))

    if a<18:
        raise ia
    
    print("You are eligible for voting...")
    
except ia:
    print("Sorry,You are not eligible for voting...")
    
except ValueError:
    print("Error:Please enter proper Value")

# 7. Write a program to handle IndexError when accessing a list.

try:
    l1 = list(input("Enter List here:").split())
    index = int(input("Enter index number:"))
    print("Index Value is", l1[index])

except IndexError:
    print("Error:In List this Index Doesn't found...")

except ValueError:
    print("Error:Please enter proper Value")

# 8. Write a program that takes two numbers and handles all possible errors.

try:
    u1 = int(input("Enter the Number: "))
    u2 = int(input("Enter the divisible number: "))
    print("Answer is", u1 / u2)

except ValueError:
    print("Error: Please enter a proper value.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
    
except Exception:
    print("Error: Something went wrong.")

# 9. Write a program to log errors to a file instead of printing them.

try:
    n1=int(input("Enter first number:"))
    n2=int(input("Enter second number:"))
    n = n1/n2
    print("Output:", n)

except Exception as a:
    f=open("error.log","a")
    f.write(str(a) + "\n")
    f.close()
    
    print("Error are Happend,please check files which name is error.log") 
    
# 10. Write a program that validates an email format and raises an exception for invalid ones.

class ve(Exception):
    pass

try:
    e = input("Please enter your email:")
    if "@gmail.com" not in e:
        raise ve
    
    print("valid Email")

except ve:
    print("Invalid Email")