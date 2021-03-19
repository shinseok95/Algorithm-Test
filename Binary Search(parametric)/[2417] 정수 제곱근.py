import sys

# 파라메트릭 
def parametric(n):

  start = 0
  end = sys.maxsize

  while start<=end:
    
    mid = start + (end-start)/2
    target = mid*mid
    
    if target >= n:
      end = mid-1
    else:
      start = mid+1
  
  return int(end + 1)
      
N = int(input())

print(parametric(N))