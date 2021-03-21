from math import sqrt, floor

def sq(N):

  if cache[N]!=5:
    return cache[N]
  
  n = floor(sqrt(N))

  if  N-(n**2) ==0:
    cache[N] = 1
    return cache[N]
  
  for i in range(n,0,-1):
    count = 1+sq(N-(i**2))
    
    if 0< count <=4 and count < cache[N]:
      cache[N]=count

  return cache[N]

global cache
N = int(input())

cache = [5]*50001

print(sq(N))