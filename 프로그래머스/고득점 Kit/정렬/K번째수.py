def find(arr,k):
    sorted_arr = sorted(arr)
    return sorted_arr[k-1]

def solution(array, commands):
    answer = []
    for n in range(len(commands)):
        i,j,k = commands[n][0],commands[n][1],commands[n][2]
        answer.append(find(array[i-1:j],k))
    return answer