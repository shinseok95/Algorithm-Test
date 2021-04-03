"""
몇 문제를 풀어보니 다익스트라 알고리즘을 활용할 때 가장 중요한 점은 "이 문제에 다익스트라 알고리즘을 적용할 수 있는가", "시간 복잡도는 충족하는가" 인 것 같다.

왜냐하면 다익스트라 자체는 정형화된 내용이라서, 적용할 수 있는 문제라면 기계적으로 적용할 수 있다.

이 문제는 한 노드에서 다른 노드로의 최단 시간을 구하는 문제로 다익스트라 알고리즘을 적용할 수 있는 문제다.

시간복잡도는 우선 노드가 10만개, 간선은 -1,+1,*2로 3개*10만개이므로 30만개다.(물론 50000만이 넘어가면 *2가 10만을 넘어가므로 간선은 2개가 된다.)

다익스트라 알고리즘의 시간복잡도는 O(ElogV)이므로 30만*17 = 500만 정도 나온다.

즉, 시간복잡도도 충족하기에 다익스트라 알고리즘을 활용하여 이 문제는 해결 가능하다.

"""

from heapq import heappush, heappop

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

      cost = dist + i[1]

      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heappush(q,(cost,i[0]))

INF = int(1e9)

N,K = map(int,input().split())
graph = [[] for _ in range(100001)]
distance = [INF]*(100001)

for i in range(100001):
  
  if i == 0:
    graph[i].append((1,1))
  elif i == 100000:
    graph[i].append((99999,1))
  else:
    graph[i].append((i-1,1))
    graph[i].append((i+1,1))
  
  if 1<=i<=50000:
    graph[i].append((2*i,0))

dijkstra(N)
print(distance[K])