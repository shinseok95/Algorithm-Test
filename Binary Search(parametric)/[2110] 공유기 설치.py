import sys 

def parametric(data,N,C):

  start = 1
  end = data[-1]-data[0]+1

  while start<=end:
    
    mid = (start+end)//2
    count = 0
    distance = 0

    for d in data:
      
      if d<distance:
        continue
      else:
        distance = (d+mid)
        count += 1

    if count<C:
      end = mid-1
    else:
      start = mid+1
    
  return start-1


N,C = map(int,sys.stdin.readline().split())

data = []

for _ in range(N):
  coordinates = int(sys.stdin.readline())

  data.append(coordinates)

data.sort()

print(parametric(data,N,C))
