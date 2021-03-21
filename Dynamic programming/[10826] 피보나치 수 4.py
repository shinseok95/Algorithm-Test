"""
파이썬이 아니었다면, 문자열로 풀어야함
숫자가 너무 커지기 때문에(10000까지 들어옴)
"""

import sys
sys.setrecursionlimit(10**5)

def dfs(n):

  if cache[n]!=0:
    return cache[n]

  if n==0:
    cache[n]=0

  elif n==1 or n==2:
    cache[n] = 1
  
  else:
    cache[n] = dfs(n-1)+dfs(n-2)
  
  return cache[n]

N = int(input())
cache = [0]*(N+1)
dfs(N)

print(cache[N])