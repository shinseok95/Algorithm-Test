"""
경우의 수를 잘못 계산해서, 
cache[2] = cache[i-1]+(i//2)라는 어이없는 점화식을 도출해냈다.

알고보니 cache[i] = cache[i-1]+cache[i-2]로 간단히 해결되는 문제였다.

그리고 이를 bottom up 방식으로 풀려고 했으나, 1000000개의 int를 배열로 저장해두다 보니 메모리 초과가 나왔다.

생각해보니 직전 2개의 수를 제외하고는 필요없었다. 

아직도 정말 많이 부족하다고 느낀다 ㅠㅠ
"""

import sys

N = int(sys.stdin.readline())

cache = [0]*3
cache[0]=1
cache[1]=2

for _ in range(3,N+1):
  cache[2] = (cache[1]+cache[0])%15746

  cache[0] = cache[1]
  cache[1] = cache[2]

if N==1:
  print(1)
elif N==2:
  print(2)
else:
  print(cache[2])
