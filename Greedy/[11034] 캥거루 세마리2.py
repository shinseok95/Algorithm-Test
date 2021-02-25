while True:

  try:
    data = list(map(int,input().split()))

    left= data[1]-data[0]-1
    right= data[2]-data[1]-1
    
    print(right if right>left else left)
    
  except:
    exit()