import sys

def parametric(daily,N,M):

  start = max(daily)
  end = (start*N)
  result = 0

  while start<=end:
    
    mid = (start+end)//2
    wallet = 0
    m = 0

    for money in daily:
      
      if money<=wallet:
        wallet -= money
      else:
        wallet = (mid - money)
        m+=1

    if m<=M:
      end= mid-1
      result = mid
    else:
      start = mid+1

  return result
        
N,M = map(int,sys.stdin.readline().split())

daily = []

for _ in range(N):
  money = int(sys.stdin.readline().rstrip())
  daily.append(money)

if N==M:
  print(max(daily))
elif M==1:
  print(sum(daily))
else:
  print(parametric(daily,N,M))