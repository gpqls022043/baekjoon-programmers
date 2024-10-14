#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	char word[100] = { 0 };
	char rword[100] = { 0 };
	int size = 0;
	int tf = 1;

	scanf("%s", word);

	for (int i = 0; i < sizeof(word); i++)
	{
		if (word[i] == 0) break;
		else size += 1;
	}

	for (int i = 0; i < size; i++)
	{
		rword[i] = word[size - 1 - i];
	}

	for (int i = 0; i < size; i++)
	{
		if (word[i] != rword[i])
		{
			tf = 0;
			break;
		}
	}
	
	printf("%d", tf);
}