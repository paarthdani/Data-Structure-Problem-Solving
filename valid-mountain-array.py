# Given an array of integers arr, return true if and only if it is a valid mountain array.
# Recall that arr is a mountain array if and only if:
#
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
#     arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
#     arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
#
# Input: arr = [0,3,2,1]
# Output: true

def valid_mountain_array(arr):
    if len(arr) < 3:
        return False
    flag = 0
    for i in range(1, len(arr)):
        if flag == 0:
            if arr[i - 1] < arr[i]:
                continue
            elif arr[i - 1] > arr[i] and i != 1:
                flag = 1
                continue
            else:
                return False
        elif flag == 1:
            if arr[i - 1] > arr[i]:
                continue
            else:
                return False
    if flag == 0:
        return False
    return True


l = [0, 2, 3, 4, 5, 2, 2]
print(valid_mountain_array(l))
