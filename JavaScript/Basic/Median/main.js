function calc_median(data) 
{
    var half = (data.length/2)|0;
    var temp = data.sort(fn);

    if (temp.length%2) {
        return temp[half];
    }

    return (temp[half-1] + temp[half])/2;
}

// メイン
function main()
{
	data = new Array(1, 2, 3, 4, 5); 
	alert( "計算結果　:　" + calc_median(data) );
}
