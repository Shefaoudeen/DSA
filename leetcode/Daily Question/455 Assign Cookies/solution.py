greed = list(map(int, input().split()))
cookies = list(map(int, input().split()))

noOfCookies = 0
feed = 0

for i in range(0, len(cookies)):
    noOfCookies += cookies[i]

index = 0

isCookieNotZero = True
isFeedNotFull = True

while (isCookieNotZero and isFeedNotFull):
    if (greed[index]) > 0:
        greed[index] -= 1
        noOfCookies -= 1
        if (greed[index] == 0):
            feed += 1
    if (index == len(greed)-1):
        pass
    else:
        index += 1
    if (feed == len(greed)):
        isFeedNotFull = False
    if (noOfCookies == 0):
        isCookieNotZero = False

print(feed)
