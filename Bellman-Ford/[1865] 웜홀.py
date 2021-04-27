"""
벨만 포드를 모르고 다익스트라로 풀었는데, 풀렸다..

그래서 다시 벨만 포드로 풀어봐야한다..
"""

import sys
from heapq import heappush,heappop

def dijkstra(start,n,N):

  q = []
  distance[n][start] = 0
  heappush(q,(0,start))
  visited = [False]*(N+1)

  while q:

    dist,now = heappop(q)
    
    if distance[n][now] < dist:
      continue
    
    for i in graph[now]:
      cost = dist + i[1]
      
      if distance[n][i[0]] > cost:

        if i[1] < 0:
          if not visited[i[0]]:
            distance[n][i[0]] = cost
            heappush(q,(cost,i[0]))
            visited[i[0]] = True
        else:
          distance[n][i[0]] = cost
          heappush(q,(cost,i[0]))

T = int(sys.stdin.readline())
INF = int(1e9)

for _ in range(T):
  N,M,W = map(int,sys.stdin.readline().split())
  graph = [[] for _ in range(N+1)]
  distance = [[INF]*(N+1) for _ in range(N+1)]

  for _ in range(M):
    s,e,t = map(int,sys.stdin.readline().split())
    graph[s].append((e,t))
    graph[e].append((s,t))
  
  for _ in range(W):
    s,e,t = map(int,sys.stdin.readline().split())
    graph[s].append((e,t*-1))
  
  for n in range(1,N+1):
    dijkstra(n,n,N)

  flag = False

  for i in range(1,N+1):
    for j in range(1,N+1):
      if distance[i][j] + distance[j][i] <0:
        flag = True
        break
    if flag:
      break
  
  if flag:
    print('YES')
  else:
    print('NO')
