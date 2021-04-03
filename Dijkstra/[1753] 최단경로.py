"""
다익스트라 알고리즘을 공부하고 처음으로 풀어본 최단 경로 문제다.

이 문제는 노드가 최대 2만, 간선이 30만개 이므로 만약 선형탐색으로 문제를 풀었다면 O(V^2)의 시간 복잡도를 때문에 시간초과가 떴을 것이다.

그래서 우선순위 큐를 통해 해결하였고, O(ElogV) 이므로 대략적으로 계산해보면 30만 * 15 = 450만번 정도의 연산이 걸리게 된다.

"""

import sys
import heapq

def dijkstra(start):
  
  queue = []
  heapq.heappush(queue,(0,start))
  distance[start] = 0

  while queue:

    dist,now = heapq.heappop(queue)

    if distance[now] < dist:
      continue
    
    for i in graph[now]:
      cost = i[1] + dist

      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(queue,(cost,i[0]))

INF = int(1e9)
V,E = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(V+1)]
distance = [INF]*(V+1)

start = int(sys.stdin.readline())

for _ in range(E):
  u,v,w = map(int,sys.stdin.readline().split())

  graph[u].append((v,w))

dijkstra(start)

for i in range(1,V+1):
  
  if distance[i] == INF:
    print("INF")
  else:
    print(distance[i])


  
