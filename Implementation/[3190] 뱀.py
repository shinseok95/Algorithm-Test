import sys
from collections import deque

state = 'R'

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
cnt = 0

graph = [[0]*(N+2) for _ in range(N+2)]
turn = deque([])
snake = deque([(1,1)])

for i in range(N+2):
  for j in range(N+2):

    if i == 0 or i == N+1:
      graph[i][j] = 1
    else:
      if j == 0 or j == N+1:
        graph[i][j] =1

for _ in range(K):
  r,c = map(int,sys.stdin.readline().split())
  graph[r][c] = 2

L = int(sys.stdin.readline())

for _ in range(L):
  t, d = sys.stdin.readline().split()
  turn.append((int(t),d))

while True:
  
  if state == 'R':
    if len(turn) > 0 and turn[0][0] == cnt:
      if turn[0][1] == 'L':
        state = 'U'
        snake.appendleft((snake[0][0]-1,snake[0][1]))
      else:
        state = 'D'
        snake.appendleft((snake[0][0]+1,snake[0][1]))
      
      turn.popleft()
    
    else:
      snake.appendleft((snake[0][0],snake[0][1]+1))

  elif state == 'L':
    if len(turn) > 0 and turn[0][0] == cnt:
      if turn[0][1] == 'L':
        state = 'D'
        snake.appendleft((snake[0][0]+1,snake[0][1]))
      else:
        state = 'U'
        snake.appendleft((snake[0][0]-1,snake[0][1]))
      
      turn.popleft()
    
    else:
      snake.appendleft((snake[0][0],snake[0][1]-1))

  elif state == 'U':
    if len(turn) > 0 and turn[0][0] == cnt:
      if turn[0][1] == 'L':
        state = 'L'
        snake.appendleft((snake[0][0],snake[0][1]-1))
      else:
        state = 'R'
        snake.appendleft((snake[0][0],snake[0][1]+1))
      
      turn.popleft()
    
    else:
      snake.appendleft((snake[0][0]-1,snake[0][1]))
  else:
    if len(turn) > 0 and turn[0][0] == cnt:
      if turn[0][1] == 'L':
        state = 'R'
        snake.appendleft((snake[0][0],snake[0][1]+1))
      else:
        state = 'L'
        snake.appendleft((snake[0][0],snake[0][1]-1))
      
      turn.popleft()
    
    else:
      snake.appendleft((snake[0][0]+1,snake[0][1]))

  head_r = snake[0][0]
  head_c = snake[0][1]

  if graph[head_r][head_c] == 2:
    graph[head_r][head_c] = 1
  elif graph[head_r][head_c] == 0:
    graph[head_r][head_c] = 1

    tail_r,tail_c = snake.pop()

    graph[tail_r][tail_c] = 0
  else:

    cnt+=1
    break
  
  cnt+=1

print(cnt)

