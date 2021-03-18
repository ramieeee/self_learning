#include <stdio.h>

void BubbleSort(int ary[], int len);

int main(void)
{
	int arr[7] = { 1, 2, 3, 4, 5, 6, 7 };
	int i, len;
	len = sizeof(arr) / sizeof(int);

	BubbleSort(arr, len);
	for (i = 0; i < len; i++)
		printf("%d ", arr[i]);

	printf("\n");
	return 0;
}

void BubbleSort(int ary[], int len)
{
	int i, j;
	int temp;

	for (i = 0; i < len - 1; i++)
	{
		for (j = 0; j < (len - i) - 1; j++)
		{
			if (ary[j] < ary[j + 1])
			{
				temp = ary[j];
				ary[j] = ary[j + 1];
				ary[j + 1] = temp;
			}
		}
	}

}