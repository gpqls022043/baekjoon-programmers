#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main()
{
	char ch[100];

	scanf("%s", &ch);

	printf("%d", strlen(ch));

	return 0;
}