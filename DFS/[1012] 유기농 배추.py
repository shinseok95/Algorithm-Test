import sys
sys.setrecursionlimit(50000)

def dfs(graph,x,y):
  
  global n,m

  if x >= m or x<=-1 or y>=n or y<=-1:
    return False

  if graph[y][x] == 0:
    return False

  graph[y][x] = 0

  dfs(graph,x,y+1)
  dfs(graph,x+1,y)
  dfs(graph,x,y-1)
  dfs(graph,x-1,y)

  return True
  
T = int(input())

result = list()

for i in range(T):
  m,n,k = map(int,input().split())

  count =0
  graph = [[0]*m for _ in range(n)]
  
  for j in range(k):
    x,y = map(int,input().split())
    graph[y][x] = 1

  for p in range(n):
    for q in range(m):
      
      if dfs(graph,q,p):
        count +=1
  result.append(count)

for n in result:
  print(n)