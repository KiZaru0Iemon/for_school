～ インターネットの課題の解析を少し楽にするプログラム ～

１．python3.0以上を使用できる環境にしてください．
２．google chromeブラウザを開いてください．(その他のブラウザの動作確認はしていません。)
３．調べたいurlを検索
４．デベロッパーツール(検証)を押して、Networkを押す．
５．そこに出てきたリスト上で右クリック
６．"Save all as HAR with content"を押して，名前を変更せずに保存
７．保存したファイルの拡張子をjson拡張子に変更
８．解析したいデータを "json_data" フォルダ にすべて保存
９．カレントディレクトリを"json_analysis.py"と"json_data"を保存したフォルダに"cd"コマンドを利用して変更
10．その後，"python json_analysis.py"とコマンドを
    うって実行すれば、結果が出てくるはず
    (コマンドの"python"というところは実行環境によっては"python3"とか"py"とかになる)

注：１．実行確認が終わった後は，json_dataフォルダの中身を削除し，自分の調べたいデータを入れなおしていってください．
    ２．文字コードの関係で動かない場合があります．(UnicodeErrorみたいのが出ます。)
        その場合は23行目付近の" open_file = open(fname, 'r') "というコードのopen関数部分の引数に
        " open(fname, 'r', encoding='utf-8') "と引数を付け足して見てください。おそらくそれで治ります。
        治んなかったら別の要因が考えられます。
    ３．あくまで下記に記載しているプロトコルしか調べません。そのため、総プロトコル数値と各プロトコル数の合計値が同じになるとは限りません。
    ４．本プログラムはrequestとresopnseのプロトコルは1つのプロトコルと見なして計算しています。
    ５．たまにブラウザからjsonファイルを保存した時に，json形式が完全ではないファイルが保存される場合があるようです。
    そういう場合は，jsonファイル作成工程をやり直してから，システムを実行してみてください．

[ファイル構造↓]
任意のフォルダ------json_analysis.py
               |
               -----json_data------url1.json
                               |
                               ----url2.json
                               |
                               ----url3.json
                               |
                               .
                               .
                               .

[実行結果↓]
==========================
url : (url名)

protocol sum : (総使用プロトコル数)

http/1.0 : (各使用プロトコル数) /(総使用プロトコル数)  (本プロトコル使用割合)
http/1.1 : (各使用プロトコル数) /(総使用プロトコル数)  (本プロトコル使用割合)
http/2.0 : (各使用プロトコル数) /(総使用プロトコル数)  (本プロトコル使用割合)
http/3.0 : (各使用プロトコル数) /(総使用プロトコル数)  (本プロトコル使用割合)
h3-29    : (各使用プロトコル数) /(総使用プロトコル数)  (本プロトコル使用割合)

==========================

[the whole average(全体の平均値)]
http/1.0 : ()%
.
.
.
