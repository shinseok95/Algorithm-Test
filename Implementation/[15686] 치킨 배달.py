import sys
from itertools import combinations

def calculate(r1,c1,r2,c2):
  return abs(r1-r2)+abs(c1-c2)

N,M = map(int,sys.stdin.readline().split())
graph =[list(map(int,sys.stdin.readline().split())) for _ in range(N)]

chicken = []
house = []
result = sys.maxsize

for i in range(N):
  for j in range(N):
    if graph[i][j] == 1:
      house.append((i,j))
    elif graph[i][j] == 2:
      chicken.append((i,j))
    else:
      continue

c_chicken = list(combinations(chicken,M))

for c in range(len(c_chicken)):
  
  dist = 0
  for h in range(len(house)):
    min_dist = sys.maxsize
    for m in range(M):
      min_dist = min(min_dist,calculate(house[h][0],house[h][1],c_chicken[c][m][0],c_chicken[c][m][1]))
    dist+=min_dist
  
  result = min(result,dist)

print(result)
    