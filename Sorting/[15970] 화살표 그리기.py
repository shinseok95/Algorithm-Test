import sys

N = int(sys.stdin.readline())
data = [[] for _ in range(N+1)]
result = 0

for _ in range(N):
  
  d,c = map(int,sys.stdin.readline().split())
  
  data[c].append(d)

for i in range(1,N+1):

  length = len(data[i])

  if length == 0 :
    continue
  
  data[i].sort()
  
  result += data[i][1]-data[i][0]

  for j in range(1,length-1):
    
    if data[i][j+1]-data[i][j] > data[i][j]-data[i][j-1]:
      result+=data[i][j]-data[i][j-1]
    else:
      result+=data[i][j+1]-data[i][j]

  result += data[i][-1]-data[i][-2]

print(result)
  