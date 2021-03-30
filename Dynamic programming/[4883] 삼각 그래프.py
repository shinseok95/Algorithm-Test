"""
엉뚱한 숫자(graph[1][0] 대신 graph[1][1])를 더하고 있어서 생각보다 시간이 오래걸렸다ㅠㅠ

그러나 문제 자체는 쉬운 편이었다.

그냥 주어진 조건으로 이어주면 된다.
"""

import sys

T = 0

while True:
  
  T+=1
  N = int(sys.stdin.readline())

  if N == 0:
    break
  
  graph = []
  dp = [[0]*3 for _ in range(2)]

  for _ in range(N):
    
    graph.append(list(map(int,sys.stdin.readline().split())))
  
  dp[1][0] = graph[0][1]+graph[1][0]
  dp[1][1] = min(dp[1][0],graph[0][1],graph[0][1]+graph[0][2])+graph[1][1]
  dp[1][2] = min(dp[1][1],graph[0][1],graph[0][1]+graph[0][2])+graph[1][2]

  dp[0][0] = dp[1][0]
  dp[0][1] = dp[1][1]
  dp[0][2] = dp[1][2]

  if N==2:
    print("{}. {}".format(T,dp[1][1]))
    continue

  for i in range(2,N-1):
    dp[1][0] = min(dp[0][0],dp[0][1])+graph[i][0]
    dp[1][1] = min(dp[0][0],dp[0][1],dp[0][2],dp[1][0])+graph[i][1]
    dp[1][2] = min(dp[0][1],dp[0][2],dp[1][1])+graph[i][2]

    dp[0][0] = dp[1][0]
    dp[0][1] = dp[1][1]
    dp[0][2] = dp[1][2]

  dp[1][0] = min(dp[0][0],dp[0][1])+graph[N-1][0]
  dp[1][1] = min(dp[0][0],dp[0][1],dp[0][2],dp[1][0])+graph[N-1][1]
  
  print("{}. {}".format(T,dp[1][1]))

  