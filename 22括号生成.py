def generateParenthesis(n: int) -> [str]:
    return getAll(n)


def getAll(n: int):
    if n == 1:
        return {'()'}
    else:
        re = set()
        for l in getList(n):
            if l[0] == 1 or l[0] == n-1:
                temp = list(getAll(n-1))
                for i in range(len(temp)):
                    re.add('('+temp[i]+')')
                    re.add('()'+temp[i])
                    re.add(temp[i]+'()')
            else:
                t1 = list(getAll(l[0]))
                t2 = list(getAll(l[1]))
                for i in range(len(t1)):
                    for j in range(len(t2)):
                        re.add(t1[i]+t2[j])
        return re


def getList(n: int):
    l = []
    for i in range(1, n):
        l.append([i, n-i])
    return l


print(generateParenthesis(5))
