---
title: "Plugins"
linkTitle: "Plugins"
description: https://plugins.embulk.org/
date: 2020-07-08T00:00:25+09:00
---

## About

- [Built-In Plugins](https://www.embulk.org/docs/built-in.html)
- https://plugins.embulk.org/ ... embulk org公式提供のものもあるが、コアに含まれていないものはこちら

## Input Plugins

一覧: https://plugins.embulk.org/#input

### MySQL

https://github.com/embulk/embulk-input-jdbc/tree/master/embulk-input-mysql

公式プラグイン。

Config（一部）:

 key | description
-----|-------------
 select | SELECT句に渡すカラムリストをカンマ区切り文字列で渡す。デフォルトは `*`
 options | JDBCに渡す追加オプション。詳細は後掲
 column_options | See below

HINTS:

- 特定のカラムを対象から外したいときは `select` で指定すればよい。 `column_options` にはそういうオプションはなさそう

#### options

JDBCに渡す追加オプション。

 key | default | description
-----|---------|-------------
 tinyInt1isBit | true | デフォルトだと `TINYINT(1)` はBOOL値とみなされるが、falseにするとちゃんとMySQLに入っているバイト値を読んでくれる

参考:

- [Problem with MySQL TINYINT(1) type · Issue #53 · embulk/embulk-input-jdbc](https://github.com/embulk/embulk-input-jdbc/issues/53)

#### column_options

MySQLの各カラムに対する変換方法を指定することができる。

 key | value | description
-----|-------|-------------
 type | 例: `string, boolean, timestamp` | embulk内で処理するときにこの型として扱われる。デフォルトは自動変換。自動変換で都合が悪いときは指定が必要になる
 timestamp_format | 例: `%Y-%m-%d %H:%M:%S` | MySQLでDATE, TIME, DATETIME型で、かつ、embulk内で `string` 型として処理される場合にこの書式が使われる
 timezone | 例: `"+0900"` | MySQLでDATE, TIME, DATETIME型で、かつ、embulk内で `string` 型として処理される場合に有効になり、このタイムゾーンの値としてフォーマットされる

## Output Plugins

一覧: https://plugins.embulk.org/#output

### BigQuery

https://github.com/embulk/embulk-output-bigquery

Configuration（一部）:

 Property | Type | required? | Default | Description
----------|------|-----------|---------|-------------
 mode | string | optional | "append" | 追記、入れ替えなどいくつかのモードがある
 project | string | 基本的にY | | GCP PROJECT_ID
 dataset | string | Y | | BQ dataset
 table | string | Y | | BQ table
 schema_file | string | optional | | path/to/schema.json
 source_format | string | Y | "CSV" | 他には "NEWLINE_DELIMITED_JSON"
 compression | string | optional | "NONE" | ローカルファイルを圧縮するかどうか（"GZIP" or "NONE"）

参考:

- [EmbulkのGCS/BigQuery周りのプラグインについて](https://www.slideshare.net/oreradio/embulk-plugin-gcs-bigquery) ... 2015年作者による発表資料

#### Formatterの性能問題

https://github.com/embulk/embulk-output-bigquery#formatter-performance-issue に書かれている問題。

レコードをCSVやJSONにフォーマットする機能があるが、組み込みのプラグインはJRubyで書かれていて、Javaのものより遅いので、Javaで書かれたFilterプラグインを使うといいとのこと。

例:

- [civitaspo/embulk-filter-to_json](https://github.com/civitaspo/embulk-filter-to_json)
- [civitaspo/embulk-filter-to_csv](https://github.com/civitaspo/embulk-filter-to_csv)

#### BQの4GB制限への対応

2015年4月からイシューが積まれている https://github.com/embulk/embulk-output-bigquery/issues/6

ワークアラウンド:

- [Local Executor](#local)のオプションによってファイル分割数を上げる
- 非圧縮オプションを使う。これで5TBまで行ける

参考:

- [割り当てと上限 | BigQuery | Google Cloud](https://cloud.google.com/bigquery/quotas?hl=ja#load_jobs)
- [embulk-output-bigqueryプラグインでBQの4GB制限に引っ掛かる場合の対処方法 - Qiita](https://qiita.com/progrhyme/items/e8507c892f9e923cf5f3)

#### OutputPlugin 'bigquery' is not found

たまに起こるエラー。連続でジョブを動かしていると起こりやすいような気がする。  
GitHubでembulk本体にイシューが上がっている:

- [Sometimes failed to run(can not copy embedded jar to temp directory) · Issue #1148 · embulk/embulk](https://github.com/embulk/embulk/issues/1148)

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">EmbulkでBigQueryにExportしてると、体感7回に1回ぐらいこれが出るな。<a href="https://t.co/mozaRkl6vx">https://t.co/mozaRkl6vx</a></p>&mdash; progrhyme (@progrhyme) <a href="https://twitter.com/progrhyme/status/1280795278040170497?ref_src=twsrc%5Etfw">July 8, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

ワークアラウンド:

- イシューの下の方にあるように、 `GEM_HOME` 環境変数の設定と `gem jruby-openssl` のインストールで回避できる
- リトライで成功することもあるけど、↑の方が確実

中の人によれば、近々bigquery pluginはJavaに書き換えられるとか。

<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">そんなに急いでないので、後日お手隙の際に詳しいことを教えていただけると助かります。(同様の人に改善例があるとお伝えするので)、なお今日の勉強会で発表がありましたが、近々embulk-output-bigqueryはJavaに書き直されてその問題はなくなると思います。(近日がいつかは別として) <a href="https://twitter.com/hashtag/embulk?src=hash&amp;ref_src=twsrc%5Etfw">#embulk</a></p>&mdash; Hiroyuki Sato (@hiroysato) <a href="https://twitter.com/hiroysato/status/1281128725317181441?ref_src=twsrc%5Etfw">July 9, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

## File Formatter Plugins

一覧（コアにないもの）: https://plugins.embulk.org/#file-formatter

### CSV

https://www.embulk.org/docs/built-in.html#csv-formatter-plugin

built-in plugin.

Options（一部）

 name | type | default | desription
------|------|---------|------------
 newline_in_field | enum | `LF` | 改行を含む値の中の改行コード

## Executor Plugins

一覧（コアにないもの）: https://plugins.embulk.org/#executor

### Local

https://www.embulk.org/docs/built-in.html#local-executor-plugin

ローカルのスレッドを使ってタスクを実行する。唯一のビルトインExecutor Plugin.

Options:

 name | type | default | description
------|------|---------|-------------
 max_threads | integer | 2x CPUコア数 | 最大並行スレッド数
 min_output_tasks | integer | 1x CPUコア数 | ページ分割を伴う最小の出力タスク数

Example:

```YAML
exec:
  max_threads: 8         # run at most 8 tasks concurrently
  min_output_tasks: 1    # disable page scattering
in:
  type: ...
  ...
out:
  type: ...
  ...
```
