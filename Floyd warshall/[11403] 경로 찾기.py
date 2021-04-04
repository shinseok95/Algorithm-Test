"""
플로이드 워셜 알고리즘을 응용한 문제 유형이다.

기존의 플로이드 워셜 문제는 최단 거리를 구하는 것이 특징이라면, 이 문제는 해당 경로가 존재하는 지를 물어보고있다.

즉, 
min(graph[i][j],graph[i][k]+graph[k][j])가 아닌,

if graph[i][k] == 1 and graph[k][j] == 1 :
  graph[i][j] = 1

로 접근해야한다.
  
"""

import sys

N = int(sys.stdin.readline())
graph = []

for _ in range(N):
  graph.append(list(map(int,sys.stdin.readline().split())))

for k in range(N):
  for i in range(N):
    for j in range(N):
      if graph[i][j] == 1:
        continue
      else:
        if graph[i][k] == 1 and graph[k][j] == 1:
          graph[i][j] = 1

for i in range(N):
  print(*graph[i])[24