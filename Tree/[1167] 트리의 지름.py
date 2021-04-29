import sys
from collections import deque

def bfs(n):

  global max_dist, max_point

  q = deque([(n,0)])
  visited = [False]*(N+1)
  visited[n] = True
  while q:

    n,d = q.popleft()
    if max_dist < d:
      max_dist = d
      max_point = n
    
    for next_n,next_d in graph[n]:
      if not visited[next_n]:
        visited[next_n] = True
        q.append((next_n,d+next_d))
  
N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]

max_dist = 0
max_point = 0

for _ in range(N):
  input_data = list(map(int,sys.stdin.readline().split()))

  i = 1
  while True:
    if input_data[i] == -1:
      break
    graph[input_data[0]].append((input_data[i],input_data[i+1]))
    i+=2  

bfs(1)
max_dist = 0

bfs(max_point)
sys.stdout.write(str(max_dist))