"""

전형적인 부분합 문제다.

이 문제는 DP로 푸는 방법과, i번째까지 합을 모두 구한뒤 right-left로 구하는 방법이 있다.

하지만 이 문제의 입력은 100000만개이므로, 
만약 후자의 방법을 사용한다면 시간초과가 뜰 것이다.

그러므로 DP를 사용해야하며, 점화식은 다음과 같다.

P(N) = max(P(i-1)+Data(i),Data(i)) (N>1)
P(N) = Data(N) (N = )
"""

import sys

N = int(sys.stdin.readline())
P = list(map(int,sys.stdin.readline().split()))

dp = [0] * N
dp[0] = P[0]

for i in range(1,N):
  dp[i] = max(dp[i-1]+P[i], P[i])

print(max(dp))