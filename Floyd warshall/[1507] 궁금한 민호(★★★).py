"""

<다른 사람의 풀이봄>

플로이드 와샬 문제의 변형 문제다.
아직도 잘 이해가 되지 않는다.

우선, 기존의 플로이드 와샬 문제랑 다르게, 이미 최단 경로가 정해져있다.

그리고 도로 개수의 최솟값을 구하고, 그 도로의 거리값을 더하는 문제다.


여기서 신기한 접근법은, 이미 최단 거리가 구해져있으므로, 거꾸로 플로이드 와샬을 돌려서 직접 연결되어있는지 확인하는 것이다.

예를 들어, graph[i][j] == graph[i][k] + graph[k][j]가 성립하는 경우에는 i->j로 갈 필요 없이, i->k->j로 가면 되기 때문에 해당 도로를 지워도 된다. 

그리고 graph[i][j] > graph[i][k]+graph[k][j] 인 경우에는, graph[i][j]가 최단 거리인데 더 최단 거리가 존재하는 것이므로, 해당 경우에는 불가능한 경우다.

그러므로 -1을 출력해준다.

"""

import sys

def floyd():
  
  for k in range(N):
    for i in range(N):
      for j in range(N):

        if i==j or i==k or j==k:
          continue
        if graph[i][j] == graph[i][k]+graph[k][j]:
          check[i][j]=False
        elif graph[i][j] > graph[i][k]+graph[k][j]:
          return False

  return True

N = int(sys.stdin.readline())
result = 0 

graph = []
for _ in range(N):
  graph.append(list(map(int,sys.stdin.readline().split())))

check = [[True] * N for _ in range(N)]

floyd()

if not floyd():
  print(-1)
else:
  for i in range(N):
    for j in range(i,N):
      if check[i][j]:
        result += graph[i][j]
  
  print(result)