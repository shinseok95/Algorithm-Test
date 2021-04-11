import sys
from collections import deque

N,W,L = map(int,sys.stdin.readline().split())
car = list(map(int,sys.stdin.readline().split()))

q = deque([0]*W)
i = 0
count = 0

while q:
  
  q.popleft()
  
  if i<N and sum(q)+car[i] <= L:
    q.append(car[i])
    i+=1

  else:
    if i<N:
      q.append(0)
  
  count += 1

print(count)
  