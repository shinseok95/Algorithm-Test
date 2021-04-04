"""
해당 문제는 node수가 최대 500개, edge수가 최대 124,750개나 되는 문제다.
그래서 플루이드 워셜로 푼다면 pypy3가 아닌 이상 시간초과가 뜰 수 밖에 없다.

우선 플루이드 워셜로는 다음과 같은 아이디어로 접근하였다.

1. 각 노드가 접근할 수 있는 노드들을 모두 구한다. (O(N^3))
2. 각 노드들을 순회하며, 노드 n이 접근 불가능한 노드 m를 찾고, 노드 m 또한 노드 n에 접근이 불가능한지 체크한다. (만약 둘다 접근이 불가능하면 두 노드의 순서를 알 수 없음) (O(N^2))

이렇게 구하는 경우, 시간복잡도는 O(N^3)이 되므로 노드가 500개인 경우 1초안에 해결하는 것이 불가능하다.

그래서 BFS로 해결할 수 있는 방법을 생각했다.
아이디어는 다음과 같다.

1. 각 노드별로 모든 Edge를 탐색하며, 도달할 수 있는 노드의 수를 cnt에 저장한다.
2. 이때, 노드 i에서 노드 j에 접근할 수 있을 때, i의 cnt에만 1을 더해주는 것이 아닌 j의 cnt에도 1을 더해준다. (양방향으로 접근 가능한지 체크를 해야하기 때문)
3. 이후 cnt가 노드 개수와 같은 노드를 찾는다.

이렇게 구하는 경우, N * E의 시간 복잡도가 나온다.
이 문제에서는 500 * 124,750 이므로, 대략 6000만번의 연산이 걸린다.
파이썬에서는 시간초과가 나올 수 있지만, 노드별로 visited를 통해 중복 접근을 제어해주면 시간초과가 나오지 않는다.
"""

import sys

N,M = map(int,sys.stdin.readline().split())
graph = [[0]*(N+1) for _ in range(N+1)]
cnt = 0

for i in range(M):
  a,b = map(int,sys.stdin.readline().split())

  graph[a][b] = 1

for k in range(1,N+1):
  for i in range(1,N+1):
    for j in range(1,N+1):
      
      if i == j :
        graph[i][j] = 0
      else:
        if graph[i][j] == 1:
          continue

        if graph[i][k] == 1 and graph[k][j] == 1:
          graph[i][j] =1

for i in range(1,N+1):

  flag = True
  for j in range(1,N+1):
    
    if i==j:
      continue

    if graph[i][j] == 0:
      if graph[j][i] == 0:
        flag = False
        break
  
  if flag:
    cnt+=1

print(cnt)

"""
import sys
from collections import deque

N,M = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
cnt = [1]*(N+1)
q = deque([])

for _ in range(M):
  a,b = map(int,sys.stdin.readline().split())
  
  graph[a].append(b)

for i in range(1,N+1):
  
  visited = [False]*(N+1)

  q.append(i)
  visited[i] = True

  while q:

    j = q.popleft()

    if i!=j:
      cnt[i] += 1
      cnt[j] += 1

    for k in graph[j]:
    
      if not visited[k]:
        visited[k] = True

        q.append(k)

sys.stdout.write(str(cnt.count(N)))
"""


    