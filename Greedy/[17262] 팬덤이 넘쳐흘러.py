N = int(input())

data = []

for i in range(N):
  data.append(tuple(map(int,input().split())))

first_student=sorted(data,key= lambda a:a[1])[0]

last_student=sorted(data,key= lambda a:a[0])[N-1]

result = last_student[0]-first_student[1]

if result <=0:
  print(0)

else :
  print(result)