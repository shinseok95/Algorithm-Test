import sys
from collections import deque

sys.setrecursionlimit(10**6)

def dfs(graph,visited,v):
  
  if visited[v] == True:
    return
  
  visited[v] = True

  print(v, end=' ')

  for i in graph[v]:
    dfs(graph,visited,i)

def bfs(graph,visited,v):

  queue = deque([v])
  visited[v]=True
        
  while queue:
    
    tmp = queue.popleft()
    print(tmp,end=' ')

    for i in graph[tmp]:
      
      if not visited[i]:
        visited[i]=True
        queue.append(i)

N,M,V = map(int,input().split())

graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)

for _ in range(M):
  v1,v2 = map(int,input().split())
  
  graph[v1].append(v2)
  graph[v2].append(v1)

for i in range(N):
  graph[i]= sorted(graph[i])

dfs(graph,visited,V)
print()
visited = [False]*(N+1)
bfs(graph,visited,V)
