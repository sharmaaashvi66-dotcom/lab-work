import math

print("N\tN^2\tN^3\tSquare Root")

i = 1

while i <= 15:
    square = i * i
    cube = i * i * i
    root = math.sqrt(i)

    print(i, "\t", square, "\t", cube, "\t",
          format(root, ".4f"))

    i += 1