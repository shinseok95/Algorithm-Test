from collections import deque

def bfs(A,B):
  
  queue = deque([(A,1)])
  
  while queue:

    a,cnt = queue.popleft()

    if a==B:
      global count
      count=cnt
      break

    mul_a = 2*a
    plus_a = int(str(a)+'1')
    
    if mul_a<=B:
      queue.append((mul_a,cnt+1))

    if plus_a<=B:
      queue.append((plus_a,cnt+1))
  
A,B = map(int,input().split())
count = -1

bfs(A,B)

print(count)
