N,M = map(int,input().split())

if N>=3:
  if M>=7:
    print(M-2)

  else:
    print(M if M<4 else 4)

elif N==2:
  print(((M+1)//2) if ((M+1)//2)<4 else 4)

else:
  print(1)

  