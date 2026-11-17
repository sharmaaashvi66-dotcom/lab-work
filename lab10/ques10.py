def stats(nums):
    small = min(nums)
    large = max(nums)
    avg = sum(nums) / len(nums)
    return (small, large, avg)
nums = list(map(int, input().split()))
result = stats(nums)
print(result)