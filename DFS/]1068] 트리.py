def dfs(children,visited,v):
  
  if visited[v]==True:
    return

  visited[v] = True

  if len(children[v])==0:
  
    global result
    result-=1
    return
  
  for i in children[v]:
    dfs(children,visited,i)

N = int(input())
parents = list(map(int,input().split()))
remove_node = int(input())

children = [[] for _ in range(N)]
visited = [False]*N

result = 0

for i in range(N):
  for j in range(N):
    
    if parents[j]==i:
      children[i].append(j)

# leaf node count

for i in range(N):
  if len(children[i])==0:
    result+=1

# leaf node remove

dfs(children,visited,remove_node)

if len(children[parents[remove_node]])==1:
  result+=1
  
print(result)
