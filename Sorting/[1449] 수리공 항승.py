import sys
from collections import deque

N,L = map(int,sys.stdin.readline().split())

data = list(map(int,sys.stdin.readline().split()))
data.sort()
queue = deque(data)

first_spot = queue.popleft()
tape = [first_spot-0.5,first_spot-0.5+L]
count = 1

while queue:
  
  spot = queue.popleft()
  
  if tape[0]<spot<tape[1]:
    continue
  else:
    tape[0]=spot-0.5
    tape[1]=tape[0]+L
    count+=1

print(count)

  
