"""
벨만 포드를 모르고 다익스트라로 풀었는데, 풀렸다..

그래서 벨만 포드로 다시 풀어보았고, 이번 문제가 벨만 포드 알고리즘을 활용하여 음의 사이클이 존재하는지 확인하는 문제라는 것을 알 수 있었다.

기존의 다익스트라의 경우, N번 함수를 호출했어야하는 반면 벨만 포드는 딱 한번만 함수를 호출하면 됐었다.

다음부터 음의 값이 있는 그래프 문제, 음의 사이클을 찾는 문제는 벨만 포드로 접근해야겠다.
"""

import sys

def bf(n):
  distance[n][n] = 0

  for i in range(N):
    for j in range(len(edges)):

      cur = edges[j][0]
      next_node = edges[j][1]
      cost = edges[j][2]

      if distance[next_node] != INF and distance[n][next_node] > distance[n][cur] + cost:
        distance[n][next_node] = distance[n][cur] + cost

        if i == N - 1:
          return True

  return False

T = int(sys.stdin.readline())
INF = int(1e9)

for _ in range(T):
  N, M, W = map(int, sys.stdin.readline().split())
  edges = []
  distance = [[INF] * (N + 1) for _ in range(N + 1)]

  for _ in range(M):
    s, e, t = map(int, sys.stdin.readline().split())
    edges.append((s, e, t))
    edges.append((e, s, t))

  for _ in range(W):
    s, e, t = map(int, sys.stdin.readline().split())
    edges.append((s, e, t * -1))

  if bf(1):
    print('YES')
  else:
    print('NO')

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
"""