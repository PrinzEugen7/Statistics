// 合計値の計算
function calcSum(data)
{
    var sum = 0;
    for (i=0; i<data.length; i++) {
      sum = sum + data[i];
    }
    return (sum);
}

// 平均値の計算
function calcAve(data)
{
    return (calcSum(data) / data.length);
}

// メイン
function main()
{
	data = new Array(1, 2, 3, 4, 5); 
	alert( "計算結果　:　" + calcAve(data) );
}
