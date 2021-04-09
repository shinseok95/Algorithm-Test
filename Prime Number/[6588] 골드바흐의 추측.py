import sys

max_value = 1000000
prime_bool_list = [True for i in range(max_value+1)]
prime_list = []

for i in range(2,int(max_value**0.5)+1):
  
  if prime_bool_list[i]:
    j = 2

    while i*j <= max_value:
      prime_bool_list[i*j]=False
      j+=1

for i in range(3,max_value):
  if prime_bool_list[i]:
    prime_list.append(i)

while True:
  
  N = int(sys.stdin.readline())  
  if N == 0:
    break
  
  existed = False

  for i in prime_list:
    if prime_bool_list[N-i]:
      sys.stdout.write("{} = {} + {}\n".format(N,i,N-i))
      
      existed = True
      break
  
  if not existed:
    sys.stdout.write("Goldbach's conjecture is wrong.\n")
