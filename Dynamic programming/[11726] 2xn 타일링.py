"""
[1904] 01타일 문제와 동일한 논리의 문제로, 피보나치 수열을 이용하는 문제다.
"""

N = int(input())
cache = [0]*3
cache[0] = 1
cache[1] = 2

if N == 1:
  print(1)
elif N == 2:
  print(2)
else:
  for _ in range(2,N):
    cache[2] = cache[0]+cache[1]

    cache[0],cache[1] = cache[1],cache[2]

  print(cache[2]%10007)