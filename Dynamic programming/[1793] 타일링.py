"""

말장난이 너무 심한 문제이다
2X0일 때는 채울 타일이 없으니 모두 채워진 것으로 친다.
즉, n==0일때, dp[0]은 1이라는 것이다.

그리고 n이 1 이상이 되는 순간 채울 타일이 생겼으니 dp[0]은 0이 된다.

흠... 너무 말장난이다..

그리고 이 문제는 데이터가 몇 개 들어올지도, breaking point도 주지 않는다.
처음보는 케이스라서 어떻게 입력받아야지 할지 몰라서 못풀었으나, 질문 게시판에 입력받는 방법이 나와있었다.

흠..여러모로 생각이 많아지는 문제다

"""
"""
import sys

dp = [0]*251
dp[0] = 0
dp[1] = 1
dp[2] = 3

for i in range(3,251):
  dp[i] = dp[i-2]*2 + dp[i-1]

for n in map(int, sys.stdin.read().split()):

  if n == 0 :
    print(1)
  else:
    print(dp[n])

"""
dp = [0]*251
dp[0] = 0
dp[1] = 1
dp[2] = 3

for i in range(3,251):
  dp[i] = dp[i-2]*2 + dp[i-1]

while True:
    try: 
      n = int(input())

      if n == 0 :
        print(1)
      else:
        print(dp[n])
    
    except: break