def d(n):
  
  if cache[n] != 0 :
    return cache[n]

  if n==0 or n==1:
    cache[n] = 1
  
  else:
    for i in range(n):
      cache[n] += d(i)*d(n-i-1)
  
  return cache[n]

N = int(input())
cache = [0]*(N+1)

print(d(N))