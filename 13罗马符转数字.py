def romanToInt(s: str) -> int:
    l = len(s)
    point = -1
    num = 0
    while (point < l-1):
        point += 1
        char = s[point]
        if (char == "M"):
            num += 1000
            continue
        if (char == "D"):
            num += 500
            continue
        if (char == "C"):
            if (point != l-1):
                if (s[point+1] == "M"):
                    point += 1
                    num += 900
                    continue
                if (s[point+1] == "D"):
                    point += 1
                    num += 400
                    continue
            num += 100
            continue
        if (char == "L"):
            num += 50
            continue
        if (char == "X"):
            if (point != l-1):
                if (s[point+1] == "C"):
                    point += 1
                    num += 90
                    continue
                if (s[point+1] == "L"):
                    point += 1
                    num += 40
                    continue
            num += 10
            continue
        if (char == "V"):
            num += 5
            continue
        if (char == "I"):
            if (point != l-1):
                if (s[point+1] == "X"):
                    point += 1
                    num += 9
                    continue
                if (s[point+1] == "V"):
                    point += 1
                    num += 4
                    continue
            num += 1
            continue
    return num


print(romanToInt("MCMXCIV"))
