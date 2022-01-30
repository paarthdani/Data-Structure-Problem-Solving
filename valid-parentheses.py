# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is
# valid.
#
# An input string is valid if:
#
#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.
#
# Input: s = "()[]{}"
# Output: true
#
# Input: s = "(]"
# Output: false


def is_valid(s):
    l = []
    dict = {")": "(", "}": "{", "]": "["}
    for i in s:
        if i == '[' or i == '{' or i == "(":
            l.append(i)
        elif (i == "]" or i == "}" or i == ")") and len(l) > 0:
            if l[-1] == dict.get(i):
                l.pop()
            else:
                return False
        else:
            return False

    if len(l) == 0:
        return True
    else:
        return False


s = "()"
print(is_valid(s))
