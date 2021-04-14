import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):

  funcs = sys.stdin.readline().rstrip()
  size = int(sys.stdin.readline())

  if size == 0: 
    if 'D' in funcs:
      sys.stdin.readline().rstrip()
      sys.stdout.write('error\n')

      continue
      
  numbers = sys.stdin.readline().rstrip()
  numbers = list(numbers[1:-1].split(","))
  numbers=deque(numbers)

  # True : 왼쪽 / False : 오른쪽
  direction = True
  error_flag= False

  for f in funcs:

    if f == 'R':
      direction = not direction
    else:
      if numbers:
        if direction :
          numbers.popleft()
        else:
          numbers.pop()
      else:
        error_flag = True
        break

  if error_flag:
    sys.stdout.write('error\n')
  else:
    if not direction :
      numbers.reverse()

    print("[",",".join(numbers),"]",sep="")
  
  
    
        