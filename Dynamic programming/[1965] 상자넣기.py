"""
자신보다 이전에 가장 많은 자식을 품고 있는 박스를 고르는 것이 키포인트다.

왜냐하면, 이 문제는 박스를 품을 때, 그 차이까지 고려하는 것이 아닌 단순히 품기만 한다.

즉, 이전에 자신보다 작은 박스 중 가장 많은 박스를 품고있는 것을 고르는 것이 최선인 것이다.

"""

import sys 

N = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split()))
dp = [0]*N

for i in range(1,N):
  for j in range(i-1,-1,-1):
    
    if data[j]<data[i]:
      dp[i] = max(dp[j]+1,dp[i])

print(max(dp)+1)