"""
이 문제 또한 2시간정도 고민하다가 결국 다른 사람 풀이를 봤다..

만약 동전의 순서가 중요한 문제였다면 쉽게 풀었을 것 같다.

그러나 순서가 중요하지 않기 때문에, 중복되는 정답을 걸러내기 쉽지 않았다.

그래서 다른 사람의 풀이를 보니 꽤나 간단한 점화식이었다.

dp[n번째 동전][현재 값]

dp[n][k] = dp[n-1][k] (coin[n]<k)

dp[n][k] = dp[n-1][coin[n]-j]+dp[n-1][k] (coin[n]>=k)

첫 번째 점화식은 n번째 코인의 값이 현재 값보다 크다면 n번째 코인을 이용해서 어떻게든 현재값을 만들어내지 못하기 때문에 n번째 코인을 사용하지 않은 경우의 수를 가져온다.

두 번째 점화식은 n번째 코인의 값이 현재 값보다 크기때문에 n번째 코인을 이용해서 현재 값을 만들어 낼 수 있다.

그러므로, 즉, 현재 코인 값을 뺀 값을 만드는 경우의 수 + 현재 코인을 사용하지 않고 만드는 경우의 수를 더해주면 된다.

예를 들어, k==7일 때 현재 코인의 값이 5라면 현재 코인을 사용해서 2를 만드는 경우의 수 + 현재 코인을 이용하지 않고 7을 만드는 경우의 수를 더해주면 된다.


"""

import sys
  
N,K = map(int,sys.stdin.readline().split())

coins = [0]

for _ in range(N):
  coin = int(sys.stdin.readline())

  coins.append(coin)

coins.sort()

dp = [[0]*(K+1) for _ in range(2)]

dp[0][0] = 1

for i in range(1,N+1):
  for j in range(K+1):

    if coins[i]>j:
      dp[1][j] = dp[0][j]
    else:
      dp[1][j] = dp[1][j-coins[i]]+dp[0][j]

  dp[0]=dp[1][:]

sys.stdout.write(str(dp[1][K]))
