def get_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "F"
n = int(input())
grades = {}
for i in range(n):
    name, marks = input().split()
    marks = int(marks)
    grade = get_grade(marks)
    print(name + ":", grade)
    if grade in grades:
        grades[grade] = grades[grade] + 1
    else:
        grades[grade] = 1

print("Grade count:")
print(grades)