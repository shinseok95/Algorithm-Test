"""

21.07.02
삼성 SW 역량평가 2020년 하반기 기출문제 1-1
풀이 결과 : 정답
풀이 시간 : 30분

이전에 풀어본 문제라서 빨리 해결할 수 있었다.

deque의 rotate 함수는 정말 좋은 것 같다
"""

import sys
from collections import deque

def move():
  global cb, robot,N,K
  cnt = 0

  # step 1
  cb.rotate(1)
  robot.rotate(1)

  # step 2
  if robot[N-1]:
    robot[N-1] = False
  
  # step 3
  if robot[N-2] and cb[N-1] > 0:
    robot[N-2] = False
    cb[N-1] -= 1

  for i in range(N-3,-1,-1):
    if robot[i] and not robot[i+1] and cb[i+1] > 0:
      robot[i] = False
      robot[i+1] = True
      cb[i+1] -= 1
  
  # step 4
  if cb[0] > 0:
    cb[0] -= 1
    robot[0] = True
  
  # step 5
  for i in range(2*N):
    if cb[i] == 0:
      cnt += 1

  return cnt

N,K = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
cb = deque(A)
robot = deque([False]*2*N)
step = 1

while True:
  cnt = move()
  if cnt >= K:
    break
  else:
    step += 1

print(step)
