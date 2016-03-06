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

// 分散の計算
function calc_var(data)
{
    var ave = calc_ave(data);    // 平均値
    var varia = 0;
    for (i=0; i<data.length; i++) {
        varia = varia + Math.pow(data[i] - ave, 2);
    }
    return (varia / data.length);
}

// 標準偏差の計算
function calc_std(data)
{
    return Math.sqrt(calc_var(data));    // 分散の平方根
}

// メイン
function main()
{
	data = new Array(1, 2, 3, 4, 5); 
	alert( "計算結果　:　" + calc_std(data) );
}
