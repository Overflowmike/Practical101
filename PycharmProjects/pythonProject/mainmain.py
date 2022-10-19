# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# # if __name__ == '__main__':
# #     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
#
# #integer
#
# number1 = 12345
# number2 = -12345
# long_number = 112223444546738339393939330003003003
#
# # print(type(number1))      # <....... int>
# # print(type(number2))      # <....... int>
# # print(type(long_number))  # <....... int>
# #
# # name = 10          # int
# # print(type(name))  # <... int>
# #
# # name = 'testify'   # str
# # print(type(name))  # <... str>
# #
# # name = False       # bool
# # print(type(name))  # <... bool>
#
# #Task 1
# pythonTask = 'hello world'
# # print(pythonTask)
#
# #name = 'Michael Alabi'
# #print(name)
#
#
# #Task 2
# #
# # variable_name = 'my_var'    # str
# # print(type(variable_name))  # <... str>
# #
# # variable_name = 12.6        # int
# # print(type(variable_name))  # <... int>
# #
# # int_variable = 200          # int
# # print(type(int_variable))   # <... int>
# #
# #
# # name = 'Michael Alabi'      # int
# # print(name)                 # <... int>
#
# name = "Testify"
# lesson = 'Python, String and Concatenation'
#
# # escape sequence
#
# article = "This is an article\na multiline article\n\tEach text.\b"
# print(article)
#
# # concatenation
# # group = "wood"
# # attr = "peckers"
# # bird = group + attr
# #
# # print(bird)
# # print("Python " + "Programming" + " Language")



# Task 3 Module 3B
#
# gender = "Mr"
# name = " Michael"
# biodata = gender + name
#
# print(biodata)


# print("Arithmetic Operators\n")
#
# result = 6 + 4 # addition
# print(result)
#
# result = 6 - 4 # subtraction
# print(result)
#
# result = 6 * 4 # Multiplication
# print(result)
#
# result = 6 /2 # division
# print(result)
#
# result = 6 % 4 # modulus
# print(result)
#
# print("Compound Arithmetic Operators\n")
#
# result = 6
# result += 4
# print(result)
#
# result = 6
# result -= 4
# print(result)
#
# result = 6
# result *= 4
# print(result)

# result = 6
# result /= 2
# print(result)
#
# result = 6
# result %= 4
# print(result)
#
# print("Increment and Decrement")
#
# result = 6
# result += 1
# print(result)
#
# result = 6
# result -= 1
# print(result
#
#
print("Conditional Statement\n")

number = 5

# if statement
if 5 == 5:
    print("5 is equal to 5")

# if-else statement
if number == 1:
   print("5 is equal to 1")

else:
    print("5 is not equal to 1")

# elif statement
if number == 1:
    print("5 == 1")
elif number == 3:
    print("5 == 3")
elif number == 5:
    print("number is 5")
elif number == 6:
    print("number is 6")

print("Relational Operators\n")

# greater than >
if number > 4:
    print("Number is greater than 4")

# lesser than <
if number < 6:
    print("Number is lesser than 6")

# equals to ==
if number == 5:
    print("Number is equal to 5")

# no equals to !=
if number != 4:
    print("Number is equal to 5")

# greater than or equals to >=
if number >= 3:
    print("Number is greater than or equals to 3")

# less than or equals to <=
if number <= 10:
    print("Number is less than or equals to 10")



# Logical Operators

number1 = 10
number2 = 20

print("\nLogical AND\n")

if number1 == 10 and number2 == 20:
    print("AND: Number1 = 10, Number2 = 20")

if number1 == 5 and number2 == 20:
    print("AND: Number1 = 5, Number2 = 20")

print("\nLogical or \n")

if number1 == 10 or number2 == 20:
    print("OR: Number1 = 10, Number2 = 20")

if number1 == 5 or number2 == 20:
    print("AND: Number1 = 5, Number2 = 20")

print("\nLogical not\n")

if not number1 == 10:
    print("NOY: Number1 = 10")

if not number1 == 5:
    print("NOY: Number1 = 5")


# for loop
print("for loop\n")

fruits = ["Apple", "Banana", "Coconut"]

for fruit in fruits:
    print("Fruit: ", fruit)

name = "Python"
for ch in name:
    print("Character:", ch)

# iterate number
number = 5
for i in range(number):
    print("Number: ", i)

# while loop
print("\nwhile loop\n")

number = 10
while number > 0:
    print("Number is", number)
    number -= 1



print("Break\n")

number = 5
for i in range(number):
    if i == 3:
        break
    print("for: Number:", i)

while number > 0:
    if number == 3:
        break
    print("While: Number:", number)
    number -= 1

print("\ncontinue\n")

number = 5
for i in range(number):
    if i == 3:
        continue
    print("for: Number:", i)

while number > 0:
    if number == 3:
        number -= 1
        continue
    print("While: Number:", number)
    number -= 1

print("\nelse\n")

number = 5
for i in range(number):
    print("for: Number:", i)
else:
    print("for: end of loop")

while number > 0:
    print("while: Number:", number)
    number -= 1
else:
    print("while: end of loop")


print("\nelse, for and while\n")

number = 5
for i in range(number):
    if i == 3:
        continue
    print("for: Number:", i)
else:
    print("for: end of loop")


print("\nelse, continue and break\n")

number = 5
for i in range(number):
    if i == 3:
        continue
    print("for: Number:", i)
else:
    print("for: end of loop")

while number > 0:
    if number == 3:
        number -= 1
        continue
    print("while: Number:", number)
    number -= 1
else:
    print("While: end of loop")

print("\nelse and break\n")

number = 5
for i in range(number):
    if i == 3:
        break
    print("for: Number:", i)
else:
    print("for: end of loop")

while number > 0:
    if number == 3:
        break
    print("while: Number:", number)
    number -= 1
else:
    print("while: end of loop")




print("function\n")

def greet():
    print("Hello World from Python")

def goodbye():
    print("Thank you")
    print("Good bye")

greet()
goodbye()



print("Annoymous function")

def greet():
    print("Hello World")

def accept(cb):
    cb("Hello")

hello = lambda : print("Hello World Annoymously")

hello()
accept(lambda x: print(x))





print("\nrequired parameter")

def greet(name):
    print("Hello", name)

greet("Michael")

print("\ndefault parameter")

def add(num1 = 10, num2 = 15):
    result = num1 + num2

    print("Result", result)

add()
add(5)
add(5, 5)

print("\nkeyword parameter")

def minus(num1, num2):
    result = num1 - num2
    print("Result", result)

minus(num1=10, num2=5)
minus(num2=5, num1=10)

print("\narbitrary/variadic keyword parameter")

def print_kvalue(**kargs):
    print("Args:", kargs, kargs['num1'], kargs['num2'])

print_kvalue(num1=1, num2= 2)



# print("\nReturn statement")
#
# def add_and_return(num1, num2):
#     result = num1 + num2
#     return result
#
# res = add_and_return(50, 50)
# print("50 + 50:", res)
#
# def check_number(number):
#     if number > 5:
#         return
#     print("Number:", number)
#
# check_number(1)
# check_number(3)
# check_number(5)
# check_number(6)
# check_number(10)




name = 'Testify' # Global Variable

def greet():
    language = "Python" # Local variable
    print("Name", name, "Language", language)
    print(language)

def hello():
    framework = "Selenium"  # local variable
    print("Name", name, "framework", framework)
    print(framework)

plaform = "web"

def print_platform():
    plaform = "Mobile"
    print("Platform", plaform)

print(name)
greet()
hello()
print_platform()



# Recursion

def reduce_number_loop(num):
    while num >= 0:
        print (num)
        num -= 1

def reduce_number_recursion(num):
    print(num)
    if num == 0:
        return
    reduce_number_recursion(num -1)

reduce_number_loop(5)
print()
reduce_number_recursion(5)



import string



#
# def print_hello():
#     print("Hello World")
#     print_hello()
#
#
# print_hello()



str = "  Phew  kung paw  "

print(str)
print(str.strip())
print(str.lstrip())
print(str.rstrip())
print(str.translate({ord(c): None for c in string.whitespace}))



name = "testify for testing and automation school, with testify"
#
# # len -> get the size of string
# size = len(name)
# print("Size: ", size)
#
# # upper -> convert a string to upper case
# upper_value = name.upper()
# print("Upper:", upper_value)
#
# # lower -> convert a string to lower case
# lower_value = name.lower()
# print("Lower:", lower_value)
#
# # capitalized -> convert the first character to upper case
# capitalized_value = name.capitalize()
# print("Capitalized:", capitalized_value)
#
# # count => count the occurrence of a value in a string
# testify_count = name.count("testify")
# print("testify count:", testify_count)
#
# t_count = name.count("t")
# print("t count:", t_count)
#
# # find -> get the position of a value in the string
# for_position = name.find("for")
# print("for position:", for_position)


# split -> it split a string to array using the specified value
split_name = name.split("and")
print("Splitted (and):", split_name)

splitted_name_space = name.split(" ")
print("Splitted (space):", splitted_name_space)



languages = ["python", "java", "C#"]
print("List:", languages)

# append -> add new item at end of list
languages.append("javascript")
print("append:", languages)

# insert -> add new item at any position in the list
languages.insert(0, "c")
languages.insert(2, "php")
print("insert:", languages)

# pop -> remove an item from the specified position
languages.pop(0)
print("pop-0:", languages)
languages.pop()
print("pop:", languages)

# remove -> remove an item by value
languages.remove("php")
print("remove:", languages)

# count -> return the number of occurrence of item in a list
languages.append("java")
count_java = languages.count("java")
print("list:",languages)
print("count:", count_java)

# len -> count the number of items in a list
length = len(languages)
print("len:", length)




food = {
    "grains": "Rice",
    "solid": "Yam",
    "liquid": "Custard",
    "noodles": "Indomie"
}

print("dictionary:", food)

# get -> fetch a value using specified key
grains = food.get("grains")
print("get-1:", grains)
solid = food.get("solid")
print("get-2:", solid)

# keys -> return the keys as a list
food_keys = food.keys()
print("keys:", food_keys)

# values -> return the keys as a list
food_values = food.values()
print("values:", food_values)

# pop -> remove a key-value pair using the specified key
food.pop("solid")
print("pop:", food)

# update -> add more key-value pairs into a dictionary
food.update({"protein": "beans"})
food.update({"flour": "bread", "poultry": "turkey"})
print("update:", food)



# class
class Human:
    name = "Michael"
    group = "Test Automation"
    level = "Level 3"

    def get_name_group_level(self):
        return self.name + ":" + self.group + ":" + self.level

# objects
Michael = Human()
print(Michael.name, Michael.group, Michael.level, Michael.get_name_group_level())



class Animal:

    group = "Mammal"
    can_automate = True

    def __init__(self, name):
        self.name = name

cat = Animal("Cat")
dog = Animal("Dog")

print(cat.name)
print(dog.name)

print(cat.group)
print(dog.group)

class Human:

    group = "Male"
    leg_count = 4
    can_walk = True

    def __init__(self, name):
        self.name = name

Michael = Human("Michael")
get_description = Michael("This is Human")
print("\nMichael:", Michael.name,  )



print(Michael.name)

print(Michael.group)

print(Michael.leg_count)
print(Michael.can_walk)


# # import main
#
#
# class Animal:
#
#     group = "Mammal"
#     leg_count = 4
#
#     def __int__(self):
#         self.name = "Unknown"
#
# class Vehicle:
#     can_fly = False
#     tire_count = 4
#
#     # parameterized constructor
#     def __int__(self, make):
#         self.make = make
#
# animal = Animal()
# #print("Animal:", self.name, animal.group)
#
# toyota = Vehicle("Toyota")
# print("\nVehicle:", toyota.make, toyota.can_fly)
#
# lexus = Vehicle("Lexus")
# print("\nVehicle:", lexus.make, lexus.can_fly)


# class Animal:
#     group = "Mammal"
#     leg_count = 4
#     name = "emma"
#
# # default constructor
#
#     def _init_(self, name):
#         self.name = "Unknown"
#         name = self.name
#
#
# class Vehicle:
#     can_fly = False
#     tire_count = 4
#     make = "Toyota"
#
#      # parameterized constructor
#     def __int__(self, make):
#         self.make = make
#
# animal = Animal()
# print("Animal:", animal.name, animal.group)
#
# toyota = Vehicle()
# print("\nVehicle:", toyota.make, toyota.can_fly)


class Human:
    group = "Mammal"
    leg_count = 4
    name = "Mike"
    can_walk = True
    get_description = "This is human"

    def _init_(self, get_description):
        self.get_description = "This is human"

    def set_leg_count(self, count):
         self.leg_count = count


male = Human()
print("Human:", male.get_description)


human = Human()
human.set_leg_count(4)
print("\nHuman:", human.name, human.leg_count)


# Lesson 20

#
# class Vehicle:
#     model = "Corolla"
#     make = "Toyota"
#     production_year = "1990"
#
#     def print_vehicle_info(self):
#         print("\nVehicle{", self.model, ",", self.make + "}")
#
# class Car(Vehicle):
#
#     def __int__(self, make, model):
#         self.model = model
#         self.make = make
#
# class Plane(Vehicle):
#     model = "Aeroplane"
#     make = "Boeing"
#
# vehicle1 = Vehicle()
# vehicle1.print_vehicle_info()
#
# car1 = Car()
# car1.print_vehicle_info()
#
# plane1 = Plane()
# plane1.print_vehicle_info()


class Human:
    group = "Mammal"
    leg_count = 4
    can_walk = True
    get_gender = "Male"
    gender = "Male"
    count = 4
    fe_gender = "Female"
    fe_count = 3


def print_human_info(self):
    print("\nHuman{", self.get_gender, ",", self.leg_count, self.fe_gender, self.fe_count + "}")


class Man(Human):

    def __int__(self, get_gender, leg_count, count="4", gender="Male", fe_gender="Female", fe_count=3):
        self.get_gender = gender
        self.leg_count = count

    def print_human_info(self):
        pass


class Woman(Human):

    def print_human_info(self):
        pass

    fe_gender = "Female"
    fe_count = 3

human = Human()
print("\nHuman:", human.get_gender, human.leg_count)


human = Human()
print("\nHuman:", human.fe_gender, human.fe_count)

man = Man()
man.print_human_info()

woman = Woman()
woman.print_human_info()



# Lesson 21


class Vehicle:
    def drive_direction(self):
        print("Vehicle: Drive Forward")

class Plane(Vehicle):

    def drive_direction(self):
        print("Plane: Drive Upward")

class SubMarine(Vehicle):
    def drive_direction(self):
        print("SubMarine: Drive Downward")

vehicle = Vehicle()
vehicle.drive_direction()

plane = Plane()
plane.drive_direction()

SubMarine = SubMarine()
SubMarine.drive_direction()


# Task

class Human:
    group = "Mammal"
    leg_count = 4
    can_walk = True
    get_gender = "Unknown"
    gender = "man"
    count = 4
    fe_gender = "woman"
    fe_count = 3


def print_human_info(self):
    print("\nHuman{", self.get_gender, ",", self.leg_count, self.fe_gender, self.fe_count + "}")


class Man(Human):

    def __int__(self, get_gender, leg_count, count="4", gender="Man", fe_gender="Female", fe_count=3):
        self.get_gender = gender
        self.leg_count = count

    def print_human_info(self):
        pass


class Woman(Human):

    def print_human_info(self):
        pass

    get_gender = "Female"
    fe_count = 3

human = Human()

man = Human()
print("\nMan:", human.gender)

woman = Human()
print("\nWoman:", human.fe_gender)

man = Man()
man.print_human_info()

woman = Woman()
woman.print_human_info()



# Lesson 22
# class User:
#
#     _first_name = "Testify"
#     _last_name = "QA"
#     _attendance = 1
#     def get_name(self):
#         return "User-" + self._first_name
#
#     def get_attendance(self):
#         value = self._attendance * 20
#         return value
#
# user = User()
# print(user.get_name())
# print(user.get_attendance())
#
# user = User()
# print(user._first_name)
#
# user = User()
# print(user._last_name)

#Task
class Hunt:
    _weapon = "Assault Rifle"
    _assaultRifle = "Not Available"

    def get_weapon(self):
        return  self._assaultRifle

    def __int__(self):
        self._weapon

hunt = Hunt()
print(hunt.get_weapon())

# Lesson 23
# class LoginSession:
#
#     _email = "user@test.com"
#     _password = "password"
#
#     def get_email(self):
#         return self._email
#
#     def get_password(self):
#         return "********"
#
# session = LoginSession()
# print(session.get_email())
# print(session.get_password())

# Task
class User:

    _password = "password"

    def get_password(self):
        return self._password

class ActiveUser(User):

    def get_password(self):
        return "********"

active =ActiveUser()
print(active.get_password())


# Lesson 24

import abc


class IWebElement(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_name(self):
        pass

    @abc.abstractmethod
    def set_style(self, style):
        pass


class DivElement(IWebElement):

    def get_name(self):
        return "div"

    def set_style(self, style):
        print("Div Style:", style)


class SpanElement(IWebElement):

    def get_name(self):
        return "span"

    def set_style(self, style):
        print("Span Style:", style)

class ButtonElement(IWebElement):

        def get_name(self):
            return "button"

        def set_style(self, style):
            print("Button Style:", style)

#
# div_element = DivElement()
# print(div_element.get_name())
# div_element.set_style("width: 100px; height: 100px")
#
# span_element = SpanElement()
# print(span_element.get_name())
# span_element.set_style("hour: 10; minutes: 50")
#
# button_element = ButtonElement()
# print(button_element.get_name())
# button_element.set_style("clickable: True; toggle: false")

# Task
class Vehicle:

    @abc.abstractmethod
    def drive_direction(self):
        pass

class Car(Vehicle):

    def drive_direction(self):
        return "Drive forward"

class Plane(Vehicle):

    def drive_direction(self):
        return "Drive Upward"

vehicle_direction= Vehicle()
print(vehicle_direction.drive_direction())

car_direction= Car()
print(car_direction.drive_direction())

plane_direction= Plane()
print(plane_direction.drive_direction())

