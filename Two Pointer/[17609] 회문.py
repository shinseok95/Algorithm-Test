import sys

T = int(sys.stdin.readline())

for _ in range(T):
  string = list(sys.stdin.readline().rstrip())
  
  left = 0
  right = len(string)-1
  left_cnt = 0
  right_cnt = 0
  result = 0

  while left<=right:
    
    if string[left] == string[right]:
      left+=1
      right-=1
    
    else:
      left+=1
      left_cnt+=1
  
  if left_cnt == 0:
    sys.stdout.write('0\n')
  elif left_cnt == 1:
    sys.stdout.write('1\n')
  else:
    left = 0
    right = len(string)-1

    while left<=right:
    
      if string[left] == string[right]:
        left+=1
        right-=1
    
      else:
        right-=1
        right_cnt+=1
  
    if right_cnt == 1:
      sys.stdout.write('1\n')
    else:
      sys.stdout.write('2\n')

    
  