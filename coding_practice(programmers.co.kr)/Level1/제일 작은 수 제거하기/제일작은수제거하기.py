def solution(arr):
    answer = arr

    if len(arr) == 1:
        answer = [-1]
        return answer
    answer.remove(min(answer))
    return answer
