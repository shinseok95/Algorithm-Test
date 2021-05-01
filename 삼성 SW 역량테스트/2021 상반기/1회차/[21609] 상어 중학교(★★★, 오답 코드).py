"""
21.05.01
삼성 SW 역량평가 2021년 기출문제 -2
풀이 결과 : 틀림
풀이 시간 : 3시간

오답 이유 : 2시간 전에 전체적인 구조는 다 구했는데, 시간초과를 해결하지 못함..

"""

import sys
from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(R,C):

  visited = [[False]*(N+1) for _ in range(N+1)]
  q = deque([(R,C)])
  visited[R][C] = True
  
  block_set = []
  block_normal_set = []

  set_info = [1,0,0,0]

  while q:

    r,c = q.popleft()
    block_set.append((r,c))
    
    if graph[r][c] != 0:
      block_normal_set.append((r,c))

    for i in range(4):
      next_r = r+dr[i]
      next_c = c+dc[i]

      if 1<=next_r<=N and 1<=next_c<=N:
        if not visited[next_r][next_c]:
          if graph[next_r][next_c] == -1:
            continue

          elif graph[next_r][next_c] == -2:
            continue
        
          elif graph[next_r][next_c] == graph[R][C]:
            visited[next_r][next_c] = True
            q.append((next_r,next_c))

            set_info[0]+=1
          
          elif graph[next_r][next_c] == 0:

            visited[next_r][next_c] = True
            q.append((next_r,next_c))

            set_info[0]+=1
            set_info[1]+=1

  if len(block_normal_set) == 0:
    set_info[2] = -1
    set_info[3] = -1
  else:
    block_normal_set.sort(key=lambda x : (x[0],x[1]))
    set_info[2] = block_normal_set[0][0]
    set_info[3] = block_normal_set[0][1]

  return block_set,set_info

def move(C):

  for R in range(N,0,-1):

    if graph[R][C] == -1 or graph[R][C] == -2:
      continue
    
    q = deque([(R,C)])
    cnt = 0

    while q:
      r,c = q.popleft()

      next_r = r+dr[1]
      next_c = c+dc[1]

      if 1<=next_r<=N and 1<=next_c<=N:
        if graph[next_r][next_c] == -2:
          q.append((next_r,next_c))
          cnt+=1
        else:

          if cnt > 0:
            graph[r][c] = graph[R][C]
            graph[R][C] = -2
          break

      else:
        if cnt > 0 :
          graph[N][C] = graph[R][C]
          graph[R][C] = -2
        break

def turn():
  
  next_graph = [[] for _ in range(N)]
  next_graph = [[0]*(N+1)] + next_graph

  for c in range(N,0,-1):
    next_graph[N+1-c].append(0)
    for r in range(1,N+1):
      next_graph[N+1-c].append(graph[r][c])

  return next_graph


N,M = map(int,sys.stdin.readline().split())
graph = [[0]*(N+1)]
result = 0

for _ in range(N):
  graph.append([0]+list(map(int,sys.stdin.readline().split())))

while True:

  set_list = []
  block_list = []

  for r in range(1,N+1):
    for c in range(1,N+1):

      if graph[r][c] == -2 or graph[r][c]==-1:
        continue

      block_set, set_info = bfs(r,c)
      
      if len(block_set) == 1 or set_info[0]-set_info[1] == 0:
        continue

      block_list.append(block_set)
      set_list.append(set_info)

  if len(set_list) == 0:
    break
  
  set_list.sort(key= lambda x : (-x[0],-x[1],-x[2],-x[3]))

  for i in range(len(block_list)):
    if block_list[i][0][0] == set_list[0][2] and block_list[i][0][1] == set_list[0][3]:

      for r,c in block_list[i]:
        graph[r][c] = -2

      result += set_list[0][0]*set_list[0][0]

      for j in range(1,N+1):
        move(j)

      graph = turn()

      for j in range(1,N+1):
        move(j)
      
      break
      
print(result)