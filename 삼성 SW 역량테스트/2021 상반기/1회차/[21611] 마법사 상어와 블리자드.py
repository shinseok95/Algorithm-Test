"""

21.04.30

삼성 SW 역량평가 2021년 기출문제 -4

풀이 결과 : 정답
풀이 시간 : 2시간
"""

import sys
from collections import deque

dr = [0,-1,1,0,0]
dc = [0,0,0,-1,1]
dirc = [3,2,4,1]

def ice_breaking(d,s):
  
  global N,graph

  r = (N+1)//2
  c = (N+1)//2

  for i in range(s):    
    next_r = r+dr[d]
    next_c = c+dc[d]

    if 1<=next_r<=N and 1<=next_c<=N:
      graph[next_r][next_c] = 0
      
      r = next_r
      c = next_c
    else:
      break

def push(q):

  global direction

  r = (N+1)//2
  c = (N+1)//2

  for d,s in direction:
    for _ in range(s):
      next_r = r+dr[d]
      next_c = c+dc[d]

      if 1<=next_r<=N and 1<=next_c<=N:
        if len(q) != 0:
          graph[next_r][next_c] = q.popleft()
        else:
          graph[next_r][next_c] = 0

        r = next_r
        c = next_c
    
def pop():

  global direction
  q = deque()

  r = (N+1)//2
  c = (N+1)//2

  for d,s in direction:
    for _ in range(s):
      next_r = r+dr[d]
      next_c = c+dc[d]
      
      if 1<=next_r<=N and 1<=next_c<=N:
        
        if graph[next_r][next_c] != 0:
          q.append(graph[next_r][next_c])
        r = next_r
        c = next_c

  return q

def bomb(q):
  
  global result

  if len(q)==0:
    return False,deque()

  stack = deque([q[0]])
  last = q[0]
  i = 1
  cnt = 1
  flag = False

  while True:

    if i ==len(q):
      break

    if q[i] == last:
      cnt += 1
    else:
      if cnt >= 4:
        flag = True

        for _ in range(cnt):
          stack.pop()
        
        result += cnt*last
        
      cnt = 1
      last = q[i]
    stack.append(q[i])
    i+=1
  
  return flag,stack
  
def change(q):

  if len(q)==0:
    return deque()

  changed_q = deque()
  last = q[0]
  cnt = 1
  i = 1

  while True:
    
    if last != q[i]:
      changed_q.append(cnt)
      changed_q.append(last)
      last = q[i]
      cnt = 1
    else:
      cnt+=1
    
    i+=1

    if i == len(q):
      changed_q.append(cnt)
      changed_q.append(last)
      break
  
  return changed_q

N,M = map(int,sys.stdin.readline().split())
result = 0
graph = [[0]*(N+1)]
magics = []
direction =[]
n = 1
d = 0
sum_cnt = 0

while True:
  sum_cnt+=n

  if sum_cnt<=(N*N)-1:
    direction.append((dirc[d%4],n))
    
    if dirc[d%4] == 1 or dirc[d%4] == 2:
      n+=1
    d+=1

  else:
    direction.append((dirc[d%4],n-1))
    break

for _ in range(N):
  graph.append([0]+list(map(int,sys.stdin.readline().split())))

for _ in range(M):
  d,s = map(int,sys.stdin.readline().split())
  magics.append((d,s))

for d,s in magics:
  flag = True
  ice_breaking(d,s)
  q = pop()
  
  while flag:
    flag, q = bomb(q)

  q = change(q)
  
  push(q)

print(result)