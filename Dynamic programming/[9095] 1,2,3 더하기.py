"""
[1904] 01타일
[2193] 이친수와 비슷한 문제이다.

1,2,3이라는 제한된 조건을 주고, 이를 통해 숫자를 표현하라는 문제이며,
cache[3] = cacha[0] + cache[1] + cache[2] 로써 해결된다.

"""

T = int(input())

for _ in range(T):
  N = int(input())
  cache = [1,2,4,0]

  if 1<=N<=3:
    print(cache[N-1])
  else:
    for i in range(3,N):
      cache[3] = cache[0]+cache[1]+cache[2]

      cache[0],cache[1],cache[2] = cache[1],cache[2],cache[3]
    
    print(cache[3])