import sys 

N = int(input())
P = [0]+list(map(int,sys.stdin.readline().split()))
dp = [0]*(N+1)
dp[1] = 1

for i in range(2,N+1):
  for j in range(i-1,0,-1):
    
    if P[i]>=P[j]:
      continue
    else:
      if dp[i]<dp[j]:
        dp[i]=dp[j]
  
  dp[i]+=1

print(max(dp))   