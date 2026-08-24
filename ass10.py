# 1. Create a base class Animal and subclasses Dog and Cat.

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def n(self):
        print("Dog name is", self.name)

class Cat(Animal):
    def n(self):
        print("Cat name is", self.name)

d1 = Dog("Charlie")
d1.n()

c1= Cat("Roxy")
c1.n()

# 2. Create a class hierarchy for Vehicle → Car → ElectricCar.

class Vehical:
    def __init__(self, name ,type):
        self.name = name
        self.type = type  

class Car(Vehical):
    def n(self):
        print("Car name is", self.name)
        
class ElectricCar(Car):
    def e(self):
        print("Car type is", self.type)

c1 = Car("BE6","Electric-Car")
c1.n()
e1 = ElectricCar("Electic-Car","EV")
e1.e()

# 3. Implement method overriding in a base and derived class.
# Same method name in parent + child class = Method Overriding

class Animal:
    def __init__(self,name):
        self.name=name
    
    def main(self):
        print("Animal name is", self.name)
        
class Dog(Animal):
    def n(self):
        print("Dog name is", self.name)

a1 = Animal("Dog")
a1.main()

d1 = Dog("Charlie")
d1.n()

# 4. Demonstrate multiple inheritance with two parent classes.

class A:
    def Pi(self):
        print("Pi value is 3.14 or 22/7")

class B:     
    def Circle(self,r):
        print("Area of Circle using 3.14 is", 3.14 * r * r)
  
class C(A,B):      
    def Main(self,r):
        print("Area of Circle using 22/7 is", 22/7 * r * r)
    
c1 = C()
c1.Pi()
c1.Circle(5) 
c1.Main(5)

# 5. Create a polymorphic function that works with different shapes.

class Shape:
    def area(self):
        print("Area of Shape:")
        
class Circle(Shape):
    def area(self):
        r = int(input("Please enter the radius of Circle:"))
        print("Area of Circle is",3.14 * r * r)


class Rectangle(Shape):
    def area(self):
        l = int(input("Please enter the Length of Rectangle:"))
        w = int(input("Please enter the Width of Rectangle:"))
        print("Area of Rectangle is",l * w)


class Triangle(Shape):
    def area(self):
        b = int(input("Please enter the Base of Triangle:"))
        h = int(input("Please enter the Height of Triangle:"))
        print("Area of Triangle is",0.5 * b * h)

s1 = Shape()
s1.area()

c1 = Circle()
c1.area()

r1 = Rectangle()
r1.area()

t1 = Triangle()
t1.area()     
        
# 6. Create a Bank system with SavingsAccount and CurrentAccount classes.

class Bank:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    
    def detail(self):
        print("Account user name is",self.name)
        print("Account balance is",self.balance)

class Saving(Bank):
    def s(self):
        print("Account type : Saving")

class Current(Bank):
    def c(self):
        print("Account type : Saving")

s1 = Saving("Vasu","100000")
s1.detail()
s1.s()

c1 = Current("Rahul","50000")
c1.detail()
c1.c()

# 7. Create a class with private attributes and getter/setter methods.
# Getter → used to get/read a value.
# Setter → used to change/update a value.

class Bank:
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance
    
    def detail(self):
        print("Account user name is",self.name)
        print("Account balance is",self.__balance)

    def g(self):
        return self.__balance

    def s(self,balance):
        self.__balance = balance

b1 = Bank("Vasu",100000)
b1.detail()

print("After Changes Your bank detail are shown below:")
b1.s(50000)
b1.detail()

# 8. Create Teacher and Student class to show inheritance.

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def detail(self):
        print("Name:",self.name)
        print("Age:",self.age)
        
class Teacher(Person):
    def __init__(self,name,age,subject,salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary
    
    def det(self):
        print("Subject:",self.subject)
        print("Salary:",self.salary)

class Student(Person):
    def __init__(self,name,age,roll_no,course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course
    
    def det(self):
        print("Roll no:",self.roll_no)
        print("Course:",self.course)

t1 = Teacher("Bhavisha",29,"Java",20000)
t1.detail()
print("Type : Teacher")
t1.det()

print()

t1 = Student("Parth",19,43,"B.tech")
t1.detail()
print("Type : Student")
t1.det()

# 9. Create a MusicPlayer class and subclass Spotify to override play method.

class MusicPlayer:
    def play(self):
        print("Playing music")

class Spotify(MusicPlayer):
    def play(self):
        print("Playing music on Spotify app")

m1 = MusicPlayer()
m1.play()

s1 = Spotify()
s1.play()

# 10. Demonstrate the use of super() in inheritance.

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def detail(self):
        print("Name:",self.name)
        print("Age:",self.age)
        
class Teacher(Person):
    def __init__(self,name,age,subject,salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary
    
    def det(self):
        print("Subject:",self.subject)
        print("Salary:",self.salary)

t1 = Teacher("Kartik",31,"Science",25000)
t1.detail()
print("Type : Teacher")
t1.det()
