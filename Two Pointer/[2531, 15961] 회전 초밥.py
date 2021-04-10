"""
두가지 방향으로 문제를 해결하였다.

첫 번째는 set을 이용해서 중복을 제거하고 개수를 세는 것이고, 두 번째는 two pointer를 통해 개수를 세는 것이었다.

첫 번째 방법은 만약 데이터가 많았다면 시간초과가 나왔을 것 같다.

그러나, 두 번째 방법은 데이터가 많더라도 O(N)의 시간복잡도가 걸리므로 크게 문제가 되지 않는다.

우선 스시 종류를 리스트로 만들고, 해당 스시가 있다면 리스트에서 +1을 해준다. 

그리고 start와 end를 한칸씩 오른쪽으로 옮겨주면서 start의 개수를 1개 줄이고, end의 개수를 1개 늘려준다.

이 때, start의 개수가 0개가 된다면 cnt를 하나 줄여주고, end가 0이었다가 1로 늘어나면 cnt를 하나 늘려준다

추가적으로 조건2에서 만약 초밥들 중 사장이 서비스로 주는 초밥이 없다면 1을 더해줘야한다는 조건이 있기 때문에, 그것까지 고려해주면 된다.


생각보다 어려웠고, 많은 연습이 필요할 것 같다.
"""

"""
import sys

N,D,K,C = map(int,sys.stdin.readline().split())
data=[int(sys.stdin.readline()) for _ in range(N)]

max_cnt = 0

for i in range(N-K+1):
  interval_list = list(set(data[i:i+K]+[C]))

  max_cnt = max(max_cnt,len(interval_list))

for i in range(N-K+1,N):
  interval_list = list(set(data[i:]+data[:K-(N-i)]+[C]))

  max_cnt = max(max_cnt,len(interval_list))

print(max_cnt)
"""

import sys

N,D,K,C = map(int,sys.stdin.readline().split())
data=[int(sys.stdin.readline()) for _ in range(N)]
sushi = [0]*(D+1)

for i in range(K):
  sushi[data[i]] += 1

max_cnt = 0
cnt = len(set(data[:K]))

for start in range(1,N-K+1):

  end = start+K-1

  sushi[data[start-1]] -= 1
  if sushi[data[start-1]] == 0 :
    cnt -=1
  
  if sushi[data[end]] == 0 :
    cnt += 1
  sushi[data[end]] += 1

  if sushi[C] == 0 :
    max_cnt = max(max_cnt,cnt+1)
  else:
    max_cnt = max(max_cnt,cnt)

for start in range(N-K+1,N):

  end = K-(N-start)-1

  sushi[data[start-1]] -= 1
  if sushi[data[start-1]] == 0 :
    cnt -=1
  
  if sushi[data[end]] == 0 :
    cnt += 1
  sushi[data[end]] += 1

  if sushi[C] == 0 :
    max_cnt = max(max_cnt,cnt+1)
  else:
    max_cnt = max(max_cnt,cnt)

print(max_cnt)