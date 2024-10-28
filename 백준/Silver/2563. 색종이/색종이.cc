#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	char white_board[100][100] = { { 0 } };
	int num, x, y, index_x, index_y;
	int result = 0;

	scanf("%d", &num);

	for (int i = 0; i < num; i++)
	{
		scanf("%d %d", &x, &y);

		index_x = x - 1;
		index_y = y - 1;

		for (int j = index_x; j < index_x + 10; j++)
		{
			for (int k = index_y; k < index_y + 10; k++)
			{
				white_board[j][k] = 'T';
			}
		}
	}

	for (int i = 0; i < 100; i++)
	{
		for (int j = 0; j < 100; j++)
		{
			if (white_board[i][j] == 'T') result += 1;
		}
	}

	printf("%d", result);
}