import sys

N = int(sys.stdin.readline())

data = list(map(int,sys.stdin.readline().split()))

X = int(sys.stdin.readline())

counter = dict()
result = 0

for i in range(N):
  counter[data[i]]=(True,i)

for i in range(N):
  
  value = X-data[i]

  if value <=0:
    continue
  else:
    if counter.get(value) != None and counter[value][1]>i:
      result+=1

print(result)