#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main()
{
	int t;
	char ch[1000];

	scanf("%d", &t);

	for (int i = 0; i < t; i++)
	{
		scanf("%s", &ch);

		printf("%c%c\n", ch[0], ch[strlen(ch) - 1]);
	}


}