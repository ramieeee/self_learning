def solution(array, comm):
    answer = []
    for i in range(len(comm)):
        temp = sorted(array[comm[i][0] - 1:comm[i][1]])
        answer.append(temp[comm[i][2] - 1])
    return answer
