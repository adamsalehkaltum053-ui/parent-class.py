
# 1
class Animal :
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Animal Name: {self.name}")
class Dog(Animal):
    pass
d1 = Dog("Rex")
d1.display_name()


#2
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"Hi,I'm {self.name} and I am {self.age} years old.")

class Student(Person):
    pass
s1 = Student("Alice",20)
s1.introduce()


#3
class vehicle:
    def start(self):
        print("vehicle is starting.")

class Car(vehicle):
    def start(self):
        print("Car engine is started.")

My_Car = Car()
My_Car.start()



#4
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_info(self):
        print(f"Manager name: {self.name}, Salary {self.salary:,}  Dept: {self.department}")


m1 = Manager("Sarah", 85000, "Engineering")
m1.display_info()



#5
class Shape:

    def __init__(self, color):
        self.color = color


class Circle(Shape):

    def describe(self):
        print(f"I am a {self.color} Circle.")


class Rectangle(Shape):

    def describe(self):
        print(f"I am a {self.color} Rectangle.")


class Triangle(Shape):

    def describe(self):
        print(f"I am a {self.color} Triangle.")



shapes = [Circle("Red"), Rectangle("Blue"), Triangle("Green")]

for shape in shapes:
    shape.describe()



#6
class Animal:

    def speak(self):
        pass


class Dog(Animal):

    def speak(self):
        print("Woof!")


class Cat(Animal):

    def speak(self):
        print("Meow!")


class Bird(Animal):

    def speak(self):
        print("Chirp!")



animals = [Dog(), Cat(), Bird()]

for animal in animals:
    animal.speak()



#7
class Student:

    student_count = 0  

    def __init__(self, name):
        self.name = name
        Student.student_count += 1  

    @classmethod
    def print_total_students(cls):
        print(f"Total students registered: {cls.student_count}")



s1 = Student("Alex")
s2 = Student("Ben")
s3 = Student("Clara")
s4 = Student("David")
s5 = Student("Emma")

Student.print_total_students()






#8
class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid amount.")


class SavingsAccount(BankAccount):

    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added ({interest:.2f}). Updated balance: {self.balance:.2f}")



acc = SavingsAccount("John", 1000, 0.05)
acc.deposit(500)
acc.withdraw(200)
acc.add_interest()




#9
class Engine:

    def __init__(self, engine_type):
        self.engine_type = engine_type


class Car:

    def __init__(self, model, engine):
        self.model = model
        self.engine = engine  

    def display_info(self):
        print(f"Car Model: {self.model} | Engine Type: {self.engine.engine_type}")


v8_engine = Engine("V8 Turbo")
my_car = Car("Ford Mustang", v8_engine)
my_car.display_info()




