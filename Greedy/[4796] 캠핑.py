data = []
result = 0

while True:
  
  tmp_data = list(map(int,input().split()))

  # breaking point check
  if tmp_data[0]== 0 and tmp_data[1] == 0 and tmp_data[2] == 0:
    break

  else:
    data.append(tmp_data)


for i in range(len(data)):
  q = data[i][2] // data[i][1]
  r = data[i][2] % data[i][1]

  result += q*data[i][0]
  
  if r < data[i][0]:
    result+=r
  else:
    result+=data[i][0]

  print(f"Case {i+1}: {result}")
  result =0

  
