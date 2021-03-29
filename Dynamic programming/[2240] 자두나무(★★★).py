"""
2시간동안 고민해봤지만 결국 풀지 못하고 다른 사람의 풀이를 봤다.

확실히 실버1부터 난이도가 올라간 느낌이다.

우선 이 문제는 3차원 DP를 이용해서 bottom up 방식을 통해 풀어야하는 문제다.

dp[현재 위치][현재 시간][움직인 횟수]로 나눠서 dp를 만들고, 현재 시간에 따른 움직인 횟수의 경우의 수를 모두 계산하면 된다.

예를 들어, 
dp[1][3][2]는 3초가 지났고, 지금까지 2번 움직여서 1번 나무에 있는 경우의 최댓값이다.

이때 최대값을 구하기 위해서 점화식은 다음과 같다.

현재 떨어지는 나무가 1인 경우,

dp[1][i][j] = max(dp[1][i-1][j]+1,dp[2][i-1][j-1]+1)

dp[2][i][j] = max(dp[1][i-1][j-1],dp[2][i-1][j])

현재 떨어지는 나무가 2인 경우,

dp[1][i][j] = max(dp[1][i-1][j],dp[2][i-1][j-1])

dp[2][i][j] = max(dp[1][i-1][j-1]+1,dp[2][i-1][j]+1)

"""

import sys

T,W = map(int,sys.stdin.readline().split())

trees = [0]
dp = [[[0]*(W+2) for _ in range(T+1)] for _ in range(3)]

for _ in range(T):
  tree = int(sys.stdin.readline())
  trees.append(tree)

for i in range(1,T+1):
  for j in range(1,W+2):
    
    if trees[i] == 1:

      dp[1][i][j] = max(dp[1][i-1][j]+1,dp[2][i-1][j-1]+1)

      dp[2][i][j] = max(dp[1][i-1][j-1],dp[2][i-1][j])

    else:

      if i==1 and j==1:
        continue
      
      dp[1][i][j] = max(dp[1][i-1][j],dp[2][i-1][j-1])

      dp[2][i][j] = max(dp[1][i-1][j-1]+1,dp[2][i-1][j]+1)

ans = max(max(dp[1][T]),max(dp[2][T]))

print(ans)

