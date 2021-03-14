from collections import deque

dr = (-1,1,0,0)
dc = (0,0,-1,1)

def bfs(graph,distance,visited):
  global N,M
  queue = deque([])

  for n in range(N):
    for m in range(M):
      
      if graph[n][m] == 1:
        visited[n][m] = True
        distance[n][m] = 1
        queue.append((n,m))
      
      elif graph[n][m] == -1:
        visited[n][m] = True
        distance[n][m] = -1

  while queue:

    r,c = queue.popleft()

    for i in range(4):

      next_r = r+dr[i]
      next_c = c+dc[i]

      if 0<=next_r<N and 0<=next_c<M:
        if not visited[next_r][next_c]:
          
          visited[next_r][next_c] = True
          distance[next_r][next_c] = distance[r][c] +1
          queue.append((next_r,next_c))
      

M,N = map(int,input().split())

graph = []
visited = [[False]*M for _ in range(N)]
distance = [[0]*M for _ in range(N)]

for _ in range(N):
  graph.append(list(map(int,input().split())))

bfs(graph,distance,visited)

zero_flag = False
result = max(map(max,distance))

for n in range(N):
  if distance[n].count(0):
    zero_flag=True
    break

if zero_flag:
  print(-1)
else:
  print(result-1)


