import sys
sys.setrecursionlimit(10**6)

def dfs(graph,visited,r,c):
  
  if visited[r][c] == True:
    return

  visited[r][c] = True

  if graph[r][c] == 0:
    return

  global count,N
  count+=1

  if r-1 >=0:
    dfs(graph,visited,r-1,c)
  if r+1 <N:
    dfs(graph,visited,r+1,c)
  if c-1 >=0:
    dfs(graph,visited,r,c-1)
  if c+1 <N:
    dfs(graph,visited,r,c+1)

N = int(input())

visited = [[False]*N for _ in range(N)]
graph = []
count = 0
count_list = []

for _ in range(N):
  tmp = input()
  graph.append(list(map(int,tmp)))

for i in range(N):
  for j in range(N):
    count = 0
    dfs(graph,visited,i,j)

    if count > 0 :
      count_list.append(count)


print(len(count_list))

if len(count_list) > 0 :
  
  count_list = sorted(count_list)
  for i in range(len(count_list)):
    print(count_list[i])