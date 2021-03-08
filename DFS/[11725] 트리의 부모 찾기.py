import sys
sys.setrecursionlimit(100000)

def dfs(graph,visited,v,parent):

  visited[v]=True

  global result
  result[v]=parent

  for i in graph[v]:
    
    if visited[i]==False:
      dfs(graph,visited,i,v)

N = int(input())

graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)
result = [0]*(N+1)

for i in range(N-1):
  
  u,v = map(int,sys.stdin.readline().rsplit())
  graph[u].append(v)
  graph[v].append(u)

dfs(graph,visited,1,0)

for i in range(2,N+1):
  print(result[i])