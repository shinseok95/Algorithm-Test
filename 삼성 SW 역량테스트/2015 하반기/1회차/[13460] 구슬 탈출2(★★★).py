"""
21.05.01
삼성 SW 역량평가 2015년 하반기 기출문제 -1
풀이 결과 : 해결못함
풀이 시간 : 2시간
오답 이유 : 애초에 접근을 잘못했음
하나하나 움직여주는 방식으로 했는데, 알고보니 bfs로 접근했어야 했음

"""

import sys
from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def move(r,c,d):
  
  cnt = 0
  
  while graph[r+dr[d]][c+dc[d]] != '#' and graph[r][c] != 'O':
    
    r += dr[d]
    c += dc[d]
    cnt+=1
  
  return r,c,cnt

def bfs(red_r,red_c,blue_r,blue_c,count):

  q = deque([(red_r,red_c,blue_r,blue_c,count)])
  visited = [[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
  visited[red_r][red_c][blue_r][blue_c] = True

  while q:

    rr,rc,br,bc,cnt = q.popleft()

    if cnt > 10:
      break

    for i in range(4):

      next_rr,next_rc,r_c = move(rr,rc,i)
      next_br,next_bc,b_c = move(br,bc,i)

      if graph[next_br][next_bc] != 'O':
        if graph[next_rr][next_rc] == 'O':
          print(cnt)
          return

        if next_rr == next_br and next_rc == next_bc:
          if r_c > b_c:
            next_rr -= dr[i]
            next_rc -= dc[i]
          else:
            next_br -= dr[i]
            next_bc -= dc[i]
      
        if not visited[next_rr][next_rc][next_br][next_bc]:
          visited[next_rr][next_rc][next_br][next_bc] = True
          q.append((next_rr,next_rc,next_br,next_bc,cnt+1))
  
  print(-1)

N,M = map(int,sys.stdin.readline().split())
graph = []

for _ in range(N):
  graph.append(list(sys.stdin.readline().rstrip()))

for r in range(N):
  for c in range(M):
    if graph[r][c] == 'R':
      red_r = r
      red_c = c
    elif graph[r][c] == 'B':
      blue_r = r
      blue_c = c

bfs(red_r,red_c,blue_r,blue_c,1)