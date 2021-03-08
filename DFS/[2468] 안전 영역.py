import sys
sys.setrecursionlimit(10**6)

def dfs(graph,visited,r,c,rain):
  
  if visited[r][c] == True:
    return
  
  visited[r][c] = True

  if graph[r][c] <= rain:
    return

  global result
  result +=1

  if r-1 >= 0 :
    dfs(graph,visited,r-1,c,rain)

  if r+1 < len(graph) :
    dfs(graph,visited,r+1,c,rain)

  if c-1 >= 0 :
    dfs(graph,visited,r,c-1,rain)

  if c+1 < len(graph) :
    dfs(graph,visited,r,c+1,rain)
   

N = int(input())

graph = []
visited = [[False] * N for _ in range(N)]

result = 0
count=[]
count_list = []

for _ in range(N):
  graph.append(list(map(int,input().split())))

for n in range(max(map(max,graph))+1):
  for i in range(N):
    for j in range(N):
      result = 0 
      dfs(graph,visited,i,j,n)
      
      if result != 0:
        count.append(result)

  if len(count) > 0 :
    count_list.append(len(count))
    count= []
  
  visited = [[False] * N for _ in range(N)]

print(max(count_list))

