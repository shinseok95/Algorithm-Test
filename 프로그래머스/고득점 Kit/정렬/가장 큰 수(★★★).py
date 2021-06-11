"""

정렬에서 comparator를 커스텀하는 방법을 몰라서 틀렸다..

functool 라이브러리에서
functool.cmp_to_key(comparator)를 활용하자!!
"""

import functools

def comp(a,b):
    t1, t2 = a+b, b+a
    
    if int(t1) > int(t2) :
        return 1
    elif int(t1) < int(t2):
        return -1
    else:
        return 0

def solution(numbers):
    
    str_numbers = list(map(str,numbers))
    str_numbers.sort(key = functools.cmp_to_key(comp), reverse = True)
    
    answer = "".join(str_numbers)
    
    if int(answer) == 0:
        return "0"
    else:
        return answer