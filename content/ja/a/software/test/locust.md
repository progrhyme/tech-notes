---
title: "Locust"
linkTitle: "Locust"
description: https://locust.io/
date: 2020-05-25T18:28:01+09:00
---

Python製で割とよく使われている負荷試験ツール。

## Getting Started

- https://docs.locust.io/en/stable/index.html
  - https://docs.locust.io/en/stable/installation.html
  - https://docs.locust.io/en/stable/quickstart.html

メモ:

- installはpipで。  
- 発射台が1台なら `locust -f path/to/locustfile.py --host=https://your-site.com/` で実行される。 
  - `--no-web` オプションをつけない限りwebサーバが立ち上がり(デフォルトは http://localhost:8089 )、テスト実行状況やメトリクスが見れて便利
- 発射台をmaster + slave複数台で構成することもできる

## Documentation

- APIリファレンス : https://docs.locust.io/en/stable/api.html

## locustコマンド

SYNOPSIS:

```sh
locust -f locustfile.py --host=https://example.com 

locust -f locustfile.py --host=https://example.com  --no-web -c 100 -r 5 -t 30m

## 20分毎に20クライアントずつ増加させる
locust -f locustfile.py --host=https://example.com  --no-web -c 100 -r 5 -t 1h40m \
  --step-load --step-clients 20 --step-time 20m
```

Options:

 Option | Description
----------|-----------------
 -f <LOCUSTFILE>, --locustfile <LOCUSTFILE> | locust python script file
 --no-web | Web UIを起動しない
 -c <クライアント数>, --clients <クライアント数> | 最大同時クライアント数
 -r <HATCH_RATE>, --hatch-rate <HATCH_RATE> | 秒間でいくつクライアントを生成するか
 -t <実行時間>, --run-time <実行時間> | <実行時間> 実行した後、停止する。ex: `300s`, `20m`, `3h`, `1h30m`
 --csv <CSVFILEBASE> | CSVに統計情報を保存
 --logfile <LOGFILE> |
 --step-load | 一定時間ごとにクライアント数を増加させる。--step-clients, --step-timeの指定が必要
 --step-clients <クライアント数> |
 --step-time <時間> |

## Configuration
### locustfile

https://docs.locust.io/en/stable/writing-a-locustfile.html

- Locust class
  - `wait_time` ... クライアントがタスク間に挟むインターバルを設定する
    - https://docs.locust.io/en/stable/api.html#module-locust.wait_time
    - `between(min_wait, max_wait)` ... 最小時間、最大時間の間のランダムな時間
    - `constant(wait_time)` ... 一定時間
    - `constant_pacing(wait_time)` ... 実行時間によらず、一定間隔でタスクを実行する。例えば、 `wait_time = constant_pacing(1)` としたとき、実行時間が0.3秒なら次の待ち時間は0.7秒に、実行時間が0.2秒なら待ち時間は0.8秒になる。


## Features
### Step Load Mode

https://docs.locust.io/en/stable/running-locust-in-step-load-mode.html

`--step-load` オプションを使って、一定時間ごとに負荷を増加させる。

### master-slave構成で分散実行

https://docs.locust.io/en/stable/running-locust-distributed.html

- 1台のマシンでもコアが複数あればマルチコアの恩恵を受けられる

※Qiitaにも書いた。[Locustを1台のマシンで分散実行する（CLI編） - Qiita](https://qiita.com/progrhyme/items/2bf7e9ad24baf2c24951)

Example:

```sh
##!bash

host=
locustfile=yourlocustfile.py
slave_num=15     # slave数（並列数 - 1）
max_clients=200  # 最大クライアント数
duration=90m     # 総実行時間
step_clients=5   # クライアントの増加数 / インターバル
step_interval=1m # インターバル

## master
nohup taskset -c 0 locust -f $locustfile --no-web \
  -c $max_clients -t $duration -H $host \
  --master --expect-slaves $slave_num \
  --step-load --step-clients $step_clients --step-time $step_interval \
  --logfile output/locust.master.log -L WARNING --csv output/locust.master.$(date +'%Y%m%d_%H%M') \
  &> /dev/null &
## slaves
for no in $(seq 1 ${slave_num}); do
  nohup taskset -c $no locust -f $locustfile --no-web \
    -c $max_clients -H $host \
    --slave --master-host 127.0.0.1 \
    --logfile output/locust.slave$no.log -L WARNING --csv output/locust.slave$no.$(date +'%Y%m%d_%H%M') \
    &> /dev/null &
done
```

NOTE:

- master:
  - `--master` オプションを付ける
  - `--expect-slaves=N` オプションで接続を待ち受けるslaveの数を指定する。指定のslave数に達してから試験開始する
  - `--step-load` オプションはmasterで指定する
  - 待受けポート番号を変える場合は `--master-bind-port=<ポート番号>` オプションで。デフォルトは `5557` ポート
- slave:
  - `--slave`, `--master-host <masterのアドレス>` を指定する
  - ポート番号がデフォルトと異なるなら `--master-port=<ポート番号>` オプションで指定

Tips:
- slaveの数を増やすとmasterの負荷が上がる気がする


## How-to
### Locustでプロキシサーバ経由でテストリクエスト送信

https://github.com/locustio/locust/issues/203 によると環境変数を設定するだけでも行けるということなのだが、私が試したときは駄目だったので、下のようにした

```Python
proxies = {}
if 'HTTP_PROXY' in os.environ:
    proxies['http'] = os.environ['HTTP_PROXY']
if 'HTTPS_PROXY' in os.environ:
    proxies['https'] = os.environ['HTTPS_PROXY']
self.client.get('/api', params=params, proxies=proxies)
```

※このやり方はpython-requestsに依存している

### FastHttpLocustを使ってパフォーマンスアップ

[Increase Locust’s performance with a faster HTTP client — Locust 0.14.5 documentation](https://docs.locust.io/en/stable/increase-performance.html)

- デフォルトのHTTPクライアントとしてpython-requestsを使っているが、geventhttpclientを使うFastHttpLocustを代わりに使うことができる
  - python-requestsと非互換なところもあるので注意

Example:

```Python
from locust import TaskSet, task, between
from locust.contrib.fasthttp import FastHttpLocust

class MyTaskSet(TaskSet):
    @task
    def index(self):
        response = self.client.get("/")

class MyLocust(FastHttpLocust):
    task_set = MyTaskSet
    wait_time = between(1, 60)
```
