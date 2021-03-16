N,M = map(int,input().split())
data = dict()
result = []

for _ in range(N+M):
  name = input()

  if data.get(name) == None:
    data[name] = 1
  else:
    data[name] +=1

for item in data.items():
  
  if item[1] != 1:
    result.append(item[0])

print(len(result))

for name in sorted(result):
  print(name)