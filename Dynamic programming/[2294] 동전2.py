"""

[2293] 동전1 을 참고해서 해결하였다.

동전1의 경우, 경우의 수를 모두 구하는 것이었으나, 이번 문제는 최소 동전 개수를 구하는 것이었다

그래서 동전1에서 구한 원리를 동일하게 이용하였다

동전의 값이 현재 k 값보다 크다면, 이전 동전 값의 개수를 가져오고,  현재 동전의 값이 k 값보다 작거나 같다면 dp[n][k-coin[n]]+1과 dp[n-1][k] 중 더 적은 것을 저장한다.

즉, 현재 동전이 한개 추가됐을 때와 현재 동전이 추가 되지 않았을 때 개수를 비교해서 더 작은 것을 저장한다면, 최소 개수를 보장할 수 있는 것이다.

점화식은 다음과 같다.

dp[n][k] = min(dp[n][k-coin[n]]+1, dp[n-1][k]) (coin[n]<=k)

dp[n][k] = dp[n-1][k]

"""

import sys 

N,K = map(int,sys.stdin.readline().split())

coins = []

for _ in range(N):
  coin = int(sys.stdin.readline())
  coins.append(coin)

coins = list(set(coins))
N = len(coins)

coins = [0]+coins
coins.sort()

dp_1 = [[0]*(K+1) for _ in range(N+1)]
dp_2 = [[0]*(K+1) for _ in range(N+1)]

dp_1[0][0] = 1

for i in range(K+1):
  dp_2[0][i] = i

for n in range(1,N+1):
  for k in range(K+1):
    
    if coins[n] > k:

      dp_1[n][k] = dp_1[n-1][k]
      dp_2[n][k] = dp_2[n-1][k]
    
    else:

      dp_1[n][k] = dp_1[n][k-coins[n]] + dp_1[n-1][k]
      dp_2[n][k] = min(dp_2[n][k-coins[n]]+1,dp_2[n-1][k])

if dp_1[N][K] == 0:
  sys.stdout.write('-1')
else:
  sys.stdout.write(str(dp_2[N][K]))