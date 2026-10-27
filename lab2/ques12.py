
basic = float(input("Enter basic salary: "))

hra = basic * 0.20
ta = basic * 0.05
da = basic * 0.10

gross = basic + hra + ta + da

print("HRA =", hra)
print("TA =", ta)
print("DA =", da)
print("Gross salary =", gross)
