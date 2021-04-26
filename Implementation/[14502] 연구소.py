import sys
from collections import deque
from itertools import combinations

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(R,C):
  
  global graph,visited, N,M

  q = deque()
  q.append((R,C))
  visited[R][C] = True

  cnt = 0
  
  while q:
    r,c = q.popleft()

    for i in range(4):
      next_r = r+dr[i]
      next_c = c+dc[i]

      if 0<=next_r<N and 0<=next_c<M:
        if graph[next_r][next_c] == 0:
          if not visited[next_r][next_c]:
            cnt += 1
            visited[next_r][next_c] = True
            q.append((next_r,next_c))

  return cnt

N,M = map(int,sys.stdin.readline().split())

graph = []
v_list = []
empty_list = []

zero_cnt = 0
min_cnt = sys.maxsize

for i in range(N):
  graph.append(list(map(int,sys.stdin.readline().split())))

  for j in range(M):

    if graph[i][j] == 0:
      empty_list.append((i,j))
      zero_cnt += 1
    
    elif graph[i][j] == 2:
      v_list.append((i,j))
    
wall_list = list(combinations(empty_list,3))

for wall in wall_list:

  visited = [[False]*M for _ in range(N)]
  cnt = 0

  graph[wall[0][0]][wall[0][1]] = 1
  graph[wall[1][0]][wall[1][1]] = 1
  graph[wall[2][0]][wall[2][1]] = 1

  for r,c in v_list:
    cnt += bfs(r,c)
  
  graph[wall[0][0]][wall[0][1]] = 0
  graph[wall[1][0]][wall[1][1]] = 0
  graph[wall[2][0]][wall[2][1]] = 0
  
  min_cnt = min(min_cnt,cnt)

print(zero_cnt-min_cnt-3)