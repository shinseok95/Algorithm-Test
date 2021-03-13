from collections import deque

dr = [-1,-2,-2,-1,1,2,2,1]
dc = [-2,-1,1,2,2,1,-1,-2]

def bfs(graph,visited,my_r,my_c,to_r,to_c):

  global I

  queue = deque([(my_r,my_c)])
  

  while queue:
    
    r,c = queue.popleft()

    if visited[r][c] == True:
      continue
    
    visited[r][c] = True
    
    if r==to_r and c == to_c :
      return
      
    for i in range(8):
      
      if 0<=r+dr[i]<I and 0<=c+dc[i]<I:
        queue.append((r+dr[i],c+dc[i]))
        graph[r+dr[i]][c+dc[i]]=graph[r][c]+1


N = int(input())

for _ in range(N):
  
  I = int(input())

  my_r,my_c = map(int,input().split())

  to_r,to_c = map(int,input().split())

  graph=[[0]*I for _ in range(I)]
  visited = [[False]*I for _ in range(I)]

  bfs(graph,visited,my_r,my_c,to_r,to_c)
  
  print(graph[to_r][to_c])

  
  