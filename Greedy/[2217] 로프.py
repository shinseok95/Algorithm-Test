N = int(input())
w = []
result = []

for _ in range(N):
  w.append(int(input()))

w.sort()

for i in range(N): 
  result.append((w[i]*(N-i)))

print(max(result))

  
