"""
퇴사를 할 때까지 최대 수익을 거둬야하는 문제다.

각 일자별로 상담일수와 이익이 주어지는데 여기서 키포인트는 만약 오늘의 상담을 할 수 있는 상황이더라도 만약 최대 이익을 보장하지 못한다면 상담을 하지 말아야 한다는 것이다.

이를 보장하기 위해, 퇴사 하루 전부터 N일 전까지 뒤에서부터 차근차근 최대 이익을 보장해주며 진행하면 O(N)의 시간복잡도로 해결 할 수 있다.

예를 들어, 5일에 주어진 상담이 2일이 걸리고 10을 받는다. 
5일의 상담을 하는 경우는 7일의 최대이익 + 10의 이익이 생기며, 5일의 상담을 하지 않는 경우는 6일의 최대이익이 된다.

여기서 둘 중 더 큰 것을 선택하면 5일째의 최대이익을 보장할 수 있다.

점화식은 다음과 같다.

DP[i] = DP[i+1] (i+DAY[i] > N+1)
DP[i] = max(DP[i+DAY[i]]+P[i],DP[i+1]) (i+DAY[i] < N+1)

"""

import sys

N = int(sys.stdin.readline())
dp = [0]*(N+2)
data =[[0,0]]

for i in range(1,N+1):
  t,p = map(int,sys.stdin.readline().split())
  data.append([t,p])

for i in range(N,0,-1):

  if i+data[i][0] > N+1:
    dp[i] = dp[i+1]
  
  else:
    dp[i] = max(dp[i+data[i][0]]+data[i][1],dp[i+1])

print(dp[1])

  
