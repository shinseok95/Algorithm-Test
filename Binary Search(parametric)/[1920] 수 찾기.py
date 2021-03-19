import sys

def binary_search(A,left,right,target):

  start = left
  end = right

  while start<=end:
    
    mid = (start+end)//2

    if A[mid] == target:
      return True
    
    elif A[mid] > target:
      end = mid-1
    
    else:
      start = mid+1
  
  return False
      

N = int(sys.stdin.readline())

A = sorted(list(map(int,sys.stdin.readline().split())))

M = int(sys.stdin.readline())

data = list(map(int,sys.stdin.readline().split()))

length = len(A)-1

for n in data:
  
  if binary_search(A,0,length,n):
    print(1)
  else:
    print(0)