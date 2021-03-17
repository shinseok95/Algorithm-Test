import sys

N = int(sys.stdin.readline())
data_list = [[] for _ in range(51)]

for _ in range(N):
  
  tmp = sys.stdin.readline().rstrip()
  
  sum_value = 0

  for i in range(len(tmp)):
    
    if tmp[i].isdigit():
      sum_value += int(tmp[i])
  
  data_list[len(tmp)].append((sum_value,tmp))

for data in data_list:
  
  length = len(data)

  if length == 0:
    continue
  elif length ==1:
    print(data[0][1])
  else:
    data.sort(key=lambda x : (x[0],x[1]))

    for d in data:
      print(d[1])
