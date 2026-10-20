# Display square, cube and square root from 1 to 15

print("N\tN^2\tN^3\tSquare Root")

for n in range(1, 16):
    square = n ** 2
    cube = n ** 3
    square_root = n ** 0.5

    print(f"{n}\t{square}\t{cube}\t{square_root:.4f}")