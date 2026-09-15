# 1. Create a Car class with attributes like brand, model, and speed, and methods to accelerate/brake.

class Car:
    def __init__(self,brand,model,speed):
        self.brand=brand
        self.model=model
        self.speed=speed 
    
    def accelerate(self):
        self.speed += 50
        print("After Acceleration speed is", self.speed)
 
    def brake(self):
        self.speed -= 30
        print("After brake speed is", self.speed)   
        
brand = input("Enter car Brand:")
model = input("Enter car Model:")
speed = int(input("Enter car Speed:"))  

c1 = Car(brand,model,speed)
print(" Car brand is",c1.brand,"\n","Car model is",c1.model,"\n","Car maximum speed is",c1.speed)
c1.accelerate()
c1.brake() 

# 2. Create a BankAccount class with deposit and withdraw methods.

class Bank:
    def __init__(self,balance):
        self.balance = balance
        
    def dep(self):
        self.balance += 1500
        print("After deposit your total bank balance is", self.balance)

    def wit(self):
        self.balance -= 800
        print("After withdraw your total bank balance is", self.balance)
        
balance = int(input("Enter your total bank balance:"))

b1 = Bank(balance)

print("Your available bank balance is",b1.balance)

b1.dep()
b1.wit()       

# 3. Create a Student class with a method to calculate average marks.

class Stu:
    def __init__(self,mark):
        self.mark=mark
    
    def avg(self):
        add = 0
        for i in self.mark:
            add += i
            
        print("Your Average Marks is", add/5)

m1 = int(input("Enter Maths Marks:"))
m2 = int(input("Enter Science Marks:"))
m3 = int(input("Enter English Marks:"))
m4 = int(input("Enter Sanskrit Marks:"))
m5 = int(input("Enter SS Marks:"))

mark = [m1, m2, m3, m4, m5]
m1 = Stu(mark)
print(m1.mark)
m1.avg()       

# 4. Create a Rectangle class with methods to find area and perimeter.

class Rectangle():
    
    def __init__(self,length,width):
        self.length = length
        self.width = width
        
    def area(self):
        ar = self.length * self.width
        print("Area of rectangle is",ar)
    
    def parimeter(self):
        ar = 2*(self.length * self.width)
        print("Parimeter of rectangle is",ar)
        
len=int(input("Enter total length of rectangle:"))
wid=int(input("Enter total width of rectangle:"))
rec = Rectangle(len,wid)
rec.area()
rec.parimeter()     

# 5. Create an Employee class that displays salary details.

class Employee:
    def __init__(self,name,salary,leave_days):
        self.name = name
        self.salary = salary
        self.leave_days = leave_days
    
    def total(self):
        total_cut_salary = 0
        for i in range(self.leave_days):
            total_cut_salary += 350
        
        print(" But after reduction your total amount of salary is", self.salary-total_cut_salary)

name = input("Enter your name:")       
salary = int(input("Enter your total bank balance:"))
leave = int(input("Enter number of leaves:"))

s1 = Employee(name,salary,leave)
print(" Hey",s1.name,"\n Your this month salary is",s1.salary)
s1.total()

# 6. Create a Book class to store title, author, and price, and display details.

class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

title = input("Enter title of book:")
author = input("Enter book's author name:")
price = int(input("Enter price of book:"))
b1=Book(title,author,price)
print(" Book Name is",b1.title , "\n", "Book's author name is",b1.author, "\n" , "Price of book is",b1.price)

# 7. Create a Circle class to find area and circumference.

class Circle:
    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        area = 3.141592653589793*(self.radius**2)
        print("Area of circle is",area)
    
    def circumference(self):
        circumference = 2*(3.141592653589793 * self.radius)
        print("Circumference of circle is",circumference)
        
radius = int(input("Enter the radius of circle:"))
r1 = Circle(radius)
r1.area()
r1.circumference()

# 8. Create a Laptop class with a method to apply discounts on price.

class Laptop:
    def __init__(self,laptop,price,student_id):
        self.laptop=laptop
        self.price=price
        self.student_id=student_id
        
    def dis(self):
        if self.laptop.lower() == "android" and self.student_id.lower() == "yes":
            dis = 20
        elif self.laptop.lower() == "ios" and self.student_id.lower() == "yes":
            dis=15
        elif self.laptop.lower() == "android":
            dis = 15
        elif self.laptop.lower() == "ios":
            dis = 10
            
        discount = self.price*dis/100
        print("Your final price of laptop after festival season discount is", self.price-discount)

laptop= input("What Laptop you needed (Android / IOS):")
price= int(input("Enter laptop price:"))
student_id=input("You have student-id [Yes/No]:")

l1 = Laptop(laptop,price,student_id)
l1.dis()

# 9. Create a Flight class with seat booking functionality.

class Flight:
    def __init__(self,flight_name,destination,available_seat):
        self.flight_name = flight_name
        self.destination = destination
        self.available_seat = available_seat
        
    def seat(self):
        
        s1 = 5
        s2 = 7
        s3 = 3
        s4 = 11
        
        if self.flight_name.lower() == "indigo" and self.destination.lower() == "mumbai" and self.available_seat.lower() == "yes":
            que = input("seat are available you need to book ? [Yes / No]")
            if que.lower() == "yes":
                s1 -= 1
                print("Your Seat are booked successfully")
                print("Available seat:", s1)
            else:
                print("Thank you for visit!!!")       

        elif self.flight_name.lower() == "indigo" and self.destination.lower() == "delhi" and self.available_seat.lower() == "yes":
            que = input("seat are available you need to book ? [Yes / No]")
            if que.lower() == "yes":
                s2 -= 1
                print("Your Seat are booked successfully")
                print("Available seat:", s2)
            else:
                print("Thank you for visit!!!")

        elif self.flight_name.lower() == "airindia" and self.destination.lower() == "mumbai" and self.available_seat.lower() == "yes":
            que = input("seat are available you need to book ? [Yes / No]")
            if que.lower() == "yes":
                s3 -= 1
                print("Your Seat are booked successfully")
                print("Available seat:", s3)
            else:
                print("Thank you for visit!!!")
                
        elif self.flight_name.lower() == "airindia" and self.destination.lower() == "delhi" and self.available_seat.lower() == "yes":
            que = input("seat are available you need to book ? [Yes / No]")
            if que.lower() == "yes":
                s4 -= 1
                print("Your Seat are booked successfully")
                print("Available seat:", s4)
            else:
                print("Thank you for visit!!!")
                
        elif self.available_seat.lower() == "no":
            print("Sorry!!! Seats are not Available") 
            print("Thank you for visit!!!") 
        
        else:
            print("Thank you for visit!!!")
        
flight_name = input("Enter flight name [IndiGo / AirIndia] :")
destination = input("Enter your destination [Mumbai  / Delhi] :")
available_seat = input("Are seat available? [Yes / No] :")
f1 = Flight(flight_name,destination,available_seat)
f1.seat()

# 10. Create a Shop class with a method to add and list products.

class Shop:
    def __init__(self):
        self.product=[]
    
    def add(self):
        name = input("Enter product name:")
        price = input("Enter product price:")
        self.product.append([name , price])
    
    def display(self):
        print("Here are the detail about all products:")
        print(self.product)

s1 = Shop()

s1.add()
s1.add()
s1.add()

s1.display()