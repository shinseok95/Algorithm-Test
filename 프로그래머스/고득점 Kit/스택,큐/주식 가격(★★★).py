"""
처음 내가 생각해낸 방법은 O(N^2)라서 input이 100,000를 풀 순 없었다.

정말 고민하다가, "주식 가격이 감소할 때만 무언가를 하면 되겠구나" 라는 것까지는 도출해냈다
그런데 그걸 어떻게 구현할지를 생각하지 못해서, 다른 사람의 풀이를 보게 됐다.

다른 사람의 풀이는 정말 간단했다.

우선 증가할 때는 stack에 인덱스를 넣어두고, 만약 감소할 때는 스택의 값이 감소할 때의 값보다 크지않은 경우까지 스택을 빼주면 된다.

"""

from collections import deque

def solution(prices):
    length = len(prices)
    answer = [length-i-1 for i in range(len(prices))]
    stack = deque([0])
    
    for i in range(1, len(prices)):
        while stack:
            index = stack[-1]

            if prices[index] > prices[i]:
                answer[index] = i - index
                stack.pop()
            else:
                break
        
        stack.append(i)
        
    return answer