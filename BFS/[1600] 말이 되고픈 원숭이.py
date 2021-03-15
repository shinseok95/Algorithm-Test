from collections import deque

h_dr = [-1,-2,-2,-1,1,2,2,1]
h_dc = [-2,-1,1,2,2,1,-1,-2]
m_dr = [-1,1,0,0]
m_dc = [0,0,-1,1]

def bfs(graph,visited):

  global K,W,H

  queue = deque([(0,0,K,0)])
  visited[0][0].append(K)

  while queue:

    r,c,k,cnt = queue.popleft()
    
    if c==W-1 and r==H-1:
      result.append(cnt)
      print(cnt)
      exit()
    
    if 0<k:

      for i in range(8):
        n_r = r+h_dr[i]
        n_c = c+h_dc[i]
        n_k = k-1

        if 0<=n_r<H and 0<=n_c<W:
          if graph[n_r][n_c]!= 1 and not visited[n_r][n_c][n_k]:
            queue.append((n_r,n_c,n_k,cnt+1))
            visited[n_r][n_c][n_k]=True

    for i in range(4):
      n_r = r+m_dr[i]
      n_c = c+m_dc[i]
      n_k = k

      if 0<=n_r<H and 0<=n_c<W:

        if graph[n_r][n_c]!= 1 and not visited[n_r][n_c][n_k]:
          
          queue.append((n_r,n_c,n_k,cnt+1))
          visited[n_r][n_c][n_k]=True


K = int(input())
W,H = map(int,input().split())

graph = []
visited = []

for _ in range(H):
  visited.append([[False]*(K+1) for _ in range(W)])
result = []

for _ in range(H):
  graph.append(list(map(int,input().split())))

bfs(graph,visited)

print(-1)