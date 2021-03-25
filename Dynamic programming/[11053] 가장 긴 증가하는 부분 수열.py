"""
[1965] 상자넣기

와 동일한 논리의 문제다

bottom-up 방식으로 P[0:i] 중에 P[i]보다 작은 수의 DP값을 비교해나가며 DP값이 가장 큰 수를 골라서 +1 해주면 된다.

i번째 전까지의 DP값들이 최대값을 보장해주기 때문에, 이 후 DP값 또한 최대값을 보장해준다.

"""

import sys 

N = int(input())
P = [0]+list(map(int,sys.stdin.readline().split()))
dp = [0]*(N+1)
dp[1] = 1

for i in range(2,N+1):
  for j in range(i-1,0,-1):
    
    if P[i]<=P[j]:
      continue
    else:
      if dp[i]<dp[j]:
        dp[i]=dp[j]
  
  dp[i]+=1

print(max(dp))    
