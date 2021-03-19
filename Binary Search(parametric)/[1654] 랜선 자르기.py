import sys

def parametics(data,K,N):
  
  start =1
  end = 2**31-1

  while start<=end:

    mid = (start+end)//2
    target = 0

    for n in data:
      target += n//mid
    
    if target < N:
      end = mid-1
    else:
      start = mid+1
    
  return end
    
K,N = map(int,sys.stdin.readline().split())
data = []

for _ in range(K):
  data.append(int(sys.stdin.readline()))

print(parametics(data,K,N))