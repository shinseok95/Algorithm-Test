from collections import deque

def bfs(graph,visited,v):
  
  queue = deque([v])
  visited[v] = True

  global count

  while queue:
    
    tmp = queue.popleft()
    count += 1

    for i in graph[tmp]:
      
      if visited[i] == False:
        
        visited[i] = True
        queue.append(i)


N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]
count_list = [0]

for _ in range(M):
  v1,v2 = map(int,input().split())
  
  graph[v2].append(v1)


for i in range(1,N+1):
  
  visited = [False] * (N+1)
  count = 0

  bfs(graph,visited,i)

  count_list.append(count)

max_value = max(count_list)

for i in range(1,N+1):

  if count_list[i]==max_value:
    print(i,end=' ')
  