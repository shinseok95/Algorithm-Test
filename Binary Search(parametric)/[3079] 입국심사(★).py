import sys

def parametric(mans,N,M):
  
  start = 1
  end = max(mans)*M
  result = 0

  while start<=end:
    
    mid = (start+end)//2
    count = 0
    
    for man in mans:
      
      count += (mid//man)

    if count<M:
      start = mid+1
    else:
      end = mid-1
      result = mid
  
  return result
    
N,M = map(int,sys.stdin.readline().split())

mans= []

for _ in range(N):
  
  man = int(sys.stdin.readline())
  mans.append(man)

mans.sort()

print(parametric(mans,N,M))


  