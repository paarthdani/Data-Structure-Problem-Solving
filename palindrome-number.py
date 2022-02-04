# Given an integer x, return true if x is palindrome integer. An integer is a palindrome when it reads the
# same backward as forward. For example, 121 is a palindrome while 123 is not.

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
#
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
#
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# def isPalindrome(self, x: int) -> bool:
#     return str(x) == str(x)[::-1]


def is_palindrome(x):
    if x < 0:
        return False
    x1 = x
    sum = 0
    while x > 0:
        a = x % 10
        sum = (sum*10) + a
        x = x // 10
    return x1 == sum


i = 0
print(is_palindrome(i))
