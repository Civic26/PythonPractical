#single line comment
""" multi line comment
test haha
tester
"""

"""
DATE:
PROJECT:
AUTHOR:

"""

    # 1# spaces x 4
    # 1
 #white spaces
a = ("      Natalie")
print(a.strip())

# a = 9
# b = 10
# c = 11



#
# if a < b:
#     print("a is > than b")
#
# if a < b:
# print("A is > than b")
#
# if a < b:
#         print("A is > than b")
#
#     if a < b:
#         print("A is > than b")


print("test")#

#=====================================

# Functions

#Creating a Function
#In Python a function is defined using the def keyword:

#def yadz_function():
 #   print("Natalie says hello")
def yadz_function():
    print("Natalie says Hello")
def can_be_anything():
    print("what would you like to print?")

#Calling a Function
#To call a function, use the function name followed by parenthesis:

yadz_function()
can_be_anything()

#Arguments

#Information can be passed into functions as arguments.
#Arguments are specified after the function name, inside the parentheses.
#You can add as many arguments as you want, just separate them with a comma.
#
# def my_function(fName):
#     print("Your first Name is: " + fName)
#
# my_function("Yadz")
#
# def my_name(bname):
#     print("hello world")
# my_name("jesse")
#
# def test(Lname):
#     print("your last name is:" + Lname)
#
# test("Moodley")
# test("Thomas")
# test("greenwood")
#
#
#
#
# # def add(num1, num2):
# #     print(num1 + num2)
# #
# # add(5, 10)
# def add (num1, num2):
#     print(num1 + num2)
# add(5, 10)
#
# def sub(num3, num4):
#     print(num3 - num4)
# sub(50, 30)
#
#
# #Number of Arguments
# #By default, a function must be called with the correct number of arguments.
# # Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments,
# # not more, and not less.
#
# # def printFnameLname(fName, lName): #Method Signiture
# #     print(fName + " " + lName)
# #
# # printFnameLname("Yadhir", "Maharaj")
# #
# # def dognames(dog1, dog2, dog3):
# #     print(dog1 + " " + dog2 + " " + dog3)
# #
# # dognames("chole", "Noodles", "Storm")
#
# def carnames(car1, car2, car3):
#     print(car1 + " " + car2 + " " + car3)
#
# carnames("Cerubino", "Abigail", "Beth")
#
#
# #Arbitrary Arguments, *args
# #If you do not know how many arguments that will be passed into your function,
# # add a * before the parameter name in the function definition.
# #This way the function will receive a array of arguments, and can access the items accordingly:
#
# def printColours(*colours):
#     print("The first colour is: " + colours[0])
#
# printColours("Yellow", "red", "blue")
#
# def printcars(*cars):
#     print("the first car is:" + cars[3])
#
# printcars("honda", "MAZDA", "toyota","merc")


#Default Parameter Value

#def printCountry (country = "Norway"):
#    print("I am from " + country)

#printCountry("Sweden")
#printCountry("SA")
#printCountry()
#printCountry("India")

def printCountry(country = "not specified"):
    print("I am from " + country)

printCountry("SA")
printCountry("India")
printCountry()
printCountry()

#Return Values
#To let a function return a value, use the return statement:

# def doubled(num):
#     return 2 * num
#
# print(doubled(3))
# print(doubled(5))
# print(doubled(9))

def doubled(num):
    return 2 * num
print(doubled(3))
print(doubled(5))
print(doubled(10))

# def triple(number):
#     return 3 * number
#
# print(triple(2))
# print(triple(3))
# print(triple(5))

def triple(number):
    return 3 * number

print(triple(2))
print(triple(10))
print(triple(20))

#The pass Statement
#function cannot be empty, but if you for some reason have a function with no content,
#put in the pass statement to avoid getting an error.

def send_Email():
    pass

print("normal code below pass")