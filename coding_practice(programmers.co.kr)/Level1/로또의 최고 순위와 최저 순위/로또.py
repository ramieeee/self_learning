def solution(lottos, win_nums):
    answer = [0, 0]
    win_count = 0
    zero_count = 0
    for i in lottos:
        if i == 0:
            zero_count += 1
        for j in win_nums:
            if i == j:
                win_count += 1
    if zero_count + win_count == 0:
        answer[0] = 6
    else:
        answer[0] = 7 - (win_count + zero_count)
        
    if win_count == 0 or win_count == 1:
        answer[1] = 6
    else:
        answer[1] = 7 - win_count
    return answer
