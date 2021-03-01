def dfs(graph,visited,w,h,W,H):
  
  # out of range check
  if w<0 or w>=W:
    return False
  if h<0 or h>=H:
    return False 

  # visited check
  if visited[h][w] == True:
    return False
  
  visited[h][w] = True
  
  if graph[h][w] != 1:
    return False

  for a,b in step:
    dfs(graph,visited,w+b,h+a,W,H)

  return True

count = 0
step = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

while True:
  W,H = map(int,input().split())
  data = []

  #breaking point
  if W==0 and H==0:
    break

  visited = [[False]*W for _ in range(H)]

  for i in range(H):
      data.append(list(map(int,input().split())))

  for h in range(H):
    for w in range(W):
      result = dfs(data,visited,w,h,W,H)

      if result == True:
        count+=1

  print(count)
  count=0
  
