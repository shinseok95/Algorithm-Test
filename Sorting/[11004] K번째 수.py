import sys

# Quick selection (O(N))

def quick_selection(arr,start,end,K):
  
  pivot = start
  left = start+1
  right = end
  
  while left<=right:

    while left<=end and arr[pivot]>=arr[left]:
      left+=1
    while right>start and arr[pivot]<=arr[right]:
      right-=1

    if left>right:
      arr[pivot],arr[right] = arr[right],arr[pivot]
    else:
      arr[right],arr[left] = arr[left], arr[right]
  
  if right==K:
    return arr[right]

  elif right>K:
    return quick_selection(arr,start,right-1,K)

  elif right<K:
    return quick_selection(arr,right+1,end,K)
  

N,K = map(int,sys.stdin.readline().split())

data = list(map(int,sys.stdin.readline().split()))

print(quick_selection(data,0,len(data)-1,K-1))