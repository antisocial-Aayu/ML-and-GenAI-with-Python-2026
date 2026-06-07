
# Program 1: Print First 10 Natural Numbers

def print_natural_numbers():
    for i in range(1, 11):
        print(i)

print_natural_numbers()

# Program 2: Calculate Sum of First N Natural Numbers

def sum_natural_numbers(n):
    total = 0

    for i in range(1, n + 1):
        total += i

    return total

n = int(input("Enter N: "))
print("Sum =", sum_natural_numbers(n))

# Program 3: Reverse a Number

def reverse_number(num):
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    return reverse

num = int(input("Enter a number: "))
print("Reversed Number =", reverse_number(num))

# Program 4: Count Digits in a Number

def count_digits(num):
    count = 0

    while num > 0:
        count += 1
        num = num // 10

    return count

num = int(input("Enter a number: "))
print("Number of digits =", count_digits(num))

# Program 5: Check Palindrome Number

def is_palindrome(num):
    original = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    return original == reverse

num = int(input("Enter a number: "))

if is_palindrome(num):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
n
# Program 6: Generate Fibonacci Series

def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Enter number of terms: "))
fibonacci(n)

# Program 7: Calculator Using Functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice: "))

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == 1:
    print("Result =", add(a, b))
elif choice == 2:
    print("Result =", subtract(a, b))
elif choice == 3:
    print("Result =", multiply(a, b))
elif choice == 4:
    print("Result =", divide(a, b))
else:
    print("Invalid Choice")


file = open("student.txt", "w")

file.write("Name: Rahul\n")
file.write("Marks: 88\n\n")

file.write("Name: Priya\n")
file.write("Marks: 92\n\n")

file.write("Name: Arjun\n")
file.write("Marks: 85\n\n")

file.close()

print("Student details saved successfully.")

# 2. Read data from the file

file = open("student.txt", "r")
data = file.read()
print("\nStudent Details:")
print(data)
file.close()

# 3. Handle division by zero using exception handling

try:
    a = int(input("\nEnter numerator: "))
    b = int(input("Enter denominator: "))

    result = a / b
    print("Result =", result)

except ZeroDivisionError:
    print("Cannot divide by zero.")

# 4. Create a Student class with name and marks

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("\nStudent Object Details:")
        print("Name:", self.name)
        print("Marks:", self.marks)

s1 = Student("garv", 95)
s1.display()
