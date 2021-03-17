import sys
from collections import deque

N = int(sys.stdin.readline())
data = []
result = []

for _ in range(N):
  
  s,e = map(int,sys.stdin.readline().split())

  data.append((s,e))

data.sort(key=lambda x : (x[0],x[1]))

queue = deque(data)

s,e = queue.popleft()
result.append([s,e])

while queue:
  
  s,e = queue.popleft()
  
  if result[-1][1]<=s:
    result.append([s,e])
    
  else :

    for i in range(len(result)):
    
      if result[i][0] < s:
        if result[i][1] > e:
          result[i][0] = s
          result[i][1] = e
          break
      
print(len(result))

      