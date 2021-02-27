N = int(input())
data = []
result = 0

for i in range(N):
  data.append(int(input()))

data.sort(reverse=True)

for i in range(len(data)):
  
  tip = data[i]-i

  if tip>0:
    result+=tip
  else:
    continue

print(result)