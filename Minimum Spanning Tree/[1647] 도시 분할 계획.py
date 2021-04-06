"""
해당 문제는 최소 신장 트리 문제다.

그러나 주의해야할 점은 한 마을을 두 마을로 나눈다는 조건이 있다는 것이다.

쉽게 생각하면 두 마을로 나눈 다음 두 마을에서 최소 신장 트리 알고리즘을 사용하면 되지만, 더 쉽게 생각하면 한 마을에서 최
"""

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

N,M = map(int,sys.stdin.readline().split())
parent = [i for i in range(N+1)]
edges = []
dist = []

for _ in range(M):
  a,b,c = map(int,sys.stdin.readline().split())
  edges.append((a,b,c))

edges.sort(key = lambda x : x[2])

for edge in edges:

  a,b,c = edge

  if find(a) != find(b):
    union(a,b)
    dist.append(c)

print(sum(dist[:-1]))