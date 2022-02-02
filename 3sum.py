# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and
# j != k, and nums[i] + nums[j] + nums[k] == 0. Notice that the solution set must not contain duplicate triplets.

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

def three_sum(nums):
    result = []
    for i in range(len(nums)-1):
        dict = {}
        curr = 0 - nums[i]
        print("curr",curr)
        for j in range(i+1, len(nums)):
            curr_new = curr - nums[j]
            print("curr_new",curr_new)
            if dict.get(curr_new) is None:
                dict[nums[j]] = j
                print(dict)
            else:
                print(dict,i,j)
                result.append([nums[i], nums[j], nums[dict.get(curr_new)]])
                print(result)

    res = []
    check = set()
    for i in result:
        hash = tuple(sorted(i))
        if hash not in check:
            res.append(list(hash))
            check.add(hash)

    return res


l = [-1, 0, 1, 2, -1, -4]
print(three_sum(l))
