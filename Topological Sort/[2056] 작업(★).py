"""
이 문제는 위상정렬을 통해서 해결할 수 있는 문제다.

하지만 까다로운 조건은 서로 선행관계가 없는 작업들은 동시에 수행이 가능하다는 점이었다.

그래서 queue에 index와 그 index까지 걸린 시간을 함께 넣어줬다.

그런데 9%에서 계속 오답이 뜨는데 도저히 모르겠어서 다른 질문을 보고 문제을 알게 되었다.

이 문제는 DP적인 사고도 할 수 있었어야 했다.

왜냐하면, 만약 
3
100 0
10 0
5 2 1 2

인 경우, 100일 때는 3번 노드의 indgree가 1이기 때문에 q에 들어가지 않는다.
그리고 10일 때 3번 노드의 indegree가 0이 되기 때문에, 큐에는 (3,10)이 들어가게 된다.

즉, 해당 노드의 indegree가 0이 되었을 때, 해당 노드를 가리키는 모든 노드들의 시간을 비교하고 가장 큰 시간을 넣어줘야하는 것이었다.

전혀 생각치도 못한 반례였고, 여전히 많이 부족하다는 생각을 하게 된다.

"""

import sys
from collections import deque

def topology_sort():
  
  q = deque()

  for i in range(1,N+1):
    if indegree[i] == 0 :
      q.append((i,0))
  
  while q:
    now,t = q.popleft()
    result[now] = t+times[now]
    
    for v in graph[now]:
      indegree[v] -= 1

      if indegree[v] == 0:
        next_t = 0

        for i in topology[v]:
          next_t= max(next_t,result[i])

        q.append((v,next_t))
        
      
N = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
topology = [[] for _ in range(N+1)]
indegree = [0]*(N+1)
times = [0]*(N+1)
result = [0]*(N+1)

for i in range(1,N+1):
  node = list(map(int,sys.stdin.readline().split()))
  
  times[i] = node[0]
  
  for j in range(node[1]):
    graph[node[2+j]].append(i)
    topology[i].append(node[2+j])
    indegree[i] += 1

topology_sort()
print(max(result))
