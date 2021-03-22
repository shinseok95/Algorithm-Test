
"""
대표적인 구간합 문제이다.
전형적인 풀이는 아래와 같고, DP 풀이로 풀어보려고 한다.

T = int(input())

for _ in range(T):
  N = int(input())
  data = list(map(int,input().split()))
  cache = [sum(data[:i]) if i>0 else 0 for i in range(N+1)]

  result = -999999

  for i in range(N):
    for j in range(i+1,N+1):
      tmp = cache[j]-cache[i]
      if result < tmp:
        result = tmp

  print(result)
"""

"""
i번째 수가 포함되는 부분중에서 가장 큰 수를 보장하기 위해서는 i-1번째까지의 합이 양수이면 더해주고, 음수이면 더해주지 않는 방식으로 해결 가능하다.

점화식은 다음과 같다.

P(N) = max(0,P(N-1))+data[N] (N>0)
P(N) = arr[N] (N==0)

수열 P에서 가장 큰 수를 고른다면 (max(P)), 이는 가장 큰 부분합을 의미한다.

"""

T = int(input())

for _ in range(T):
  N = int(input())
  data = list(map(int,input().split()))
  cache = [data[0]]

  for i in range(1,N):
    cache.append(max(0,cache[i-1])+data[i])
  
  print(max(cache))