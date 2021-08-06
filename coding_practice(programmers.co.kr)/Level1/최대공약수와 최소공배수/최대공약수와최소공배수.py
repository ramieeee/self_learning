def solution(n, m):
    answer = [n, m]
    
    for i in range(1, 1000000):
        if m % i == 0 and n % i == 0:
            answer[0] = i
    answer[1] = int(n * m / answer[0])
    return answer
