"""
Zero의 Case를 다루는 것에 있어서 꽤나 까다로웠다

Case 1 : len(sum1) < len(sum2)
zero를 sum2에 넣어줘야한다.

Case 2 : len(sum1) > len(sum2)
zero를 sum1에 넣어줘야한다

Case 3 : len(sum1) == len(sum2)
앞서 숫자들을 sum1에서부터 넣어줬기 때문에,
같은 자리 수라면 sum1이 sum2이 작을 수 밖에 없다(sort되어있었기 때문)

그렇기에 zero 또한 더 작은 수인 sum1부터 넣어줘야한다. 
"""

while True:
  data = list(map(int,input().split()))
  if data.pop(0) == 0:
    break

  data.sort()
  zero = data.count(0)

  sum1=list()
  sum2=list()

  for i in range(zero):
    data.pop(0)

  for i in range(len(data)):
    
    if i%2==0:
      sum1.append(str(data[i]))
    else:
      sum2.append(str(data[i]))

  for i in range(zero):
    
    if len(sum1)>len(sum2):
      sum2.insert(1,'0')
    elif len(sum1)<len(sum2):
      sum1.insert(1,'0')
    else:
       sum1.insert(1,'0')
  
  num1 = int(''.join(sum1))
  num2 = int(''.join(sum2))
  print(num1+num2)