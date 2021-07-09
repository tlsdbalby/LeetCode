def threeSum(nums: list) -> [list]:
    re = []
    l = len(nums)
    if (l < 3):
        return re
    nums.sort()
    for i in range(l):
        if (nums[i] > 0):
            break
        if (i != 0 and nums[i] == nums[i-1]):
            print("co!")
            continue
        print("nco!")
        L = i + 1
        R = l - 1
        while (L < R):
            if (nums[i] + nums[L] + nums[R] > 0):
                R -= 1
            elif (nums[i] + nums[L] + nums[R] < 0):
                L += 1
            elif (nums[i] + nums[L] + nums[R] == 0):
                re.append([nums[i], nums[L], nums[R]])
                L += 1
                R -= 1
                while(nums[L] == nums[L+1]):
                    L += 1
                while(nums[R] == nums[R-1]):
                    R -= 1
    return re


def binarySearch(arr, l, r, x):

    # 基本判断
    if r >= l:

        mid = int(l + (r - l)/2)

        # 元素整好的中间位置
        if arr[mid] == x:
            return mid

        # 元素小于中间位置的元素，只需要再比较左边的元素
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)

        # 元素大于中间位置的元素，只需要再比较右边的元素
        else:
            return binarySearch(arr, mid+1, r, x)

    else:
        # 不存在
        return -1


print(threeSum([0, 0, 0]))
