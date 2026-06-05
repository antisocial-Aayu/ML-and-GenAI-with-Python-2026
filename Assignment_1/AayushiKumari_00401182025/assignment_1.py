# Find area of rectangle

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

area = length * breadth

print("Area of Rectangle =", area)




# Find simple interest

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time (in years): "))

si = (principal * rate * time) / 100

print("Simple Interest =", si)


# Celsius to Fahrenheit conversion

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit =", fahrenheit)


# Calculate average of 3 numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

average = (num1 + num2 + num3) / 3

print("Average =", average)



# Find square and cube of a number

num = int(input("Enter a number: "))

square = num ** 2
cube = num ** 3

print("Square =", square)
print("Cube =", cube)


# Swap two numbers without using a third variable

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a = a + b
b = a - b
a = a - b

print("After Swapping:")
print("a =", a)
print("b =", b)



# Student Report Program

# Taking student details as input
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

# Taking marks of 3 subjects
marks1 = float(input("Enter marks in English: "))
marks2 = float(input("Enter marks in Mathematics: "))
marks3 = float(input("Enter marks in Science: "))

# Calculating total marks
total = marks1 + marks2 + marks3

# Calculating percentage
percentage = (total / 300) * 100

# Displaying student report
print("\n----- STUDENT REPORT -----")
print("Name:", name)
print("Roll Number:", roll_no)
print("English Marks:", marks1)
print("Mathematics Marks:", marks2)
print("Science Marks:", marks3)
print("Total Marks:", total)
print("Percentage:", percentage, "%")