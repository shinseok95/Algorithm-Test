def dp(n):

  if zero_cache[n] != -1 and one_cache[n] != -1:
    return (zero_cache[n],one_cache[n])

  if n == 0:
    zero_cache[n] = 1
    one_cache[n] = 0
    return (zero_cache[n],one_cache[n])

  elif n == 1:
    zero_cache[n] = 0
    one_cache[n] = 1
    return (zero_cache[n],one_cache[n])

  else:
    zero_f,one_f = dp(n-1)
    zero_s,one_s = dp(n-2)

    zero_cache[n] = zero_f+zero_s
    one_cache[n] = one_f+one_s

    return (zero_cache[n],one_cache[n])

T = int(input())

zero_cache = [-1]*41
one_cache = [-1]*41

for _ in range(T):

  N = int(input())
  
  zero,one= dp(N)
  print(zero,one)
  