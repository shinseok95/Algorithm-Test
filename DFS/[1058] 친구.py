import sys
sys.setrecursionlimit(10**7)

def dfs(graph,v,stage):
  
  global n, visited
  if stage >2:
    return False

  visited[v] = 1
  
  for i in range(n):
    if graph[v][i]==1:
      dfs(graph,i,stage+1)

  return True

n = int(input())
graph =[[0]*n for _ in range(n)]

result =0

for i in range(n):
  s = input()
  
  for j in range(n):
    if s[j] =='Y':
      graph[i][j] = 1

for i in range(n):

  visited= [0]*n
  dfs(graph,i,0)
  
  result= max(result,sum(visited)-1)

print(result)