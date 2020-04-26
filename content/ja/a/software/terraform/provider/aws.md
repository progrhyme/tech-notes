---
title: "AWS"
linkTitle: "AWS"
description: >
  https://www.terraform.io/docs/providers/aws/
date: 2020-04-26T23:20:34+09:00
---

## Provider Configuration

- `max_retries` ... APIのリトライ回数を指定できる

## Data Sources

### acm_certificate

https://www.terraform.io/docs/providers/aws/d/acm_certificate.html

ACM証明書の情報取得

参考:

- [Terraform v0.7.9 でACMのデータソースが導入されました ｜ Developers.IO](https://dev.classmethod.jp/cloud/aws/terraform-supports-acm-data-source-in-v-0-7-9/ "Terraform v0.7.9 でACMのデータソースが導入されました ｜ Developers.IO")
- [ACMで取得した証明書をterraformで配置する - tjinjin's blog](http://cross-black777.hatenablog.com/entry/2016/11/17/231733 "ACMで取得した証明書をterraformで配置する - tjinjin's blog")

### caller_identity

https://www.terraform.io/docs/providers/aws/d/caller_identity.html

Terraform実行中のAWSアカウントのID等の情報を取得する。

参考:

- [*.tf 内で AWS アカウント ID を自動参照(取得)する aws_caller_identity Data Source - Qiita](https://qiita.com/gongo/items/a2b83d7402b97ef43574 "*.tf 内で AWS アカウント ID を自動参照(取得)する aws_caller_identity Data Source - Qiita")

### iam_policy_document

https://www.terraform.io/docs/providers/aws/d/iam_policy_document.html

IAM PolicyのJSONをHCLっぽく定義できる。  
JSONテンプレートより融通が効くし、syntax checkも掛かるので、便利なことがある。

### region

https://www.terraform.io/docs/providers/aws/d/region.html

`provider` で設定したリージョンを取得できる。

### sns_topic

https://www.terraform.io/docs/providers/aws/d/sns_topic.html

SNS TopicのARNを取得できる。

### ssm_parameter

https://www.terraform.io/docs/providers/aws/d/ssm_parameter.html

EC2 Parameter Storeからデータ取得

```terraform
# "foo"という名前のパラメータストアを取得
data "aws_ssm_parameter" "foo" {
  name  = "foo"
}
```

- `SecureString` であっても特にKSM keyを指定する必要はない。内部的にdecryptしてくれるみたい。
  - "terraformのstateの中ではraw textで保存されるから気をつけてね"って書いてある。

参考:

- [terraform と パラメータストア - yBlog](http://ymmtmsys.hatenablog.com/entry/2017/06/28/000822 "terraform と パラメータストア - yBlog")
- https://aws.amazon.com/jp/ec2/systems-manager/parameter-store/

## Resources

### appautoscaling関連

Application AutoScaling.  
ECS Serviceなどのオートスケール設定。

- https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy.html
- https://www.terraform.io/docs/providers/aws/r/appautoscaling_target.html

### autoscaling関連

- https://www.terraform.io/docs/providers/aws/r/autoscaling_group.html
- https://www.terraform.io/docs/providers/aws/r/launch_configuration.html

### cloudwatch関連

- https://www.terraform.io/docs/providers/aws/r/cloudwatch_log_group.html
  - `retention_in_days` ... ログの保持期間。とり得る値は http://docs.aws.amazon.com/ja_jp/AmazonCloudWatchLogs/latest/APIReference/API_PutRetentionPolicy.html に示されている。 `0` を指定すると無期限になる。
- https://www.terraform.io/docs/providers/aws/r/cloudwatch_log_subscription_filter.html
  - ElasticsearchやKinesisにサブスクライブするやつ
- https://www.terraform.io/docs/providers/aws/r/cloudwatch_metric_alarm.html
  - CloudWatch Alarmによる監視の作成
  - namespaceに指定する値は https://docs.aws.amazon.com/ja_jp/AmazonCloudWatch/latest/monitoring/aws-namespaces.html を参照。
  - 各namespaceで有効なmetric_nameやdimentionsフィールドの名前もAWSドキュメントを参照する。
- https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_rule.html
  - `schedule_expression` の書式は http://docs.aws.amazon.com/ja_jp/AmazonCloudWatch/latest/events/ScheduledEvents.html
- https://www.terraform.io/docs/providers/aws/r/cloudwatch_event_target.html


### ec2関連

- https://www.terraform.io/docs/providers/aws/r/ami.html
- https://www.terraform.io/docs/providers/aws/r/ebs_volume.html
- https://www.terraform.io/docs/providers/aws/r/eip.html
- https://www.terraform.io/docs/providers/aws/r/instance.html

### ecs関連

- https://www.terraform.io/docs/providers/aws/r/ecr_repository.html
- https://www.terraform.io/docs/providers/aws/r/ecr_repository_policy.html
- https://www.terraform.io/docs/providers/aws/r/ecs_cluster.html
- https://www.terraform.io/docs/providers/aws/r/ecs_service.html
  - `placement_strategy` ... ECSタスク配置戦略。See https://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/task-placement-strategies.html
- https://www.terraform.io/docs/providers/aws/r/ecs_task_definition.html
  - 指定可能なパラメーターについては、[タスク定義パラメーター - Amazon Elastic Container Service](https://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/task_definition_parameters.html "タスク定義パラメーター - Amazon Elastic Container Service") を参照。

動的ポートマッピングをする場合、task_definitionでhostPortを0にする:

```HCL
# ecs_task_definition.tf
resource "aws_ecs_task_definition" "service" {
  :
  container_definitions = "${file("task-definitions/service.json")}"
  :
}

# task_definitions/service.json
[
  {
    :
    "portMappings": [
      {
        "containerPort": 3000,
        "hostPort": 0,
    ]
  },
  :
]
```

参考:

- [terraformで開発者個人別に自由にECSにコンテナをデプロイできる開発環境を用意する - Qiita](https://qiita.com/joker1007/items/c44a443036439ce535b4 "terraformで開発者個人別に自由にECSにコンテナをデプロイできる開発環境を用意する - Qiita")
- [TerraformでECS+ECRする話](https://www.slideshare.net/SatoshiHirayama/terraformecsecr "TerraformでECS+ECRする話")

### elasticsearch関連

- https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain.html
  - Exported Attributes:
    - `domain_id` ... `${AWSアカウントID}/${クラスタ名}` . 監視のdimentionとしてはそのままでは使えない。
- https://www.terraform.io/docs/providers/aws/r/elasticsearch_domain_policy.html

### iam関連

- https://www.terraform.io/docs/providers/aws/r/iam_access_key.html
- https://www.terraform.io/docs/providers/aws/r/iam_group.html
- https://www.terraform.io/docs/providers/aws/r/iam_group_policy_attachment.html
- https://www.terraform.io/docs/providers/aws/r/iam_instance_profile.html
- https://www.terraform.io/docs/providers/aws/r/iam_policy.html
- https://www.terraform.io/docs/providers/aws/r/iam_role.html
- https://www.terraform.io/docs/providers/aws/r/iam_role_policy.html
- https://www.terraform.io/docs/providers/aws/r/iam_user.html
- https://www.terraform.io/docs/providers/aws/r/iam_user_policy.html ... 当該IAM Userにだけつけるインラインポリシー
- https://www.terraform.io/docs/providers/aws/r/iam_user_policy_attachment.html
- policyとroleの紐付け
  - https://www.terraform.io/docs/providers/aws/r/iam_policy_attachment.html
    - policy : roleが1対多。コード化されていないroleへの紐付けは削除される。
  - https://www.terraform.io/docs/providers/aws/r/iam_role_policy_attachment.html
    - policy : roleが1対1.

### kms関連

- https://www.terraform.io/docs/providers/aws/r/kms_alias.html ... alias for KMS key
- https://www.terraform.io/docs/providers/aws/r/kms_key.html ... KMS master keyの作成・管理

### lambda関連

- https://www.terraform.io/docs/providers/aws/r/lambda_function.html
  - runtime ... 利用できるruntimeについては [CreateFunction - AWS Lambda](https://docs.aws.amazon.com/ja_jp/lambda/latest/dg/API_CreateFunction.html#SSS-CreateFunction-request-Runtime "CreateFunction - AWS Lambda") を見る。
- https://www.terraform.io/docs/providers/aws/r/lambda_permission.html
  - マネジメントコンソールだと"Triggers"のタブ
  - 許可したリソースからLambdaを実行することができる


### lb関連

ALB等の作成・管理:

- https://www.terraform.io/docs/providers/aws/r/lb.html
- https://www.terraform.io/docs/providers/aws/r/lb_listener.html
- https://www.terraform.io/docs/providers/aws/r/lb_target_group.html

CLB:

- https://www.terraform.io/docs/providers/aws/r/elb.html

### rds関連

- https://www.terraform.io/docs/providers/aws/r/db_event_subscription.html ... RDSイベント通知
- https://www.terraform.io/docs/providers/aws/r/rds_cluster.html ... Aurora用(?)
- https://www.terraform.io/docs/providers/aws/r/rds_cluster_instance.html ... Aurora用(?)
- https://www.terraform.io/docs/providers/aws/r/db_instance.html
- ~~https://www.terraform.io/docs/providers/aws/r/db_subnet_group.html~~ ... これはEC2 Classic用でもう使うことはなさそう。
- https://www.terraform.io/docs/providers/aws/r/db_security_group.html
- https://www.terraform.io/docs/providers/aws/r/rds_cluster_parameter_group.html
- https://www.terraform.io/docs/providers/aws/r/db_parameter_group.html

### route53関連

- https://www.terraform.io/docs/providers/aws/r/route53_zone.html
  - `vpc_id` を指定するとPrivate Hosted Zoneになる。
  - `delegation_set_id` を指定するとPublic Hosted Zoneになる。
- https://www.terraform.io/docs/providers/aws/r/route53_record.html
  - Route53のDNSレコード作成・管理


### s3関連

- https://www.terraform.io/docs/providers/aws/r/s3_bucket.html
- https://www.terraform.io/docs/providers/aws/r/s3_bucket_policy.html

### sns関連

- https://www.terraform.io/docs/providers/aws/r/sns_topic.html
- https://www.terraform.io/docs/providers/aws/r/sns_topic_policy.html
- https://www.terraform.io/docs/providers/aws/r/sns_topic_subscription.html
  - ※emailのサブスクリプションは作成できない。メール認証が必要なので。

### vpc関連

- https://www.terraform.io/docs/providers/aws/r/default_route_table.html
  - これはimportに対応していない
  - route_table + main_route_table_associationで代替できそう
- https://www.terraform.io/docs/providers/aws/r/main_route_table_assoc.html
- https://www.terraform.io/docs/providers/aws/r/route.html
  - route_tableと一緒に使うとまずそう
- https://www.terraform.io/docs/providers/aws/r/route_table.html
- https://www.terraform.io/docs/providers/aws/r/subnet.html
- https://www.terraform.io/docs/providers/aws/r/vpc.html
  - Route 53のPrivate DNSを使うには、 `enable_dns_hostnames`, `enable_dns_support` を `true` にする。


### budgets_budget

https://www.terraform.io/docs/providers/aws/r/budgets_budget.html

Budgetにコストアラートを設定できたり。

### dynamodb_table

https://www.terraform.io/docs/providers/aws/r/dynamodb_table.html

DynamoDB table作成


### security_group

https://www.terraform.io/docs/providers/aws/r/security_group.html

Security Groupの作成・管理

### sqs_queue

https://www.terraform.io/docs/providers/aws/r/sqs_queue.html

SQS Queueの作成・管理

### ssm_parameter

https://www.terraform.io/docs/providers/aws/r/ssm_parameter.html

EC2 Parameter Storeにデータを保存する。
