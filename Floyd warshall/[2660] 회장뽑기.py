"""
i->i로 가는 경우를 0으로 처리해주지 않아서 꽤나 시간이 걸렸다.

이 문제는 단순 거리가 아닌 회원들간의 관계를 통해 거리를 표현하였다.

예를 들어, 나와 직접적인 친구, 나와 건너서 아는 사이, 나와 건너 건너 아는 사이 등으로 거리를 매긴 것이다.

이런 유형의 문제가 나온다면 이 문제가 뭘 의미하는 지 잘 파악해야할 것 같다.


"""

import sys

INF = int(1e9)
N = int(sys.stdin.readline())
graph = [[INF]*N for _ in range(N)]

"""

import sys

INF = int(1e9)
N = int(sys.stdin.readline())
graph = [[INF]*N for _ in range(N)]
scores = []
min_score = INF

for i in range(N):
  for j in range(N):
    if i == j:
      graph[i][j] = 0

while True:
  a,b = map(int,sys.stdin.readline().split())

  if a==-1 and b==-1:
    break
  else:
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

for k in range(N):
  for i in range(N):
    for j in range(N):
      graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in range(N):
  score = max(graph[i])
  min_score = min(min_score,score)

  scores.append(score)

print(min_score,scores.count(min_score))

for i in range(N):
  if scores[i] == min_score:
    print(i+1,end=' ')