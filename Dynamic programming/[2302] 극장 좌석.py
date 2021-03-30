"""
오랜만에 내 힘으로 푼 DP 문제다.

처음에는 이 문제를 어떻게 해결할까 고민을 하다가, 일반 좌석은 양쪽 좌우로만 움직일 수 있다는 제한 조건을 통해 bottom up을 이용하면 해결할 수 있겠다는 생각이 들었다.

예를 들어, 만약 1자리만 있다면 경우의 수는 한가지일 것이다.

그리고 2자리만 있다면, 경우의 수는 12, 21로 두 가지 일 것이다.

마지막으로 3자리만 있다면, 경우의 수는 '1+32'+'12+3','21+3'으로 세 가지 일것이다.

즉, dp[i]=dp[i-1]+dp[i-2]라는 점화식이 도출된다.

하지만 우리는 vip라는 제한사항이 있다. 만약 추가되는 좌석이 vip좌석이라면 무조건 그 좌석에만 앉아야하므로 dp[i]=dp[i-1]가 된다.

또한 vip+1번째 좌석 또한 vip좌석이 고정되어있기에, dp[i]=dp[i-1]로 해줘야한다. 왜냐하면 vip좌석과 현재 좌석이 바뀔 수 없기 때문이다.

최종적으로 점화식은 다음과 같다.

dp[i] = dp[i-1]+dp[i-2] (not vip or vip+1)

dp[i] = dp[i-1](vip or vip+1)

dp[i] = 1 (i=0 or 1)


"""

import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

vip = []
dp = [0]*(N+1)
dp[0] = 1
dp[1] = 1

for i in range(M):
  seat = int(sys.stdin.readline())
  vip.append(seat)
  vip.append(seat+1)

vip = set(vip)

for i in range(2,N+1):
  
  if i in vip:
    dp[i] = dp[i-1]
  else:
    dp[i] = dp[i-1]+dp[i-2]

print(dp[N])