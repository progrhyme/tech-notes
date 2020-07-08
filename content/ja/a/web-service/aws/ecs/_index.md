---
title: "ECS"
linkTitle: "ECS"
date: 2020-07-08T23:08:55+09:00
weight: 150
---

EC2インスタンスをホストとしてDockerコンテナを容易にクラスタリング・サービス化する。タスクランナーとしても使える。

## Getting Started

- ドキュメント: http://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/Welcome.html
- 最新AMI: http://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/ecs-optimized_AMI.html

## 仕様

- [タスクのライフサイクル \- Amazon EC2 Container Service](http://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/task_life_cycle.html)
- [Amazon ECS イベント - Amazon Elastic Container Service](http://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/ecs_cwe_events.html "Amazon ECS イベント - Amazon Elastic Container Service")
  - コンテナインスタンスやタスクの状態変更イベント

### タスク定義

- https://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/task_definitions.html

#### タスク定義パラメーター

- [タスク定義パラメーター \- Amazon Elastic Container Service](https://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/task_definition_parameters.html)

以下のようなものがある:

- `volumesFrom` ... `docker run` の `--volumes-from` オプションに相当。

### サービス

- [サービスロードバランシング - Amazon Elastic Container Service](https://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/service-load-balancing.html#load-balancing-concepts "サービスロードバランシング - Amazon Elastic Container Service")
  - 1つのサービスに紐付けられるLBは1つだけ。複数ポートをサーブしたい場合は、サービスを分ける必要がある。
- [Amazon ECS タスク配置戦略 - Amazon Elastic Container Service](https://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/task-placement-strategies.html "Amazon ECS タスク配置戦略 - Amazon Elastic Container Service")
  - タスクをどう配置するか。AZ間で分散する、利用インスタンス数を最小にするなど選べる。
  - ECSサービスでは作成時に選択する。

Tips:

- ECSをタスクランナーとして使うときも、サービスを作っておくとタスク定義をテンプレート的に使い回せるので便利
- 「Run more like this」で環境変数など上書きしたタスクを実行することが可能

## Features
### 動的ポートを使ってALBからロードバランス

`docker run` の `-P` オプションに相当するポートマッピング方式で、ホスト側の任意のエフェメラルポートにコンテナのポートがマッピングされる。

これによってALBからロードバランスすることができる。

これを使うとECSホストとなるインスタンスが1台しかいなくても、コンテナをローリング更新できる。

固定ポート方式だと、ホスト側のポートが被るので新しいコンテナをデプロイできない。

参考:

- [Amazon ECSのELB構成パターンまとめ(ALB対応) ｜ Developers.IO](https://dev.classmethod.jp/cloud/ecs-elb-recipes/ "Amazon ECSのELB構成パターンまとめ(ALB対応) ｜ Developers.IO")
- [Dockerコンテナの作成からECSの動的ポート＋ALBでロードバランスするまで【cloudpack大阪ブログ】 - Qiita](https://qiita.com/taishin/items/eb759a8ec0c583fc5ebd "Dockerコンテナの作成からECSの動的ポート＋ALBでロードバランスするまで【cloudpack大阪ブログ】 - Qiita")


### Service Auto Scaling

コンテナの数を機械的にスケールさせたい場合、クラスタインスタンスのAuto Scalingとは別にService Auto Scalingを設定する必要がある。

参考:

- [サービスの Auto Scaling - Amazon Elastic Container Service](http://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/service-auto-scaling.html "サービスの Auto Scaling - Amazon Elastic Container Service")
- [Amazon ECSでAuto Scaling \| Amazon Web Services ブログ](https://aws.amazon.com/jp/blogs/news/automatic-scaling-with-amazon-ecs/)
- [ECSのオートスケール戦略 \- Carpe Diem](http://christina04.hatenablog.com/entry/2017/10/19/190000)

### CloudWatch Logs連携

Logging Driverとしてawslogsを使うことでCloudWatch Logsにログ収集できる。

- [コンテナインスタンスでの CloudWatch Logs の使用 - Amazon Elastic Container Service](http://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/using_cloudwatch_logs.html "コンテナインスタンスでの CloudWatch Logs の使用 - Amazon Elastic Container Service")

### CloudWatch Event

- [Amazon ECS イベント - Amazon Elastic Container Service](http://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/ecs_cwe_events.html "Amazon ECS イベント - Amazon Elastic Container Service")

以下のようなイベントをCloudWatch Eventでトリガにすることができる:

- コンテナの状態変化
- タスクの状態変化
- :

## ノウハウ
### タスクの異常終了を監視する

上述のCloudWatch EventでLambdaを呼び出し、Lambda側で `lastStatus` や `exitCode` を判別すれば良い。

TODO: コードサンプルを書く。

参考:

- [Amazon ECSイベントストリームで、クラスタの状態を監視 | Amazon Web Services ブログ](https://aws.amazon.com/jp/blogs/news/monitor-cluster-state-with-amazon-ecs-event-stream/ "Amazon ECSイベントストリームで、クラスタの状態を監視 | Amazon Web Services ブログ")

### デバッグ出力の有効化

http://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/docker-debug-mode.html

```sh
$ sudo vi /etc/sysconfig/docker

## OPTIONSに下のように"-D"を足す。
OPTIONS="-D --default-ulimit nofile=1024:4096"

$ sudo service docker restart
$ sudo start ecs
```

### EBS Dockerボリュームの変更

デフォルト22Gなのだが、ワークロードが高い場合、Burst Balanceを使い切る可能性がある。  
ボリュームを拡張しておくことでキャパシティを上げることができるが、変えたい場合はEC2作成時やLaunch Configurationで変える必要がある。

デバイス名 `/dev/xvdcz` のボリュームを変えれば良い。

Terraformの場合、 [aws_launch_configuration](https://www.terraform.io/docs/providers/aws/r/launch_configuration.html) resourceの `ebs_block_device` ブロックで設定する。

```Terraform
resource "aws_launch_configuration" "my_ecs_launch_config" {
  :
  ebs_block_device {
    device_name = "/dev/xvdcz"
    volume_type = "gp2"
    volume_size = 50
  }
}
```

参考:

- [Amazon EBS ボリュームの種類 - Amazon Elastic Compute Cloud](http://docs.aws.amazon.com/ja_jp/AWSEC2/latest/UserGuide/EBSVolumeTypes.html "Amazon EBS ボリュームの種類 - Amazon Elastic Compute Cloud")

### ECSログコレクター

http://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/ecs-logs-collector.html

このスクリプトでインスタンスのログを集めて、診断に役立つようにAWSサポートと共有できるそうだ。

### タスク・イメージのクリーンアップ設定

参考:

- [Amazon ECSでタスク/イメージの自動クリーンアップが有効になりました ｜ Developers\.IO](https://dev.classmethod.jp/cloud/ecs-auto-cleanup/)

## How-to
### IAM設定

Terraformとかで構築してると、IAM設定がよくわからなくて気が狂いそうになる。  
1回動くと満足するが、次やるときにはやり方を忘れている。

- ECSサービスに設定するIAMロール
  - [Amazon ECS サービススケジューラ IAM ロール - Amazon Elastic Container Service](https://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/service_IAM_role.html)
  - 2019年1月現在は、指定しなくても勝手にAWSがマネージドなIAMロールを設定してくれるはず。
- ECSタスク実行IAMロール
  - [Amazon ECS タスク実行 IAM ロール \- Amazon Elastic Container Service](https://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/task_execution_IAM_role.html)
  - AssumeRoleで `Service: ecs-tasks.amazonaws.com` を許可する
  - IAMポリシーはマネージドなのがあるので、それをロールにアタッチすればよい


### クラスタ更新

やり方:

- Terraform
- [ecs-deploy](https://github.com/silinternational/ecs-deploy/blob/develop/ecs-deploy)
  - AWS CLIとjqを使ってシェルスクリプトで実装された便利ツール

参考:

- [CircleCI \+ ecs\-deploy で ECS にデプロイをする \- kakakakakku blog](https://kakakakakku.hatenablog.com/entry/2017/04/27/105327)


### プライベートレジストリを使う

See [プライベートレジストリの認証 - Amazon Elastic Container Service](https://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/private-auth.html "プライベートレジストリの認証 - Amazon Elastic Container Service")

### インスタンスをクラスタから外す

一時的に外したい場合。

- AutoScaling Groupからデタッチ
  - https://docs.aws.amazon.com/ja_jp/autoscaling/latest/userguide/detach-instance-asg.html
- ECSクラスタからインスタンスを外す
  - Drainingに変えれば良いと思う

### インスタンスを減らす

↑の操作は安全だが、台数を減らすのは難しい。  
というのはAutoScaling Groupでインスタンスの設定数を減らすことになるのだが、このときどのインスタンスが落とされるかを制御できないからだ。  

このときはAutoScaling Groupのライフサイクルフックを設定するのが王道のようだ。

または、落とされたくないインスタンスを保護するという手もある。

- [amazon web services \- ECS ASG scaling down policy recommendations \- Stack Overflow](https://stackoverflow.com/questions/45020323/ecs-asg-scaling-down-policy-recommendations/45036485#45036485)

参考:

- [Amazon ECS におけるコンテナ インスタンス ドレイニングの自動化方法 | Amazon Web Services ブログ](https://aws.amazon.com/jp/blogs/news/how-to-automate-container-instance-draining-in-amazon-ecs/ "Amazon ECS におけるコンテナ インスタンス ドレイニングの自動化方法 | Amazon Web Services ブログ")
- [Amazon EC2 Auto Scaling ライフサイクルフック - Amazon EC2 Auto Scaling (日本語)](https://docs.aws.amazon.com/ja_jp/autoscaling/ec2/userguide/lifecycle-hooks.html "Amazon EC2 Auto Scaling ライフサイクルフック - Amazon EC2 Auto Scaling (日本語)")


### コンテナ間でのデータボリュームの共有

参考:

- [ECSでコンテナインスタンス間でデータボリュームを同期したい時 \- hatappi\.blog](http://hatappi.hateblo.jp/entry/2017/05/12/175933)

## 参考

- [ECS運用のノウハウ \- Qiita](https://qiita.com/naomichi-y/items/d933867127f27524686a)
