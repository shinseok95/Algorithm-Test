D,K = map(int,input().split())

a=1
b=1
A=1
B=1

for i in range(D-2,1,-1):
  tmp = b
  b = a+b
  a = tmp

while a*A<K:
  while a*A + b*B <=K:
    
    if (a*A + b*B) == K:
      print(A)
      print(B)
      exit()
    else:
      B+=1
  A+=1
  B=A

