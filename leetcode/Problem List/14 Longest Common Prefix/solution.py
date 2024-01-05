def longestCommonPrefix(strs):
    strs.sort(key=len)
    sample = strs[0]
    string = ""
    print(strs)
    if (len(strs) > 1):
        for i in range(0, len(sample)):
            letter = str(sample[i])
            status = False
            for j in range(1, len(strs)):
                if (str(strs[j][i]) == letter):
                    status = True
                else:
                    status = False
                    return string
            if (status == True):
                string += letter
        return string
    else:
        return sample


strs = list(map(str, input().split()))
print(longestCommonPrefix(strs))

## FINISHED##
