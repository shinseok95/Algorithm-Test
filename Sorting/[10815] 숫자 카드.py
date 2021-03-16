import sys

N = int(sys.stdin.readline())

cards = list(map(int,sys.stdin.readline().split()))

M = int(sys.stdin.readline())

search = list(map(int,sys.stdin.readline().split()))

result = dict()

for card in cards:
  result[card] = True
  
for data in search:

  if result.get(data) == None:
    print(0,end=' ')
  else:
    print(1,end=' ')