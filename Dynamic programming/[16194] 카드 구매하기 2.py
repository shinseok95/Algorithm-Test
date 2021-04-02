import sys

N = int(sys.stdin.readline())
P = [0]+list(map(int,sys.stdin.readline().split()))
dp = [0]*(N+1)

for i in range(1,N+1):
  min_value = sys.maxsize
  for j in range(1,i+1):
    value = dp[i-j]+P[j]

    if min_value > value:
      min_value = value
  dp[i] = min_value

print(dp[N])