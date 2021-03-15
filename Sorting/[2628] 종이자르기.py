c,r = map(int,input().split())
N = int(input())

ver = [0,r]
hor = [0,c]

ver_length=[]
hor_length=[]
area=[]

for _ in range(N):
  t,n = map(int,input().split())

  if t == 0 :
    ver.append(n)
  else:
    hor.append(n)

ver.sort()
hor.sort()

for i in range(len(hor)-1):
  hor_length.append(hor[i+1]-hor[i])
for i in range(len(ver)-1):
  ver_length.append(ver[i+1]-ver[i])

for i in hor_length:
  for j in ver_length:
    area.append(i*j)

print(max(area))