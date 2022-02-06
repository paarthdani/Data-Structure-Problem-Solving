# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
#
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#
# Input: numRows = 1
# Output: [[1]]


def generate(numRows):
    res = [[1]]
    if numRows == 1:
        return res
    res.append([1,1])
    if numRows == 2:
        return res
    else:
        for i in range(2,numRows):
            l1 = [0]*(i+1)
            l1[0] = 1
            l1[-1] = 1
            for j in range(1,len(l1)-1):
                l1[j] = res[i-1][j] + res[i-1][j-1]
            res.append(l1)
    return res


numRows = 6
print(generate(numRows))