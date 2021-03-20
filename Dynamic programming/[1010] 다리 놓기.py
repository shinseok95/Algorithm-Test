T = int(input())

for _ in range(T):
  N,M = map(int,input().split())

  table = [[0] * (M+1) for _ in range(N+1)]

  for i in range(1,M+1):
    table[1][i] = i

  for i in range(2,N+1):
    for j in range(i,M+1):
      table[i][j]=sum(table[i-1][i-1:j])
  
  print(table[N][M])
  
