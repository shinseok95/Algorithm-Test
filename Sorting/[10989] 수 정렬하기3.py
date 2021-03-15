import sys

SIZE = 10001
N = int(sys.stdin.readline())
data = [0]*SIZE

for _ in range(N):
  data[int(sys.stdin.readline())]+=1

for i in range(1,SIZE):
  for _ in range(data[i]):
    sys.stdout.write(str(i)+'\n')
