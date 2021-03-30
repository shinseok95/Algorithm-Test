"""
도저히 점화식이 떠오르지 않아서 다른 사람의 풀이를 봤다.

그리고 LIS라는 알고리즘을 통해 풀 수 있다는 것을 알 수 있었다.

([11053] 가장 긴 증가하는 부분 수열)

우선 선이 엉켜있지 않기 위해서는 순서대로 그 값이 커지면 된다.

예를 들어, 1일때는 1, 2일때는 2, 3일때는 3라면 순서대로 값이 증가하기 때문에 엉켜있지 않게된다.

그러나 만약 1일때는 3, 2일때는 1, 3일때는 2라면 순서대로 증가하지 않기 때문에 선이 엉키게 된다.

그렇다면 전체 전깃줄의 개수에서 가장 긴 증가하는 부분 수열의 크기를 빼주면, 순서대로 증가하지 않는 전깃줄을 빼는 것과 동일하게 된다.
"""

import sys 
N = int(sys.stdin.readline())
data = [0]*(501)
dp = [0]*(501)

for _ in range(N):
  a,b = map(int,sys.stdin.readline().split())

  data[a] = b

for i in range(1,501):

  if data[i] == 0 :
    continue
  
  if dp[i] == 0:
    dp[i] = 1

  for j in range(1,i):
    
    if data[j] == 0:
      continue

    if data[j] <data[i]:
      dp[i] = max(dp[i],dp[j]+1)

print(N-max(dp))