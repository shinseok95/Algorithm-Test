import sys

def refund(n):

  global data

  if data[n] != -1 :
    return data[n]

  if 1<=n<5:
    if n in [1,3]:
      data[n] = 0
      return data[n]

    else:
      data[n] = n//2
      return data[n]

  if n%5==0:
    data[n] = n//5
    return data[n]

  for i in range(n//5,-1,-1):

    if (n-(5*i)) % 2 == 0:
      data[n] = i + (n-(5*i)) // 2
      return data[n]
    else:

      tmp = refund(n-(5*i))

      if tmp != 0:
        data[n] = i+tmp
        return data[n]

N = int(sys.stdin.readline())
data = [-1]*(N+1)

result = refund(N)

if result == 0:
  print(-1)
else:
  print(result)
