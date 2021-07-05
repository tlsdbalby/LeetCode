def longestCommonPrefix(strs: list) -> str:
    if (len(strs) == 1):
        return strs[0]
    p1 = 0
    sl = len(strs[0])
    if (sl == 0):
        return ""
    while p1 < sl:
        char = strs[0][p1]
        for p2 in range(1, len(strs)):
            l = len(strs[p2])
            if (l == 0):
                return ""
            if (p1 < l):
                if char == strs[p2][p1]:
                    continue
            print(p1)
            return strs[0][:p1]
        p1 += 1
    return strs[0][:p1]


print(longestCommonPrefix(["flower", "flower"]))
