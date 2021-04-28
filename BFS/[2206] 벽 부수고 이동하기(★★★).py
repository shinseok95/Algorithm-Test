"""
역시나 풀지 못했다.

모든 경우의 수로 푸는 것은 시간복잡도가 안될 것 같았었는데, 역시나 시간초과가 떴다.

찾아보니 3차원 리스트를 이용해서 벽을 이용해서 왔는지 그때 그때 확인해줘야 했다.

예를 들어, 다음 장소가 벽일때, 이전에 벽을 이미 뚫고 왔다면 나아가지 못할 것이고, 아직 뚫고 오지 않았다면 이를 체크하고 넘어갈 수 있을 것이다.

그리고 다음 장소가 벽이 아닐 때는, 이전에 벽을 이미 뚫고 왔든지 안뚫고 왔든지 상관없이 그냥 그대로 지나가면 될 것이다.

이를 코드로 표현하면,

graph[next_r][next_c] == 0 이면 
visited[next_r][next_c][z] = visited[r][c][z]+1

graph[next_r][next_c] == 1 이면
q.append((next_r,next_c,z))

z==1이면 X

z==0이면
visited[next_r][c][1] = visited[r][c][0]+1
q.append((next_r,next_c,1))


다음에 다시 풀어봐야할 것 같다.
"""
import sys
from collections import deque
dr = [1,0,0,-1]
dc = [0,1,-1,0]

def bfs():

  q = deque()
  q.append((0,0,0))

  visited=[[[0]*M for _ in range(N)] for _ in range(2)]
  visited[0][0][0] = 1

  while q:

    r,c,z = q.popleft()

    if r == N-1 and c == M-1:
      return visited[z][r][c]

    for i in range(4):
      next_r = r+dr[i]
      next_c = c+dc[i]

      if 0<=next_r<N and 0<=next_c<M and visited[z][next_r][next_c] == 0:
        if graph[next_r][next_c] == 1 and z == 0:
          visited[1][next_r][next_c] = visited[0][r][c]+1
          q.append((next_r,next_c,1))
        
        elif graph[next_r][next_c] ==0:
          visited[z][next_r][next_c] = visited[z][r][c]+1
          q.append((next_r,next_c,z))

  return -1

N,M = map(int,sys.stdin.readline().split())

graph = []

for r in range(N):
  cols = sys.stdin.readline().rstrip()
  graph.append(list(map(int,cols)))

if N==1 and M==1 and graph[0][0] == 0:
  sys.stdout.write(str(1))
else:
  sys.stdout.write(str(bfs()))