import sys

N = int(sys.stdin.readline())
data = [[] for _ in range(101)]

for _ in range(N):
  
  name, k,e,m = sys.stdin.readline().split()
  k,e,m = int(k),int(e),int(m)

  data[k].append((name,k,e,m))

for i in range(100,0,-1):
  
  length = len(data[i])

  if length==0 :
    continue

  elif length == 1:
    print(data[i][0][0])
    continue

  else:

    data[i].sort(key=lambda x : x[0])
    data[i].sort(key=lambda x : x[3],reverse=True)
    data[i].sort(key=lambda x : x[2])

    for j in range(length):
      print(data[i][j][0])
