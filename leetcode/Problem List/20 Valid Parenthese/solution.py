def isValid(s):
    n = len(s)
    store = []
    for i in range(0, n):
        flag = False
        if (str(s[i]) == '(' or str(s[i]) == '[' or str(s[i]) == '{'):
            store.append(str(s[i]))
        else:
            if (store != []):
                lastSym = store.pop()
                if (lastSym == '(' and str(s[i]) == ')'):
                    flag = True
                elif (lastSym == '[' and str(s[i]) == ']'):
                    flag = True
                elif (lastSym == '{' and str(s[i]) == '}'):
                    flag = True
                else:
                    return False
            else:
                return False

    if (store == []):
        return flag
    else:
        return False


s = list(map(str, input().split()))
print(isValid(s))

## FINISHED##
