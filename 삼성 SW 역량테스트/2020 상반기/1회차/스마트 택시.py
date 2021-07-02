"""
21.07.02
삼성 SW 역량평가 2020년 상반기 기출문제 2-4
풀이 결과 : 정답
풀이 시간 : 1시간 30분

한 가지의 문제와 한 가지의 실수로 시간이 오래걸렸다.

첫 번째는 최단거리 손님을 찾는 문제였다. 

나는 단순히 처음 시작할 때 손님의 위치를 정렬하고 시작하면 bfs로 최단 거리를 검색할 수 있을 거라고 생각했다.

그런데 생각해보면 아니었다.

최소 거리의 손님을 모두 구한 후, 그 중에서 정렬을 해줬어야 했다.


두 번째는 행과 열을 헷갈렸다..
그래서 계속 customers[i][1]을 먼저 정렬하고, 그 후에 customers[i][0]을 정렬했다..

"""

import sys
from collections import deque
import functools

dr = [0,-1,0,1]
dc = [-1,0,1,0]

def comp(a,b):

  global customers

  if customers[a][0] > customers[b][0]:
    return 1
  elif customers[a][0] < customers[b][0]:
    return -1
  else:
    if customers[a][1] > customers[b][1]:
      return 1
    elif customers[a][1] < customers[b][1]:
      return -1
    else:
      return 0

def find(r,c):
  global N,M,P,graph,customers
  
  visited = [[False]*(N+1) for _ in range(N+1)]
  q = deque([(r,c,0)])
  visited[r][c] = True

  min_cnt = int(1e9)
  min_customers = []

  while q:
    r,c,cnt = q.popleft()

    if cnt > min_cnt:
      break

    for i in range(M):
      if customers[i][0] == r and customers[i][1] == c:
        min_customers.append(i)
        min_cnt = min(min_cnt,cnt)

    for i in range(4):
      next_r = r+dr[i]
      next_c = c+dc[i]

      if 0<next_r<=N and 0<next_c<=N:
        if not visited[next_r][next_c]:
          if graph[next_r][next_c] == 0:
            visited[next_r][next_c]=True
            q.append((next_r,next_c,cnt+1))  
  
  if len(min_customers) > 0:
    min_customers.sort(key = functools.cmp_to_key(comp))
    return min_customers[0],min_cnt
  else:
    return -1, min_cnt

def drive(R,C,end_r,end_c):
  global N,M,P,graph

  visited = [[False]*(N+1) for _ in range(N+1)]
  q = deque([(R,C,0)])
  visited[R][C] = True

  while q:

    r,c,cnt = q.popleft()

    if r == end_r and c == end_c:
      return cnt

    for i in range(4):
      next_r = r + dr[i]
      next_c = c + dc[i]

      if 0<next_r<=N and 0<next_c<=N:
        if not visited[next_r][next_c]:
          if graph[next_r][next_c] == 0:
            visited[next_r][next_c]=True
            q.append((next_r,next_c,cnt+1))  

  return -1
  

N,M,P = map(int,sys.stdin.readline().split())
graph = [[1]*(N+1)]
for _ in range(N):
  graph.append([1]+list(map(int,sys.stdin.readline().split())))
R,C = map(int,sys.stdin.readline().split())
customers = []
for _ in range(M):
  customers.append(list(map(int,sys.stdin.readline().split())))

while True:

  if M > 0:
    i,P_find = find(R,C)

    if i == -1:
      print(-1)
      exit()
  else:
    break

  if P_find > P :
    print(-1)
    exit()
  else:
    P -= P_find
  
  r,c = customers[i][0],customers[i][1]
  end_r, end_c = customers[i][2], customers[i][3]

  P_drive = drive(r,c,end_r,end_c)

  if P_drive == -1:
    print(-1)
    exit()

  if P_drive > P :
    print(-1)
    exit()
  else:
    P += P_drive

  del customers[i]
  M -= 1
  R,C = end_r,end_c

print(P)
  
