def get_total_count_of_multiple(nums):
    total_count = {}
    for i in range(1, 10):
        count = 0
        for ele in nums:
            if ele % i == 0:
                count += 1
        total_count[i] = count
    return total_count

n = int(input())  # number of inputs
nums = []

for _ in range(n):
    ele = int(input())
    nums.append(ele)

mp = get_total_count_of_multiple(nums)
print(mp)