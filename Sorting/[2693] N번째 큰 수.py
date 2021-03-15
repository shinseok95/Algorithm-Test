N = int(input())
data = []

for _ in range(N):
  data.append(list(map(int,input().split())))
  
for i in range(N):
  data[i].sort(reverse=True)
  print(data[i][2])