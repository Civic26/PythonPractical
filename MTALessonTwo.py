#0 = false
#1->infinity = true

# var1 = 100
#
# if var1:
#     print("1 - Got a true expression value")
#     print(var1)
# else:
#     print("1 - Got a false expression value")
#     print(var1)

# var1 = 100
# if var1:
#     print("1 is true!")
#     print(var1)
# else:
#     print("1 is false!")
#     print(var1)

# var2 = 0
#
# if var2:
#     print("2 - Got a true expression value ")
#     print(var2)
# else:
#     print("2 - Got a false expression value")
#     print(var2)
#
# print("Good Bye!")

# varA = 100
#
# if varA:
#     print("1 - got a true expression value!")
#     print(varA)
# else:
#     print("1 - Got a false expression value!")
#     print(varA)
# egA = 26
#
# if egA:
#     print("correct")
#     print(egA)

# var2 = 0
# if var2:
#     print("expression is true!!")
#     print(var2)
# else:
#     print("expression is False!!")
#     print(var2)

#======================================================================

# var = 100
# var1 = 199
# if var == 200:
#     print("1 - Got a true expression value")
#     print(var)
# if var1 == 200:
#     print("equal to or the same as 199")
#     print(var1)
# elif var == 150:
#     print("2 - Got a true expression value")
#     print(var)
# elif var1 == 100:
#     print("not the same as 100")
#     print(var1)
# elif var == 100:
#     print("2 - Got a true expression value")
#     print(var)
# elif var1 == 198:
#     print("very close but not the same")
#     print(var1)
#  else:
#     print("4 - Got a false expression value")
#     print(var)
# else:
#     print(var1, "is the number")

#
# print("Good Bye!!")

# if var == 200:
#     print("1 - got a true expression value")
#     print(var)
# elif var == 100:
#     print("2 - got a true expression value")
#     print(var)
# elif var ==100:
#     print("4 - got a false expression value")
#     print(var)
# else:
#     print("4 - Got a false expression value")
#     print(var)
#
# print("Good Bye")

# var2 = 125
# if var2 == 5:
#     print("yes or no")
#     print(var2)
# elif var2 == 124:
#     print("nope")
#     print(var2)
# else:
#     print("the number is " + str(var2))
#==================================================
#Nested If Statement

# num = float(input("Enter a number please:"))
# var1 = float(input("enter a number"))
#
# if var1 >= 0:
#     if var1 == 0:
#         print("zero")
#     else:
#         print("positive number")
# else:
#     print("negative number")

# if num >= 0:
#     if num == 0:
#         print("Zero")
#     else:
#         print("Positive number")
# else:
#     print("Negative number")
#
# numA = float(input("enter a number please:"))
#
# if numA >= 0:
#     if numA == 0:
#         print("zero")
#     else:
#         print("positive number")
# else:
#     print("negative number")

#=============================================
#Compound Condition

number1 = 100
number2 = 1000
number3 = 10000

# if number2 > number1 and number2 < number3:
#     print("Number2 is in the middle")
# if number2 > number1 and number2 < number3:
   # print("number 2 is in the middle")
# if number2 > number1 and number2 <number3:
#     print("Number2 is in the middle")
# if number1 > number3 or number1 < number2:
#     print("one of the conditions is true")
# if number1 > number3 or number1 < number2:
#     print("or condition returned true")
#
# if number1 > number3 or number1 < number2:
#     print("or condition returned true")

#=========================================
#While loop
count = 1

#
# while count < 11:
#     print("first loop the count is " + str(count))
#     count += 1 #count = count + 1

# while count < 11:
#     print("the count is " + str(count))
#     count += 1
# while count < 5:
#     print("the count is currently on number " + str(count))
#     count += 1

#================

#Continue Key-word

i = 0
a = "Natalie"

# while i < len(a):
#     print("Current LETTER : " + a[i])
#     i += 1

# while i < len(a):
#     print("current letter is :" + a[i])
#     i += 1

# while i < len(a):
#     if a[i] == 'i' or a[i] == 't':
#         i += 1
#         continue
#     print("Current letter : " + a[i])
#     i += 1
# while i < len(a):
#     if a[i] == 'i' or a[i] == 't':
#         i += 1
#         continue
#     print("current letter is " +a[i])
#     i += 1
#
# j = 0
# b ="Jesse"
#
# while j < len(b):
#     if b[j] == 'k' or b[j] =='s':
#         j += 1
#         continue
#     print("test 101  : " + b[j])
#     j += 1
#
# i = 0
# a = "jesse"
#
# while i < len(a):
#     if a[i] == 'i' or a[i] == 'e':
#         i += 1
#         continue
#     print("letters are " + a[i])
#     i += 1

#=================================

# q = 0
# p = "Yadhir"
#
# while q < len(p):
#     if p[q] == 'a' or p[q] == 's':
#         q += 1
#         break
#     print("Current Letter : " + p[q])
#     q += 1
#
# print("I am outside loop!!")
#
# i = 0
# a = "Natalie"
# while i < len(a):
#     if a[i] == 'i' or a[i] == 't':
#         i += 1
#         break
#     print("letters are " + a[i])
#     i += 1
#
# print("im outside the loop")
# w = 0
# o = "tim"
#
# while w < len(o):
#     if o[w] == "k" or o[w] == "m":
#         w += 1
#         break
#     print("letters :" + o[w])
#     w += 1
#
# print("I know what you did last summer")
#
# #===============================================
#
# #Pass
#
# a = "YadzYadz"
# i = 0
#
# # while i < len(a):
# #     i += 1
# #     pass
# # print("Value of i : " + str(i))
# while i < len(a):
#     i += 1
#     pass
# print("whatever has been requested of you")
#
a = 33
b = 200
# if b > a:
#     pass


#===============================
#nested loops

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
#
# for x in adj:
#     for y in fruits:
#         print(x, y)

# adj = ["red", "big", "tasty"]
# fruit = ["apple", "banana", "cherry"]
#
# for x in adj:
#     for y in fruit:
#         print(x,y)


# adj = ["blue", "yellow", "red"]
# animals = ["Elephant", "Goat", "Horse"]
#
# for nat in adj:
#     for jes in animals:
#         print(nat, jes)

#
# type = ["greedy", "naughty", "cute"]
# dogs = ["Storm", "Chole", "Jackie"]
# for x in type:
#     for y in dogs:
#         print(x,y)

#while count < 5:
#    while innerCount < len(alphabet):
#        print(str(count) + alphabet[innerCount])
#        innerCount += 1
#    count += 1

# alphabet = ["a", "b", "c", "d"]
# count = 1
# innerCount = 0
#
# # alphabet = ["a", "b", "c", "d"]
# # count = 1
# # innerCount = 1
# while count < 5:
#     while innerCount < len(alphabet):
#         print(str(count) + alphabet[innerCount])
#         innerCount += 1
#     count += 1
#     innerCount = 1

# while count < 5:
#     while innerCount < len(alphabet):
#         print(str(count) + alphabet[innerCount])
#         innerCount += 1
#     count += 1
#     innerCount = 1

# print("Something here")

# letters = ["n", "a", "t", "a", "l", "i", "e"]
# count = 1
# innerCount = 0
#
# while count < 7:
#     while innerCount < len(letters):
#         print(str(count) + letters[innerCount])
#         innerCount += 1
#     count +=1
#     innerCount =1