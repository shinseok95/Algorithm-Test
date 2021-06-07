"""

30분 고민하다가 답을 모르겠어서, 다른 사람의 아이디어를 확인하였다.

Best First Search를 이용한 문제다.
검은 방을 흰색 방으로 바꾼 횟수를 기준으로 priority queue에 넣고, 그 수가 적은 것을 기준으로 먼저 길을 찾는다.

그렇게 되면, 가장 적은 횟수를 보장하며 길을 찾게 된다.
"""

import sys
from heapq import heappush, heappop

dr = (0,1,0,-1)
dc = (1,0,-1,0)

def bfs():
  
  q = []
  heappush(q,(0,0,0))
  visited = [[False]*N for _ in range(N)]
  visited[0][0] = True

  while q:
    cnt, r, c= heappop(q)

    if r== N-1 and c == N-1:
      return cnt
    
    for i in range(4):
      next_r = r+dr[i]
      next_c = c+dc[i]

      if 0<=next_r<N and 0<=next_c<N:
        if not visited[next_r][next_c]:
          visited[next_r][next_c] = True
          
          if graph[next_r][next_c] == 0:
            heappush(q,(cnt+1,next_r,next_c))
          else:
            heappush(q,(cnt,next_r,next_c))

N = int(sys.stdin.readline())
graph = []

for _ in range(N):
  line = list(sys.stdin.readline().rstrip())
  graph.append(list(map(int,line)))

result = bfs()

sys.stdout.write(str(result))