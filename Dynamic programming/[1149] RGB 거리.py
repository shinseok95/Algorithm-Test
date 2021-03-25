"""
Bottom up으로 해결 가능한 문제

조건 첫번째는 최솟값을 구해라는 것이고,
조건 두번째는 i번째는 i-1번째와 동일한 열이면 안된다는 것이다.

그렇다면 i-1번째에서 해당 열과 다른 열들 중 가장 작은 수를 i번째의 열과 더해주는 것을 3번 반복해주면 된다.(RGB 3개 열이 있다)

점화식은 다음과 같다

dp[i][0] = min(dp[i-1][1],dp[i-1][2])+P[i-1][0]

dp[i][1] = min(dp[i-1][0],dp[i-1][2])+P[i-1][1]

dp[i][2] = min(dp[i-1][0],dp[i-1][1])+P[i-1][2]

"""

import sys 

N = int(sys.stdin.readline())
P = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

dp = [[0]*3 for _ in range(N+1)]

for i in range(1,N+1):
  
  dp[i][0] = min(dp[i-1][1],dp[i-1][2])+P[i-1][0]
  dp[i][1] = min(dp[i-1][0],dp[i-1][2])+P[i-1][1]
  dp[i][2] = min(dp[i-1][0],dp[i-1][1])+P[i-1][2]

print(min(dp[N]))
  