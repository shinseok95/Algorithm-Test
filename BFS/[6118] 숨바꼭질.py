from collections import deque

def bfs(graph,visited,distance,V):

  queue = deque([V])
  visited[V] = True

  while queue:

    v = queue.popleft()

    for i in graph[v]:

      if visited[i] == False:
        
        visited[i] = True
        distance[i] = distance[v]+1
        queue.append(i)

N,M = map(int,input().split())

graph=[[] for _ in range(N+1)]
visited = [False]*(N+1)
distance = [0]*(N+1)

for _ in range(M):
  a,b = map(int,input().split())
  
  graph[a].append(b)
  graph[b].append(a)

bfs(graph,visited,distance,1)

index = distance.index(max(distance))
size = distance[index]
count = distance.count(max(distance))

print(index,size,count)