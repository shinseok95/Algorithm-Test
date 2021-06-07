import sys
from heapq import heappush, heappop

INF = int(1e9)

def dik(n,dist,graph):
  
  q = []
  heappush(q,(0,n))

  while q:
    d, now = heappop(q)

    if dist[now] < d:
      continue
    
    for i in graph[now]:
      cost = d + i[1]

      if cost < dist[i[0]]:
        dist[i[0]] = cost
        heappush(q,(cost,i[0]))

N,M,X = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
rev_graph = [[] for _ in range(N+1)]
for _ in range(M):
  s,e,t = map(int,sys.stdin.readline().split())
  graph[s].append((e,t))
  rev_graph[e].append((s,t))

dist = [INF] * (N+1)
dik(X,dist,graph)

s_dist = [INF] * (N+1)
dik(X,s_dist,rev_graph)

result = [x+y for x,y in zip(dist,s_dist)]

result[X] = -1
result[0] = -1

print(max(result))