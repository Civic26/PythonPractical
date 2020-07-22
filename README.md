# Perform Operations using Data Types and Operators
# Control Flow with Decisions and Loops
# Perform Input and Output Operations
# Document and Structure Code
# Perform Troubleshooting and Error Handling
# Perform Operations Using Modules and Tools
#  """
# Evaluate an expression to identify the data type Python will assign to each variable
x = "10"  # string
y = 10  # Int
z = 1.0  # float
a = True  # Boolean / bool

# =================================================================================================

# Perform data and data type operations
# -> Convert from one data type to another type

varA = "1"
varB = 1
varC = 1.0
varD = False
varE = "True"

# int conversion
# ansA = int(varC)
# print(ansA)
# string conversion
ansB = str(varC)
print(ansB)
print(type(ansB))
# ansB = str(varB)
# print(type(ansB))

ansC = str(varB)  # prac
print(type(ansC))
ansC = str(varB)
print(type(ansC))

# float conversion
ansC = float(varB)
# print(ansC)
# ansC = float(varB)
# print(type(ansC))

ansC = float(varB)  # Prac
print(type(ansC))
# test bool conversion
ansD = bool(varE)
print(type(ansD))

# test convert bool to string and int
ansE = str(varD)
print(ansE)

ansF = int(varD)
print(ansF)

# =================================================================================================


# (Python has 4 types of Arrays --> List, Dictionary, Tuple, Set)

# Construct data structures ----> (List) and (Dictionary)
# Perform Indexing and Slicing

# Lists

# cars = ["Mazda", "Audi", "BMW"]
# cars = ["Mazda", "Audi", "BMW", "Merc", "Kwid", "Toyota", "Hyandai"]
# print(cars)

# cars = ["Mazda", "Audi", "BWM", "Merc", "Kwid", "Toyota", "Hyandai"] #prac
# print(cars)
CARS = ["MAZDA", "AUDI", "BMW", "HONDA", "TOYOTA", "MERC"]
print(CARS)
print(CARS[-5:-3])
# print(cars[-4:-1])
# Access Item in List 6


# print(cars[1])
# print(CARS[1])
# print(CARS[-2])
# print(cars[1])
# print(cars[4])

# print(cars[0])
# Negative indexing 7
# print(cars[-1])
# print(cars[-2])
# print(cars[-5]) #BMW
# print(cars[-1])
# print(cars[-2])
# print(cars[-6])

# print(cars[-7])#hyandai
# print(cars[-6])#Toyota
# print(cars[-5])#Kwid
# print(cars[-1])#Mazda

# -0 == 0
# -1 != 1


# Range of Indexes
# print(CARS[-2:-5])


# print(cars[1:5])
# print(cars[3:6])
# print(cars[:4])
# print(cars[:6])
# print(cars[2:])
# print(cars[3:])

# Range of negative indexes
# print(cars[-4:-1])
# print(CARS[-3:-5])
# print(CARS[-3:-5])
# print(cars[-6:-1])

# loop through List
#
# # for car(can be named Anything) in cars(list):
# #     print(car(list)
# #for car in cars:
#    # print(car)
#
# for test in CARS:
#     print(test)
# #Check if item exists in list
#
# # if "Merc" in cars:
# #     print("Yes, Merc is in cars")
#
# #if "Merc" in cars:
#     #print ("Yes, Merc is in cars")
#
if "MERC" in CARS:
    print("yes, this car is available!")
# =================================================================================================

# Dictionaries

# dictionaryName = {
#     key: value,
#     key: value,
#     key: value
# }

# carsDictionary = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# # print(carsDictionary)
#
# MTAPractice = {
#     "brand": "Honda",
#     "model": "Civic",
#     "year": 2017
# }
# print(MTAPractice)
# print(MTAPractice["brand"])
# print(MTAPractice["model"])
# print(MTAPractice["year"])
# #carsDictionary = {
#    # "brand": "ford",
#    # "Model": "Mustang",
#   #  "year": 1964
# #}
# #print(carsDictionary)
#
# #carsDictionary = {
# #    "brand": "FORD",
# #    "Model": "Mustang",
#  #   "year": 1964
# #}
#
#
#
# #prac
# #Access an item from a dictionary
#
# # print(carsDictionary["Model"]) #Mustang
# #print(carsDictionary["brand"])
# #print(carsDictionary["brand"])#prac
# # print(carsDictionary.get("brand")) #ford
# #print(carsDictionary.get("brand"))
#
# #change value
# #
# # carsDictionary["year"] = 2018
# # print(carsDictionary["year"])
#
# #carsDictionary["year"] = 2020
# #print(carsDictionary["year"])
#
# MTAPractice["year"] = 2020
# print(MTAPractice["year"])
# MTAPractice["model"] = "CRV"
# print(MTAPractice["model"])
# MTAPractice["brand"] = "HondaSUV"
# print(MTAPractice["brand"])
# #loop through Dictionary
# # for car in carsDictionary:
# #     print(car)
# for b in MTAPractice:
#      print(b)
# #printing out keys
# #for car in carsDictionary:
# #    print(car)
#
# #printintg out values
# #for x in carsDictionary:
# #    print(carsDictionary[x])
#
# #for j in carsDictionary.values():
#    ## print(j)
# for a in MTAPractice:
#     print(MTAPractice[a])
# #for y in carsDictionary:
#    # print(y + ":" + str(carsDictionary[y]))
#
# #for y in carsDictionary:
#   #  print(y + ":" + str(carsDictionary[y]))
#
#
# #or x, y in carsDictionary.items():
#  #   print(x, y)
#
# #for x, y in carsDictionary.items():
#     #print(x, y)
#
# # Check if key exists in dictionary
#
# #if "Model" in carsDictionary:
#    # print("Yes, model exists in dictionary!!")
#
# #if "Model" in carsDictionary:
#    # print("yes, model exist in dictionary!!")
#
# # find number of items in dictionary
#
# #print(len(carsDictionary))
# print(len(MTAPractice))
# #print(carsDictionary)
#
# #Add new item to dictionary
#
# #carsDictionary["colour"] = "red"
# MTAPractice["colour"] = "Silver"
# print(MTAPractice)
# MTAPractice["tyres"] = "18 inch"
# print(MTAPractice)
# #print(carsDictionary)
#
# #carsDictionary["colours"] = "red"
#
# #print(carsDictionary)
#
# #remove item
#
# #carsDictionary.pop("colour")
# #print(carsDictionary)
# MTAPractice.pop("tyres")
# print(MTAPractice)
#
# #carsDictionary.pop("colours")
# #print(carsDictionary)

# #Nested dictionary

# carsNestedDictionary = {
#     "car1": {
#         "brand": "FORD",
#         "Model": "Mustang",
#         "year": 1964
#     },
#     "car2": {
#         "brand": " AUDI",
#         "Model": "TT",
#         "year": "2020"
#     }
# }
# nails = {
#     "hands": {
#        "tips1": "gel",
#         "tips2": "Acrylic",
#         "tips3": "powder acrylic"
#     },
#     "toe nails": {
#         "toenails1": "buff and polish",
#         "toenails2": "file nails",
#         "toenails3": "colour polish"
#     },
# }
# print(nails)
#
# carsNestedDictionary = {
#     "cars1": {
#         "brand": "ford",
#         "Model": "bantam",
#         "year": "2007"
#
#     },
#     "cars2": {
#         "brand": "Honda",
#         "Model": "Civic",
#         "Year": "2017"
#     }
# }
# print(carsNestedDictionary)
#
# family = {
#     "child1": {
#         "name": "Yadz",
#         "year": "1996"
#     },
#     "child2": {
#         "name": "Yuvi",
#         "year": "1993"
#     }
# }
#
# family = {
#     "child1": {
#         "name": "Natalie",
#         "year": "1993"
#     },
#     "child2": {
#         "name": "Nerisha",
#         "year": "1988"
#     }
# }
# print(family)
# """
#
# PracticeforMTA = {
#     "test1": {
#         "car1": "Opel Corsa",
#         "Car2": "Merc A Class",
#         "Car3": "Toyota Corolla",
#         "Car4": "Honda Civic"
#     },
#     "test2": {
#         "car1colour": "White",
#         "car2colour": "Gold",
#         "car3colour": "Bronze",
#         "car4colour": "Silver"
#     }
# }
# print(PracticeforMTA)

# #=========================================

# #Converting from a list to a Dictionary

# takeout_prices = [2.50, 2.75, 4.50, 5.00, 5.00]

# takeout_prices = [2.7, 4.87, 5.8, 6.87]

# takeout_prices = {
#     'single_chips': 2.50,
#     'large_chips': 2.75,
#     'single_fish': 4.50,
#     'large_fish': 5.00
# }

# takeout_prices = {
#     'single_chips': 2.50,
#     'large_chips': 2.78,
#     'single_fish': 4.50,
#     'large_fish': 5.00
# }


# #dict.fromkeys()

# fruits = ["Apple", "Pear", "Peach", "Banana"]

# fruit_dictionary = dict.fromkeys(fruits)

# print(fruit_dictionary)


# cars = ["Opel", "Merc", "Toyota", "HONDA"]

# car_dictionary =dict.fromkeys(cars, "in stock!")
# print(car_dictionary)


# # Dictionary Comprehension

# fruits = ["Apple", "Pear", "Peach", "Banana"]

# fruit_dictionary = {fruit: "In Stock!!!!!!!!!" for fruit in fruits}

# print(fruit_dictionary)

# fruits = ["apple", "pear", "peach", "Banana"]

# fruit_dictionary = {fruit: "in stock ????????" for fruit in fruits}

# print(fruit_dictionary)

# ==================BELOW IS NOT MTA RELATED====================

# # Convert Two Lists into a Dictionary

# fruits = ["Apple", "Pear", "Peach", "Banana"]
# prices = [2.50, 2.75, 4.50, 5.00]

# fruit_dictionary = dict(zip(fruits, prices))

# print((fruit_dictionary))

# fruit1 = ["Apple", "Banana", "pear", "cherry"]
# Prices1 = [2.50, 2.75, 4.50, 5.00]

# fruit_dictionary = dict(zip(fruit1, Prices1))

# print(fruit_dictionary)

# ##==================ABOVE IS NOT MTA RELATED====================

# #======================================================================
# #BODMAS
# # Determine the sequence of execution based on operator precedence
#
# #Arithmetic Operaters
# #--------------------
# #practice
# """
# x = 10
# y = 20
# print('x + y =', x+y)
# print(x+y)
# """
#
# #e = 10
# #f = 25
# #print('e + f =', e + f)
# #print(e + f)
# """
# x = 15
# y = 4
# a = 20
# b = 5
#
# # Output: x + y = 19
# print('x + y =', x+y)
# print(a+b) #25
# """
# # Output: x - y = 11
# #print('x - y =',x-y)
# """x = 10
# y = 5
# print('x - y =', x - y)
# print(x - y)
# """
# # Output: x * y = 60
# #print('x * y =',x*y)
# #x = 5
# #y = 10
# #print('x * y =', x * y)
# #print(x * y)
# # Output: x / y = 3.75
# #print('x / y =',x/y)
# #x = 10
# #y = 2
# #print('x / y =', x / y)
# #print(x / y)
#
# # Output: x // y = 3 --> Floor Division
# #print('x // y =',x//y)
# #x = 20
# #y = 6print('x // y =', x // y)
# #print(x // y)
#
# # Output: x ** y = 50625 -->Exponent
# #print('x ** y =',x**y)
# x = 3
# y = 5
# print('x ** y =', x ** y)
# print(x ** y)
# #===================================================================
#
# #Comparison operators
# #=====================
#
# x = 10
# y = 12
#
# # Output: x > y is False
# #print('x > y is',x>y)
# #print('x > y is', x > y)
# #print(x > y)
# # Output: x < y is True
# #print('x < y is',x<y)
# #print('x < y is', x < y)
#
# # Output: x == y is False
# #print('x == y is',x==y)
# #print ('x == y is', x == y)
#
# # Output: x != y is True
# #print('x != y is',x!=y)
# #print('x != y is', x != y)
#
# # Output: x >= y is False
# #print('x >= y is',x>=y)
# #print('x >= y is', x >= y)
# # Output: x <= y is True
# #print('x <= y is',x<=y)
# #print('x <= y is', x <= y)
#
# #=============================================
# #Logical operators are the "and", "or", "not" operators.
#
# # x = False
# # y = False
#
# # i = True
# # l = False
# # o = not False
# # p = True
# # q = True
#
# # print(not o)
# #
# # #print('x and y is',x and y) #false
# # print ('x and y is', x and y)
# #
# # #print('x or y is',x or y) #true
# # #print ('x or y is', x or y)
# #print('not x is',not x) #Will return true if x is false( not will only work with one var. )
# # print('not x is', not x)
# # print()
# # print('not x is', not x)
# # print(not x)
# #print(not p)
#
# #============================================
#
# #Assignment operator********NEED HELP HERE
# # x = 0
# # x = 5 # =
# # print(x)
# #
# #
# # print (x)
# x = 0
# x += 5 # x = x + 5
# print(x)
#
# x = 0
# x -= 5 # x = x - 5
# print(x)
#
# x = 0
# x *= 5 # x = x * 5
# print(x)
#
# x = 10
# x /= 5 # x = x / 5
# print(x)
#
# x = 10
# x %= 5 # x = x % 5 --> Modulas --> gets remainder
# print(x)
#
# x = 14
# x //= 5 # x = x // 5
# print(x)
#
# x = 3
# x **= 5 # x = x ** 5
# print(x)
#
# # 5 more to go
#
# #=========================================
#
# #Identity Operators --> They are used to check if two values (or variables) are located on the same part of the memory.
# # is
# # is not
#
# x1 = 5
# y1 = 5
# x2 = "Hello"
# y2 = "Hello"
# x3 = [1, 2, 3]
# y3 = [1, 2, 3]
#
# #print(x1 is not y1) #False
# #print(x1 is not y1)
# #print(x2 is y2) #True
# #print(x2 is y2)
#
# #print(x3 is y3) #True
# #print(x3 is y3)
# #========================================
#
# #Membership Operators ---> They are used to test whether a value or variable is found in a sequence (list, dictionary, string)
# # in
# # not in
#
# #x = "Hello World"
# #y = {1: "a", 2: "b"}
# x = "Hello World"
# y = {1: "a", 2: "b"}
#
# #print("H" in x) #True
# print("H" in x)
# #print("hello" not in x) #True
# print("hello" not in x)
#
# #print(1 in y) #True
# print(1 in y)
#
# #print("a" in y) #True INCORRECT!!!
# print("a" in y)

# #prac

# size = {
#     "Small": "size 8",
#     "Medium": "size 10",
#     "Large": "Size 12"
# }
#
# print(size)
# print(size["Medium"])

# ==============================================
# List exercise:

# studentMarks = [10, 20, 30, 40, 50]
# studentMarks[2] = 100

# print(studentMarks)
# print(studentMarks[1: 4])

# for x in studentMarks:
#     print(str(x) + "%")

# for car in cars:
#    print(car)
# ==============================================
# Dictionary exercise:
#
# studentMarks1 = {
#     "natalie": 100,
#     "Yadhir": 99,
#     "Maurice": 89,
#     "Kate": 60,
#     "jj": 50
# }

# print(studentMarks1["Yadhir"])
# studentMarks1["jj"] = 1000
# print(studentMarks1)

a = 10
b = 5

num = a + b
print(num)  # 15
#
num = a - b
print(num)  # 5
#
num = a * b
print(num)  # 50
#
num = a / b
print(num)  # 2
#
num = a % b
print(num)  # 0 remainder
#
num = a ** b
print(num)  # to the power of
#
num = a // b
print(num)  # rounding down 2 divide and round down

# Accept 1 number input from the user and store it in a variable
userAge = int(input())
print("the number is " + str(userAge))

# Check if that number is even or odd
if userAge % 2 == 0:
    print("the number is even")
else:
    print("the number is odd")

# Print out the version of Python you are using   [sys]

import sys

print("Python Version")
print(sys.version)
print("version info.")
print(sys.version_info)
