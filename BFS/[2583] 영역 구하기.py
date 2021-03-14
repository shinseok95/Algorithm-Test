from collections import deque

def bfs(graph,visited,m,n):
  
  global M,N,result
  queue = deque([(m,n)])
  count = 0 

  while queue:
    
    r,c = queue.popleft()

    if visited[r][c] == True:
      continue

    visited[r][c] = True

    if graph[r][c] == 0:
      continue

    count += 1

    if 0<=r-1<M:
      queue.append((r-1,c))

    if 0<=r+1<M:
      queue.append((r+1,c))

    if 0<=c-1<N:
      queue.append((r,c-1))

    if 0<=c+1<N: 
      queue.append((r,c+1))

  if count != 0 :
    result.append(count)


M,N,K = map(int,input().split())

graph = [[1]*N for _ in range(M)]
visited = [[False]*N for _ in range(M)]
result = []

for _ in range(K):
  
  c1,r1,c2,r2 = map(int,input().split())

  for i in range(r1,r2):
    for j in range(c1,c2):
      graph[i][j]=0

for i in range(M):
  for j in range(N):
    
    bfs(graph,visited,i,j)

if len(result) != 0 :
  
  result = sorted(result)
  print(len(result))
  
  print(*sorted(result))

else:
  print(0)