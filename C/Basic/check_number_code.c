#include <stdio.h>

int main(void)
{
	// 変数の宣言
	int num = -78;
	// 数値の符号を調べる
	if (num > 0)
		printf("%dは正", num);
	else if (num == 0)
		printf("%d は0", num);
	else
		printf("%dは負", num);

	return 0;
}
