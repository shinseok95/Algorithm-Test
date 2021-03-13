from collections import deque

def bfs(graph,visited,X,K):
  
  queue = deque([X])
  visited[X] = True

  while queue:
    
    x = queue.popleft()
    
    if x == K:
      return

    if 0<=(x-1)<=100000:
      if not visited[x-1]:
        visited[x-1] = True
        graph[x-1]=graph[x]+1
        queue.append(x-1)
    
    if 0<=(x+1)<=100000:
      if not visited[x+1]:
        visited[x+1] = True
        graph[x+1]=graph[x]+1
        queue.append(x+1)
    
    if 0<=(2*x)<=100000:  
      if not visited[2*x]:
        visited[2*x] = True
        graph[2*x]=graph[x]+1
        queue.append(2*x)

X,K = map(int,input().split())
graph=[0]*100001
visited = [False]*100001

bfs(graph,visited,X,K)

print(graph[K])