"""
처음에 계속 오답이 떴는데, 알고보니 문제를 잘못이해해서였다.

원래는 코드를 뿌요가 터지는지 체크를 가장 밑에 줄만 했다.

그러나 밑에서 안터지고 위에서 터지는 경우도 존재하였다.

즉, row가 0인 것만 bfs를 돌릴 것이 아니라, row X col을 전부 돌렸어야 했다.

결론 : 문제를 잘 보자!
"""

import sys
from collections import deque

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(r,c):

  ch = graph[r][c]
  q = deque([(r,c)])
  visited[r][c] = True

  while q:

    r,c = q.popleft()
    
    if graph[r][c] != ch:
      continue

    stored.append((r,c))

    for i in range(4):
      next_r = r+dr[i]
      next_c = c+dc[i]
      
      if 0<=next_r<6 and 0<=next_c<12:
        if not visited[next_r][next_c]:
          q.append((next_r,next_c))
          visited[next_r][next_c] = True
  

graph = [[] for _ in range(6)]
result = 0

for _ in range(12):
  
  data = sys.stdin.readline().rstrip()

  graph[0].append(data[0])
  graph[1].append(data[1])
  graph[2].append(data[2])
  graph[3].append(data[3])
  graph[4].append(data[4])
  graph[5].append(data[5])

graph[0].reverse()
graph[1].reverse()
graph[2].reverse()
graph[3].reverse()
graph[4].reverse()
graph[5].reverse()

while True:

  result_flag = False

  for i in range(6):
    for j in range(12):
      if graph[i][j] == '.':
        continue
    
      visited = [[False]*12 for _ in range(6)]
      stored = []

      bfs(i,j)

      if len(stored) < 4:
        continue
      else:

        for k in range(len(stored)):
          r,c = stored[k]
          graph[r][c] = '.'

        result_flag = True
  
  if not result_flag:
    break
  else:
    for i in range(6):
      while graph[i].count('.') != 0:
        graph[i].remove('.')
        
      length = len(graph[i])
      for _ in range(12-length):
        graph[i].append('.')
    result+=1

print(result)

