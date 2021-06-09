import sys
from collections import deque

N,M = map(int,sys.stdin.readline().split())

indegree = [0]*(N+1)
graph = [[] for _ in range(N+1)]
result = []

for _ in range(M):
  line = list(map(int,sys.stdin.readline().split()))

  for i in range(1,len(line)-1):
    graph[line[i]].append(line[i+1])
    indegree[line[i+1]] += 1

q = deque()

for i in range(1,N+1):
  if indegree[i] == 0:
    q.append(i)

while q:
  n = q.popleft()
  indegree[n] -= 1
  result.append(n)

  for i in graph[n]:
    indegree[i] -= 1

    if indegree[i] == 0:
      q.append(i)
      
if len(result) != N:
  print(0)
else:
  for i in range(N):
    print(result[i])