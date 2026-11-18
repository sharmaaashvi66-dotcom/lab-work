names = input().split()
vote = {}
for i in names:
    if i in vote:
        vote[i] = vote[i] + 1
    else:
        vote[i] = 1
for i in vote:
    print(i + ":", vote[i])
print("Winner:", winner)