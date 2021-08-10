def solution(score):
    answer = ''
    n = 0
    m = 0
    for i in range(len(score)):
        temp = []

        for j in range((len(score))):
            temp.append(score[j][i])
        if score[n][m] == max(temp):
            if temp.count(max(temp)) == 1:
                temp.remove(max(temp))
        elif score[n][m] == min(temp):
            if temp.count(min(temp)) == 1:
                temp.remove(min(temp))
        n += 1
        m += 1
        avr = sum(temp) / len(temp)
    
        if avr >= 90:
            answer += 'A'
        elif avr >= 80 and avr < 90:
            answer += 'B'
        elif avr >= 70 and avr < 80:
            answer += 'C'
        elif avr >= 50 and avr < 70:
            answer += 'D'
        else:
            answer += 'F'
    return answer
