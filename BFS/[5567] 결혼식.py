from collections import deque

def bfs(graph,visited,distance,V):
  
  queue = deque([V])
  visited[V] = True

  while queue:
    v = queue.popleft()

    for i in graph[v]:
      
      if visited[i] == False:
        queue.append(i)
        visited[i]=True
        distance[i] = distance[v]+1

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)
distance = [0]*(N+1)
count = 0

for _ in range(M):
  a,b = map(int,input().split())
  
  graph[a].append(b)
  graph[b].append(a)

bfs(graph,visited,distance,1)

for i in range(2,N+1):
  if 0<distance[i]<=2:
    count+=1

print(count)