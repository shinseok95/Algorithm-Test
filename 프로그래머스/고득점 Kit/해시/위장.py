"""

고득점 Kit에서 해시 문제이긴 했는데, 해시는 그다지 중요하지 않은 문제였다.

우선 나는 n개 종류의 옷이 있다면, 경우의 수를 구하기 위해 

nC1 , nC2 , ... nCn을 구한다음 각 종류별로 옷의 개수를 곱해주는 방식을 생각했다.

예를 들어, 3가지 종류의 옷이 있고, 각각은 1,1,2개의 옷이 있을 때, 두 가지 옷을 입을 경우의 수는 (1*1 + 1*2 + 1*2)다.

이를 위해 Combinations 함수를 통해 모든 조합을 구한 뒤, 다 곱해서 더했더니 시간초과가 떴다.

그래서 생각한 내 코드의 문제는 중복된 계산을 한다는 것이었다. 그래서 이를 divide and conqure로 풀기로 했다.

예를 들어, 1,1,1,2의 옷이 있다면

1,1 / 1,2
1 / 1 / 1 / 2

를 한다음 left+right+(left*right)를 해주면 모든 경우의 수가 중복된 계산없이 풀린다.

"""

"""

그런데 다른 사람의 풀이를 보니, 더 충격적인 방법이 있었다.

우선 모든 경우의 수는 다음과 같은 수식으로 풀린다.

 (a + 1)(b + 1)(c + 1) - 1 = (a + b + c) + (ab + bc + ca) + abc

 즉, 1,1,1,2가 있으면, (1+1)*(1+1)*(1+1)*(2+1) -1를 하면 되는 것이었다

 그리고 이를 적용할 수 있는 functools 라이브러리의 reduce 함수 또한 존재하였다.

 reduce(적용할 함수, list, 초기값)을 적용한다면,

 reduce(lambda a,b : a*(b+1), list,1) -1가 된다

 참 사람들 대단하다...

"""

"""

다른 사람 풀이

def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer

"""

def divide_and_conqure(array,left,right):
    
    if left == right:
        return array[left]
    
    mid = (right+left)//2
    
    left_value = divide_and_conqure(array,left,mid)
    right_value = divide_and_conqure(array,mid+1,right)
    
    return left_value + right_value + (left_value * right_value)

def solution(clothes):
    spy = dict()
    
    for cloth in clothes:
        if spy.get(cloth[1]) == None:
            spy[cloth[1]] = 1
        else:
            spy[cloth[1]]+=1
    
    spy_clothes = list(spy.values())
    
    return divide_and_conqure(spy_clothes,0,len(spy_clothes)-1)