"""
로직은 맞은 것 같으나, 파이썬의 느린 특성상 통과하진 못헀다.

pypy3로만 통과해서 뭔가 찝찝한 느낌...
"""

import sys
from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(R,C):

  q = deque([])
  q.append((R,C))

  visited[R][C] = True
  cnt = 0
  total =0

  while q:

    r,c = q.popleft()

    contry.append((r,c))
    cnt += 1
    total += graph[r][c]

    for i in range(4):
      
      next_r = r+dr[i]
      next_c = c+dc[i]

      if 0<=next_r<N and 0<=next_c<N:
        if not visited[next_r][next_c]:
          if left<=abs(graph[r][c]-graph[next_r][next_c])<=right:
            visited[next_r][next_c] = True
            q.append((next_r,next_c))
  
  return cnt,total

N,left,right = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
result = 0

contry = []

while True:
  
  move = False
  visited = [[False]*N for _ in range(N)]
  tmp_graph = [[0]*N for _ in range(N)]

  for i in range(N):
    for j in range(N):

      if visited[i][j]:
        continue

      contry = []
      cnt,total = bfs(i,j)

      if cnt > 1:
        move = True
        avg = total//cnt
        
        for r,c in contry:
          tmp_graph[r][c] = avg
      else:
        tmp_graph[i][j] = graph[i][j]
      
      contry.clear()

  if not move:
    break
  else:
    result+=1
    graph = tmp_graph

sys.stdout.write(str(result))
  