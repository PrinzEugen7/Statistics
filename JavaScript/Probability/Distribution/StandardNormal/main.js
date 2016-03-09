// 正規分布の計算
var normRand = function (m, s) {
    var a = 1 - Math.random();
    var b = 1 - Math.random();
    var c = Math.sqrt(-2 * Math.log(a));
    if(0.5 - Math.random() > 0) {
        return c * Math.sin(Math.PI * 2 * b) * s + m;
    }else{
        return c * Math.cos(Math.PI * 2 * b) * s + m;
    }
};

// メイン
function main()
{
	var N = 10;	// サンプル数
	var Y = [];
	// サンプル数Nだけ標準正規分布を求める
	for (var i = 0; i < N; i++) {
		Y[i] = normRand(0, 1);
	}
	// 計算結果の表示
	alert(Y);
}
