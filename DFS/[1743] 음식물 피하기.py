import sys
sys.setrecursionlimit(100000)

def dfs(graph,visited,r,c):
  
  # break point(visite check)
  if visited[r][c] == True:
    return
  
  visited[r][c] = True

  # break point(trash check)
  if graph[r][c] == False :
    return

  global result
  result+=1

  # up,down,left,right
  
  if r-1 >=1 :
    dfs(graph,visited,r-1,c)
  
  if r+1 < len(graph):
    dfs(graph,visited,r+1,c)

  if c-1 >=0 :
    dfs(graph,visited,r,c-1)

  if c+1 < len(graph[r]):
    dfs(graph,visited,r,c+1)
  

N,M,K = map(int,input().split())

graph = [[False]*(M+1) for _ in range(N+1)]

visited = [[False]*(M+1) for _ in range(N+1)]

result = 0
result_list = []

for _ in range(K):
  r,c = map(int,input().split())
  
  graph[r][c]=True

for i in range(1,N+1):
  for j in range(1,M+1):

    result = 0
    dfs(graph,visited,i,j)
    result_list.append(result)


print(max(result_list))

