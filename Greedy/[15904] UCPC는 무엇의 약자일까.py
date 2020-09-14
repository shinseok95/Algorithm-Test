"""
반례를 생각하지 않고 단순히 UCPC가 존재하는지만 고려했다가 늦게서야 순서도 고려해야한다는 것을 알아챘다

U는 제일 먼저
C2는 제일 마지막
C1은 U 다음
P는 C1과 C2 사이

이렇게 생각하고 접근하니까 간단하게 풀렸다

앞으로도 무조건 이런 문자열 문제가 나오면 순서에 대한 함정이 있지 않을까 고려해야겠다
"""


data = input()

UCPC=list()
U=-1
C1=-1
P=-1
C2=-1

for c in data:
  if c == 'U' or c== 'C' or c=='P':
    UCPC.append(c)
  else:
    continue

for i in range(len(UCPC)):
  
  if UCPC[i] == 'U':
    U=i
    break

for i in range(len(UCPC)-1,-1,-1):

  if UCPC[i] == 'C':
    C2 = i
    break

for i in range(U+1,C2):
  
  if UCPC[i] == 'C':
    C1=i
    break

for i in range(C1+1,C2):

  if UCPC[i] == 'P':
    P=i
    break

if U != -1 and C1 != -1 and P != -1 and C2 != -1:
  if U<C1<P<C2:
    print("I love UCPC")
else:
  print("I hate UCPC")


  """
  좀 더 좋은 풀이!!
  
  import sys
input = lambda : sys.stdin.readline().rstrip()

arr = input()
check_list = ['U', 'C', 'P', 'C']
check = True

for i in range(len(check_list)):
    if check_list[i] in arr:
        check = True
        idx = arr.find(check_list[i])
        arr = arr[idx + 1:]
    else:
        check = False
        break

if check:
    print('I love UCPC')
else:
    print('I hate UCPC')
  """