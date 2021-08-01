def solution(x, n):
    answer = [x]
    
    for i in range(n - 1):
        answer.append(x + answer[-1])
    return answer
