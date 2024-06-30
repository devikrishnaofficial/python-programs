N = int(input("Enter the number of students: "))
students = []

for i in range(1, N + 1):
    print(f"\nStudent {i}:")
    name = input("Enter name: ")
    roll_no = input("Enter roll number: ")
    total_mark = float(input("Enter total marks: "))
    student = {
        'name': name,
        'roll_no': roll_no,
        'total_mark': total_mark
    }
    students.append(student)
highest_mark_student = max(students, key=lambda x: x['total_mark'])

print("\nDetails of the student with the highest total marks:")
print(f"Name: {highest_mark_student['name']}")
print(f"Roll No: {highest_mark_student['roll_no']}")
print(f"Total Marks: {highest_mark_student['total_mark']}")