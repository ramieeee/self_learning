#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int chbase(int num)
{
    int stack = 0;
    while (num > 0)
    {
        stack = (stack * 3) + (num % 3);
        num /= 3;
    }
    return (stack);
}

int solution(int num)
{
    return (chbase(num));
}
