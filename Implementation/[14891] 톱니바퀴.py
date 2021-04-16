import sys
from collections import deque

def dfs(n,d):

  if visited[n] :
    return
  
  visited[n] = True
  turn[n] = d

  left_n = n-1
  right_n = n+1

  if 0<=left_n<4:
    if not visited[left_n]:
      if gear[left_n][2] != gear[n][6]:
        dfs(left_n,d*(-1))
  
  if 0<=right_n<4:
    if not visited[right_n]:
      if gear[n][2] != gear[right_n][6]:
        dfs(right_n,d*(-1))
  
gear =[]
for _ in range(4):
  tmp = list(sys.stdin.readline().rstrip())
  tmp = list(map(int,tmp))
  gear.append(deque(tmp))

k = int(sys.stdin.readline())
result = 0

for _ in range(k):
  n,d = map(int,sys.stdin.readline().split())

  turn = [0]*4
  visited =[False]*4

  dfs(n-1,d)

  for i in range(4):
    if turn[i] != 0:
      gear[i].rotate(turn[i])

for i in range(4):

  if gear[i][0] != 0:
    result += 2**i

print(result)

  

