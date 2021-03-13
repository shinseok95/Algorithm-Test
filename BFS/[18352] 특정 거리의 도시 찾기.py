from collections import deque

def bfs(graph,visited,distance,X,K):
  
  queue = deque([X])

  while queue:
    
    x = queue.popleft()

    visited[x]=True

    if distance[x] == K:

      global result
      result.append(x)

    for i in graph[x]:

      if not visited[i]:
        
        visited[i] = True
        distance[i]=distance[x]+1
        queue.append(i)

N,M,K,X = map(int,input().split())

graph=[[] for _ in range(N+1)]
distance=[0]*(N+1)
visited = [False]*(N+1)

result = []

for _ in range(M):

  a,b = map(int,input().split())
  graph[a].append(b)

bfs(graph,visited,distance,X,K)

if len(result)==0:
  print(-1)
else :
  result=sorted(result)

  for i in result:
    print(i)
