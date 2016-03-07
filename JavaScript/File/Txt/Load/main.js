document.getElementById("drop").addEventListener("drop", onDrop, false);

//  ******** ドロップ時のファイル読み取り処理
function onDrop(event){
	var files = event.dataTransfer.files;
	var disp = document.getElementById("dispData");
	disp.innerHTML ="";

	for(var i=0; i< files.length; i++){
		// FileReaderオブジェクトの生成
		var reader = new FileReader();
		f = files[i];
		reader.onload = function (evt) {
			// FileReaderが取得したテキストをそのままdivタグに出力
			dispData.innerHTML = reader.result;
			// ファイルの情報を表示
			dispFn.innerHTML = "Name：" + f.name; // ファイル名
			dispSize.innerHTML = "Size：" + f.size+"[byte]"; // ファイルサイズ
			dispType.innerHTML = "Type：" + f.type; // ファイルタイプ
		}
		// readAsTextメソッドでファイルの内容を取得
		//reader.readAsText(f, 'shift-jis');
		reader.readAsText(f, 'utf-8');
	}
	// ラウザ上でファイルの展開を抑止
	event.preventDefault();
}

//  ******** ブラウザ上でファイルの展開を抑止
function onDragOver(event){ 
	event.preventDefault(); 
}
