#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int len(char *s)
{
    int i = 0;
    
    while (*s)
    {
        s++;
        i++;
    }
}

int solution(const char *s)
{
    int answer = 0;
    int neg = 1;
    
    while (*s == '-' || *s == '+')
    {
        if (*s == '-')
            neg *= -1;
        else if (*s == '+')
            neg *= 1;
        s++;
    }
    while (*s >= '0' && *s <= '9')
    {
        answer = (answer * 10) + (*s - '0');
        s++;
    }
    return (neg * answer);
}
