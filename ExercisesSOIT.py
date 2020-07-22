# Arrays:
#
# Create an array called "cars" with 5 elements in it (the elements can be names of any cars)
Cars = ["Opel", "Merc","Toyota", "Honda", "Ford"]
# Print out the 4th element in the array
print(Cars[3])
# Remove the 3rd element of the array and then print out the whole array
Cars.pop(2)
print(Cars)

# For-loops:
#
# Create an array called "fruits" with 3 elements in it (the elements can be names of any fruit)
fruits = ["Pineapple", "Mango", "Guava"]
# use a for loop to loop through the array and print out each element
for fruit in fruits:
    print(fruit)

# If-Statments:
# (Compare 3 numbers)
# Declare 3 integer variables (300, 155, 280)
a = 300
b = 155
c = 280
# use an if statment to see which is the largest and which is the smallest
if a < b:
    print("a is less that b")
elif a > c:
    print("a is more than c")

# Print out the largest and smallest
if a > c:
    print("a is the largest and b is the smallest")

# (Compare 3 numbers one line)
# If-statment One-line:
# Use an one-line if statement to print out the biggest and smallest number
if a > b and c > a: print("a is greater that b and c!")

# While loop:
#
# (Print one-fifty)
# Use a while loop to print out number 1 to 50
i = 0
while i < 51:
    print(i)
    i = i + 1
# (Find sum natural numbers)
# Write a program to find the sum of first 10 natural numbers

sum = 1
while sum < 11:
    print(sum)
    sum = sum + 1

# Dictionary:
# Initialize a dictionary called studentMarks with 5 key-value pairs
StudentMarks = {
    "Natalie": 10,
    "Jesse": 9,
    "Ben": 5,
    "Abbi": 6,
    "Beth": 7
}
# Add another item to the dictionary
StudentMarks["newName"] = 8
# print out the whole dictionary
print(StudentMarks)
# use a loop to print out each key of the dictionary
for names in StudentMarks:
    print(names)
# use a loop to print out each value of the dictionary
for x in StudentMarks:
    print(StudentMarks[x])
# use a loop to print out each key and value pair of the dictionary
for x, y in StudentMarks.items():
    print(x, y)
# Check if the key "Yadhir" exists in the dictionary
if "Yadhir" in StudentMarks:
    print("Yes the name Yadhir exists")
else:
    print("The name Yadhir does not exist")

# # FILE HANDLING REAL-WORLD
#

import sys
import io

try:
    #open file stream
    file = open("file_name.txt", "w")
except IOError:
    print("There was an error writing to file")
    sys.exit()
print("Enter File"),
print("' When finished")
while file_text != file_finish:
    file_text = raw_input("Enter text: ")
    if file_text == file_finish:
        #close the file
        file.close()
        break
    file.write(file_text)
    file.write("\n")
file.close()
file_name = raw_input("Enter filename: ")
if len(file_name) == 0:
    print("Next time please enter something")
    sys.exit()
try:
    file = open(file_name, "r")
except IOError:
    print("There was an error reading the file")
    sys.exit();
file_text = file.read()
file.close();
print( file_text)