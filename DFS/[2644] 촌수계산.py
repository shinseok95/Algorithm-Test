N = int(input())
A,B = map(int,input().split())
M = int(input())

graph=[[] for _ in range(N+1)]
visited=[False]*(N+1)
result = 0

for i in range(M):
  node1,node2 = map(int,input().split())
  graph[node1].append(node2)
  graph[node2].append(node1)

def dfs(graph,v,b,visited,ans):

  if visited[v]==True:
    return

  if v==b:
    global result
    result = ans
    return

  visited[v] = True
  if v!=b:
    ans+=1

  for i in graph[v]:
    dfs(graph,i,b,visited,ans)

dfs(graph,A,B,visited,0)

print(result if result>0 else -1)

