def removeDuplicates(nums: [int]) -> int:
    l = len(nums)
    if (l <= 1):
        return l
    else:
        p1 = 0
        p2 = 1
        re = 1
        while (p2 < l):
            if (nums[p1] == nums[p2]):
                p2 += 1
            else:
                p1 += 1
                nums[p1] = nums[p2]
                p2 += 1
                re += 1
    return re


param = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates(param))
print(param)
