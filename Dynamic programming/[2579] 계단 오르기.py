"""
거의 처음으로 깔끔하게 풀어본 DP문제였다. 

우선 이 문제는 Top-down 문제(memorization)으로 접근해야한다.

가장 마지막 계단을 무조건 밟아야하는 것을 힌트로, 마지막 계단에서 1칸 전과 2칸 전으로 나눠서 재귀적으로 접근한다.

이 때, 그래프를 그려보면 최적 부분 구조를 이루는 것을 알 수 있으며, 또한 중복되는 부분 문제가 존재한다는 것을 알 수 있다.

"""

import sys 
sys.setrecursionlimit(10**5)

def dp(n):

  if cache[n] != -1:
    return cache[n]

  if n == 0:
    cache[n] = 0
  elif n == 1:
    cache[n] = data[1]
  elif n == 2:
    cache[n] = data[1]+data[2]
  else:
    
    left = dp(n-2)
    right = data[n-1]+dp(n-3)

    cache[n] = max(left,right)+data[n]
  
  return cache[n]

global cache,data

N = int(sys.stdin.readline())
data = [0]
cache = [-1]*(N+1)

for _ in range(N):
  data.append(int(sys.stdin.readline()))

sys.stdout.write(str(dp(N)))
