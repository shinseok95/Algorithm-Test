import sys

N = int(sys.stdin.readline())
data = list(map(int,sys.stdin.readline().split()))

left = 0
right = len(data)-1

min_value = sys.maxsize
min_left = 0
min_right = 0

while left<right:
  
  value = data[left]+data[right]

  if value == 0:
    min_left = left
    min_right = right
    break
  elif value < 0:
    
    if abs(value) < abs(min_value):
      min_value = value
      min_left = left
      min_right = right

    left += 1
  
  else:

    if abs(value) < abs(min_value):
      min_value = value
      min_left = left
      min_right = right

    right -= 1

print(data[min_left], data[min_right])