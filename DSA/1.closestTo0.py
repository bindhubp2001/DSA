#Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.


def closestTo0(nums):
    nums.sort(key=lambda x: (abs(x), -x))
    return nums[0]  

print(closestTo0([8, 5, 10])) #5