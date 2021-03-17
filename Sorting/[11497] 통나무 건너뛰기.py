import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):

  N = int(sys.stdin.readline())
  data = sorted(list(map(int,sys.stdin.readline().split())),reverse=True)
  
  queue = deque([data[0]])
  max_value = 0

  for i in range(1,len(data)):
    
    if i%2==1:
      queue.appendleft(data[i])
    else:
      queue.append(data[i])

  max_value = abs(queue[-1]-queue[0])

  for i in range(0,len(queue)-1):
  
    tmp_value = abs(queue[i+1]-queue[i])
    if tmp_value > max_value:
      max_value = tmp_value
  
  print(max_value)
    
