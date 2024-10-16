#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int arr[9][9] = { { 0 } };
	int max = 0;
	int x = 0;
	int y = 0;

	for (int j = 0; j < 9; j++)
	{
		for (int i = 0; i < 9; i++)
		{
			scanf("%d", &arr[i][j]);
		}
	}

	for (int j = 0; j < 9; j++)
	{
		for (int i = 0; i < 9; i++)
		{
			if (arr[i][j] >= max)
			{
				max = arr[i][j];
				x = i + 1;
				y = j + 1;
			}
		}
	}

	printf("%d\n", max);
	printf("%d %d", y, x);
}