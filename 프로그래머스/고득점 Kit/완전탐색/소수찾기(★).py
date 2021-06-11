"""

0~9까지의 숫자 7개이므로
총 1,2,3,4,5,6,7개의 조합을 순열로 구하고, 붙인 다음에, 소수임을 판정하였다.

사실 이렇게 풀면 시간이 많이 걸리는데, 경우의 수가 그리 많지 않아서 통과할 수 있었다.
"""

from itertools import permutations

def is_prime(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    
    return True

    
def solution(numbers):
    
    numbers_list = list(numbers)
    numbers_set = set()
    answer = 0
    
    for i in range(1,len(numbers)+1):
        numbers_perm = list(permutations(numbers_list,i))
        
        for j in range(len(numbers_perm)):
            numbers_set.add(int("".join(numbers_perm[j])))
    
    for n in numbers_set:
        if n == 0 or n==1:
            continue
        if is_prime(n):
            answer += 1
    
    return answer