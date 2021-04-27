"""

오히려 너무 많은 생각을 해서 틀린 문제다.

1부터 N까지의 최단 경로를 구하는 문제지만, 주어진 두 노드를 꼭 지나야한다는 조건이 붙어있다. (이미 지나온 노드나 간선 또한 지날 수 있다.)

그렇기에 나는 1->v1->v2->N 또는 1->v2->v1->N의 경우만 구하면 되구나 생각했다.

그래서 다익스트라로 1->v1, 1->v2, v1->v2, v1->N, v2->N을 구하고 최소값을 출력하는 방식으로 구현하였다.

그러나 테스트케이스를 만들어서 돌려보니, 만약 1->v1->N->v2->N의 경우가 정답으로 나옴을 알 수 있었다.

우선은 이런 경우는 불가능하다고 생각하고 다른 방법을 구해보려고 노력했지만, 계속 오답이 나왔고 결국 질문 게시판을 보니 처음에 생각했던 그대로 하면 된 것이었다.

...좀 어이가 없지만, 너무 많이 생각한 내 잘못..

"""

import sys
from heapq import heappop, heappush

INF = int(1e9)

def dijkstra(start):

  q = []

  heappush(q,(0,start))
  distance[start] = 0

  while q:

    dist,now = heappop(q)

    if distance[now] < dist:
      continue
    
    for i in graph[now]:

      cost = i[1] + dist

      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heappush(q,(cost,i[0]))

N,E = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):
  v1,v2,dist = map(int,sys.stdin.readline().split())

  graph[v1].append((v2,dist))
  graph[v2].append((v1,dist))

v1, v2 = map(int,sys.stdin.readline().split())

distance = [INF] * (N+1)
dijkstra(1)

one_to_v1 = distance[v1]
one_to_v2 = distance[v2]

distance = [INF] * (N+1)
dijkstra(v1)

v_to_v = distance[v2]
v1_to_N = distance[N]

distance = [INF] * (N+1)
dijkstra(v2)

v2_to_N = distance[N]

if one_to_v1 + v_to_v + v2_to_N < one_to_v2 + v_to_v + v1_to_N:
  result = one_to_v1 + v_to_v + v2_to_N
else:
  result = one_to_v2 + v_to_v + v1_to_N

if result < 1e9:
  print(result)
else:
  print(-1)
