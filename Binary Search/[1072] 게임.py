import math
import sys

# 파라메틱스
def parametic(X,Y,Z):
  
  start = 0
  end = sys.maxsize
  target = 0

  while start<=end:

    mid = (start+end)//2
    target = math.floor(((Y+mid)*100)/(X+mid))

    if target<=Z:
      start = mid+1
    else:
      end = mid-1

  return end+1

X,Y = map(int,input().split())
Z = math.floor((Y*100)/X)

if Z==100 or Z==99:
  print(-1)
else:
  print(parametic(X,Y,Z))