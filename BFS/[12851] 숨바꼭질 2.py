"""
bfs를 이용해 최단시간을 구하고, 그 방법의 수를 구하는 문제였다.

90% 이상의 뼈대는 30분정도만에 만들 수 있었는데, 나머지 10%의 반례를 찾는데 한시간 넘게 사용한 것 같다.

결론적으로 말하자면, 대부분의 bfs는 중복을 방지하기 위해 queue에 넣기 위해 곧바로 append를 해주지만, 이 문제는 곧바로 append를 해주면 안된다.

왜냐하면 만약 곧바로 append를 해주면, 같은 시간이 걸리지만 경로가 다른 경우가 만들어지지 않기 때문이다

더 자세히 말하자면, 앞서 다른 방법으로 찾아왔지만 결국 같은 지점에 도착할 수 있다면, 이를 중복 처리해버리면 그 경우의 수는 모두 무시가 되는 것이다.

예를 들어, 1->(1+1)->(2*2) 인 경우와 1->(1*2)->(2*2)는 다른 경우의 수로 다뤄야한다.

"""

import sys
from collections import deque

MAX_POINT = 100001

def bfs():
  global cnt,min_time,MAX_POINT

  q = deque()
  q.append((K,0))
  visited[K] = True

  while q:
    n,d = q.popleft()

    visited[n] = True

    if n == N:
      min_time = d
      cnt += 1
      break
      
    if n%2==0:
      if 0<=n//2<MAX_POINT:
        if not visited[n//2]:
          q.append((n//2,d+1))

    if 0<=n-1<MAX_POINT:
      if not visited[n-1]:
        q.append((n-1,d+1))
        
    if 0<=n+1<MAX_POINT:
      if not visited[n+1]:
        q.append((n+1,d+1))
        
  while q:
    n,d = q.popleft()
    
    if n == N and d==min_time:
      cnt+= 1
    
N,K = map(int,sys.stdin.readline().split())

visited = [False]*(MAX_POINT)
min_time = 0
cnt = 0

bfs()

print(min_time)
print(cnt)