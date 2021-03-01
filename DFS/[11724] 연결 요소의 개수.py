def dfs(graph,visited,V):
  
  if visited[V] == True:
    return 0

  visited[V] = True
  
  for v in graph[V]:
    dfs(graph,visited,v)

  return 1

N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)
result = 0

for i in range(M):
  u,v = map(int,input().split())
  
  graph[u].append(v)
  graph[v].append(u)

for n in range(1,N+1):
  result += dfs(graph,visited,n)
  
print(result)