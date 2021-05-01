"""

21.04.30

삼성 SW 역량평가 2021년 기출문제 -3

풀이 결과 : 정답
풀이 시간 : 1시간
"""

import sys

dr = [0,0,-1,-1,-1,0,1,1,1]
dc = [0,-1,-1,0,1,1,1,0,-1]

def move(d,s):

  global clouds,N,visited

  for i in range(len(clouds)):
    next_r = clouds[i][0]+(dr[d]*s)
    next_c = clouds[i][1]+(dc[d]*s)
    
    if next_r<1:
      while next_r<1:
        next_r+=N
    elif next_r>N:
      while next_r>N:
        next_r-=N

    if next_c<1:
      while next_c<1:
        next_c+=N
    elif next_c>N:
      while next_c>N:
        next_c-=N

    clouds[i][0] = next_r
    clouds[i][1] = next_c
    
    visited[next_r][next_c] = True

def water_copy(r,c):
  
  global A,N

  for i in range(1,9):
    if i%2!=0:
      continue
    
    next_r = r+dr[i]
    next_c = c+dc[i]

    if 1<=next_r<=N and 1<=next_c<=N:
      if A[next_r][next_c] > 0:
        A[r][c] += 1
    
N,M = map(int,sys.stdin.readline().split())

A = [[0]*(N+1)]
moving = []
clouds = [[N,1],[N,2],[N-1,1],[N-1,2]]
visited = [[False] * (N+1) for _ in range(N+1)]

for _ in range(N):
  A.append([0]+list(map(int,sys.stdin.readline().split())))
for _ in range(M):
  d,s = map(int,sys.stdin.readline().split())
  moving.append((d,s))

for d,s in moving:
  move(d,s)

  for r,c in clouds:
    A[r][c] += 1
  for r,c in clouds:
    water_copy(r,c)

  clouds = []

  for r in range(1,N+1):
    for c in range(1,N+1):
      if A[r][c] >= 2:
        if not visited[r][c]:
          clouds.append([r,c])
          A[r][c] -= 2
        else:
          visited[r][c] = False

result = 0

for r in range(1,N+1):
  for c in range(1,N+1):
    result+=A[r][c]

sys.stdout.write(str(result))