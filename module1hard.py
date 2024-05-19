grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = sorted(students)
student_grades = {}
for student, grade in zip(students_list, grades):
    average = sum(grade) / len(grade)
    student_grades[student] = average
print(student_grades)

