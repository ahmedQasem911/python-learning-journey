# ----------------------------------------------------------
# Student Grade Calculator
# Asks for a student's name and four subject grades, then
# prints the total percentage and whether the student passed
# (50% or higher).
# ----------------------------------------------------------

student_name = input("Enter student's name: ")

science_grade = int(input("Enter science grade: "))
technology_grade = int(input("Enter technology grade: "))
english_grade = int(input("Enter English grade: "))
math_grade = int(input("Enter maths grade: "))

total_grade = science_grade + technology_grade + english_grade + math_grade

max_grade = 400
total_percentage = int((total_grade / max_grade) * 100)

did_student_pass = total_percentage >= 50

sporting_activities = bool(int(input("Enter 1 if the student participated in sporting activities, 0 if not: ")))

print(f"{student_name} participated in sporting activities: {sporting_activities}")
print("--------------------------------------------------")
print(f"{student_name}'s total percentage is {total_percentage}%")
print(f"{student_name} passed to the next semester: {did_student_pass}")