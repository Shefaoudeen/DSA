def findContentChildren(g, s):
    g.sort()
    s.sort()

    feed = 0

    for i in range(0, len(g)):
        for j in range(0, len(s)):
            count = g[i]
            if (s[j] >= g[i]):
                feed += 1
                break

    return feed


g = list(map(int, input().split()))
s = list(map(int, input().split()))
print(findContentChildren(g, s))
