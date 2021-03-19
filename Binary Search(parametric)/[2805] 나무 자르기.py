import sys

def parametric(trees,N,M):
  
  start = 0
  end = 10**9

  while start <= end:

    mid = (start+end)//2
    target = 0

    for tree in trees:
      
      if tree>mid:
        target += (tree-mid)

    if target>=M:
      start = mid+1
    else:
      end = mid-1
    
  return start-1

N,M = map(int,sys.stdin.readline().split())

trees = list(map(int,sys.stdin.readline().split()))

print(parametric(trees,N,M))