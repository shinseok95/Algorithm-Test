import sys
from itertools import combinations

def find(parent,x):
  if parent[x] != x:
    parent[x] = find(parent,parent[x])
  
  return parent[x]

def union(parent,a,b):
  
  p_a = find(parent,a)
  p_b = find(parent,b)

  if parent[p_a] < parent[p_b]:
    parent[p_b] = parent[p_a]
  else:
    parent[p_a] = parent[p_b] 

def cal_dist(x1,y1,x2,y2):
  return ((x2-x1)**2+(y2-y1)**2)**0.5

N = int(sys.stdin.readline())
result = 0

tmp_star = [i for i in range(1,N+1)]
tmp_edges = list(combinations(tmp_star,2))

star = [(0,0)]

for _ in range(N):
  x,y = map(float,sys.stdin.readline().split())
  star.append((x,y))

edges = []

for a,b in tmp_edges:
  edges.append((cal_dist(star[a][0],star[a][1],star[b][0],star[b][1]),a,b))

edges.sort()

parents = [0] *(N+1)

for i in range(1,N+1):
  parents[i] = i

for cost,a,b in edges:
  if find(parents,a) != find(parents,b):
    result+=cost
    union(parents,a,b)

print("%.2f"%result)