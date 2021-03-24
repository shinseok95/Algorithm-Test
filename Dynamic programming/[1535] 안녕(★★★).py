"""
Greedy로는 도저히 문제가 풀리지 않아서 결국 다른 사람의 풀이를 봤다.
찾아보니 전형적인 0-1 knapsack 문제라고 한다. 알고리즘 전공 수업에서 배운 내용인데, 확실히 복습을 안하니 전혀 기억이 나지 않았다. 

점화식은 다음과 같다.

P[i,w] = P[i-1,w] (wi > w)
p[i,w] = max(vi + P[i-1,w-wi], p{i-1}[w]) (wi<=w)

만약 현재 넣으려는 물건의 무게보다 가방이 작다면, 이전의 값들을 가져오고, 
가방이 더 크다면 현재 물건의 무게를 비웠을 때의 최적값 + 현재 물건의 값과 현재 물건을 넣지 않은 값 중 큰 것을 선택해서 넣는다.

이렇게 진행하다보면 최종적으로 최적의 값을 구할 수 있다.

다음 문제에 적용을 해본다면,

P[n] = P[n-1][l] (L[n] <= l)
P[N] = max(J[n] + P[n-1][l-L[n]], P[n-1][l])

으로 적용 가능하다.

"""

import sys

N = int(sys.stdin.readline())
L = [0] + list(map(int,sys.stdin.readline().split()))
J = [0] + list(map(int,sys.stdin.readline().split()))

dp = [[0]*101 for _ in range(N+1)]

for n in range(1,N+1):
  for l in range(1,101):

    if L[n] >= l :
      dp[n][l] = dp[n-1][l]
    else:
      dp[n][l] = max(J[n]+dp[n-1][l-L[n]],dp[n-1][l])

print(dp[N][100])