N = int(input())
students = []

for _ in range(N):
  K,H,G = map(int,input().split())
  students.append((K,H,G))

students = sorted(students,key=lambda x : x[2],reverse=True)

print(students[0][0],students[0][1])
print(students[1][0],students[1][1])

if students[0][0] == students[1][0]:

  for i in range(2,len(students)):

    if students[i][0] != students[0][0] and students[i][0] != students[1][0]:

      print(students[i][0],students[i][1])
      break

else:
  print(students[2][0],students[2][1])