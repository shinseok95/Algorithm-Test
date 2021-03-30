import sys

T = int(sys.stdin.readline())

for _ in range(T):
  
  N = int(sys.stdin.readline())
  coins = [0]+list(map(int,sys.stdin.readline().split()))
  M = int(sys.stdin.readline())

  dp = [[0]*(M+1) for _ in range(N+1)]
  dp[0][0] = 1
  
  for i in range(1,N+1):
    for j in range(M+1):

      if coins[i]<=j:
        dp[i][j] = dp[i][j-coins[i]]+dp[i-1][j]
      else:
        dp[i][j] = dp[i-1][j]
  
  print(dp[N][M])