# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative
# order of the elements may be changed. Return total elements after placing the final result in the first k slots of
# nums. Do not allocate extra space for another array. You must do this by modifying the input array in-place with
# O(1) extra memory.
#
# Input: nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2
# Output: 5, nums = [0, 1, 4, 0, 3, _, _, _]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.


def remove_element(nums, val):
    i = 0
    print(len(nums))
    while i < len(nums):
        if nums[i] == val:
            nums.remove(i)
            i -= 1
        i += 1

    return nums


print(remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2))
