  
"""
21.06.30
삼성 SW 역량평가 2020년 하반기 기출문제 2-1
풀이 결과 : 정답
풀이 시간 : 3시간


한 문장 잘못적었다가 2시간동안 헤맸다..
멘탈 터지기 전에 꼼꼼하게 코딩하자..
"""


import sys
import math

dr = [0,1,0,-1]
dc = [-1,0,1,0]

sr=[0,-1,1,-1,1,-2,2,-1,1,0]
sc=[-2,-1,-1,0,0,0,0,1,1,-1]
sm=[0.05,0.1,0.1,0.07,0.07,0.02,0.02,0.01,0.01,0.55]

def move(R,C,D):
  
  global A

  r = R + dr[D]
  c = C + dc[D]

  if A[r][c] == 0:
    return r,c
  else:
    scatter(r,c,D)
    return r,c

def scatter(R,C,D):

  global answer, N, A
  total = 0

  # west
  if D == 0:
    for i in range(10):
      next_r = R+sr[i]
      next_c = C+sc[i]
      amount = math.floor(A[R][C] * sm[i])

      if 0<=next_r<N and 0<=next_c<N:
        if i == 9:
          A[next_r][next_c] += (A[R][C]-total)
        else:
          A[next_r][next_c] += amount
          total+=amount
      else:
        if i == 9:
          answer += (A[R][C]-total)
        else:
          answer += amount
          total+=amount
    
  # south
  elif D == 1:
    for i in range(10):
      next_r = R+(sc[i]*-1)
      next_c = C+sr[i]*-1
      amount = math.floor(A[R][C] * sm[i])

      if 0<=next_r<N and 0<=next_c<N:
        if i == 9:
          A[next_r][next_c] += A[R][C]-total
        else:
          A[next_r][next_c] += amount
          total+=amount
      else:
        if i == 9:
          answer += A[R][C]-total
        else:
          answer += amount
          total+=amount

  # east
  elif D == 2:
    for i in range(10):
      next_r = R+sr[i]
      next_c = C+(sc[i]*-1)
      amount = math.floor(A[R][C] * sm[i])

      if 0<=next_r<N and 0<=next_c<N:
        if i == 9:
          A[next_r][next_c] += A[R][C]-total
        else:
          A[next_r][next_c] += amount
          total+=amount
      else:
        if i == 9:
          answer += A[R][C]-total
        else:
          answer += amount
          total+=amount

  # north
  else:
    for i in range(10):
      next_r = R+sc[i]
      next_c = C+sr[i]
      amount = math.floor(A[R][C] * sm[i])

      if 0<=next_r<N and 0<=next_c<N:
        if i == 9:
          A[next_r][next_c] += A[R][C]-total
        else:
          A[next_r][next_c] += amount
          total+=amount
      else:
        if i == 9:
          answer += A[R][C]-total
        else:
          answer += amount
          total+=amount
  
  A[R][C] = 0

N = int(sys.stdin.readline())
A = []
r,c = N//2, N//2
answer = 0
n = 1

for _ in range(N):
  A.append(list(map(int,sys.stdin.readline().split())))

while True :
  
  for i in range(n):
    r,c  = move(r,c,0)

    if r == 0 and c == 0:
      print(answer)
      exit()
      
  for i in range(n):
    r,c = move(r,c,1)

  for i in range(n+1):
    r,c = move(r,c,2)

  for i in range(n+1):
    r,c = move(r,c,3)

  n+=2
