// 合計値を計算
function sum(data)
{
    var sum = 0;
    for (i=0; i<data.length; i++) {
      sum = sum + data[i];
    }
    return (sum);
}

// 平均値を計算
function ave(data)
{
    return (sum(data) / data.length);
}

// 分散値を計算
function varia(data)
{
    var vari = 0;
	var ave = ave(data);    // 平均値
    for (i=0; i<data.length; i++) {
		vari = vari + Math.pow(data[i] - ave, 2);
    }
    return (vari / data.length);
}

// メイン
function main()
{
	data = new Array(1, 2, 3, 4, 5); 
	alert( "計算結果　:　" + varia(data) );
}
