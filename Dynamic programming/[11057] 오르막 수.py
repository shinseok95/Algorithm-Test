mod = 10007
N = int(input())
dp = [[0]*10 if i != 1 else [1]*10 for i in range(N+1)]

if N == 1:
  print(sum(dp[1]))
else:
  for i in range(2,N+1):
    for j in range(10):
      dp[i][j] = sum(dp[i-1][j:])%mod
  
  print(sum(dp[N])%mod)

