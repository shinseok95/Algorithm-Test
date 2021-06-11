"""
수학적으로 접근해서 풀었다.

노란색의 row수를 1개씩 증가시켜가면서, 사각형 모양으로 만들어지는 경우(yellow % row)를 모두 비교하였다.

갈색은 노란색 사각형의 가로, 세로 길이에 따라 개수가 정해지기 때문에(2*(c+2) + 2*(r+2) - 4), 이를 정해진 갈색 개수와 비교해서 같아지면 그것이 정답이 된다.
"""

def solution(brown, yellow):
    answer = []
    
    for r in range(1,yellow+1):
        if yellow % r == 0:
            c = yellow // r
            if (2*(c+2)) + (2*(r+2)) - 4 == brown:
                answer = [c+2,r+2]
                break
                
    return answer