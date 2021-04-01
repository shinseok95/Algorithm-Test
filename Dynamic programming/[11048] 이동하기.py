"""
이번 문제는 메모이제이션을 통해 해결하였다.

최대값인 것을 까먹고 헤매다가 생각보다 많은 시간을 소모했으나, 나름 쉽게 풀린 것 같다.
"""

import sys
sys.setrecursionlimit(10**5)

global N,M,dn,dm

dn = (1,0,1)
dm = (0,1,1)

def dfs(graph,dp,visited,n,m):

  if dp[n][m] != -1:
    return dp[n][m]
  
  result = 0

  for i in range(3):

    next_n = n+dn[i]
    next_m = m+dm[i]

    if 0<=next_n<=N-1 and 0<=next_m<=M-1:

      if not visited[next_n][next_m]:
        
        result = max(result,dfs(graph,dp,visited,next_n,next_m))

        visited[next_n][next_m] = True

      else:
        result = max(result,dp[next_n][next_m])
  
  dp[n][m] = result + graph[n][m]

  return dp[n][m]

N,M = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
dp = [[-1]*M for _ in range(N)]

print(dfs(graph,dp,visited,0,0))
