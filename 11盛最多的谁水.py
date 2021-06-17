# 自己的方法：双for，从前向后+从后向前，加入一个边界条件：每次最大值是当前元素*距离，若是maxV大于这个值，则不必继续第二个for的从后向前。时间勉强合法
def maxArea(height: [int]) -> int:
    l = len(height)
    maxV = -1
    for i in range(l):
        t1 = height[i]
        if (i != l-1):
            if (maxV > (t1*(l-1 - i))):
                continue
            for j in range(l-1, i, -1):
                t2 = height[j]
                s = t1 if t1 < t2 else t2
                temp = s * (j - i)
                if (temp > maxV):
                    maxV = temp
                if (maxV > (t1 * (j-i))):
                    break
        else:
            t1 = height[i] if height[i] < height[i-1] else height[i-1]
            maxV = t1 if t1 > maxV else maxV
    return maxV


# LeetCode的标准答案：双指针，x从头到尾，y从尾到头，记录每次的min(x,y)*距离，然后x和y中较小的按序移动，直到x=y
# 主要是对题目本质的抽象理解，官方题解写的很好，详见官解
def LeetCodemaxArea(height: [int]) -> int:
    l = len(height)
    x = 0
    y = l-1
    maxV = -1
    while (x != y):
        t1 = height[x]
        t2 = height[y]
        s = t1 if t1 < t2 else t2
        t = s * (y - x)
        if (maxV < t):
            maxV = t
        if (s == t1):
            x += 1
        else:
            y -= 1
    return maxV


print(LeetCodemaxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
