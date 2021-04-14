import sys

dr = [0,0,0,-1,1]
dc = [0,1,-1,0,0]

N,M,r,c,K = map(int,sys.stdin.readline().split())

graph = []

for _ in range(N):
  graph.append(list(map(int,sys.stdin.readline().split())))

funcs = list(map(int,sys.stdin.readline().split()))

h = [0,0,0]
v = [0,0,0,0]

for f in funcs:
  
  next_r = r+dr[f]
  next_c = c+dc[f]
  
  if 0<=next_r<N and 0<=next_c<M:

    tmp_h = [0,0,0]
    tmp_v = [0,0,0,0]

    #오른쪽 이동
    if f==1:
      tmp_h[0] = v[1]
      if graph[next_r][next_c] == 0:
        tmp_h[1] = h[2]
      else:
        tmp_h[1] = graph[next_r][next_c]
      tmp_h[2] = v[3]

      tmp_v[0] = v[0]
      tmp_v[1] = tmp_h[1]
      tmp_v[2] = v[2]
      tmp_v[3] = h[0]
      
    #왼쪽 이동
    elif f==2:

      tmp_h[0] = v[3]
      if graph[next_r][next_c] == 0:
        tmp_h[1] = h[0]
      else:
        tmp_h[1] = graph[next_r][next_c]
      tmp_h[2] = v[1]

      tmp_v[0] = v[0]
      tmp_v[1] = tmp_h[1]
      tmp_v[2] = v[2]
      tmp_v[3] = h[2]

    #위쪽 이동
    elif f==3:

      tmp_h[0] = h[0]
      if graph[next_r][next_c] == 0:
        tmp_h[1] = v[0]
      else:
        tmp_h[1] = graph[next_r][next_c]
      tmp_h[2] = h[2]

      tmp_v[0] = v[3]
      tmp_v[1] = tmp_h[1]
      tmp_v[2] = v[1]
      tmp_v[3] = v[2]

    #아래쪽 이동
    else:

      tmp_h[0] = h[0]
      if graph[next_r][next_c] == 0:
        tmp_h[1] = v[2]
      else:
        tmp_h[1] = graph[next_r][next_c]
      tmp_h[2] = h[2]

      tmp_v[0] = v[1]
      tmp_v[1] = tmp_h[1]
      tmp_v[2] = v[3]
      tmp_v[3] = v[0]
    
    v = tmp_v
    h = tmp_h

    r = next_r
    c = next_c

    if graph[next_r][next_c] == 0:
      graph[next_r][next_c] = v[1]
    else:
      graph[next_r][next_c] = 0

    print(v[3])
