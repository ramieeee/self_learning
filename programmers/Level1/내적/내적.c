#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int *a, int a_len, int *b, int b_len)
{
    int answer = 0;
    int i = -1;
    
    while (++i < a_len)
        answer += (a[i] * b[i]);
    return answer;
}
