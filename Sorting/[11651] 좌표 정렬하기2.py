import sys

SIZE = 100000
N = int(sys.stdin.readline())
data = [[] for _ in range(2*SIZE+1)]

for _ in range(N):

  tmp = list(map(int, sys.stdin.readline().split()))

  data[tmp[1]+SIZE].append(tmp[0])

for i in range(len(data)):
  
  tmp = len(data[i])
  if tmp ==0:
    continue
  elif tmp==1:
    print(data[i][0],i-SIZE)
  else:
    data[i].sort()
    for v in data[i]:
      print(v,i-SIZE)