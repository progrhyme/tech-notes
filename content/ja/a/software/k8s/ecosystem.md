---
title: "エコシステム"
linkTitle: "エコシステム"
description: 関連ソフトウェア製品など
date: 2020-05-07T11:10:18+09:00
weight: 15
---

## 参考

- [Kubernetesのエコシステムをまとめる - Qiita](https://qiita.com/cvusk/items/100dfb955150ef8964e5) 2018年5月時点
- [k3s と MicroK8s の違いを考える - Qiita](https://qiita.com/ynott/items/89941c36c606a8384028)

## マニフェスト管理

※ * は当サイト内のページ

- [kustomize]({{<ref "/a/software/k8s/kustomize.md" >}}) *
- [Helm](https://helm.sh/)
- [ksonnet](https://github.com/ksonnet/ksonnet)
  - 2019年2月で更新が止まっている。参考: [Welcoming Heptio Open Source Projects to VMware](https://tanzu.vmware.com/content/blog/welcoming-heptio-open-source-projects-to-vmware)

## クラスタ構築

- kubeadm ... 公式

参考:

- [2019年版・Kubernetesクラスタ構築入門 | さくらのナレッジ](https://knowledge.sakura.ad.jp/20955/)

### 開発・テスト用

- Minikube（See below）
- [Kind](https://kind.sigs.k8s.io/)
  - 参考:
    - [Kind で量産する使い捨て Kubernetes #cicd_test_night / CICD Test Night 5th - Speaker Deck](https://speakerdeck.com/ytaka23/cicd-test-night-5th)
    - [kindで軽量テスト用Kubernetesクラスタを作る＆運用する時のTIPS - Qiita](https://qiita.com/Hiroyuki_OSAKI/items/2395e6bbb98856df12f3)
- [MicroK8s](https://microk8s.io/) ... Canonical社が出してるやつ
  - 参考: [第560回 microk8sでお手軽Kubernetes環境構築：Ubuntu Weekly Recipe｜gihyo.jp … 技術評論社](https://gihyo.jp/admin/serial/01/ubuntu-recipe/0560)

#### Minikube

https://github.com/kubernetes/minikube

ローカルでKubernetesを動かすためのツール。  
Linuxのみだが、ハイパーバイザを噛まさず、ローカルのdocker上に直接クラスタを構築することもできる。

- https://kubernetes.io/docs/getting-started-guides/minikube/ ... 導入ガイド
  - ※先にkubectlをインストールしておくこと

参考:

- [minikubeでローカルKubernetesクラスタを5分でつくる方法 - Qiita](https://qiita.com/mumoshu/items/8f55ee830d8e5c172dd4)
- [minikube でローカルでのテスト用 Kubernetes を構築 – 1Q77](https://blog.1q77.com/2016/10/setup-kubernetes-1-4-using-minikube/)
- [ローカルでkubernetesを動かせるminikubeを試す - 年中アイス](http://reiki4040.hatenablog.com/entry/2017/04/11/221122)

## クライアント

kubectlと周辺ツールについては[kubectl]({{< ref "/a/software/k8s/kubectl.md" >}})を見よ。

- K9s ... See below

### K9s

[K9s - Manage Your Kubernetes Clusters In Style](https://k9scli.io/)

Documents:

- [Install](https://k9scli.io/topics/install/)
- [Commands](https://k9scli.io/topics/commands/)

参考:

- [k9sで快適なk8sライフを送ろう！ - エニグモ開発者ブログ](https://tech.enigmo.co.jp/entry/2019/12/17/090000)

#### CLI

オプション

 オプション | 意味
----------|------
 `--readonly` | 更新操作を無効にする

NOTE:

- モニタリング用途で使う場合、 `--readonly` をつけるべき

#### インタラクティブモード


`k9s` コマンド起動後の操作

 コマンド | 意味
---------|-----
 `:q[uit]`, `Ctrl+c` | 終了
 `<Esc>` | 元の画面に戻る
 `:ctx` | context選択
 `:ns` | namespace選択
 `/` | リソースフィルタ。あいまい検索。 `-l` でラベルセレクトも使える
 `d`, `y` | describe, YAMLを見る
 `e` | 編集
 `l` | ログ表示
 `Ctrl+d` | リソースを削除する
 `Ctrl+k` | リソースを停止（Kill）する（**確認ダイアログはない**）

## CI/CD

※ * は当サイト内のページ

- [Argo CD](https://argoproj.github.io/argo-cd/)
- [Concourse](https://concourse-ci.org/)
  - 参考: [Kubernetesを前提としたCI/CDパイプラインの具体例と、本番運用に必要なもの (1/2)：コンテナベースのCI/CD本番事例大解剖（3） - ＠IT](https://www.atmarkit.co.jp/ait/articles/1909/04/news005.html)
- [Jenkins X](https://jenkins-x.io/)
- [Prow](https://github.com/kubernetes/test-infra/tree/master/prow)
  - 参考: [KubernetesベースのCI/CDシステムProwに入門してみた | CyberAgent Developers Blog](https://developers.cyberagent.co.jp/blog/archives/22072/)
- Skaffold（See below）
- [Spinnaker]({{< ref "/a/software/spinnaker/_index.md" >}}) *
- [Tekton](https://tekton.dev/)

参考:

- [Spinnaker vs. Argo CD vs. Tekton vs. Jenkins X: Cloud-Native CI/CD](https://www.inovex.de/blog/spinnaker-vs-argo-cd-vs-tekton-vs-jenkins-x/)

### Skaffold

開発・本番向けにKubernetesクラスタに継続的デリバリーを実施するコマンドラインツール。

- https://github.com/GoogleContainerTools/skaffold
- https://skaffold.dev/

## 暗号化

- [bitnami-labs/sealed-secrets: A Kubernetes controller and tool for one-way encrypted Secrets](https://github.com/bitnami-labs/sealed-secrets)
  - Secretを暗号化してセキュアに管理する方法を提供してくれる

参考:

- [Sealed Secretsを利用したKubernetes Secretリソースのセキュアな管理 - Uzabase Tech Blog](https://tech.uzabase.com/entry/2020/03/10/171733)

## その他

- [K3s: Lightweight Kubernetes](https://k3s.io/) ... Rancherが出してる軽量版K8s
- [ksync | Sync files between your local system and a kubernetes cluster.](https://ksync.github.io/ksync/)
