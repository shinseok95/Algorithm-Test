"""
플로이드 워셜로 해결 가능한 문제이나 파이썬에서는 시간초과를 받을 수 밖에 없다ㅠ

pypy3로 해결했으나 찝찝한 느낌

"""

import sys

INF = int(1e9)
V,E = map(int,sys.stdin.readline().split())

graph = [[INF] * (V+1) for _ in range(V+1)]
min_dist = INF

for _ in range(E):
  a,b,c = map(int,sys.stdin.readline().split())

  graph[a][b] = c

for k in range(1,V+1):
  for i in range(1,V+1):
    for j in range(1,V+1):

      if i==j:
        graph[i][j] = 0
      else:  
        graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in range(1,V+1):
  for j in range(1,V+1):
    
    if i==j:
      continue
    else:
      min_dist = min(min_dist,graph[i][j]+graph[j][i])

if min_dist == INF:
  print(-1)
else:
  print(min_dist)
