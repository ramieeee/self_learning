def solution(s):
    answer = True
    
    if len(s) == 4 or len(s) == 6:
        if s.isdigit() == True:
            return answer
    answer = False
    return answer
