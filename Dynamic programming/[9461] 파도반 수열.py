"""
아주 간단한 문제였다.
우선 그림을 보고 수를 나열해보고, 규칙을 찾았다.
그리고 그 규칙으로 다음의 점화식을 세울 수 있었다.

P(N) = P(N-2) + P(N-3) (N>=4)
p(N) = 1 (1<=N<=3)
"""

T = int(input())

for _ in range(T):
  N = int(input())
  
  if 1<=N<=3:
    print(1)
  else:
    cache = [1]*(N+1)
    
    for i in range(4,N+1):
      cache[i] = cache[i-2]+cache[i-3]

    print(cache[N])