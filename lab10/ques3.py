names = input().split()
votes = {}
for i in names:
    if i in votes:
        votes[i] = votes[i] + 1
    else:
        votes[i] = 1
for i in votes:
    print(i + ":", votes[i])
print("Winner:", winner)