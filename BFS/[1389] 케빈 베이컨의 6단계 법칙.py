from collections import deque

def bfs(graph,distance,visited,X):

  queue = deque([X])
  visited[X]= True

  while queue:

    x = queue.popleft()
    
    for i in graph[x]:
      
      if not visited[i]:
        
        visited[i] = True
        distance[i] = distance[x]+1
        queue.append(i)
        
N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]
result = [0]*(N+1)
result[0] = 999999

for _ in range(M):
  
  a,b = map(int,input().split())
  
  if graph[a].count(b) == 0:

    graph[a].append(b)
    graph[b].append(a)

for i in range(1,N+1):

  distance = [0]*(N+1)
  visited = [False]*(N+1)

  bfs(graph,distance,visited,i)

  result[i] = sum(distance)

print(result.index(min(result)))
