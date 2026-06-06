name = input("Enter student name: ")
roll = input("Enter roll number: ")

subjects = int(input("Enter number of subjects: "))

total = 0

for i in range(subjects):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    total += mark

percentage = total / subjects

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\nStudent Result")
print("Name:", name)
print("Roll No:", roll)
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)