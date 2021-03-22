"""
1,2,4개의 돌을 가질 수 있다는 조건을 활용해야하는 문제였다.

예들 들어, 돌의 개수가 5개라면, SK가 먼저 시작하기 때문에 CY에게 1,2,4 개의 돌을 줄 수 있다.

만약 1,2,4개의 돌에서 CY가 패배하는 경우의 수만 존재한다면, SK는 먼저 시작하는 이점을 활용하여 그 경우의 수를 선택하므로 승리하게 된다.

즉, 1 = 승리 / 2 = 패배 / 3 = 승리 / 4 = 승리의 조건으로 시작하여 5(1,2,4), 6(2,3,5), 7(3,4,6)처럼 bottom up 방식으로 채워나가면 된다. 

"""

N = int(input())
cache = [True,False,True,True]

if 1<=N<=4:
  if cache[N-1]:
    print('SK')
  else:
    print('CY')

else:
  for i in range(4,N):
    
    n_1 = cache[i-1]
    n_3 = cache[i-3]
    n_4 = cache[i-4]

    if n_1 and n_3 and n_4:
      cache.append(False)
    else:
      cache.append(True)

  if cache[N-1]:
    print('SK')
  else:
    print('CY')

  
