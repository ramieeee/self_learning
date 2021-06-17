#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool solution(const char *s)
{
    bool answer = true;
    int i = 0;
    
    while (s[i] != 0)
    {
        if (s[i] < '0' || s[i] > '9')
            return (false);
        i++;
    }
    if (i == 4 || i == 6)
        return (answer);
    answer = false;
    return (answer);
}
