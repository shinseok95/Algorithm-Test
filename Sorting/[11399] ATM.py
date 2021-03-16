import sys

N = int(sys.stdin.readline())

P = list(map(int,sys.stdin.readline().split()))
P.sort()

result = sum([P[i]*(N-i) for i in range(N)])

print(result)
