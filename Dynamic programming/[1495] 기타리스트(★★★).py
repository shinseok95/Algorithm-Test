"""
처음엔 DFS로 접근하려고 했다. 하지만 모양이 Plus,minus로 이진 트리였기 때문에, 시간 복잡도는 O(2**n)이 되므로 최대 연산 횟수는 최대 2**100나 된다.

즉, DFS로 아무리 가지치기를 하더라도 시간초과가 뜰 수 밖에 없다.

그래서 DP를 고민했지만, Plus, minus이고 N=100, M=1000이니까 2차원 리스트를 사용할 수 있겠다는 아이디어 외에는 도저히 다른 아이디어가 생각나지 않았다.

그리고 3시간동안 고민하다가 결국 다른 사람의 풀이를 봤다.

2차원 리스트까지는 맞았지만, 다른 방식의 DP로 접근해야했다.

DP[N+1][M+1]로 리스트를 선언하고,
n번째 노래에서 볼륨 m이 가능한가를 체크해야한다.

즉, DP[N번째 곡에서][볼륨 M이 가능한다]라고 해석할 수 있다.

dp[n][m]이 True라면 다음과 같은 점화식이 도출된다.

dp[n+1][m+V[n]] = True (m+V[n]<=M)
dp[n+1][m-V[n]] = True (m-V[n]>=0)

이렇게 n을 0부터 N-1까지 반복하다보면 N번째에 가능한 볼륨한 m에는 True가 되어있을 것이고, 최종적으로 dp[N]의 모든 열을 체크해서 True 인 것 중 가장 큰 것을 반환하면 된다.

 
정말 어려웠던 문제였다..
"""

import sys
sys.setrecursionlimit(10**5)

N,S,M = map(int,sys.stdin.readline().split())

V = list(map(int,sys.stdin.readline().split()))

dp = [[False] * (M+1) for _ in range(N+1)]
dp[0][S] = True

result = -1

for i in range(N):
  for j in range(M+1):
    
    if dp[i][j]:

      if j+V[i] <=M:
        dp[i+1][j+V[i]] = True
    
      if j-V[i] >=0:
        dp[i+1][j-V[i]] = True

for i in range(M+1):
  
  if dp[N][i]:
    result = max(result,i)

print(result)
      