"""
처음 풀어보는 구현 문제인데, 생각보다 빡세다..
"""

import sys

C,R = map(int,sys.stdin.readline().split())
N = int(sys.stdin.readline())
graph = []
man = None
result = 0

for i in range(N+1):
  d,n = map(int,sys.stdin.readline().split())

  if d == 1:
    r = 0
    c = n
  elif d == 2:
    r = R
    c = n
  elif d == 3:
    r = n
    c = 0
  else:
    r = n
    c = C
  
  if i == N:
    man = (r,c)
  else:
    graph.append((r,c))

for i in range(N):
  
  if abs(graph[i][0]-man[0]) == 0 :
    result += abs(graph[i][1]-man[1])
  elif abs(graph[i][0]-man[0])==R:
    result += min(graph[i][1]+man[1],C-graph[i][1]+C-man[1])+R
  elif abs(graph[i][1]-man[1])==0:
    result += abs(graph[i][0]-man[0])
  elif abs(graph[i][1]-man[1])==C:
    result += min(graph[i][0]+man[0], R-graph[i][0]+R-man[0])+C
  else:
    result += abs(graph[i][0]-man[0])+abs(graph[i][1]-man[1])

print(result)

