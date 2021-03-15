import sys

N = int(input())
data=[[] for _ in range(201)]

for _ in range(N):
  tmp = list(map(str, sys.stdin.readline().split()))

  age = int(tmp[0])  
  data[age].append(tmp[1])

for i in range(1,201):
  for name in data[i]:
    print(i, name)