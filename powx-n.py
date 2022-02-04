# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
#
# Input: x = 2.00000, n = 10
# Output: 1024.00000
#
# Input: x = 2.10000, n = 3
# Output: 9.26100
#
# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25


def my_pow(x, n):
    res = pow(x, n)
    return format(res, '.5f')


x = 2.000000
n = -2
print(my_pow(x, n))
print(pow(x, n))
