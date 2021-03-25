"""

전형적인 Top down DP문제다.
물론 완전탐색으로 구해도 되지만, 그런 경우 1초의 시간 복잡도를 충족하지 못한다.

많은 부분이 중복되기 때문에, 메모이제이션을 활용해야한다.

그런데 생각보다 시간이 많이 걸렸다.
점화식을 생각해낸 건 그리 많은 시간이 걸리진 않았는데, 구현에서 계속 헷갈려서 그런 것 같다.

0부터 시작해서 점프 길이에 따라 재귀적으로 접근하고, 그 중 가장 적은 값을 DP에 저장하면 된다.

점화식은 아래와 같다

P[i] = min(P[i],jump(n+i)+1) 


아래처럼 bottom-up 방식으로 푼 풀이도 있으니 참고하자(더 좋아보인다))

N = int(input())
li = list(map(int, input().split()))
dp = [N+1]*N
dp[0] = 0
for i in range(N):
    for j in range(1, li[i]+1):
        if i+j >= N:
            break
        dp[i+j] = min(dp[i+j], dp[i]+1)
print(dp[N-1] if dp[N-1] != N+1 else -1)
"""

import sys 
sys.setrecursionlimit(10**5)
def jump(n):

  if n==N:
    dp[n] = 0
    return dp[n]

  for i in range(1,A[n]+1):
    
    if (n+i)>N:
      break
    
    if A[n+i] == 0:
      continue

    if dp[n+i] != 1001:
      dp[n] = min(dp[n],dp[n+i]+1)
    else:
      dp[n] = min(dp[n],jump(n+i)+1)
  
  return dp[n]

global N,A,dp

N = int(sys.stdin.readline())
A = [0]+list(map(int,sys.stdin.readline().split()))

dp = [1001]*(N+1)

jump(1)

if dp[N] == 1001:
  print(-1)
else:
  print(dp[1])
