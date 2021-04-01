import sys 

N = int(sys.stdin.readline())
P = [0]+list(map(int,sys.stdin.readline().split()))
dp =[0]*(N+1)
dp[1] = P[1]

for i in range(2,N+1):
  max_value = 0
  for j in range(1,i):
    max_value = max(max_value,P[i-j]+dp[j])
  dp[i] = max(max_value,P[i])

print(dp[N])
