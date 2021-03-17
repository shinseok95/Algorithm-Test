import sys
from collections import deque
import heapq

T = int(sys.stdin.readline())

for _ in range(T):
  
  N = int(sys.stdin.readline())
  data = []
  result = []

  for _ in range(N):
    s,m = map(int,sys.stdin.readline().split())
    data.append((s,m))
  
  queue = deque(sorted(data,key=lambda x : (x[0],x[1])))
  
  heapq.heappush(result, queue.popleft()[1])

  while queue:
    
    s,m = queue.popleft()

    if result[0] > m:
      heapq.heappush(result,m)
    
  print(len(result))
  