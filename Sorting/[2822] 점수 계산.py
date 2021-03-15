import sys

data = []
sum_value =0

for i in range(1,9):

  value = int(sys.stdin.readline())
  data.append((i,value))

data.sort(key=lambda x : x[1],reverse=True)

for i in range(5):
  sum_value += data[i][1]

print(sum_value)

for v in sorted(data[:5], key=lambda x : x[0]):
  print(v[0],end=' ')
