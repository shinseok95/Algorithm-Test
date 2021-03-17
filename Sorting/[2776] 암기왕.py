import sys

T = int(sys.stdin.readline())

for _ in range(T):

  N = int(sys.stdin.readline())
  
  data1 = set(map(int,sys.stdin.readline().split()))

  M = int(sys.stdin.readline())

  data2 = list(map(int,sys.stdin.readline().split()))

  for d in data2:
    print(1) if d in data1 else print(0)

  

  
  
  