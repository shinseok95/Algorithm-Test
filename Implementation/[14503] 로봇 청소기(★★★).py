"""
반쯤 풀고 반쯤은 틀린 문제다

어찌됐든 다른 사람의 풀이를 봤으니 못푼게 맞는 것 같다.

DFS를 통해 상하좌우를 확인하고 청소할 수 있으면 그 방향으로 움직이고, 없으면 뒤로 방향을 유지한채로 움직여야한다.

그런데 돌아간다는 것을 나는 백트래킹으로 움직여야한다고 생각하다보니까, visited를 체크하고 있었고, 여기서 계속 꼬였던 것 같다.

그러나 알고보니 그냥 visited를 체크하지 않고, 네 방향 모두 청소할 곳이 없을 때 뒷공간이 1이 아니면 다시 dfs를 호출해주면 되는 것이었다.

지금까지 무조건 visited를 사용하다버릇을 하다보니, 마치 무한루프에 빠지지 않을까 걱정하며 시도를 못했었는데 아무래도 뒤에 1이 있으면 탈출한다는 것이 무한루프를 막아준 것 같다.

다음에 다시 풀어봐야할 것 같다^^
"""

import sys

dr = [-1,0,1,0]
dc = [0,1,0,-1]

def dfs(R,C,D):
  if graph[R][C] ==0:
    graph[R][C] = -1
  
  for i in range(4):

    # 왼쪽 방향으로 회전
    if D==0:
      D = 3
    else:
      D = D-1
    
    next_r = R+dr[D]
    next_c = C+dc[D]

    if 0<=next_r<N and 0<=next_c<M:
      if graph[next_r][next_c] == 0:
        dfs(next_r,next_c,D)
    
  if D<2:
    next_r = R+dr[D+2]
    next_c = C+dc[D+2]
  else:
    next_r = R+dr[D-2]
    next_c = C+dc[D-2]
    
  if graph[next_r][next_c] != 1:
    dfs(next_r,next_c,D)
  else:
    cnt = 0
    for i in range(N):
      cnt += graph[i].count(-1)
    print(cnt)
    exit()

N,M = map(int,sys.stdin.readline().split())
r,c,d = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

dfs(r,c,d)
