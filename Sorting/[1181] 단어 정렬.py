N = int(input())

values = [[] for _ in range(51)]

for _ in range(N):
  data = input()
  values[len(data)].append(data)

for i in range(1,51):
  values[i]=list(set(values[i]))
  values[i].sort()

  for data in values[i]:
    print(data)  
