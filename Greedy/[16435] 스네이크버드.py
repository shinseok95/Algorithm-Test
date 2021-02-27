N, L = map(int,input().split())
H = list(map(int,input().split()))

H.sort()

while len(H)>0:
  
  if H[0]<=L:
    L+=1
    H.pop(0)
  
  else:
    break

print(L)