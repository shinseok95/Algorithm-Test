from collections import deque

dr = [-2,-2,0,0,2,2]
dc = [-1,1,-2,2,-1,1]

def bfs(dist,visited,r1,c1,r2,c2):
  
  global N
  queue = deque([(r1,c1)])
  visited[r1][c1] = True

  while queue:
    
    r,c = queue.popleft()

    if r==r2 and c==c2:
      break
    
    for i in range(6):

      nr = r+dr[i]
      nc = c+dc[i]

      if 0<=nr<N and 0<=nc<N:
        if not visited[nr][nc]:
          
          queue.append((nr,nc))
          dist[nr][nc]=dist[r][c]+1
          visited[nr][nc]=True

N = int(input())
r1,c1,r2,c2 = map(int,input().split())

dist = [[0]*N for _ in range(N)]
visited = [[False]*N for _ in range(N)]

bfs(dist,visited,r1,c1,r2,c2)

if dist[r2][c2] == 0:
  print(-1)
else:
  print(dist[r2][c2])