# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not,
# return the index where it would be if it were inserted in order. Write an algorithm with O(log n) runtime complexity.
#
# Input: nums = [1, 3, 5, 6], target = 5
# Output: 2
#
# Input: nums = [1,3,5,6], target = 2
# Output: 1
#
# Input: nums = [1,3,5,6], target = 7
# Output: 4


def search(nums, nums1, target):
    high = len(nums) - 1
    low = 0
    mid = low + ((high - low) // 2)

    if len(nums) == 1 and nums[mid] != target:
        if nums[mid] > target:
            return nums1.index(nums[mid])
        else:
            return nums1.index(nums[mid]) + 1

    if nums[mid] == target:
        return nums1.index(nums[mid])
    elif nums[mid] > target:
        l = nums[:mid]
        if len(l) == 0:
            return nums1.index(nums[mid])
        return search(l, nums1, target)

    elif nums[mid] < target:
        l = nums[mid + 1:]
        if len(l) == 0:
            return nums1.index(nums[mid])
        return search(l, nums1, target)


def search_insert(nums, target):
    return search(nums, nums, target)


l = [1, 3, 5, 6]
target = 2
print(search_insert(l, target))
