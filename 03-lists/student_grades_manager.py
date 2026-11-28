# Student Grades Manager

LINE_WIDTH = 50

print("=" * LINE_WIDTH)
print("Student Grades Manager".center(LINE_WIDTH))
print("=" * LINE_WIDTH)

# A list containing the initial grades of students
grades = [85, 92, 78, 90, 65, 88, 92, 73]


# Task 1 – Display and Update Grades

# Display the complete list of grades
print(f"Grades: {grades}")

# Access the first and last elements using their indices
print(f"First Grade: {grades[0]}")
print(f"Last Grade: {grades[-1]}")

# Update the third student's grade (index 2)
grades[2] = 82
print(f"Grades: {grades}")


# Task 2 – Manage the Grades List

# Add a new grade (95) to the end of the list
grades.append(95)
print(f"Grades: {grades}")

# Insert a new grade (80) at index 2
grades.insert(2, 80)
print(f"Grades: {grades}")

# Remove and return the last element using pop()
grades.pop()
print(f"Grades: {grades}")


# Task 3 – Analyze the Grades

# Count the total number of students
print(f"Total Number of Students: {len(grades)}")

# Find the highest and lowest grades
print(f"Highest Grade: {max(grades)}")
print(f"Lowest Grade: {min(grades)}")

# Calculate the sum and average of all grades
print(f"Sum of all Grades: {sum(grades)}")
print(f"Average Grade: {sum(grades) / len(grades):.2f}")


# Task 4 – Sort the Grades

# Sort the grades in ascending order (lowest to highest)
grades.sort()
print(f"Sorted Grades (Ascending): {grades}")

# Sort the grades in descending order (highest to lowest)
# reverse=True changes the sorting order of the original list
grades.sort(reverse=True)
print(f"Sorted Grades (Descending): {grades}")


# Task 5 – Count Specific Grades

# Count how many students achieved a grade of 92
print(f"Number of students got 92: {grades.count(92)}")


# Task 6 – Display Each Student's Grade

# Initialize a counter to number students starting from 1
index = 1

# Iterate over the list and display each student's grade
for student_grade in grades:
    print(f"Student {index}: {student_grade}")

    # Increment the counter for the next student
    index += 1


# Task 7 – Combine Two Classes

# Create a second list containing the grades of another class
class_b = [76, 89, 94, 68, 85]

# Combine both classes into a new list using the + operator
combined_grades = grades + class_b
print(f"Combined Grades: {combined_grades}")


# Bonus Challenges

# Bonus 1 – Grade Classification

# Iterate over the grades and classify each student based on their score
for student_grade in grades:
    if student_grade >= 90:
        print("Excellent")
    elif student_grade >= 80:
        print("Very Good")
    elif student_grade >= 70:
        print("Good")
    elif student_grade >= 60:
        print("Pass")
    else:
        print("Fail")


# Bonus 2 – Find the Passing Students

# Initialize a counter to track the number of passing students
num_of_passing_students = 0

# Count students who achieved a grade of 60 or higher
for student_grade in grades:
    if student_grade >= 60:
        num_of_passing_students += 1

print(f"Number of passing students: {num_of_passing_students}")


# Bonus 3 – Reverse Ranking

# The grades are already sorted in descending order from Task 4
# Iterate over the list and assign a rank to each grade
rank = 1

for student_grade in grades:
    print(f"{rank}: {student_grade}")

    # Increment the rank for the next student
    rank += 1


# Bonus 4 – Grade Distribution

# Count how many students achieved each specified grade
print(f"Number of students got 92: {grades.count(92)}")
print(f"Number of students got 85: {grades.count(85)}")
print(f"Number of students got 78: {grades.count(78)}")
