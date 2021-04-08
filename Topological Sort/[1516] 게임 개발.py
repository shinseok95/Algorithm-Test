import sys
from collections import deque

def topology_sort():

  q = deque()

  for i in range(1,N+1):
    if indegree[i] == 0:
      q.append((i,0))
  
  while q:
    now,t = q.popleft()
    result[now] = t + times[now]

    for i in out_graph[now]:
      indegree[i] -= 1

      if indegree[i] == 0:
        max_time = 0

        for j in in_graph[i]:
          max_time = max(max_time,result[j])
        
        q.append((i,max_time))

N = int(sys.stdin.readline())

indegree = [0]*(N+1)
times = [0]*(N+1)
result = [0]*(N+1)

in_graph = [[] for _ in range(N+1)]
out_graph = [[] for _ in range(N+1)]

for i in range(1,N+1):
  node = list(map(int,sys.stdin.readline().split()))

  times[i] = node[0]

  for j in node[1:]:
    
    if j == -1:
      break
    
    in_graph[i].append(j)
    out_graph[j].append(i)
    indegree[i]+=1

topology_sort()

for i in range(1,N+1):
  print(result[i])