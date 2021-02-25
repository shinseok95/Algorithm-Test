n = int(input())
changes =[]
coins =(25,10,5,1)

for i in range(n):
  changes.append(int(input()))

for change in changes:
  for coin in coins:
    print(change // coin,end=" ")
    change = change % coin
  print() 