def isValid(s: str) -> bool:
    index = len(s)
    if (index % 2 != 0):
        return False
    stack = []
    while (index > 0):
        index -= 1
        char = s[index]
        if (char == ']' or char == '}' or char == ')'):
            stack.append(char)
        else:
            sl = len(stack)
            if (sl > 0):
                # pop()约等于弹栈，用差值来判断
                des = ord(stack.pop(sl-1)) - ord(char)
                if (des == 1 or des == 2):
                    continue
            return False

    if (len(stack) > 0):
        return False
    return True


# 使用字符是否相等的方式 或者 用ASCII码的差值，每种括号ASCII值差2或是1
def isLegal(r: str, l: str) -> bool:
    if (r == '(' and l == ')'):
        return True
    if (r == '[' and l == ']'):
        return True
    if (r == '{' and l == '}'):
        return True
    return False


print(isValid("(]"))
