import sys

N,K = map(int,sys.stdin.readline().split())
dp = [[0]*(K+1) for _ in range(N+1)]

for n in range(1,N+1):
  w,v = map(int,sys.stdin.readline().split())

  for W in range(1,K+1):
    if w > W:
      dp[n][W] = dp[n-1][W]
    else:
      dp[n][W] = max(dp[n-1][W-w]+v,dp[n-1][W])

sys.stdout.write(str(dp[N][K]))


