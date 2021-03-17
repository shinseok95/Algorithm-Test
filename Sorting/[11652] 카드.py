import sys

N = int(sys.stdin.readline())
data = dict()

for _ in range(N):
  
  number = int(sys.stdin.readline())

  if data.get(number) == None:
    data[number] = 1
  else:
    data[number] += 1

items = list(data.items())

items.sort(key=lambda x : (-x[1],x[0]))

print(items[0][0])