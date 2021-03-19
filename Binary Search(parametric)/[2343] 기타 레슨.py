import sys

def parametric(lessons,N,M):
  
  start = max(lessons)
  end = sum(lessons)
  result = 0
  
  while start<=end:
    
    mid = (start+end)//2
    remain = 0
    m = 0

    for lesson in lessons:

      if lesson <= remain:
        remain-=lesson
      else:
        remain = (mid - lesson)
        m += 1
        
    if m <= M:
      end = mid-1
      result = mid
    else:
      start = mid+1

  return result
  
N,M = map(int,sys.stdin.readline().split())

lessons = list(map(int,sys.stdin.readline().split()))

if M==1:
  print(sum(lessons))
else:
  print(parametric(lessons,N,M))