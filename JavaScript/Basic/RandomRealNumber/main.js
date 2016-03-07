function randDouble(max, min)
{
	return ( Math.random() * ( ( max + 1 ) - min ) ) + min;
}

// メイン
function main()
{
	y = randDouble(10, 30);
	alert( y );
}
