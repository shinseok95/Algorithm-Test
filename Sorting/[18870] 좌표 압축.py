import sys

N = int(sys.stdin.readline())

data = list(map(int,sys.stdin.readline().split()))

sorted_data = sorted(set(data))

comp = dict()
rank = 0

for i in range(len(sorted_data)):
  comp[sorted_data[i]] = rank
  rank+=1

for i in range(N):
  print(comp[data[i]],end=' ')