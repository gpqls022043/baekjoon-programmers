#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int num1 = 0;
	int num2 = 0;
	int i = 0;
	int result = 0;
	int count = 0;
	int arr[100] = { 0 };

	scanf("%d", &num1);
	scanf("%d", &num2);

	for (i = 0; i * i <= num2; i++) {
		if (num1 <= i * i && i * i <= num2) {
			result += i * i;
			arr[i] = i * i;
		}
		else {
			continue;
		}
	}

	if (result == 0) {
		printf("-1");
	}
	else {
		printf("%d\n", result);
		while (1) {
			count++;
			if (arr[count] != 0) {
				printf("%d", arr[count]);
				break;
			}
		}
	}
}