"""
21.07.01
삼성 SW 역량평가 2020년 하반기 기출문제 1-2
풀이 결과 : 정답
풀이 시간 : 1시간 30분

move와 merge에 대해서 정확히 이해를 못해서 오래 걸림

merge에서 move까지 하는 줄 알았음..
"""

import sys
import math
from collections import deque

dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]

all_d = [0,2,4,6]
not_all_d = [1,3,5,7]

def move():
  global graph,move_q,N

  for r in range(1,N+1):
    for c in range(1,N+1):

      if len(graph[r][c]) > 0:

        while graph[r][c]:

          m,s,d = graph[r][c].popleft()
          next_r = r+(dr[d]*s)
          next_c = c+(dc[d]*s)

          if next_r < 1 or next_r > N:
            next_r = next_r % N
            if next_r == 0:
              next_r = N
        
          if next_c < 1 or next_c > N:
            next_c = next_c % N
            if next_c == 0:
              next_c = N
        
          move_q.append((next_r,next_c,m,s,d))
  
  while move_q:
    r,c,m,s,d = move_q.popleft()
    graph[r][c].append((m,s,d))

def merge():

  global graph, merge_q, N

  for r in range(1,N+1):
    for c in range(1,N+1):
      if len(graph[r][c]) > 1:

        total_m = 0
        total_s = 0
        cnt = len(graph[r][c])
        odd_flag = False
        mean_flag = False

        while graph[r][c]:

          m,s,d = graph[r][c].popleft()
          total_m += m
          total_s += s

          if d%2 == 0:
            mean_flag = True
          else:
            odd_flag = True
          
        m = math.floor(total_m/5)
        s = math.floor(total_s/cnt)
      
        if m == 0:
          continue

        if mean_flag and odd_flag:
          for i in range(4):
            graph[r][c].append((m,s,not_all_d[i]))
        
        else:
          for i in range(4):
            graph[r][c].append((m,s,all_d[i]))

N,M,K = map(int,sys.stdin.readline().split())
graph = [[deque() for _ in range(N+1)] for _ in range(N+1)]
move_q = deque()
answer = 0

for _ in range(M):
  r,c,m,s,d = map(int,sys.stdin.readline().split())
  graph[r][c].append((m,s,d))

for _ in range(K):
  move()
  merge()

for r in range(1,N+1):
  for c in range(1,N+1):
    if len(graph[r][c]) > 0:
      while graph[r][c]:
        m,s,d = graph[r][c].popleft()
        answer += m

print(answer)