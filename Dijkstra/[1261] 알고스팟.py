"""
이 문제를 통해 많은 것을 배울 수 있었다.

우선 다익스트라 알고리즘을 통해 2차원 그래프의 최단 경로 또한 구할 수 있다는 점을 알게되었다.
지금까지는 단순히 DFS,BFS,DP등을 통해서 해결했다면, 앞으로는 다익스트라 또한 해결 후보로써 염두해둬야할 것 같다.

두번째는 Breadth first search, Best first Search, 다익스트라에 대한 차이이다.

우선 세 알고리즘 모두 queue를 사용한다는 점은 같다.

그러나 BFS는 모든 경로를 탐색하기 때문에 아무리 가지치기를 하더라도 시간이 가장 많이 소요된다.
그리고 다익스트라는 시작점을 기준으로 가장 가까운 경로를 탐색해서 나가기 때문에 시간이 더 적게 걸리지만, 시작지와 도착지 사이에 있는 대부분의 경로를 탐색한다는 단점이 있다.
마지막으로 Best first search는 현재 위치로부터 가장 가까운 점을 탐색해서 나가기 때문에 가장 시간이 적게 걸린다. 그러나 다익스트라는 시작점을 기준으로 다음 경로를 결정하는 반면 best first search는 현재 위치를 기준으로 다음 위치를 결정하기 때문에 최단 거리를 보장할 수는 없다.

이번 문제는 세가지 알고리즘으로 모두 해결할 수 있었다.

BFS : 224ms
Dijkstra : 132ms
Best FS : 100ms

"""

import sys
from heapq import heappush, heappop

def dijkstra(start_r,start_c):

  q = []

  distance[start_r][start_c] = 0
  heappush(q,(0,(start_r,start_c)))

  while q:

    dist, now = heappop(q)

    if distance[now[0]][now[1]]<dist:
      continue
    
    for i in dijkstra_graph[now[0]][now[1]]:
      
      cost = i[0]+dist
      
      if cost < distance[i[1][0]][i[1][1]]:
        distance[i[1][0]][i[1][1]] = cost
        heappush(q,(cost,(i[1][0],i[1][1])))

dr = (1,0,-1,0)
dc = (0,1,0,-1)

INF = int(1e9)
M,N = map(int,sys.stdin.readline().split())
graph = [[0]*(M+1)]
dijkstra_graph = [[] for _ in range(N+1)]
distance = [[INF]*(M+1) for _ in range(N+1)]

for i in range(N):
  graph.append([0]+list(map(int,list(sys.stdin.readline().rstrip()))))

for r in range(1,N+1):
  dijkstra_graph[r].append([0])
  for c in range(1,M+1):
    
    e = []

    for n in range(4):
      next_r = r+dr[n]
      next_c = c+dc[n]
      if 1<=next_r<=N and 1<=next_c<=M:

        if graph[next_r][next_c]==0:
          e.append((0,(next_r,next_c)))
        else:
          e.append((1,(next_r,next_c)))

    dijkstra_graph[r].append(e)

dijkstra(1,1)
print(distance[N][M])

"""
def bfs(R,C):

  queue = deque([])

  queue.append((R,C))
  distance[R][C] = 0

  while queue:

    r,c = queue.popleft()

    for i in range(4):
      next_r = r+dr[i]
      next_c = c+dc[i]
    
      if 1<=next_r<=N and 1<=next_c<=M :

        if graph[next_r][next_c] == 1:
          if distance[r][c] +1 < distance[next_r][next_c]:
            distance[next_r][next_c] = distance[r][c] +1

            queue.append((next_r,next_c))

        else:
          if distance[r][c] < distance[next_r][next_c]:
            distance[next_r][next_c] = distance[r][c]

            queue.append((next_r,next_c))
      
"""

"""
def bestfs(R,C):

  queue = []
  distance[R][C] = 0
  heappush(queue,(distance[R][C],(R,C)))

  while queue:

    dist,now = heappop(queue)

    for i in range(4):
      next_r = now[0]+dr[i]
      next_c = now[1]+dc[i]
    
      if 1<=next_r<=N and 1<=next_c<=M :

        if next_r == N and next_c == M :
          distance[next_r][next_c] = dist
          return
          
        if graph[next_r][next_c] == 1:
          if dist +1 < distance[next_r][next_c]:
            distance[next_r][next_c] = dist +1

            heappush(queue,(dist +1,(next_r,next_c)))

        else:
          if dist < distance[next_r][next_c]:
            distance[next_r][next_c] = dist

            heappush(queue,(dist,(next_r,next_c)))
"""