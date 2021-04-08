"""
[2056] 작업과 동일한 논리의 문제였다.

위상정렬이지만, 동시에 노드가 진행될 수 있고, indegree가 0이 됐을 때, 선행 노드 중 가장 긴 시간을 선택해서 다음 노드에 넘겨줘야한다.

"""

import sys
from collections import deque

def topology_sort():

  q = deque()

  for i in range(1,N+1):
    if indegree[i] == 0 :
      q.append((i,0))

  while q:
    now, t = q.popleft()
    result[now] = t+times[now]

    for i in out_graph[now]:
      indegree[i] -= 1

      if indegree[i] == 0:
        max_t = 0
        
        for j in in_graph[i]:

          max_t = max(max_t,result[j])

        q.append((i,max_t))  

T = int(sys.stdin.readline())

for _ in range(T):
  4
  N,K = map(int,sys.stdin.readline().split())
  times = [0]+list(map(int,sys.stdin.readline().split()))
  indegree = [0]*(N+1)

  out_graph = [[] for _ in range(N+1)]
  in_graph = [[] for _ in range(N+1)]

  result = [0]*(N+1)

  for _ in range(K):
    a,b = map(int,sys.stdin.readline().split())
    indegree[b] += 1

    out_graph[a].append(b)
    in_graph[b].append(a)
    
  W = int(sys.stdin.readline())

  topology_sort()
  print(result[W])