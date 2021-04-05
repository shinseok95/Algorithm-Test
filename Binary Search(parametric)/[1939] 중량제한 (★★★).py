"""

서로소 집합 문제인줄 알고 풀다가 결국 답을 봤다.

그런데 전혀 생각도 못한 이분탐색 문제였다.

최대치를 이분탐색으로 정하고, bfs를 통해 start->end까지 해당 최대치로 이동할 수 있는지를 판단해야한다.

만약 mid값으로 통과하지 못한다면, mid값을 줄이고, 통과할 수 있다면 mid값을 늘리는 방식으로 하다보면 가능하다.

답을 보고도 오랜 시간이 걸렸는데, 두가지 이유가 있었다.

첫 번째, visited를 queue에서 pop한 후에 해줘서 중복된 노드가 계속 queue에 들어갔었다.
(이것 때문에 계속 메모리 초과가 떴는데, 시간초과도 아닌 메모리 초과는 왜 떴는지 모르겠다.)

두 번째, 이분 탐색할 때, 최댓값은 end에서 최솟값은 start에서 도출된다는 걸 계속 반대로 생각하고 있었다.
"""

import sys
from collections import deque

def bfs(c):

  q = deque([s])
  visited[s] = True

  while q:

    v = q.popleft()
    
    if v == e:
      return True
  
    for i in graph[v]:
      if not visited[i[0]] and i[1]>=c:
        q.append(i[0])
        visited[i[0]] = True

  return False

N,M = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
max_value = 0

for _ in range(M):

  a,b,c = map(int,sys.stdin.readline().split())

  graph[a].append((b,c))
  graph[b].append((a,c))
  max_value = max(max_value,c)

s,e = map(int,sys.stdin.readline().split())

start = 1
end = max_value
result = 0

while start<=end:

  mid = (start+end)//2
  visited = [False for _ in range(N+1)]

  if bfs(mid):
    start = mid+1
  else:
    end = mid-1

print(end)