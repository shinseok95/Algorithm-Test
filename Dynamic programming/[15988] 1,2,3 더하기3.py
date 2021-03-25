mod = 1000000009
dp =[0]*(1000001)

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4,1000001):
    dp[i] = (dp[i-1]+dp[i-2]+dp[i-3])%mod

T = int(input())

for _ in range(T):
  N = int(input())

  if N == 1:
    print(1)
  elif N==2:
    print(2)
  elif N==3:
    print(4)
  else:
    print(dp[N])
      