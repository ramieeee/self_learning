def solution(arr1, arr2):
    a = arr1
    
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            a[i][j] = arr1[i][j] + arr2[i][j]
    return a
