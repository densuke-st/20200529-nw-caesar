# シーザー暗号簡易シフトツール

これは、2020/5/29実施のネットワーク技術の課題におけるシーザー暗号を確認するための、簡易コードになっています。

# 使い方

Linux(授業VM)上であれば、gitは普通に使えます。

```
$ git clone https://github.com/densuke-st/20200529-nw-caesar.git
$ cd 20200529-nw-caesar
$ chmod +x ./uncaesar.py
$ ./uncaesar.py
```

あとはテキストとシフト数を渡すことで処理します。
大文字アルファベット部分のみをシフトします。

```bash
$ ./uncaesar.py ./crypt.txt 1
$ ./uncaesar.py ./crypt.txt 2
```

という感じですね。

# ライセンス

こんなものに著作権を付けることはおこがましいですが、私(佐藤 大輔)が一応著作権保持者となります。

Copyright(c) 2020 SATO Daisuke <densuke@st.kobedenshi.ac.jp>

再配布、修正等についてはGPL3に準じます。
