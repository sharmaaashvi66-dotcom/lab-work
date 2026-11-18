def get_grade(m):
    if m >= 80:
        return "A"
    elif m >= 60:
        return "B"
    elif m >= 40:
        return "C"
    else:
        return "F"
n = int(input("enter"))
grades = {}
for i in range(n):
    name, marks = input().split()
    marks = int(marks)
    g = get_grade(marks)
    print(name , ":", grade)
    if g in grades:
        grades[g] = grades[g] + 1
    else:
        grades[g] = 1

print("Grade count:")
print(grades)