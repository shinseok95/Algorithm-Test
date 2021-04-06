import sys

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

V,E = map(int,sys.stdin.readline().split())
parent = [i for i in range(V+1)]
edges = []
result = 0

for _ in range(E):
  a,b,c = map(int,sys.stdin.readline().split())
  edges.append((a,b,c))

edges.sort(key=lambda x : x[2])

for edge in edges:
  
  a,b,c = edge

  if find(a) != find(b):
    union(a,b)
    result += c

print(result)