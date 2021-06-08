import sys

def find(parent,x):
  if parent[x] != x:
    parent[x] = find(parent,parent[x])
  
  return parent[x]

def union(parent,a,b):

  p_a = find(parent,a)
  p_b = find(parent,b)

  if p_a < p_b:
    parent[p_b] = p_a
  else:
    parent[p_a] = p_b

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
edges = []

for i in range(N):
  edge = list(map(int,sys.stdin.readline().split()))
  
  for j in range(i+1,N):
    if edge[j] == 1:
      edges.append((i+1,j+1))

plan = list(map(int,sys.stdin.readline().split()))

parents = [-1] * (N+1)

for i in range(1,N+1):
  parents[i] = i

for a,b in edges:
  union(parents,a,b)
for i in range(1,N+1):
  find(parents,i)

flag = False
tmp = parents[plan[0]]

for n in plan:
  if parents[n] != tmp:
    flag = True
    break

if flag:
  print("NO")
else:
  print("YES")
