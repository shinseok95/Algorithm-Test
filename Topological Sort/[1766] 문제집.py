"""
위상정렬에서 노드의 숫자가 순서에 영향을 미친다면 priority queue를 사용하자.
"""

import sys
from heapq import heappush,heappop

def topology_sort():

  q = []

  for i in range(1,N+1):
    if indegree[i] == 0 :
      heappush(q,i)
  
  while q:
    now = heappop(q)
    result.append(now)

    for i in graph[now]:
      indegree[i] -= 1

      if indegree[i] == 0 :
        heappush(q,i)

N,M = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
result = []

for _ in range(M):
  a,b = map(int,sys.stdin.readline().split())

  graph[a].append(b)
  indegree[b]+=1

topology_sort()
print(*result)