"""

만약 dfs로 접근했다면, N=500이면 2**500의 연산이 필요하다.
즉, bottom up 방식의 dp로 풀어야지 O(N**2)의 시간복잡도로 풀린다.

점화식은 간단하니까 PASS
"""

import sys

N = int(sys.stdin.readline())
data = []
dp = [[0]*i for i in range(1,N+1)]

for _ in range(N):
  data.append(list(map(int,sys.stdin.readline().split())))

for i in range(N):
  for j in range(i+1):
    
    if j == 0:
      dp[i][j] = data[i][j]+dp[i-1][j]
    elif j == i:
      dp[i][j] = data[i][j]+dp[i-1][j-1]
    else:
      dp[i][j] = data[i][j]+max(dp[i-1][j-1],dp[i-1][j])

print(max(dp[N-1]))