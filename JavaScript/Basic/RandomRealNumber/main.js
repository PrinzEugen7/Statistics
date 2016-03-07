function rand_double(max, min)
{
	return ( Math.random() * ( ( max + 1 ) - min ) ) + min;
}

// メイン
function main()
{
	y = rand_double(10, 30);
	alert( y );
}
