"""
21.06.29
삼성 SW 역량평가 2020년 하반기 기출문제 2-2

풀이 결과 : 정답
풀이 시간 : 1시간
"""

import sys
from collections import deque

dr = [0,0,1,-1]
dc = [1,-1,0,0]

def turn(R,C,L):

  global A

  tmp_A = [[0] * L for _ in range(L)]
  
  for r in range(L):
    for c in range(L):
      tmp_A[r][c] = A[R+r][C+c]
  
  for r in range(L):
    for c in range(L):
      A[R+c][C+L-1-r] = tmp_A[r][c]

def ice_beaking():

  global A,length

  beaking_list = []

  for r in range(length):
    for c in range(length):
      cnt = 0

      for i in range(4):
        next_r = r+dr[i]
        next_c = c+dc[i]
        
        if 0<=next_r<length and 0<=next_c<length:
          if A[next_r][next_c] > 0:
            cnt+=1
      
      if cnt < 3 and A[r][c] > 0:
        beaking_list.append((r,c))

  for r,c in beaking_list:
    A[r][c] -= 1

def bfs(R,C):
  
  global A,length,visited

  q = deque([(R,C)])
  visited[R][C] = True
  
  cnt = 1

  while q:

    r,c = q.popleft()

    for i in range(4):
      next_r = r+dr[i]
      next_c = c+dc[i]

      if 0<=next_r<length and 0<=next_c<length:
        if not visited[next_r][next_c]:
          if A[next_r][next_c] > 0:
            visited[next_r][next_c] = True
            cnt+=1
            q.append((next_r,next_c))
  
  return cnt

A = []
order = []
total_ice = 0
max_ice_size = 0

N,Q = map(int,sys.stdin.readline().split())

length = 2**N
visited = [[False]*length for _ in range(length)]

for _ in range(2**N):
  A.append(list(map(int,sys.stdin.readline().split())))

order = list(map(int,sys.stdin.readline().split()))

for l in order:

  if l == 0:
    ice_beaking()
    continue

  L = 2**l
  R,C = 0,0

  while 0<=R<length:
    while 0<=C<length:
      turn(R,C,L)
      C += L
    R += L
    C = 0
  
  ice_beaking()

for r in range(length):
  for c in range(length):
    total_ice += A[r][c]

    if not visited[r][c] and A[r][c] > 0:
      max_ice_size = max(max_ice_size,bfs(r,c))
  
print(total_ice)
print(max_ice_size)
