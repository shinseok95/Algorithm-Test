from collections import deque

dn = [-1,1,0,0]
dm = [0,0,-1,1]

N,M = map(int,input().split())

def bfs(graph,distance,visited,N,M):
  
  queue = deque([(0,0)])
  visited[0][0] = True

  while queue:

    n,m = queue.popleft()

    if n==(N-1) and m==(M-1):
      return
    
    for i in range(4):

      next_n = n+dn[i]
      next_m = m+dm[i]
      
      if 0<=next_n<N and 0<=next_m<M:
        if graph[next_n][next_m] ==1:
          if not visited[next_n][next_m]:
          
            visited[next_n][next_m] = True
            distance[next_n][next_m] = distance[n][m]+1
            queue.append((next_n,next_m))



graph = []

visited=[[False]*M for _ in range(N)]
distance = [[1]*M for _ in range(N)]

for _ in range(N):
  tmp = input()
  graph.append(list(map(int,tmp)))

bfs(graph,distance,visited,N,M)

print(distance[N-1][M-1])