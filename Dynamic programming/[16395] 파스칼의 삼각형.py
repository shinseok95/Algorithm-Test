def pascal(n,k):

  if cache[n][k] != 0:
    return cache[n][k]

  if k==0 or n==k:
    cache[n][k] = 1
  
  else:
    cache[n][k] = pascal(n-1,k-1)+pascal(n-1,k)

  return cache[n][k]

global cache
N,K = map(int,input().split())

cache = [[0]*(i+1) for i in range(N)]

print(pascal(N-1,K-1))