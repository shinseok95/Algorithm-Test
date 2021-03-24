"""
파이썬이 아닌 다른 언어에서는 long long형으로 숫자 크기가 커버가 되지 않아 메모이제이션을 사용해야한다고 한다.

그러나 파이썬은 알아서 다 해준다..
편하다..

"""
N,M = map(int,input().split())

mul = 1
div = 1
for i in range(N,(N-M),-1):
  mul *=i

for i in range(1,M+1):
  div *= i

print(mul//div)