re = []


def letterCombinations(digits: str) -> [str]:
    numToChar = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': [
        'm', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

    charList = []
    l = len(digits)
    if (l == 0):
        return re
    for i in range(l):
        charList.append(numToChar[digits[i]])
    getAll(charList, '')
    return re


def getAll(charList: list, s: str):
    l = len(charList)
    if (l == 1):
        for i in range(len(charList[0])):
            re.append(s+charList[0][i])
        return
    else:
        for i in range(len(charList[0])):
            getAll(charList[1:l], s+charList[0][i])


print(letterCombinations('2'))
