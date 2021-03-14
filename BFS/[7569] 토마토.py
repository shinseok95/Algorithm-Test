from collections import deque

dh = [-1,1,0,0,0,0]
dn = [0,0,1,-1,0,0]
dm = [0,0,0,0,1,-1]

def bfs(graph,distance, visited):
  
  global N,M,H
  queue = deque([])
  
  for h in range(H):
    for n in range(N):
      for m in range(M):
        
        if graph[h][n][m] == 1:
          distance[h][n][m] = 1
          visited[h][n][m] = True
          queue.append((h,n,m))

        
        elif graph[h][n][m] == -1:
          distance[h][n][m] = -1
          visited[h][n][m] = True
           

  while queue:

    h,n,m = queue.popleft()

    for i in range(6):
      
      next_h = h+dh[i]
      next_n = n+dn[i]
      next_m = m+dm[i]

      if 0<=next_h<H and 0<=next_n<N and 0<=next_m<M:
        
        if visited[next_h][next_n][next_m] == False:

          visited[next_h][next_n][next_m] = True
          distance[next_h][next_n][next_m] = distance[h][n][m]+1
          queue.append((next_h,next_n,next_m))
        

M,N,H = map(int,input().split())

graph = []
visited = [[[False]*M for _ in range(N)] for _ in range(H)]

distance = [[[0]*M for _ in range(N)] for _ in range(H)]

for _ in range(H):

  tmp = list()
  for _ in range(N):
    
    tmp.append(list(map(int,input().split())))

  graph.append(tmp)

bfs(graph,distance,visited)

max = 0
zero_flag = False
for h in range(H):
  for n in range(N):
    for m in range(M):
      
      if distance[h][n][m]==0:
        zero_flag = True

      if distance[h][n][m]>max:
        max=distance[h][n][m]
        
if zero_flag:
  print(-1)
else:
  if max == 1:
    print(0)
  else:
    print(max-1)