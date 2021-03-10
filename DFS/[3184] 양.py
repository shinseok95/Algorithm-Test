import sys
sys.setrecursionlimit(10**6)

def dfs(graph,visited,r,c):
  
  if visited[r][c] == True or graph[r][c] == '#':
    return
  
  visited[r][c] = True

  if graph[r][c] == '#':
    return
  
  global V,O,R,C

  if graph[r][c] == 'v':
    V +=1

  if graph[r][c] == 'o':
    O +=1

  if r-1 >= 0 :
    dfs(graph,visited,r-1,c)
  if r+1 <R :
    dfs(graph,visited,r+1,c)
  if c-1 >= 0 :
    dfs(graph,visited,r,c-1)
  if c+1 < C :
    dfs(graph,visited,r,c+1)

R,C = map(int,input().split())

graph = []
visited = [[False] * C for _ in range(R)]

v_result = 0
o_result = 0

for i in range(R):
  graph.append(list(input()))


for i in range(R):
  for j in range(C):

    V = 0
    O = 0

    dfs(graph,visited,i,j)

    if V ==0 and O == 0:
      continue
      
    if V>=O:
      v_result+=V

    else:
      o_result+=O

print(o_result, v_result)
