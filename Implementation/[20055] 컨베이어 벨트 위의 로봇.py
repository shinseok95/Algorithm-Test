"""

한시간 넘게 고생해서 풀었더니, 컨베이어 벨트를 구현하는 방법이 여러가지 있었다..

belt = belt[-1:]+belt[:-1]

또는

belt.rotate(1) 

으로 하면 한칸식 움직였다.

또한, 다른 사람들은 robot을 True False로 다루는 것을 알 수 있었다.

역시 구현 또한 많이 풀어봐야하는 것 같다.
"""

import sys

N,K = map(int,sys.stdin.readline().split())
belt = [-1]+list(map(int,sys.stdin.readline().split()))
robot = []

cnt = 1

left = 1
right = N

while True:

  if left == 1:
    left = (N*2)
  else:
    left -= 1
  
  if right == 1:
    right = (N*2)
  else:
    right -= 1

  if len(robot) > 0 and robot[0] == right:
    del robot[0]

  for i in range(len(robot)):
    
    now = robot[i]
    
    if now == (N*2):
      if i == 0 :
        if belt[1] != 0:
          now = 1
          belt[1] -= 1
      else:
        if robot[i-1] != 1 and belt[1] != 0:
          now = 1
          belt[1] -= 1

    else:
      if i == 0 :
        if belt[now+1] != 0:
          now +=1
          
          belt[now] -= 1
      else:
        if robot[i-1] != now+1 and belt[now+1] != 0:
          now += 1
          belt[now] -= 1

    robot[i] = now
  
  if len(robot) > 0 and robot[0] == right:
    del robot[0]
  
  if belt[left] != 0:
    robot.append(left)
    belt[left]-=1

  if belt.count(0) >= K:
    break
  else:
    cnt+=1

print(cnt)