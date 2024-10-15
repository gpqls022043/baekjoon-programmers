#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	char word[100] = { 0 };
	int num = 0;
	int length = 0;

	scanf("%s", word);

	for (int i = 0; i < sizeof(word); i++)
	{
		if (word[i] != NULL) length += 1;
		else break;
	}

	for (int i = 0; i < length; i++)
	{
		if (word[i] == 'c')
		{
			if (word[i + 1] == '=')
			{
				num += 1;
				word[i + 1] = ' ';
				i += 1;
			}
			else if (word[i + 1] == '-')
			{
				num += 1;
				word[i + 1] = ' ';
				i += 1;
			}
			else num += 1;
		}
		else if (word[i] == 'l')
		{
			if (word[i + 1] == 'j')
			{
				num += 1;
				word[i + 1] = ' ';
				i += 1;
			}
			else num += 1;

		}
		else if (word[i] == 'n')
		{
			if (word[i + 1] == 'j')
			{
				num += 1;
				word[i + 1] = ' ';
				i += 1;
			}
			else num += 1;
		}
		else if (word[i] == 's')
		{
			if (word[i + 1] == '=')
			{
				num += 1;
				word[i + 1] = ' ';
				i += 1;
			}
			else num += 1;
		}
		else if (word[i] == 'z')
		{
			if (word[i + 1] == '=')
			{
				num += 1;
				word[i + 1] = ' ';
				i += 1;
			}
			else num += 1;
		}
		else if (word[i] == 'd')
		{
			if (word[i + 1] == '-')
			{
				num += 1;
				word[i + 1] = ' ';
				i += 1;
			}
			else if (word[i + 1] == 'z')
			{
				if (word[i + 2] == '=')
				{
					num += 1;
					word[i + 2] = ' ';
					i += 2;
				}
				else num += 1;
			}
			else num += 1;
		}
		else
		{
			num += 1;
		}
	}

	printf("%d", num);
}