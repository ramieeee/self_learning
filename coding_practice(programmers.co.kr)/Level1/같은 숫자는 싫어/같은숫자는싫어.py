def solution(arr):
    answer = []
    
    answer.append(arr[0])
    for i in range(len(arr)):
        if arr[i] != answer[len(answer) - 1]:
            answer.append(arr[i])
    return answer
