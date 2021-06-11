def cal(answers, p):
    
    length = len(p)
    cnt = 0
    
    for i in range(len(answers)):
        if p[i%length] == answers[i]:
            cnt+=1
    
    return cnt

def solution(answers):
    answer = []
    cnts = []
    max_cnt = 0
    
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    
    cnts.append((cal(answers,p1),1))
    cnts.append((cal(answers,p2),2))
    cnts.append((cal(answers,p3),3))
    
    cnts.sort(key=lambda x : (-x[0],x[1]))
    
    for i in range(3):
        if cnts[i][0] > 0 :
            max_cnt = max(max_cnt, cnts[i][0])
            
            if max_cnt == cnts[i][0]:
                answer.append(cnts[i][1])
    
    return answer