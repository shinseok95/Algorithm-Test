"""

전형적인 BFS 문제다.

pypy3로는 바로 해결했으나, python3로는 시간초과가 나와서 이리저리 최적화를 해보았지만 해결할 수 없었다.

그래서 찾아보니, 한가지 논리를 추가해주면 됐었다.

현재 땅에서 갈 수 있는 경로가 2가지 이하일 때만 최대 거리가 나타난다는 점이다.

생각해보면, 갈 수 있는 거리가 3이상인 경우라면, 현재 위치에서 출발하는 것보다 한칸 더 멀리서 출발할 수 있는 경우가 존재하는 것이기 때문에 이런 경우는 제외해주면 된다.

"""

import sys
from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(row,col):
  
  q = deque()
  q.append((row,col,0))
  visited = [[False]*C for _ in range(R)]
  visited[row][col] = True

  max_val = 0

  while q:

    r,c,t= q.popleft()
    max_val = t

    for i in range(4):
      next_r = r+dr[i]
      next_c = c+dc[i]

      if 0<=next_r<R and 0<=next_c<C:
        if not visited[next_r][next_c]:
          if graph[next_r][next_c] =='L':

            visited[next_r][next_c] = True
          
            q.append((next_r,next_c,t+1))
  
  return  max_val

R,C = map(int,sys.stdin.readline().split())
graph= []
result = 0

for i in range(R):
  graph.append(list(sys.stdin.readline().rstrip()))

for i in range(R):
  for j in range(C):
    if graph[i][j] == 'W':
      continue
    
    cnt = 0

    for k in range(4):
      next_i = i+dr[k]
      next_j = j+dc[k]

      if 0<=next_i<R and 0<=next_j<C:
        if graph[next_i][next_j] =='L':
          cnt+=1
      
    if cnt>2:
      continue

    max_val = bfs(i,j)

    if result < max_val:
      result = max_val

sys.stdout.write(str(result))
    