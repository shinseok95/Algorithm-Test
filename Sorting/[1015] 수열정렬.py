N = int(input())

A = list(map(int,input().split()))

B = [[i,A[i]] for i in range(N)]

C = sorted(B,key=lambda x : x[1])

D = [[C[i][0],C[i][1],i] for i in range(N)]

E = sorted(D,key=lambda x : x[0])

for i in range(N):
  print(E[i][2],end=' ')