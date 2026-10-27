V = float(input("Enter voltage: "))
R1 = float(input("Enter resistance R1: "))
R2 = float(input("Enter resistance R2: "))
R3 = float(input("Enter resistance R3: "))
L = float(input("Enter inductance: "))

i0 = V / (R1 + R2 + R3)
i_final = V / (R1 + R3)

tau = L / (R1 + R3)

print("Initial current =", i0)
print("Final current =", i_final)
print("Time constant =", tau)

import math

t = float(input("Enter time in seconds: "))

i = i_final + (i0 - i_final) * math.exp(-t / tau)

print("Current at time t =", i)