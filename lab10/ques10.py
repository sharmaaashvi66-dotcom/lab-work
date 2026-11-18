def stats(n):
    small = min(n)
    large = max(n)
    avg = sum(n) / len(n)
    return (small, large, avg)
n = list(map(int, input().split()))
result = stats(n)
print(result)