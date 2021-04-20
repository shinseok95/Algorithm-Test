import sys

dr = [-1,1,0,0]
dc = [0,0,-1,1]

R,C,T = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(R)]

cleaner = []
result = 0

for i in range(R):
  if graph[i][0] == -1: 
    cleaner.append(i)
    cleaner.append(i+1)
    break

for _ in range(T):
  tmp_graph= [[0]*C for _ in range(R)]
  tmp_graph[cleaner[0]][0] = -1
  tmp_graph[cleaner[1]][0] = -1
  
  for r in range(R):
    for c in range(C):

      if graph[r][c] == -1:
        continue

      cnt = 0

      for i in range(4):
        next_r = r+dr[i]
        next_c = c+dc[i]

        if 0<=next_r<R and 0<=next_c<C:
          if graph[next_r][next_c] != -1:

            tmp_graph[next_r][next_c] += (graph[r][c]//5)
            
            cnt += 1
      
      if cnt > 0:
        tmp_graph[r][c] += (graph[r][c]-(graph[r][c]//5)*cnt)
  
  #상단 

  #왼쪽
  for i in range(cleaner[0]-1,0,-1):
    tmp_graph[i][0] = tmp_graph[i-1][0]
  #위쪽
  for i in range(C-1):
    tmp_graph[0][i] = tmp_graph[0][i+1]
  #오른쪽
  for i in range(cleaner[0]):
    tmp_graph[i][C-1] = tmp_graph[i+1][C-1]
  #아래쪽
  for i in range(C-1,1,-1):
    tmp_graph[cleaner[0]][i] = tmp_graph[cleaner[0]][i-1]
  tmp_graph[cleaner[0]][1] = 0
  
  #하단

  #왼쪽
  for i in range(cleaner[1]+1,R-1):
    tmp_graph[i][0] = tmp_graph[i+1][0]
  #아래쪽
  for i in range(C-1):
    tmp_graph[R-1][i] = tmp_graph[R-1][i+1]
  #오른쪽
  for i in range(R-1,cleaner[1],-1):
    tmp_graph[i][C-1] = tmp_graph[i-1][C-1]
  #위쪽
  for i in range(C-1,1,-1):
    tmp_graph[cleaner[1]][i] = tmp_graph[cleaner[1]][i-1]
  tmp_graph[cleaner[1]][1] = 0
  
  graph = tmp_graph


for i in range(R):
  for j in range(C):
    if graph[i][j] == -1:
      continue
    else:
      result+= graph[i][j]

sys.stdout.write(str(result))