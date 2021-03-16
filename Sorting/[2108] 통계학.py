import sys

N = int(sys.stdin.readline())

sum_value = 0
data = []
count = dict()

for _ in range(N):
  tmp = int(sys.stdin.readline())

  sum_value += tmp

  if count.get(tmp)==None:
    count[tmp] = 1
  else:
    count[tmp] += 1

  data.append(tmp)

data.sort()

values = list(count.values())
items = list(count.items())

C=[]

for item in items:
  
  if item[1] == max(values):
    C.append(item[0])

C.sort()

A = int(round(sum_value/N))
B = data[len(data)//2]
D = max(data)-min(data)

print(A)
print(B)

if len(C)==1:
  print(C[0])
else:
  print(C[1])

print(D)
