// 合計値の計算
function calc_sum(data)
{
    var sum = 0;
    for (i=0; i<data.length; i++) {
      sum = sum + data[i];
    }
    return (sum);
}

// 平均値の計算
function calc_ave(data)
{
    return (calc_sum(data) / data.length);
}

// メイン
function main()
{
	data = new Array(1, 2, 3, 4, 5); 
	alert( "計算結果　:　" + calc_ave(data) );
}
