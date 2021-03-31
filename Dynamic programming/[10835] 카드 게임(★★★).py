"""
나름 잘 풀었다고 생각했는데, 43%에서 계속 틀렸다.
3시간의 고민끝에 결국 다른 사람의 풀이를 봤다.

알고보니 그냥 내 DP 설계가 틀린 것이었다.

나는 DP[왼쪽 카드 번호][오른쪽 카드 번호]로 설계를 해서, DP[i][j]는 i번째 왼쪽 카드와 j번째 오른쪽 카드가 맨 위에 올려져있는 경우를 생각했다.

만약 왼쪽 카드가 오른쪽 카드보다 크다면 max(dp[i][j-1]+R[j],dp[i][j])

작거나 같다면, max(dp[i-1][j-1],dp[i-1][j])를 하면 된다고 생각했으나 반례가 상당히 많았던 것 같다.

다른 사람들은 DP[왼쪽 카드가 남은 개수][오른쪽 카드가 남은 개수]로 설계해서 풀었다.

만약 i=5,j=5라면 왼쪽 카드 5장, 오른쪽 카드 5장이 남은 상태이며,

왼쪽 카드가 오른쪽 카드보다 크다면 max(dp[i][j+1]+R[j],dp[i][j])

작거나 같다면, max(dp[i+1][j+1],dp[i+1][j])로 계산하였다.

아직까지 왜 dp[left][right]일 때, R과 L을 reverse 안해주는 지 모르겠다.

N==7이고, left가 7장 남고 right가 7장 남았으면, 더해야 하는 것은 맨 위의 카드인 R[0] 아닐까?

왜 밑에 카드인 R[7]을 더해주는지 잘 이해가지 않는다..
"""

import sys

N = int(sys.stdin.readline())
L = list(map(int,sys.stdin.readline().split()))+[0]
R = list(map(int,sys.stdin.readline().split()))+[0]

dp = [[0]*(N+1) for _ in range(N+1)]

for left in range(N-1,-1,-1):
  for right in range(N-1,-1,-1):
    if L[left] > R[right]:
      dp[left][right] = max(dp[left][right],dp[left][right+1]+R[right])
    else:
      dp[left][right] = max(dp[left+1][right+1],dp[left+1][right])
print(dp)
print(dp[0][0])