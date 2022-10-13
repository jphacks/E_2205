作業内容をすべてステージする ※余計なものが入らないように注意
$ git add .

作業ファイルをステージする
$ git add ファイル名

ステージの確認をする ※コミットにゴミが入らないか確認
$ git status

ステージをコミットする
$ git commit -m "emoji_prefix.mdを参考にコミットメッセージを書く"

コミットをpushする
$ git push

ブランチの切り替え
$ git checkout ブランチ名

新しく作ってpushしたいときは
$ git checkout -b 自分の作りたいブランチ名
色々作業をしてから↓
$ git add .
$ git commit
$ git push -u origin 自分の作ったブランチ名