def myAtoi(s: str) -> int:
    s = s.strip()
    l = len(s)
    re = 0
    dL = pow(-2, 31)
    tL = pow(2, 31)-1
    isBegin = False
    isNe = False
    for i in range(l):
        c = ord(s[i])
        if (c < 48 or c > 57):
            if (not isBegin):
                if (c == 43):
                    isBegin = True
                elif (c == 45):
                    isBegin = True
                    isNe = True
                else:
                    return re
            else:
                break
        else:
            isBegin = True
            if (c == 48 and not isBegin):
                continue
            re = re*10+(c-48)
    if isNe:
        re = -re
    if (re < dL):
        return dL
    if (re > tL):
        return tL
    return re


print(myAtoi("+10120"))
