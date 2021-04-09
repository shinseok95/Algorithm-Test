import sys

max_value = 10000
prime_bool_list = [True for i in range(max_value+1)]
prime_list = []

for i in range(2,int(max_value**0.5)+1):
  
  if prime_bool_list[i]:
    j = 2

    while i*j <= max_value:
      prime_bool_list[i*j]=False
      j+=1

for i in range(2,max_value):
  if prime_bool_list[i]:
    prime_list.append(i)

T = int(sys.stdin.readline())

for _ in  range(T):

  N = int(sys.stdin.readline())

  left = 0
  right = 0

  for i in prime_list:
    if prime_bool_list[N-i]:

      if i<=N-i:
        left = i
        right = N-i
      else:
        break

  sys.stdout.write("{} {}\n".format(left,right))

