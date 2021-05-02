"""
21.05.02
삼성 SW 역량평가 2021년 기출문제 -2

풀이 결과 : 정답
풀이 시간 : 1시간
"""

import sys
from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def find_set(R,C):

  local_visited = [[False]*N for _ in range(N)]
  q = deque([(R,C)])
  local_visited[R][C] = True
  global_visited[R][C] = True
  
  total_cnt = 1
  rainbow_cnt = 0
  point_r = R
  point_c = C

  while q:

    r,c = q.popleft()
    
    for i in range(4):
      next_r = r+dr[i]
      next_c = c+dc[i]

      if 0<=next_r<N and 0<=next_c<N:
        if not local_visited[next_r][next_c]:
          
          #검은색 블록 or 빈 공간
          if graph[next_r][next_c] == -1 or graph[next_r][next_c] == -2:
            continue
          
          # 무지개 블록
          elif graph[next_r][next_c] == 0:

            local_visited[next_r][next_c] = True
            q.append((next_r,next_c))

            rainbow_cnt+=1
            total_cnt+=1
          
          # 일반 블록 중 동일한 색상의 블록
          else:
            if graph[next_r][next_c] == graph[R][C]:
        
              local_visited[next_r][next_c] = True
              global_visited[next_r][next_c] = True
              q.append((next_r,next_c))

              if next_r< point_r:
                point_r = next_r
                point_c = next_c
              elif next_r == point_r:
                if next_c < point_c:
                  point_r = next_r
                  point_c = next_c   

              total_cnt += 1
  
  if total_cnt >= 2 and total_cnt-rainbow_cnt>0:

    return total_cnt, rainbow_cnt, point_r, point_c
  else:
    return 0,0,0,0

def bomb_set(R,C):
  
  visited=[[False]*N for _ in range(N)]
  q = deque([(R,C)])
  visited[R][C] = True

  block_value = graph[R][C]

  while q:

    r,c = q.popleft()

    graph[r][c] = -2

    for i in range(4):
      next_r = r+dr[i]
      next_c = c+dc[i]

      if 0<=next_r<N and 0<=next_c<N:
        if not visited[next_r][next_c]:
          
          #검은색 블록 or 빈 공간
          if graph[next_r][next_c] == -1 or graph[next_r][next_c] == -2:
            continue
          
          # 무지개 블록
          elif graph[next_r][next_c] == 0:

            visited[next_r][next_c] = True
            q.append((next_r,next_c))
          
          # 일반 블록 중 동일한 색상의 블록
          else:
            if graph[next_r][next_c] == block_value:
              visited[next_r][next_c] = True
              q.append((next_r,next_c))    


def move(c):
  
  for r in range(N-1,-1,-1):
    if graph[r][c] == -1 or graph[r][c] == -2:
      continue
    cnt = 0
    for next_r in range(r+1,N):
      if graph[next_r][c] == -2:
        cnt+=1
      else:
        break
    
    if cnt > 0:
      graph[r+cnt][c] = graph[r][c]
      graph[r][c] = -2

def turn():
  
  tmp_graph = [[0]*N for _ in range(N)]

  for c in range(N-1,-1,-1):
    for r in range(N):
      tmp_graph[N-1-c][r] = graph[r][c]
  
  return tmp_graph

N,M = map(int,sys.stdin.readline().split())
graph = []
result = 0

for _ in range(N):
  graph.append(list(map(int,sys.stdin.readline().split())))

while True:

  # find block set

  block_set = []
  global_visited = [[False]*N for _ in range(N)]
  for r in range(N):
    for c in range(N):
      if graph[r][c] > 0:
        if not global_visited[r][c]:
          total_cnt, rainbow_cnt,point_r,point_c = find_set(r,c)

          if total_cnt > 0:
            block_set.append((total_cnt, rainbow_cnt,point_r,point_c))
  
  block_set.sort(key = lambda x : (-x[0],-x[1],-x[2],-x[3]))

  if len(block_set) == 0:
    break
  
  bomb_set(block_set[0][2],block_set[0][3])
  result += (block_set[0][0]*block_set[0][0])

  for c in range(N):
    move(c)
  graph = turn()
  for c in range(N):
    move(c)

sys.stdout.write(str(result))
  
  
