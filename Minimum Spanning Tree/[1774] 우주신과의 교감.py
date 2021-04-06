"""
기본 최소 신장 트리 문제는 좌표간의 거리가 주어지는 반면, 이 문제는 2차원 좌표가 주어지고 거리 또한 직접 계산해야했다.

그러나 2차원 좌표의 거리만 계산할 수 있다면, (1000*1000)/2의 edge를 만들 수 있고, 이를 통해 최소 신장 트리를 만들면 된다.
"""

import sys
from math import sqrt

def find(x):

  if parent[x] != x:
    parent[x] = find(parent[x])
  
  return parent[x]

def union(a,b):
  
  A = find(a)
  B = find(b)

  if A<B:
    parent[B] = A
  else:
    parent[A] = B

def cal_dist(x1,x2,y1,y2):

  x = (x1-x2)*(x1-x2)
  y = (y1-y2)*(y1-y2)

  return sqrt(x+y)

N,M = map(int,sys.stdin.readline().split())
parent = [i for i in range(N+1)]
gods = [(0,0)]
edges = []
result = 0

for _ in range(N):
  x,y = map(int,sys.stdin.readline().split())
  gods.append((x,y))

for _ in range(M):
  i,j = map(int,sys.stdin.readline().split())

  union(i,j)

for i in range(1,N+1):
  for j in range(i+1,N+1):
  
    dist = cal_dist(gods[i][0],gods[j][0],gods[i][1],gods[j][1])
    edges.append((i,j,dist))

edges.sort(key = lambda x : x[2])

for edge in edges:

  a,b,c = edge

  if find(a) != find(b):
    union(a,b)
    result+=c

print("{:.2f}".format(result))

