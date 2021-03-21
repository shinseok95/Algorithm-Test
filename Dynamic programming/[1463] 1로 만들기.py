"""
처음에 n%3->n%2->n-1 순으로 최소 연산 횟수를 보장해주는 줄 알았다. 그래서 Top-down 방식으로 접근했으나, 이 방법은 틀렸었다.

예를 들어, 10인 경우가 반례다.
10->5->4->2->1 (4번)
10->9->3->1 (3번)

그렇다면 3가지 연산 중에 어떤 것이 최소 연산 횟수를 보장해주는 지 모르기 때문에, Bottom-up 방식으로 접근해서 세 가지 경우 중 가장 적은 연산 횟수를 선택하는 방식으로 접근해야해

"""

N = int(input())
cache = [0]*(N+1)

for n in range(2,N+1):

  value=10**9
  
  if n%3==0:
    value = 1 + cache[n//3]
  if n%2==0:
    value = min(value,1+cache[n//2])
  
  value = min(value,1+cache[n-1])

  cache[n] = value

print(cache[N])