"""

bfs를 통한 완전탐색 문제이자 구현 문제였다.

처음엔 이걸 어떻게 구현해야할까 많은 생각을 했는데, bfs를 써서 주위에 1이 있으면 다음 피자의 치즈에서 제거하고, 0이면 q에 넣는 방식을 사용하였다.


"""

import sys
from collections import deque

dr = [1,-1,0,0]
dc = [0,0,1,-1]

R,C = map(int,sys.stdin.readline().split())

pizza = [list(map(int,sys.stdin.readline().split())) for _ in range(R)]
next_pizza = [[0]*C for _ in range(R)]

time_cnt = 0
cheese_cnt = 0

for i in range(R):
  for j in range(C):
    if pizza[i][j] == 1:
      cheese_cnt+=1
    next_pizza[i][j] = pizza[i][j]

while True:

  cheese = 0
  q = deque([(0,0)])
  visited= [[False]*C for _ in range(R)]

  while q:

    r,c = q.popleft()

    for i in range(4):
      next_r = r+dr[i]
      next_c = c+dc[i]

      if 0<=next_r<R and 0<=next_c<C:
        if pizza[next_r][next_c] == 0:
          if not visited[next_r][next_c]:
            q.append((next_r,next_c))
            visited[next_r][next_c] = True
        else:
          if not visited[next_r][next_c]:
            next_pizza[next_r][next_c] = 0
            visited[next_r][next_c] = True
    
  for i in range(R):
    for j in range(C):
      if next_pizza[i][j] == 1:
        cheese +=1
  
  if cheese != 0:
    time_cnt += 1
    cheese_cnt = cheese
    pizza = next_pizza
  else:
    time_cnt += 1
    break

print(time_cnt)
print(cheese_cnt)

        
          
      
    