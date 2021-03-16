N = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort(reverse=True)

result = sum(list(map(lambda a,b : a*b,A,B)))

print(result)