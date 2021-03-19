import sys
from bisect import bisect_left,bisect_right

# bisect 사용 문제

def count_by_range(cards,n):
  left = bisect_left(cards,n)
  right = bisect_right(cards,n)
  
  return right-left

N = int(sys.stdin.readline())

cards = sorted(list(map(int,sys.stdin.readline().split())))

M = int(sys.stdin.readline())

data = list(map(int,sys.stdin.readline().split()))



for n in data:
  print(count_by_range(cards,n),end=' ')