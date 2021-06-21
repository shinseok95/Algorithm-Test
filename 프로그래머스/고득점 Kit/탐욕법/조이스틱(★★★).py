"""
대충 어떻게 구현해야할지 생각은 났으나, 구현을 하지 못했다...

왼쪽, 오른쪽으로 가는 길에서 가장 가까운 위치에 단어가 있으면, 해당 길으로 가줘야한다.

근데 중요한 점은 위 알고리즘을 A를 제외한 모든 단어들에 대해서 해줘야한다는 점이다.

어렵다..
"""

def cal_up_down(char):
    if ord(char) > ord('N'):
        return ord('Z')-ord(char)+1
    else:
        return ord(char)-ord('A')
    
def solution(name):
    
    change = [cal_up_down(n) for n in name]
    idx = 0
    answer = 0

    while True:
        answer += change[idx]
        change[idx] = 0
        
        if sum(change) == 0:
            break
        
        left, right = 1,1
        while change[idx - left] == 0:
            left += 1
        while change[idx + right] == 0:
            right += 1
        
        answer += left if left<right else right
        idx += -left if left<right else right
        
    return answer