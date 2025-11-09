# Kris Rainiell D. Basco
# November 6, 2025
# This program computes the final grade of a student with equivalent remarks.

print("Welcome to Grades Computation")

# Lecture Class Standing Grade Input
print("\nClass Standing (Lecture) 70%")

print()
assignment_lec = float(input("Enter your Lecture Assignment Grade (15%): "))
project_lec = float(input("Enter your Lecture Project Grade (20%): "))
recitation_lec = float(input("Enter your Lecture Recitation Grade (10%): "))
quiz_lec = float(input("Enter your Lecture Quiz Grade (25%): "))

# Lecture Examination Grade Input
print()
print("Examination (Lecture) 30%")

print()
examination_lec = float(input("Enter your Lecture Examination Grade (30%): "))

# Lecture Grade Computation
lecture_computation = (assignment_lec * 0.15) + (project_lec * 0.20) + (recitation_lec * 0.10) + (quiz_lec * 0.25)
total_lecture_computation = (lecture_computation) + (examination_lec * 0.30)

# Laboratory Class Standing Grade Input
print("\n\nClass Standing (Laboratory) 30%")

print()
assignment_lab = float(input("Enter your Laboratory Assignment Grade (15%): "))
project_lab = float(input("Enter your Laboratory Project Grade (20%): "))
recitation_lab = float(input("Enter your Laboratory Recitation Grade (10%): "))
quiz_lab = float(input("Enter your Laboratory Quiz Grade (25%): "))

# Laboratory Examination Grade Input
print()
print("Examination (Laboratory) 30%")

print()
examination_lab = float(input("Enter your Laboratory Examination Grade (30%): "))

# Laboratory Grade Computation
laboratory_computation = (assignment_lab * 0.15) + (project_lab * 0.20) + (recitation_lab * 0.10) + (quiz_lab * 0.25)
total_laboratory_computation = (laboratory_computation) + (examination_lab * 0.30)

# Final Grade Computation
print("\nFinal Grade Lecture (70%) + Laboratory (30%)")
final_grade = (total_lecture_computation * 0.70) + (total_laboratory_computation * 0.30)

# Equivalent and Remarks Section
print()
if final_grade >= 96.5:
    equivalent = 1.00
    remarks = ("You Passed!!!")
elif final_grade >= 93.5:
    equivalent = 1.25
    remarks = ("You Passed!!!")
elif final_grade >= 90.5:
    equivalent = 1.50
    remarks = ("You Passed!!!")
elif final_grade >= 87.5:
    equivalent = 1.75
    remarks = ("You Passed!!!")
elif final_grade >= 84.5:
    equivalent = 2.00
    remarks = ("You Passed!!!")
elif final_grade >= 81.5:
    equivalent = 2.25
    remarks = ("You Passed!!!")
elif final_grade >= 78.5:
    equivalent = 2.50
    remarks = ("You Passed!!!")
elif final_grade >= 75.5:
    equivalent = 2.75
    remarks = ("You Passed!!!")
elif final_grade >= 74.5:
    equivalent = 3.00
    remarks = ("You Passed!!!")
else:
    equivalent = 5.00
    remarks = ("You Failed!!!")

print(f"Your Final Grade is {final_grade:.2f} which is equivalent to {equivalent:.2f} {remarks}")