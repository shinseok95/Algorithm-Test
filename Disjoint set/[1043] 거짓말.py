
import sys

def find(parent,x):

  if parent[x] != x:
    parent[x] = find(parent,parent[x])

  return parent[x]

def union(parent,a,b):

  A = find(parent,a)
  B = find(parent,b)
  
  if A<B:
    parent[B] = A
  else:
    parent[A] = B

N,M = map(int,sys.stdin.readline().split())

edge = list(map(int,sys.stdin.readline().split()))
edge = edge[1:]
parent = [i for i in range(N+1)]
party = []

count  = 0

for i in edge:
  union(parent,0,i)

for _ in range(M):
  edge = list(map(int,sys.stdin.readline().split()))
  edge = edge[1:]
  party.append(edge)

  for i in range(len(edge)):
    for j in range(i+1,len(edge)):
      union(parent,edge[i],edge[j])

    for i in range(N+1):
      find(parent,i)

for i in range(M):
  
  flag = True

  for j in party[i]:
    if parent[j] == 0:
      flag = False
      break
  
  if flag:
    count+=1

print(count)
