// 合計値を計算
function sum(data)
{
    var sum = 0;
    for (i=0; i<data.length; i++) {
      sum = sum + data[i];
    }
    return (sum);
}

function main()
{
	data = new Array(1, 2, 3, 4, 5); 
	alert( "計算結果　:　" + sum(data) );
}
