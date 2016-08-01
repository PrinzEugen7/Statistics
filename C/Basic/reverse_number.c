#include <stdio.h>
     
// 数値を逆順に並び替える
int reverse(int num)
{
    int rev = 0;
    while (num > 0) {
        rev = rev * 10 + num % 10;
        num /= 10;
    }
    return rev;
}
     
int main(void)
{
    // 変数の宣言
    int num = 12345;
    // 逆順に並び替えた結果を出力
    printf("逆順に並べ替えた結果：%d", reverse(num));
    return 0;
}
