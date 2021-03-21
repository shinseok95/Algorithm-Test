"""
메모이제이션을 통해 이전에 계산한 값들은 다시 계산되지 않도록 함

https://pacific-ocean.tistory.com/199
"""

import sys 

def dp(n):

  if cache[n] != -1:
    return cache[n]
  
  max_value = 0

  for i in range(n,N+1):

    if i+data[i][0] > N+1:
      continue
    elif i+data[i][0] == N+1:
      max_value = max(max_value,data[i][1])
    else:        max_value = max(max_value,data[i][1]+dp(i+data[i][0]))

  cache[n] = max_value

  return cache[n]


global N
global cache 

N = int(sys.stdin.readline())
data = []
data.append((-1,-1))
cache= [-1]*(N+1)

for _ in range(N):
  d,m = map(int,sys.stdin.readline().split())
  data.append((d,m))

for i in range(1,N+1):
  dp(i)

print(max(cache))
