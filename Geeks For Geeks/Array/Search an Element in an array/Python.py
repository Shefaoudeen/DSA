N = int(input())
Array = list(map(int, input().split()))
X = int(input())
Answer = None

for i in range(0,N):
  if(Array[i] == X):
    Answer = i
    
print(Answer)