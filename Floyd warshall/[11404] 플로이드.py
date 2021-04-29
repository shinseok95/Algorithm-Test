import sys

INF = int(1e9)
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[INF]*(N+1) for _ in range(N+1)]
dp = [[INF] *(N+1) for _ in range(N+1)]

for _ in range(M):
  a,b,c = map(int,sys.stdin.readline().split())
  
  graph[a][b] = min(graph[a][b],c)
  
for i in range(1,N+1):
  for j in range(1,N+1):
    if i==j:
      graph[i][j] = 0

for k in range(1,N+1):
  for i in range(1,N+1):
    for j in range(1,N+1):
      graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

for i in range(1,N+1):
  for j in range(1,N+1):
    if graph[i][j] == INF:
      sys.stdout.write(str(0)+' ')
    else:
      sys.stdout.write(str(graph[i][j])+' ')
  sys.stdout.write('\n')