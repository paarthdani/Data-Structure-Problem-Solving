# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
# target.You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

nums = [3, 2, 95, 4, -3]
target = 92

hashmap = {}
result = []
for i in range(0, len(nums)):
    x = target - nums[i]
    print(x)
    print(hashmap)
    if hashmap.get(x) is not None:
        result.append(i)
        result.append(hashmap.get(x))
        break
    else:
        hashmap[nums[i]] = i
print(result)
