import sys

N,K=map(int,sys.stdin.readline().split())

data = []

G=0
S=0
D=0

ans_g=0
ans_s=0
ans_d=0

for i in range(N):
  k,g,s,d = map(int,sys.stdin.readline().split())

  if K == k:
    G=g
    S=s
    D=d
    continue

  data.append((k,g,s,d))

for x in data:
  if x[1]>G:
    ans_g+=1

for x in data:
  if x[1] == G and x[2] > S:
    ans_s+=1

for x in data:
  if x[1] == G and x[2] == S and x[3] > D:
    ans_d+=1

print(ans_g+ans_s+ans_d+1)
