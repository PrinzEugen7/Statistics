function randInt(max, min)
{
	return Math.floor(( Math.random() * ( ( max + 1 ) - min ) ) + min);
}

// メイン
function main()
{
	y = randInt(10, 30);
	alert( y );
}
