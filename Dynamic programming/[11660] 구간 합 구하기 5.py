"""
이 문제의 답을 도출하는 것은 그렇게 어렵진 않았다.

기존에 1차원 리스트에서 구간합을 구하듯이 구한 후, 행만큼 더하면 된다

그러나 문제는 파이썬에서 시간초과가 나온다.
M이 최대 100,000 , N이 1024이므로 최대 1억번의 연산을 하게되고, 즉 O(N^2)인 알고리즘을 수정해야했다.

그래서 DP를 활용한 다른 방법을 생각해냈다.

우선 DP[i][j]는 가로가 i, 세로가 j인 사각형의 합을 나타내고, 구간합은 이 사각형의 차를 이용해서 구하는 것이다.

예를 들어, (2,2), (3,4)를 구한다면,
(3,4)인 사각형 - (1,3)인 사각형 - (3,1)인 사각형 + (1,1)인 사각형
으로 구할 수 있다.

마지막에 (1,1)인 사각형의 값을 더해준 것은 앞서 두 번의 뺄셈으로 인해서 두번 빼졌기 때문이다.

점화식은 다음과 같다.

DP[x2][y2] - DP[x1-1][y2] - DP[x2][y1-1]+DP[x1-1][y1-1]

"""

import sys 

N,M = map(int,sys.stdin.readline().split())
graph = []
dp = [[0]*(N+1) for _ in range(N+1)]

for i in range(N):
  graph.append(list(map(int,sys.stdin.readline().split())))

  for j in range(1,N+1):
    dp[i+1][j] = dp[i+1][j-1]+dp[i][j]+graph[i][j-1] - dp[i][j-1]

for _ in range(M):
  x1,y1,x2,y2 = map(int,sys.stdin.readline().split())

  if x1==x2 and y1==y2:
    print(graph[x1-1][y1-1])
    continue
  
  result = dp[x2][y2]-dp[x1-1][y2]-dp[x2][y1-1]+dp[x1-1][y1-1]
  
  sys.stdout.write(str(result)+'\n')
