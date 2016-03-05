// 平均値を計算
function ave(data)
{
    var sum = 0;
    for (i=0; i<data.length; i++) {
      sum = sum + data[i];
    }
    return (sum / data.length);
}

function main()
{
	data = new Array(1, 2, 3, 4, 5); 
	alert( "平均値　:　" + ave(data) );
}
