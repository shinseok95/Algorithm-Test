import sys

def parametics(data,N,M):
  
  start = 1
  end = max(data)
  max_value = end

  while start<=end:
    
    mid = (start+end)//2
    target = 0

    for n in data:

      if n <=mid:
        target+=n
      else:
        target+=mid
        
    if mid <= max_value and target == M:
      return mid

    if target<M:
      start = mid+1
    else:
      end = mid-1
  
  return start-1

N = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())

if sum(data) <= M:
  print(max(data))
else:
  print(parametics(data,N,M))