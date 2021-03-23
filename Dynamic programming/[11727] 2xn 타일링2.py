"""
[11726] 2xn 타일링 문제와 동일한 논리의 문제다.

다만, 이전 문제는 단순히 피보나치 수열의 점화식이 나오는 문제였다면, 이번 문제는 한 가지 조건이 더 추가되었다.

2X2 타일이 추가되므로써, 1X2 타일 2개와 구분해줘야한다.

점화식은 다음과 같다.

P(N) = 2*(P(N-2))+P(N-1) (N>=3)
p(N) = 3 (N=2)
P(N) = 1 (N=1)

"""

N = int(input())
cache = [1,3,5]

if N == 1:
  print(1)
elif N == 2:
  print(3)
else:
  for _ in range(2,N):
    cache[2] = 2*cache[0] + cache[1]

    cache[0],cache[1] = cache[1], cache[2]

  print(cache[2]%10007)