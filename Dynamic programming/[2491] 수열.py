"""
단순하게 연속해서 증가, 감소하는 개수를 찾아서 더 큰 수를 출력해준다.

N의 최대 크기가 100000이므로, 1차원 for문 2번, max() 2번해서 O(N)으로 해결가능하다.

"""

N = int(input())
data = list(map(int,input().split()))
dp = [0]*N
dp[0] = 1

asc = 0
des = 0

for i in range(1,N):
  
  if data[i]>=data[i-1]:
    dp[i] = dp[i-1]+1
  else:
    dp[i] = 1

asc = max(dp)

dp = [0]*N
dp[0] = 1

for i in range(1,N):
  
  if data[i]<=data[i-1]:
    dp[i] = dp[i-1]+1
  else:
    dp[i] = 1

des = max(dp)

print(max(asc,des))