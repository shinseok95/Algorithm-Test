"""
[17626] Four Squares 문제와 매우 유사한 문제

Bottom up 방식으로 접근해서 해결하였다.

그런데 특이한 점은 python3에서 j**2는 시간초과가 뜨는데, j*j는 시간초과가 뜨지 않았다.

내부적으로 뭔가 차이가 있는지는 모르겠지만, 앞으로 j**2 보다는 j*j를 사용해야겠다.
"""

from math import sqrt,floor

N = int(input())
cache = [0]*(N+1)

for i in range(1,N+1):

  n = floor(sqrt(i))
  
  if i-(n*n) == 0:
    cache[i]=1
    continue

  else:

    count = 5

    for j in range(n,0,-1):
      count = min(count,1+cache[i-( j*j)])

    cache[i] = count

print(cache[N])