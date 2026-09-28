h=float(input("enter"))
wt=float(input("enter"))
bmi=wt/(h**2)
if bmi<18.5:
    print("underweight")
elif bmi<25:
    print("normal weight")
elif bmi<30:
    print("slighty overweight")
elif bmi<35:
    print("obese")
else:
    print("clinically obese")