import sys

def find(parent,x):
  if parent[x] != x:
    parent[x] = find(parent,parent[x])
  
  return parent[x] 

def union(parent,a,b):

  p_a = find(parent,a)
  p_b = find(parent,b)

  if money[p_a] > money[p_b]:
    money[p_a] = money[p_b]
  else:
    money[p_b] = money[p_a]

  if p_a < p_b:
    parent[p_b] = p_a
  else:
    parent[p_a] = p_b

N, M, K = map(int,sys.stdin.readline().split())

money = [0]+list(map(int,sys.stdin.readline().split()))

edges = []

for _ in range(M):
  s,e = map(int,sys.stdin.readline().split())
  edges.append((s,e))

parents = [-1] * (N+1)

for i in range(1,N+1):
  parents[i] = i

tmp = set()
result = 0

for a,b in edges:
  union(parents,a,b)
for i in range(1,N+1):
  find(parents,i)

for i in range(1,N+1):
  if parents[i] in tmp:
    continue
  
  tmp.add(parents[i])

for i in tmp:
  result+=money[i]

if K >= result:
  print(result)
else:
  print("Oh no")
