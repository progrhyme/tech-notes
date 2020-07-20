---
title: "Compute Engine"
linkTitle: "GCE"
description: https://cloud.google.com/compute/
date: 2020-05-04T09:10:38+09:00
weight: 200
---

## 仮想マシン

[マシンタイプ | Compute Engine ドキュメント | Google Cloud](https://cloud.google.com/compute/docs/machine-types?hl=ja)

### プリエンプティブルVMインスタンス

https://cloud.google.com/compute/docs/instances/preemptible

Preemptible VM Instance. AWSでいうところのスポットインスタンス。

- いつでも停止される可能性がある
- 24時間実行したら必ず停止される

#### プリエンプト処理

1. プリエンプション通知を[ACPI G2 ソフトオフ](https://en.wikipedia.org/wiki/Advanced_Configuration_and_Power_Interface#Power_states)形式でインスタンスに送信
1. [シャットダウンスクリプト](https://cloud.google.com/compute/docs/instances/create-start-preemptible-instance?hl=ja#handle_preemption)によってプリエンプションを処理。インスタンス停止前にクリーンアップ操作を実施できる
1. インスタンスが30秒以内に停止しないと、[ACPI G3 メカニカルオフ](https://en.wikipedia.org/wiki/Advanced_Configuration_and_Power_Interface#Power_states)信号がOSに送信される
1. インスタンスは `TERMINATED` 状態になる

#### プリエンプトされたかどうか調べる

https://cloud.google.com/compute/docs/instances/create-start-preemptible-instance?hl=ja#detecting_if_an_instance_was_preempted

Cloud Loggingで `compute.instances.preempted` で検索。

参考:

- [ssh - GCP VM consistently shutting down without warning - Stack Overflow](https://stackoverflow.com/questions/58256153/gcp-vm-consistently-shutting-down-without-warning)

#### 参考

- [格安に使えるGCEのプリエンプティブインスタンスの勝手に停止対策 | marketechlabo](https://www.marketechlabo.com/gce-preemptible-instance/)

### インスタンスグループ

- マネージド ... オートスケールする。インスタンステンプレートを使う
- 非マネージド ... 自前でインスタンスを登録して管理
  - [非マネージド インスタンス グループの作成 | Compute Engine ドキュメント | Google Cloud](https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-unmanaged-instances?hl=ja)

### Shielded VM

Documents:
- [Shielded VM | ドキュメント | Google Cloud](https://cloud.google.com/security/shielded-cloud/shielded-vm?hl=ja)

Features:

- セキュアブート
- [整合性モニタリング](https://cloud.google.com/compute/docs/instances/integrity-monitoring?hl=ja)

NOTE:

- 整合性チェックに引っかかると、インスタンスが起動しない（起動直後にシャットダウンする）ことがある

参考:

- [UEFI#セキュアブート]({{< ref "/a/firmware/uefi.md" >}}#セキュアブート)
- [why my google cloud instance often shut down automatically by itself - Stack Overflow](https://stackoverflow.com/questions/56100268/why-my-google-cloud-instance-often-shut-down-automatically-by-itself)

## インスタンスメタデータ

ドキュメント:

- [インスタンス メタデータの保存と取得 | Compute Engine ドキュメント | Google Cloud](https://cloud.google.com/compute/docs/storing-retrieving-metadata?hl=ja)

エンドポイントURL: `http://metadata.google.internal/computeMetadata/v1/`

## Machine Images

Beta at 2020-04-16現在

https://cloud.google.com/compute/docs/machine-images

最近リリースされたやつ。  
従来のImageとの違いは↑に書いてある。

## Images

https://cloud.google.com/compute/docs/images?hl=ja

AWS AMIみたいなもの

Documents:
- [イメージとスナップショットの共有 | Compute Engine ドキュメント | Google Cloud](https://cloud.google.com/compute/docs/images/sharing-images-across-projects?hl=ja)

NOTE:
- VMからカスタムイメージを作る場合は、VMを停止しないと駄目みたい
