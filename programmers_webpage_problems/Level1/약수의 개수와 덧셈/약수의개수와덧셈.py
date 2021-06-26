def prime_count(num):
    count = 0
    for i in range(num):
        if (num) % (i + 1) == 0:
            count += 1
    return count

def solution(left, right):
    answer = 0
    while (left <= right):
        if prime_count(left) % 2 == 0:
            answer += left
        else:
            answer -= left
        left += 1
    
    return answer
