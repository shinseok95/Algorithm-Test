N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
result = 0

for i in range(M):  
  
  node1, node2 = map(int,input().split())
  graph[node1].append(node2)
  graph[node2].append(node1)


def dfs(graph,v,visited):
  
  if visited[v]==True:
    return

  global result

  visited[v] = True
  result+=1

  for i in graph[v]:
    dfs(graph,i,visited)

dfs(graph,1,visited)

print(result-1 if result > 0 else 0)
  