"""
https://programmers.co.kr/learn/courses/30/lessons/60057

리스트 슬라이싱을 통해 단계적으로 진행해나가는 문제다.

우선 문자열의 개수가 1000개 이하라는 것에서 완전탐색으로 접근할 수 있다는 것을 알 수 있다.

그리고 점차적으로 Step을 늘려가며, 문자열을 확인해나간다면 간단히 풀 수 있다.

그러나 이러한 아이디어를 떠올리기는 하였으나, 직접 구현하는데 실패했다.

많은 문제를 풀어가며 구현 능력을 키워야겠다고 다시 한 번 느낀다.

"""

def solution(s):
    answer = len(s)
    
    for step in range(1,len(s)//2+1):
        
        compressed=""
        prev = s[0:step]
        count =1
        
        for j in range(step,len(s),step):
            
            if prev == s[j:j+step]:
                count +=1
            else:
                compressed += str(count)+prev if count>=2 else prev
                prev = s[j:j+step]
                count=1
        compressed += str(count) +prev if count>=2 else prev
        
        answer = min(answer,len(compressed))

    return answer