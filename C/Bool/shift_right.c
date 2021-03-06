#include <stdio.h>

// 10進数(整数)を2進数（文字列）に変換
char *int2bin(int x)
{
    int i;
    static char bin[40];
    for(i=31; i>=0; i--){
         bin[31-i]= ((x>>i)&1 )+'0';
   }
   bin[32]=0; // 文字列の最後に\0を挿入
   return bin;
}

int main(void)
{
	// 10進数
	int x = 78;
	// 結果表示(2進数)
	printf(" x = %s (%d)\n",int2bin( x ), x );
	printf(" x>>1 = %s (%d)\n",int2bin( x>>1 ), x>>1 );
	return 0;
}
