// 平均値の計算
function average(data)
{
    var sum = 0;
    for (i=0; i<data.length; i++) {
      sum = sum + data[i];
    }
    return (sum / data.length);
}

// 分散の計算
function varia(data)
{
    var ave = average(data);    // 平均値
    var varia = 0;
    for (i=0; i<data.length; i++) {
        varia = varia + Math.pow(data[i] - ave, 2);
    }
    return (varia / data.length);
}

// メイン
function main()
{
	data = new Array(1, 2, 3, 4, 5); 
	alert( "計算結果　:　" + varia(data) );
}
