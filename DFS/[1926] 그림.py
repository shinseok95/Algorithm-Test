import sys

# pypy3로 하면 메모리 초과가 뜸
sys.setrecursionlimit(100000)

def dfs(graph, visited, r,c):
  
  # break point check(visited)
  if visited[r][c] == True:
    return
  
  visited[r][c] = True

  # break point check(graph)
  if graph[r][c] == 0 :
    return
  
  global result
  result +=1

  if r-1>=0:
    dfs(graph,visited,r-1,c)
  
  if r+1<len(graph):
    dfs(graph,visited,r+1,c)
  
  if c-1>=0:
    dfs(graph,visited,r,c-1)
  
  if c+1<len(graph[r]):
    dfs(graph,visited,r,c+1)
  

N,M = map(int,input().split())

graph = []
visited = [[False] * M for _ in range(N)]

result_list = []
result = 0

for i in range(N):
  graph.append(list(map(int,input().split())))

for i in range(N):
  for j in range(M):

    result =0

    dfs(graph,visited, i,j)

    if result != 0 :
      result_list.append(result)

print(len(result_list))

if len(result_list)==0:
  print(0)
else:
  print(max(result_list))