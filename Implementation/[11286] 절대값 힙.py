import sys
from heapq import heappop, heappush

N = int(sys.stdin.readline())

abs_heap = []
n_count = dict()

for _ in range(N):
  n = int(sys.stdin.readline())
  
  if n == 0 :
    if len(abs_heap) == 0:
      print(0)
    else:
      k = heappop(abs_heap)
      
      if n_count.get(-k) != None:
        if n_count[-k] == 0:
          n_count[k] -= 1
          print(k)
        else:
          n_count[-k] -= 1
          print(-k)
      else:
        n_count[k] -= 1
        print(k)
  else:

    if n_count.get(n) != None:
        n_count[n] += 1
    else:
        n_count[n] = 1
    
    heappush(abs_heap,abs(n))