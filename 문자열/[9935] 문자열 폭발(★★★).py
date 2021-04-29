"""
평소에 문자열은 한번도 풀어본적이 없어서, 전혀 감이 오지 않았다.

그래서 고민하는 것보다는 빠르게 다른 사람의 풀이를 찾아봤고, 스택을 이용함을 알 수 있었다.

간단하게 말하면, 우선 현재 문자를 스택에 넣고 폭팔 문자열의 마지막 문자와 같다면 폭발 문자열만큼 스택에서 꺼내서 확인한다

그리고 만약 동일한 문자열이라면 스택에서 지워주고, 동일하지 않다면 그대로 둔다


처음에는 이 해결방법이 폭발문자열이 ab일 때 aabb같은 연속적인 문자열을 발견할 수 있을까 생각했는데, 폭발문자열의 마지막 문자가 나올때만 체크해주면 되는 것을 알 수 있었다. 
왜냐하면 처음부터 차근차근 마지막 문자와 비교해왔기 때문이다.


다음에 다시 풀어봐야겠다.
"""

import sys

input_string = sys.stdin.readline().rstrip()
bomb_string = sys.stdin.readline().rstrip()
bomb_last = bomb_string[-1]
length = len(bomb_string)
stack = []

for ch in input_string:
  stack.append(ch)

  if ch == bomb_last and ''.join(stack[-length:]) == bomb_string:
    del stack[-length:]

result = ''.join(stack)

if result == '':
  sys.stdout.write("FRULA")
else:
  sys.stdout.write(result)

"""
import sys
from collections import deque

input = sys.stdin.readline

S = list(input().rstrip())
bomb = list(input().rstrip())

temp = deque()

for s in S:
    temp.append(s)

    if len(temp) >= len(bomb):
        check = True

        for i in range(len(bomb)):
            if temp[len(temp)-len(bomb)+i] != bomb[i]:
                check = False

        if check == True:
            for _ in range(len(bomb)):
                temp.pop()
if temp:
    print(("").join(temp))
else:
    print("FRULA")
"""
  
  