int is_prime(int num)
{
    int i = num / 2;
    
    if (num <= 1)
        return (0);
    while (i > 1)
    {
        if (num % i == 0)
            return (0);
        i--;
    } 
    return (1);
}

int solution(int nums[], int nums_len)
{
    int answer = 0;
    int i = -1;
    
    while (++i < nums_len - 2)
    {
        int j = i;
        while (++j < nums_len - 1)
        {
            int k = j;
            while (++k < nums_len)
            {
                int a = nums[i] + nums[j] + nums[k];
                if (nums[i] == nums[j] || nums[j] == nums[k] || nums[k] == nums[i])
                    return (0);
                else if (is_prime(a) == 1)
                    answer++;
            }
        }
    }
    return answer;
}
