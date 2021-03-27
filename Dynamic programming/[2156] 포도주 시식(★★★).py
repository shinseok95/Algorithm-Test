"""
상당히 오랜 시간동안 풀었는데 결국 점화식을 도출하지 못했다.

다른 사람의 풀이를 보니 정말 간단한 점화식이었다

3번 연속으로 포도주를 마시지 못한다면, 경우의 수는 다음과 같다.

(1,2), (1,3), (2,3)

즉, 세 번째 포도주 입장에서 

1. 3번을 안마시고, 1,2번을 마시는 경우

2. 2번을 안마시고, 1,3번을 마시는 경우

3. 1번을 안마시고 2,3번을 마시는 경우의

점화식은 다음과 같다.


dp[i] = data[i] (i=1)
dp[i] = data[i]+data[i-1] (i=2)
dp[i] = max(dp[i-1],dp[i-2]+data[i]+dp[i-3]+data[i]+data[i-1])
(i>2)

정말..점화식 생각해내기 너무 어렵다..
"""

import sys

N = int(sys.stdin.readline())
data = [0]
dp =[0]*(N+1)

for _ in range(N):
  data.append(int(sys.stdin.readline().rstrip()))

if N == 1:
  print(data[1])
elif N == 2:
  print(data[1]+data[2])
else:
  dp[1] = data[1]
  dp[2] = data[1]+data[2]

  for i in range(3,N+1):

    dp[i] = max(dp[i-1],dp[i-2]+data[i],dp[i-3]+data[i]+data[i-1])

  print(dp[N])
