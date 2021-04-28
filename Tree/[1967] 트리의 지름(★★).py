"""

트리에 대한 공부가 잘 되어있지 않아서, 문제를 푸는데 2시간 넘게 걸렸다.
심지어 찾아보니 내가 해결한 방법이 제대로된 방법도 아니었다.

또한 트리의 지름라는 개념을 모르고 단순히 모든 경우를 계산하다보니 시간복잡도가 매우 높게 나왔다.

트리의 지름을 푸는 방법은 다음과 같다.

1. 한 노드에서 가장 멀리있는 노드를 선택한다. (DFS)

2. 해당 노드에서 가장 먼 노드까지의 거리를 구한다(DFS)

2번 과정에서 구해진 거리가 트리의 지름이 된다.

정확한 증명은 봐도 잘 이해가 안가기 때문에 일단 외우기로 하였다..

상단의 코드가 위 과정을 통해 푼 코드이고, 하단의 코드가 위 과정을 모르고 푼 코드이다.

"""

import sys
sys.setrecursionlimit(10**5)

def dfs(n,d):

  global max_dist,max_point

  for next_n, next_d in graph[n]:
    if not visited[next_n]:
      if max_dist <d+next_d:
        max_point = next_n
        max_dist = max(max_dist,d+next_d)

      visited[next_n] = True
      dfs(next_n,d+next_d)
      visited[next_n] = False

  
N = int(sys.stdin.readline())

if N == 1:
  sys.stdout.write(str(0))
  exit()

graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)

max_dist = 0
max_point = 0

for i in range(N-1):
  parent, child, cost = map(int,sys.stdin.readline().split())

  graph[parent].append((child,cost))
  graph[child].append((parent,cost))

visited[1] = True
dfs(1,0)
visited[1] = False

visited[max_point] = True
dfs(max_point,0)
visited[max_point] = False

sys.stdout.write(str(max_dist))

"""
import sys
sys.setrecursionlimit(10**5)

def dfs(n,d):
  
  global max_dist

  for next_n, next_d in graph[n]:
    if not visited[next_n]:
      if last_parent >= next_n:
        max_dist = max_dist = max(max_dist,d+next_d)

        visited[next_n] = True
        dfs(next_n,d+next_d)
        visited[next_n] = False
      else:
        max_dist = max(max_dist,d+next_d)
  
N = int(sys.stdin.readline())

if N == 1:
  sys.stdout.write(str(0))
  exit()

graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)
parents = []
last_parent = 1
max_dist = 0
sum_cost = 0

for i in range(N-1):
  parent, child, cost = map(int,sys.stdin.readline().split())

  parents.append(parent)
  sum_cost += cost
  graph[parent].append((child,cost))
  graph[child].append((parent,cost))

last_parent = max(parents)

for i in range(last_parent+1,N+1):
  visited[i] = True
  dfs(i,0)
  visited[i] = False

sys.stdout.write(str(max_dist))

"""
