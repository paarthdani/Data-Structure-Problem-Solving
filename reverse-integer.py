# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside
# the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
#
# Input: x = 123 , Output: 321
# Input: x = -123 , Output: -321
# Input: x = 120 , Output: 21


def reverse(x):
    flag = 0
    if x < 0:
        flag = 1
    a = str(abs(x))
    if flag == 1:
        a += "-"
    a = a[::-1]
    flag = int(a)
    if pow(-2,31) <= flag <= (pow(2,31)-1):
        return int(a)
    else:
        return 0


a = -1203
print(reverse(a))
