---
title: "dockerコマンド"
linkTitle: "dockerコマンド"
date: 2020-04-29T12:07:33+09:00
---

リファレンス: https://docs.docker.com/engine/reference/commandline/cli/

## v17.0.3でのコマンド体系再編について

2017年1月にリリースされたv1.13（v17.0.3）でコマンド体系が再編された。  
古いコマンドも2020年4月現在では、まだ使えるものが多そうだが、注意が必要。

参考:
- [docker container / image コマンド新旧比較 - Qiita](http://qiita.com/zembutsu/items/6e1ad18f0d548ce6c266 "docker container / image コマンド新旧比較 - Qiita")

## チートシート
### version, helpの確認

```sh
# Help
docker --help
docker <COMMAND> --help
# client/server version 表示
docker version
```

See also https://docs.docker.com/engine/reference/commandline/version/

### コンテナの起動（実行）

```sh
# コマンド実行
% docker run ubuntu /bin/echo "Hello, world" #=> Hello, world

# bash を起動し、インタラクティブモードになる
% docker run -it ubuntu /bin/bash
root@b171dd1d7831:/# 

# バックグラウンドで hello world を1秒おきに出力し続ける
% docker run -d ubuntu /bin/sh -c "while true; do echo hello world; sleep 1; done"
c6e58ecccfdb5640938443911f85fa301338e0063afe1a13ab0ffc7c93aa7f5f # container id

# Web サーバをホストのエフェメラルポートで動かす
docker run -dP training/webapp python app.py
# Web サーバをホストの 80番ポートで動かす
docker run -d -p 80:5000 training/webapp python app.py
# Web サーバを "web" という名前で動かす
docker run -dP --name web training/webapp python app.py
# Postgres サーバを "db" を、独自ネットワーク上で起動
docker run -d --net my-network --name db training/postgres

# Web サーバに /webapp というボリュームを作って起動
docker run -dP --name web -v /webapp training/webapp python app.py
# + ホストのマウントパス指定
docker run -dP --name web -v /var/lib/docker/volumes/data-webapp:/opt/webapp training/webapp python app.py
# + ホストの共有領域のデータボリュームをディレクトリ名で指定(パスは上と同じになる)
docker run -dP --name web -v data-webapp:/opt/webapp training/webapp python app.py
```

See also [run](#run)

### コンテナ操作(run 以外)

```sh
# コンテナを作成するが起動しない。オプションは run に似ている
docker create [OPTIONS] <IMAGE> [COMMAND]

# 停止
docker stop $NAME_OR_ID
# 再起動
docker start $NAME_OR_ID
# 強制停止
docker kill $ID

# コンテナ上でインタラクティブシェル(bash)実行
docker exec -it db bash

# 作成した停止済みのコンテナを削除
docker rm $NAME_OR_ID
# 停止しているコンテナの全削除。動作中のものはエラーになる
docker rm `docker ps -a -q`
```

### コンテナの情報を見る

```sh
# 動作中のコンテナ表示
docker ps
# 停止しているものも含めて表示
docker ps -a
# 停止していようがいまいが一番最近動かしたやつを表示
docker ps -l

# top
docker top $NAME_OR_ID
# コンテナにマッピングされたホストのポートを表示
docker port $NAME_OR_ID <PORT>

# ログ表示
docker logs $NAME_OR_ID
# ログを tail -f する
docker logs -f $NAME_OR_ID

# コンテナの情報を JSON で dump
docker inspect $NAME_OR_ID
# + クエリで情報を絞り込む例 x 2:
docker inspect --format='{{json .NetworkSettings.Networks}}' $NAME_OR_ID
docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $NAME_OR_ID
```

### コンテナのイメージ操作

```sh
# 変更を施したコンテナからイメージを作成する
docker commit -m "変更についてのコメント" -a "名前 <メアド>" $NAME_OR_ID [<リポジトリ>[:タグ]]
# Dockerfile からイメージ作成
docker build -t リポジトリ:タグ path/to/[Dockerfile]
# イメージにタグを付ける
docker tag $IMAGE_ID リポジトリ:タグ

# リポジトリにあるイメージを検索
docker search <キーワード>
# イメージをリポジトリから取得
docker pull <イメージ>
# イメージをリポジトリに push
docker push リポジトリ

# ローカルにあるイメージ一覧
docker images
# イメージ削除
docker rmi $ID
```

### データボリューム操作

See [volume](#volume)

### ネットワーク操作

See [network](#network)

### 不要なイメージ・ボリューム等の掃除

```sh
# 停止したコンテナを削除
docker container prune
# 不要ボリュームを削除
docker volume prune
# 古いイメージなどを削除
docker image prune
# ネットワークの掃除
docker network prune

# まとめて掃除
docker system prune
```

参考:
- [Dockerのあれこれを断捨離する - Qiita](https://qiita.com/ksato9700/items/b0075dc54dfffc64b999)
- [docker volume pruneコマンドの使い方（実例付）CE対応 | めもたんす](https://www.memotansu.jp/docker/840/)

## リファレンス
### container

コンテナ操作。

```bash
# コンテナ一覧
docker container ls [-a]

# コンテナ停止
docker container stop CONTAINER_ID_OR_NAME

# コンテナ削除
docker container rm CONTAINER_ID_OR_NAME

# 停止したコンテナを全て削除
docker container prune

# コンテナ上でインタラクティブシェル(bash)実行
docker container exec -it CONTAINER_ID_OR_NAME bash
```

### cp

https://docs.docker.com/engine/reference/commandline/cp/

ホスト - コンテナ間でファイル/ディレクトリのコピー

Syntax:

```sh
docker cp [OPTIONS] CONTAINER:SRC_PATH DEST_PATH|-
docker cp [OPTIONS] SRC_PATH|- CONTAINER:DEST_PATH
```

### image

イメージ操作。

```bash
# 一覧
docker image list [-a]

# Dockerfile からイメージ作成
docker image build -t リポジトリ:タグ <Dockerfileがあるディレクトリ>

# イメージ削除
docker image rm IMAGE_ID
```

### network

https://docs.docker.com/engine/reference/commandline/network/

ネットワークの管理

```sh
# ネットワーク一覧
docker network ls
# 特定ネットワークの情報表示
docker network inspect $NW_NAME
# コンテナをネットワークから切断
docker network disconnect $NW_NAME $CONTAINER_NAME_OR_ID
# コンテナをネットワークに接続
docker network connect $NW_NAME $CONTAINER_NAME_OR_ID
# 独自ネットワークを作成
docker network create -d $DRIVER $NW_NAME
```

### run

run はコンテナ起動コマンド。

| オプション | 意味 |
|:--------:|:-----|
| -d, --detach | バックグラウンドでコンテナを動かす |
| -e, --env | 環境変数を1つずつ指定 |
| --env-file <file> | ファイルを指定して、環境変数を設定 |
| -i, --interactive | STDIN を開く |
| --name NAME | コンテナに名前をつける |
| --net NW | ネットワーク NW に配置する。未指定だとデフォルトのネットワークになる |
| -P, --publish-all | コンテナが外部に開くポートをすべてランダムにホストのエフェメラルポートに割当てる |
| -p, --publish=[] | ポートを指定してポートを公開する |
| --privileged | 特権を付与 |
| --restart=&lt;string&gt; | コンテナが既に存在するときの再起動ポリシー。デフォルトは `no`. 他に `always` が指定可能 |
| --rm | コンテナ停止時に削除 |
| -t, --tty | TTY 割当て |
| -v, --volume=[] | データボリュームのマウント |

### volume

https://docs.docker.com/engine/reference/commandline/volume/

データボリュームの管理

```sh
# ボリューム作成
docker volume create [OPTIONS]
# flocker driver を使い my-named-volume という名前で 20GB のボリュームを作成
docker volume create -d flocker --name my-named-volume -o size=20GB

# 一覧
docker volume ls
# dangling volume をリスト
docker volume ls -f dangling=true

# 削除
docker volume rm $VOLUME_NAME
```

## 参考

非公式リファレンス系:
- [Dockerチートシート - Qiita](http://qiita.com/bungoume/items/b8911fd243d9c084bd63)
- [docker コマンド チートシート - Qiita](http://qiita.com/voluntas/items/68c1fd04dd3d507d4083)
- [Dockerコマンドラインリファレンス](https://gist.github.com/hotta/69b476ae6662c5ff67f0)

その他:
- [Dockerで不要になったコンテナやイメージを削除する - @znz blog](http://blog.n-z.jp/blog/2013-12-24-docker-rm.html)
- [(ヽ´ω`) < DockerのOperation not permittedとの戦争 - (ヽ´ω`) < *****](http://www.tsugihagi.net/entry/2014/10/05/083120)
