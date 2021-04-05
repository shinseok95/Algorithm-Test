import sys
sys.setrecursionlimit(10**5)

def find(x):
  
  if parent[x] != x:
    parent[x] = find(parent[x])
  
  return parent[x]

def union(A,B):

  a = find(A)
  b = find(B)

  if a<b:
    parent[b] = a
  else:
    parent[a] = b


N,M = map(int,sys.stdin.readline().split())
parent = [i for i in range(N+1)]

for _ in range(M):

  f,a,b = map(int,sys.stdin.readline().split())

  if f == 0:
    union(a,b)
  else:
    if find(a) == find(b):
      sys.stdout.write('YES\n')
    else:
      sys.stdout.write('NO\n')