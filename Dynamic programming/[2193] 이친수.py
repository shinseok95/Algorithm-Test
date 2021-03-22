"""
[1904] 01타일과 같은 논리의 문제다
0과 1의 2진수 문제가 나온다면 떠올려보자!
"""

N = int(input())
cache =[1,1,0]

if 1<=N<=2:
  print(1)
else:
  for _ in range(3,N+1):
    cache[2] = cache[0]+cache[1]

    cache[0] = cache[1]
    cache[1] = cache[2]

  print(cache[2])
