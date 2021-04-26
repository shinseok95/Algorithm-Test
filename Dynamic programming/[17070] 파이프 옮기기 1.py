"""
생각보다 시간 엄청 걸렸다

처음에는 dfs로 풀다가 시간초과가 나는 것을 확인하고 DP 문제임을 알 수 있었다.

그런데 dp 점화식을 세울 때, 피곤해서 그런지 생각을 많이 하지않고 계속 코드를 고치다보니 시간이 많이 걸린 것 같다.

우선 가로,세로,대각선의 상태를 나눠서 3차원의 리스트를 만들었다.

가로인 경우, c-1에서 가로와 대각선인 경우를 더해주면 되고,
세로인 경우, r-1에서 세로와 대각선인 경우를 더해주면 되고,
대각선인 경우, r-1,c-1에서 가로와 세로 그리고 대각선을 더해주면 된다.

여기서 주의해야 할 점은 벽이 있는지 확인하는 것이다.

예를 들어, 현재 r,c의 경우의 수를 구하려고 할 때, r,c에 벽이 있으면 가로,세로,대각선 모두의 경우의 수는 0이 된다.

또한 r-1,c or r,c-1에 벽이 있는 경우에는 대각선의 경우의 수가 0이 된다.


"""

import sys

N = int(sys.stdin.readline())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dp = [[[0]*N for _ in range(N)] for _ in range(3)]
wall = [[False] * N for _ in range(N)]

for r in range(N):
  for c in range(N):
    if graph[r][c] == 1:
      wall[r][c] = True

dp[0][0][1] = 1

for r in range(N):
  for c in range(2,N):

    if r == 0 :
      if not wall[r][c]:
        dp[0][r][c] = dp[0][r][c-1]

    else:
      if not wall[r][c]:
        dp[0][r][c] = dp[0][r][c-1]+dp[2][r][c-1]

      if not wall[r][c]:
        dp[1][r][c] = dp[1][r-1][c]+dp[2][r-1][c]
      
      if not wall[r][c] and not wall[r-1][c] and not wall[r][c-1]:
        dp[2][r][c] = dp[0][r-1][c-1] + dp[1][r-1][c-1] + dp[2][r-1][c-1]

sys.stdout.write(str(dp[0][N-1][N-1]+dp[1][N-1][N-1]+dp[2][N-1][N-1]))
