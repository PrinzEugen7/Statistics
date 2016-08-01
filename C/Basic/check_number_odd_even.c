#include <stdio.h>

int main(void)
{
	// 変数の宣言
	int num = 78;
	// 奇数か偶数か判定
	if (num % 2 == 0)
		printf("%dは偶数", num);
	else
		printf("%dは奇数", num);

	return 0;
}
