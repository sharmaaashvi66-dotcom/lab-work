X = int(input("Enter X: "))
Y = int(input("Enter Y: "))
N = int(input("Enter N: "))

for i in range(X + 1, Y + 1):  
    if i % N == 0:             
        print(i)
