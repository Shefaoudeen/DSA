def arrayStringsAreEqual(word1, word2):
    string1 = ""
    for word in word1:
        string1 += str(word)
    string2 = ""
    for word in word2:
        string2 += str(word)
    if (string1 == string2):
        return True
    else:
        return False


word1 = list(map(str, input().split()))
word2 = list(map(str, input().split()))
print(arrayStringsAreEqual(word1, word2))

## FINISHED##
