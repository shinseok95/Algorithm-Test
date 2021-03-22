"""
문제에서 점화식이 주어져있어서 매우 간단하게 풀 수 있었던 문제였다.
"""

def dp(n):

  if cache[n] != 0:
    return cache[n]
  
  if n<2:
    cache[n] = 1
  elif n==2:
    cache[n] = 2
  elif n==3:
    cache[n] = 4
  else:
    cache[n] = dp(n-4)+dp(n-3)+dp(n-2)+dp(n-1)
  
  return cache[n]

global cache
T = int(input())

for _ in range(T):
  
  N = int(input())
  cache = [0]*(N+1)
  
  print(dp(N))