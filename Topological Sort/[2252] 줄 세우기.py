import sys
from collections import deque

def topology_sort():

  q = deque()

  for i in range(1,N+1):
    if indegree[i] == 0:
      q.append(i)

  while q:
    now = q.popleft()
    result.append(now)

    for j in graph[now]:
      indegree[j] -= 1
      
      if indegree[j] ==0:
        q.append(j)

N,M = map(int,sys.stdin.readline().split())
graph=[[] for _ in range(N+1)]
indegree = [0]*(N+1)
result = []

for _ in range(M):
  a,b = map(int,sys.stdin.readline().split())
  
  graph[a].append(b)
  indegree[b] += 1

topology_sort()
print(*result)