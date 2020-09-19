n,l,k = map(int,input().split())

prob = list()
result =0
count = k

for i in range(n):
  easy, hard = map(int,input().split())
  prob.append((easy,hard))

prob.sort(key = lambda element : element[1])

for i in range(k):
  if prob[0][1] <= l:
    result+=140
    count-=1
    prob.remove(prob[0])
    
  else :
    break

prob.sort(key = lambda element : element[0])

for i in range(count):
  if prob[0][0] <= l:
    result +=100
    prob.remove(prob[0])

print(result)