T = int(input())
P = [0,1]
i=2

while True:
  n = P[i-1]+P[i-2]

  if n > 1000000000:
    break
  else:
    P.append(n)
    i+=1

for _ in range(T):
  N = int(input())
  result = []

  while N!=0:
    for i in range(len(P)-1,-1,-1):
      if P[i]<=N:
        result.append(P[i])
        N-=P[i]
        break
  
  result.reverse()
  print(*result)
      

