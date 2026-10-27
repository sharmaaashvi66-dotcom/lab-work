
basic = float(input("Enter basic salary: "))

hra = basic * 0.20
ta = basic * 0.05
da = basic * 0.10

gross = basic + hra + ta + da

if gross < 300000:
    tax = 0
elif gross <= 1000000:
    tax = gross * 0.10
elif gross <= 2500000:
    tax = gross * 0.20
else:
    tax = gross * 0.30

print("Gross salary =", gross)
print("Income tax =", tax)
