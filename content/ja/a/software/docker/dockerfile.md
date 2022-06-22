---
title: "Dockerfile"
linkTitle: "Dockerfile"
date: 2020-04-29T12:47:27+09:00
weight: 100
---

- 公式リファレンス: https://docs.docker.com/engine/reference/builder/
- 邦訳: [Dockerfile リファレンス — Docker-docs-ja ドキュメント](http://docs.docker.jp/engine/reference/builder.html "Dockerfile リファレンス — Docker-docs-ja ドキュメント")

## ベストプラクティス

- https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/
  - 邦訳: http://docs.docker.jp/engine/userguide/eng-image/dockerfile_best-practice.html

参考:

- [Introduce that Best practices for writing Dockerfiles](https://www.slideshare.net/ssuser1f3c12/introduce-that-best-practices-for-writing-dockerfiles) ... 2018年12月Japan Container Daysでのモリハヤさんの発表
- [効率的に安全な Dockerfile を作るには - Qiita](http://qiita.com/pottava/items/452bf80e334bc1fee69a "効率的に安全な Dockerfile を作るには - Qiita")


### ADDとCOPY

http://docs.docker.jp/engine/userguide/eng-image/dockerfile_best-practice.html#add-copy

- `COPY` で間に合うときは `COPY` を使うべき
- `ADD` は圧縮ファイルの展開などの機能もある

## .dockerignore

https://docs.docker.jp/engine/reference/builder.html#dockerignore

ADDやCOPYによってDockerイメージに含めたくないファイルを記しておく。

参考:

- [.dockerignore アンチパターン - Qiita](https://qiita.com/munisystem/items/b0f08b28e8cc26132212)

## Syntax
### 環境変数の利用

http://docs.docker.jp/engine/reference/builder.html#environment-replacement

- 全てではないが、一部の命令で環境変数の利用がサポートされている。
- `ENV` 命令で環境変数をセットすることもできる。
- コンテナ実行時に環境変数をセットする際は `docker run` に `-e KEY=${VALUE}` の形で渡す。
  - これらを `CMD` や `ENTRYPOINT` で解釈する際は、exec形式(= `["実行コマンド", "引数"...]`の形式)では展開されないため、シェル形式(= `実行コマンド 引数...`)で記す必要がある。
  - または、ラッパースクリプトを指定するという手もアリだろう。

### Instructions
#### CMD

コンテナのデフォルトの実行コマンド、またはその引数を指定する。 

```Dockerfile
CMD ["実行ファイル", "ARG1", "ARG2", ...] # exec実行形式
CMD ["ARG1", "ARG2", ...] # ENTRYPOINTのデフォルト引数
CMD <コマンド...> # シェル形式
```

- ２番目は `ENTRYPOINT` を指定した時、その引数となる。
  - `docker run <コンテナ> 引数...` として上書きできる
- 1, 3番目の形式は `ENTRYPOINT` と一緒には指定できない（はず…）
  - シェル形式の場合、 `/bin/sh -c` で起動されるようだ

#### ENTRYPOINT

コンテナのデフォルトの実行コマンドを指定する。  

```Dockerfile
ENTRYPOINT ["実行ファイル", "ARG1", "ARG2", ...] # exec形式
ENTRYPOINT 実行ファイル ARG1 ARG2 ... # シェル形式
```

- 上書きするには `--entrypoint <コマンド...>` とする。  
- シェル形式の場合、 `/bin/sh -c` で起動されるようだ
- `CMD` でデフォルト引数を与えると、 `ENTRYPOINT` として指定した「コマンド + 引数」の後に `CMD` として与えた引数がくっつく。

```Dockerfile
FROM ubuntu
ENTRYPOINT ["top", "-b"]
CMD ["-c"]
```

このコンテナを `docker run` で動かすと、 `top -b -c` が実行される。

`CMD` の方はコマンドラインで普通に上書きされる。  
上のDockerfileを `ubuntu-top` としてビルドして例を示す:

```sh
docker run --rm -it ubuntu-top       # top -b -c が実行される
docker run --rm -it ubuntu-top -n 1  # top -b -n 1 が実行される
```

参考:

- [ENTRYPOINTは「必ず実行」、CMDは「（デフォルトの）引数」 | ポケテク](https://pocketstudio.net/2020/01/31/cmd-and-entrypoint/)

#### VOLUME

`docker run` の `-v` オプションに相当。  
ホストのディレクトリをコンテナにマウントする。

参考:

- [DockerのVolume機能について実験してみたことをまとめます \- Qiita](https://qiita.com/namutaka/items/f6a574f75f0997a1bb1d)


## Tips
### CMDとENTRYPOINTがどう作用するか

http://docs.docker.jp/engine/reference/builder.html#cmd-entrypoint
