#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int counting(int num)
{
    int i = 0;
    int count = 0;
    
    while (++i <= num)
        if (num % i == 0)
            count++;
    return (count % 2) ? num * -1 : num;
}

int solution(int left, int right)
{
    int answer = 0;
    
    for (int i = left; i <= right; i++)
        answer += counting(i);
    return (answer);
}
