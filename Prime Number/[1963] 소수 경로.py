"""
풀긴 풀었는데, 지저분하게 푼 것 같다..
"""

import sys
from collections import deque

INF = int(1e9)

def bfs(prime, visited, begin,end):
  q = deque()
  q.append((0,begin))
  visited[begin] = True
  min_cnt = INF

  while q:
    cnt, n = q.popleft()

    for i in range(4):
      tmp_n = list(str(n))
      for j in range(10):
        tmp_n[3-i]=str(j)
        next_n = int("".join(tmp_n))

        if 1000<=next_n<10000 and not visited[next_n] and prime[next_n]:
          if next_n == end:
            min_cnt = min(min_cnt,cnt+1)
          else:
            visited[next_n] = True
            q.append((cnt+1,next_n))

  return min_cnt
            
prime = [True for i in range(10000)]

for i in range(2,int(10000**0.5)):
  if prime[i] == True:
    j = 2

    while i*j < 10000:
      prime[i*j] = False
      j += 1

T = int(sys.stdin.readline())
ans = []
for _ in range(T):
  begin, end = map(int,sys.stdin.readline().split())

  if begin == end :
    ans.append(0)
    continue
  visited = [False for i in range(10000)]
  res = bfs(prime,visited,begin,end)

  if res == INF:
    ans.append('Impossible')
  else:
    ans.append(res)

for i in range(T):
  print(ans[i])