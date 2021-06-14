"""

한 30분 고민하다가 Hash를 이용하여 풀었다.

최대 개수가 1,000,000개
문자열 길이가 최대 20 이므로

hash에 넣는데 20,000,000번
그리고 hash에서 검색하는데 1,000,000번

총 21,000,000번의 연산으로 가능하다
(물론, 문자열 슬라이싱에서 시간이 더 잡히긴 할듯)


그런데 더 좋은 풀이가 있어서 깃허브에 정리해놓았다.

def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

정렬을 하고, zip을 통해 인접한 두 문자열을 비교하는 것이다.
이때, startwith라는 함수가 사용되는데, 해당 문자열이 특정 문자열로 시작하는지 확인해주는 함수다.

개인적으로 정렬을 하면, 시간이 많이 소요된다고 생각했는데, 해당 코드가 훨씬 빠르게 끝났다...
"""

def solution(phone_book):
    
    cnt_dict = dict()
    
    for number in phone_book:
        for i in range(len(number)):
            if cnt_dict.get(number[0:i+1]) == None:
                cnt_dict[number[0:i+1]] = 1
            else:
                cnt_dict[number[0:i+1]] += 1
    
    for number in phone_book:
        if cnt_dict[number] > 1:
            return False
    
    return True