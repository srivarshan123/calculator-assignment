# Stage 3 - Student Grade Calculator

print("Student Grade Calculator")

name = input("Enter student name: ")

marks1 = float(input("Enter marks for Subject 1: "))
marks2 = float(input("Enter marks for Subject 2: "))
marks3 = float(input("Enter marks for Subject 3: "))

# Validation
if (0 <= marks1 <= 100) and (0 <= marks2 <= 100) and (0 <= marks3 <= 100):

    total = marks1 + marks2 + marks3
    percentage = total / 3

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "F"

    print("\n--- Result ---")
    print("Student Name:", name)
    print("Total Marks:", total)
    print("Percentage:", percentage)
    print("Grade:", grade)

else:
    print("Error: Marks must be between 0 and 100.")
