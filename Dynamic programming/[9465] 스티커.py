"""
생각보다 점화식을 생각해내는데 시간이 오래 걸렸다.
정답 비율이 49%라서 쉬울 줄 알았는데, 역시 내가 부족한가보다.

우선 문제에서 스티커를 떼어내면 그 스티커의 왼쪽,오른쪽,위,아래를 못쓴다고 한다.
그렇다면 최대 점수는 대각선으로만 더해가면 도출할 수 있지않을까?

하지만 아니었다. 만약 대각선이 아니더라도 i-2의 같은 행에 있는 스티커 또한 고를 수 있었다.

그렇다면 bottom up 방식으로 왼쪽에서 오른쪽으로 최대값을 보장해나가면서 i-1번째 대각선과 i-2번째 같은 행의 값의 최대값을 골라서 더해가면 될 것 같다.

점화식은 다음과 같다.

P[0][i] = max(P[1][i-1], P[0][i-2]) + Data[0][i]

P[1][i] = max(P[0][i-1], P[1][i-2]) + Data[1][i]

"""

import sys 

T = int(input())

for _ in range(T):
  N = int(sys.stdin.readline())

  data =[]
  dp = [[0,0,0],[0,0,0]]

  for _ in range(2):
    data.append(list(map(int,sys.stdin.readline().split())))

  for i in range(N):

    if i==0:
      dp[0][0] = data[0][i]    
      dp[1][0] = data[1][i]
    
    elif i==1:
      dp[0][1] = dp[1][0]+data[0][i]
      dp[1][1] = dp[0][0]+data[1][i]

    else:
      dp[0][2] = max(dp[1][1], dp[1][0])+data[0][i]
      dp[1][2] = max(dp[0][1], dp[0][0])+data[1][i]

      dp[0][0] = dp[0][1]
      dp[1][0] = dp[1][1]

      dp[0][1] = dp[0][2]
      dp[1][1] = dp[1][2]
  
  print(max(dp[0][2],dp[1][2]))
      


