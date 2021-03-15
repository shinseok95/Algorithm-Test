#계수정렬

import sys
N = int(input())
data = [False]*2000001

for i in range(N):
  data[int(sys.stdin.readline()) + 1000000] = True

for i in range(len(data)):
  if data[i]:
    print(i-1000000)