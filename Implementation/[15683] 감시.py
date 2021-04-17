import sys
from copy import deepcopy

def direction(r,c,d,maps):

  #북쪽
  if d == 0 :
    for i in range(r-1,-1,-1):
      if graph[i][c] != 6:
        if graph[i][c] == 0:
          maps[i][c] = -1
      else:
        break
  
  # 동쪽
  elif d == 1:
    for i in range(c+1,M):
      if graph[r][i] != 6:
        if graph[r][i] == 0 :
          maps[r][i] = -1
      else:
        break

  #남쪽
  elif d == 2:
    for i in range(r+1,N):
      if graph[i][c] != 6:
        if graph[i][c] == 0:
          maps[i][c] = -1
      else:
        break
  
  #서쪽
  else :
    for i in range(c-1,-1,-1):
      if graph[r][i] != 6:
        if graph[r][i] == 0:
          maps[r][i] = -1
      else:
        break

def dfs(i,maps):

  if i == len(cctv):
    cnt = 0   
    for r in range(N):
      for c in range(M):
        if maps[r][c]  == 0:
          cnt+=1

    return cnt
  
  result = sys.maxsize
  r,c,n = cctv[i]

  if n == 1:
    for d in range(4):
      tmp_maps = [maps[_][:] for _ in range(N)]
      #tmp_maps = deepcopy(maps)
      direction(r,c,d,tmp_maps)

      result = min(result,dfs(i+1,tmp_maps))

  elif n == 2:
    for d in range(2):
      tmp_maps = [maps[_][:] for _ in range(N)]
      #tmp_maps = deepcopy(maps)

      if d == 0 :
        direction(r,c,0,tmp_maps)
        direction(r,c,2,tmp_maps)
      else:
        direction(r,c,1,tmp_maps)
        direction(r,c,3,tmp_maps)
        
      result = min(result,dfs(i+1,tmp_maps))

  elif n == 3:
    for d in range(4):

      tmp_maps = [maps[_][:] for _ in range(N)]
      #tmp_maps = deepcopy(maps)

      if d == 0 :
        direction(r,c,0,tmp_maps)
        direction(r,c,1,tmp_maps)
      elif d == 1:
        direction(r,c,1,tmp_maps)
        direction(r,c,2,tmp_maps)
      elif d == 2:
        direction(r,c,2,tmp_maps)
        direction(r,c,3,tmp_maps)
      else:
        direction(r,c,3,tmp_maps)
        direction(r,c,0,tmp_maps)
      
      result = min(result,dfs(i+1,tmp_maps))

  elif n == 4:
    for d in range(4):
      tmp_maps = [maps[_][:] for _ in range(N)]
      #tmp_maps = deepcopy(maps)

      if d == 0 :
        direction(r,c,0,tmp_maps)
        direction(r,c,1,tmp_maps)
        direction(r,c,2,tmp_maps)

      elif d == 1:
        direction(r,c,1,tmp_maps)
        direction(r,c,2,tmp_maps)
        direction(r,c,3,tmp_maps)
      elif d == 2:
        direction(r,c,2,tmp_maps)
        direction(r,c,3,tmp_maps)
        direction(r,c,0,tmp_maps)
      else:
        direction(r,c,3,tmp_maps)
        direction(r,c,0,tmp_maps)
        direction(r,c,1,tmp_maps)
      
      result = min(result,dfs(i+1,tmp_maps))

  else:
    tmp_maps = [maps[_][:] for _ in range(N)]
      #tmp_maps = deepcopy(maps)

    direction(r,c,0,tmp_maps)
    direction(r,c,1,tmp_maps)
    direction(r,c,2,tmp_maps)
    direction(r,c,3,tmp_maps)

    result = min(result,dfs(i+1,tmp_maps))

  return result
    
  
N,M = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
cctv = []

for i in range(N):
  for j in range(M):
    if graph[i][j] != 0 and graph[i][j] != 6:
      cctv.append((i,j,graph[i][j]))

print(dfs(0,graph))