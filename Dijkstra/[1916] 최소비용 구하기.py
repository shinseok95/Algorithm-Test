import sys
from heapq import heappush,heappop

def dijkstra(start):

  q = []
  distance[start] = 0
  heappush(q,(0,start))

  while q:

    dist, now = heappop(q)

    if distance[now] < dist:
      continue
    
    distance[now] = dist

    for i in graph[now]:
      
      cost = i[1]+dist

      if cost< distance[i[0]]:
        distance[i[0]] = cost
        heappush(q,(cost,i[0]))

INF = int(1e9)
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]
distance = [INF]*(N+1)

for _ in range(M):
  u,v,w = map(int,sys.stdin.readline().split())

  graph[u].append((v,w))
  
start,end = map(int,sys.stdin.readline().split())

dijkstra(start)
print(distance[end])

