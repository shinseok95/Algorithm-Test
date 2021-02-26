N, M = map(int,input().split())

boxs = list(map(int,input().split()))
books = list(map(int,input().split()))

result = 0

for book in books:
  
  while len(boxs)>0:
    
    # 2번 case
    if boxs[0] >= book:
      boxs[0] -= book
      break
    
    # 3번 case
    else:
      result += boxs[0]
      boxs.pop(0)

# 남은 박스 용량
result += sum(boxs)

print(result)
