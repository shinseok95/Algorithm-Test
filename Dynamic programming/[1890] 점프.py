"""
DFS와 메모이제이션을 통해 해결 가능한 문제였다. 

여기서 키포인트는 이동거리가 0인 경우가 있다는 것이다.
만약 메모이제이션을 통해 방문 처리를 대체했을 경우, 이동거리가 0이 나오면 무한 루프에 빠지게 된다. (r+0,c), (r,c+0) == (r,c)이기 때문이다.

나도 처음에 방문처리를 하지 않고, 메모이제이션 값이 -1이 아닌 경우만 가지치기를 했더니, 메모리 부족이 떴다. 

웬만해서 Top down DP 문제를 풀때도 방문 처리를 해줘야겠다는 생각이 든다.

"""

import sys 
sys.setrecursionlimit(10**5)

def dfs(r,c,N):
  
  global graph,dp

  if (r<0 or r>=N) or (c<0 or c>=N):
    return 0

  if visited[r][c]:
    return dp[r][c] 

  if r == N-1 and c == N-1:
    return 1
  
  if graph[r][c] == 0:
    return 0

  visited[r][c] = True

  dp[r][c] = dfs(r+graph[r][c],c,N) + dfs(r,c+graph[r][c],N)

  return dp[r][c]

N = int(sys.stdin.readline())
graph = [[] for _ in range(N)]
dp = [[-1]*(N) for _ in range(N)]
visited = [[False]*(N) for _ in range(N)]

for i in range(N):
  graph[i] = list(map(int,sys.stdin.readline().split()))

sys.stdout.write(str(dfs(0,0,N)))