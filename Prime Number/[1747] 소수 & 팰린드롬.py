import sys

max_value = 1003001
prime_bool_list = [True for i in range(max_value+1)]
prime_list = []

for i in range(2,int(max_value**0.5)+1):

  if prime_bool_list[i]:
    j = 2
    
    while i*j<=max_value:
      prime_bool_list[i*j] = False
      j+=1

for i in range(2,max_value+1):
  if prime_bool_list[i]:
    prime_list.append(i)

N = int(sys.stdin.readline())

for prime in prime_list:

  if prime < N:
    continue
  
  flag = True

  prime_str_list = list(str(prime))
  length = len(prime_str_list)
  for i in range((length//2)):
    if prime_str_list[i] != prime_str_list[length-i-1]:
      flag = False
      break
  
  if flag:
    print(prime)
    break

"""
더 좋은 풀이

import math
n = int(input())
if n==0 or n==1:
    n=2
def prime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
while True:
    if str(n)==str(n)[::-1]:
        if (prime(int(n))):
            print(n)
            break
    n+=1
"""