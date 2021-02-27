def func(account):

  global result
  global flag

  if account ==0:
    return

  if account%2 == 0:

    # 4로 나눠떨어지는 경우, 전부 A
    if account%4 ==0:
      result+=('A'*account)

    # 4로 안나눠떨어지는 경우, AAAA,BB 조합
    else:
      result+=('A'*(account-2))+'BB'

  else:
    flag = False

board = input()
flag = True
result=''
account =0

for c in board:
  
  # X case
  if c == 'X':
    account+=1
    continue

  # . case
  else:
    func(account)
    result+='.'
    account =0


func(account)

if flag:
  print(result)
else:
  print(-1)