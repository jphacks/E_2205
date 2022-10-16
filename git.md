# 作業ファイルをステージする

```
$ git add ファイル名
$ git add .
```

一括指定はゴミが入らないように注意

## .gitignore

.gitignoreでステージしないファイルを指定することができる

[.gitgnoreの書き方](https://qiita.com/inabe49/items/16ee3d9d1ce68daa9fff)

# ステージの確認をする
```
$ git status
```

コミットにゴミが入らないか確認

## git add の取り消し

### 新規ファイルの取り消し（初回）

```
$ git rm --cached -r .
$ git rm --chahed -r ファイル名
```

### 変更の取り消し（2回目以降）

```
$ git reset HEAD
$ git reset HEAD ファイル名
```

# ステージをコミットする
```
$ git commit -m "emoji_prefix.mdを参考にコミットメッセージ"
```

# コミットをpushする
```
$ git push
```

# ブランチの切り替え
```
$ git checkout ブランチ名
```

# ブランチを切る
```
$ git checkout -b 自分の作りたいブランチ名
作業後↓
$ git add .
$ git commit
$ git push -u origin 自分の作ったブランチ名
```