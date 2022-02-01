# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


def longest_common_prefix(strs):
    common = list(strs[0])
    for i in range(1, len(strs)):
        flag, temp = 0, 0
        if strs[i] == "":
            return ""
        for j in range(min(len(common), len(strs[i]))):
            temp = j
            if common[j] == strs[i][j]:
                continue
            else:
                flag = 1
                common = common[:j]
                break
        if flag == 0:
            common = common[:temp+1]
    result = ""
    return result.join(common)


strs1 = ["ab","a"]
print(longest_common_prefix(strs1))
