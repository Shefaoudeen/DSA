nums = list(map(int, input().split()))
val = int(input())
answer = []
count = 0
for i in range(0, len(nums)):
    if (nums[i] != val):
        answer.append(nums[i])
        count+=1

for i in range(0,count):
  nums[i] = answer[i]

print(count)
