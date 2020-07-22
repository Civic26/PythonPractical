# #Math
#
# #Built-in Math Functions
#
# #min()
#
# x = min(2, 10, 25)
#
# print(x)
#
# y = min(4, 15, 22, 66, 2)
# print(y)
#
# #max()
#
# a = max(10, 2, 55, 102, 100000, 25)
# print(a)
#
# #abs() -> returns the absolute (positive) value of the specified number
#
# b = abs(-7.25)
#
# print(b)
#
# t = abs(-1254.587)
# print(t)
#
# #pow(x, y) -> returns the value of x to the power of y (x**y)
#
# c = pow(4, 3)
# print(c)
#
# g = pow(1, 2)
# print(g)
#
# #=============================================================
#
# #Math Module
#
# import math
#
# #square root
#
# x = math.sqrt(64)
#
#
# print(x)
#
# # x = math.sqrt(25)
# #
# # print(x)
#
# #ceiling -> rounds a number upwards to its nearest integer
# #
# import math
#
# x = math.ceil(1.4)
# print(x)
# #
# # x = math.ceil(2.1)
# # print(x)
# #
# # #floor -> rounds a number downwards to its nearest integer
# #
# y = math.floor(1.8)
# print(y)
# #
# # y = math.floor(2.9)
# # print(y)
#
#
#
# import math
#
# x = math.pi
#
# print(x)
#
# #=============================================================
#
# #Datetime
#
# # import datetime
# #
# # x = datetime.datetime.now()
# # print(x)
#
# # import datetime
# #
# # x = datetime.datetime.now()
# # twoHoursLater = datetime.datetime.now() + datetime.timedelta(hours = 2)
# #
# # print(twoHoursLater)
# #
# # print(x)
#
# #Date Output
#
# # import  datetime
# #
# # x = datetime.datetime.now()
# #
# # print(x.year)
# # print(x.strftime("%A"))
# # print(x.strftime("%A"))
#
# #Creating a Date
# # import datetime
# #
# # x = datetime.datetime(2020, 5, 17)
# # print(x)
#
# # import datetime
# #
# # x = datetime.datetime(2020, 11, 1)
# # print(x)
#
# #strftime() Method
#
# # import  datetime
# #
# # x = datetime.datetime(2018, 6, 1)
# #
# # print(x.strftime("%B"))
#
# # import datetime
# #
# # x = datetime.datetime(1993, 12, 5)
# #
# # print(x.strftime("%B"))
#
#
# #======================================
#
# #IO Module
#
# #In- Memory Streams
#
# # import io
# # #Writing to a buffer
# #
# # output = io.StringIO()
# # output.write("This goes into the buffer. ")
# # print("And so does this ", file=output)
# #
# # #Retrive the value written
# # print(output.getvalue())
# #
# # output.close() #discard buffer memory
# #
# #
# # #Initialize a read buffer
# # input = io.StringIO("Initial value for read buffer")
# #
# # #Read from the buffer
# # print(input.read())
#
# #======================================================
#
# #Sys module
#
# # import sys
# # print("We are cureently her: {}".format(sys.argv[0]))
#
# # import sys
# # print("we are currently here: {}".format(sys.argv[0]))
# #
# # num = 2147483647
#
# #OS Module
# #
# # import os
# # os.mkdir("tempFolder")
# # import os
# # os.mkdir("MTAFOLDER")
#
# # import os
# #
# # print(os.path)
#
#
# #======================
# #Randome Module
#
#
# # import random
# #
# # print(random.random()) #Generates a random float number between 0.0 to 1.0
# #
# # print(random.randint(1, 100))
# #
# # print(random.choice([12, 35, 67, 89, 95, 86]))
#
#
# import random
#
# # print(random.random())
# #
# # print(random.randint(1, 100))
# #
# # print(random.choice([12, 14, 155, 458, 65]))
#
# print(random.choice([1, 2, 3, 4, 5, 6]))
#
# print(random.choice([1, 2, 3, 4, 5, 6]))
#
#
#
#
#
