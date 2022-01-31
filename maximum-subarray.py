# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest
# sum and return its sum. A subarray is a contiguous part of an array.
#
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

result = nums[0]
current = nums[0]

for i in range(1, len(nums)):
    current = max(nums[i], current + nums[i])
    result = max(current, result)

print(result)
