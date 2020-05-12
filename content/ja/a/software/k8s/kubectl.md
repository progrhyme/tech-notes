---
title: "kubectl"
linkTitle: "kubectl"
date: 2020-05-01T12:15:07+09:00
weight: 150
---

Kubernetesクラスタを制御するCLI.

## Documentation

- https://kubernetes.io/docs/reference/kubectl/overview/
- リファレンス: https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands
- [kubectl Cheat Sheet - Kubernetes](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
- https://kubectl.docs.kubernetes.io/

参考:

- [Kubernetes道場 23日目 - kubectlを網羅する - Toku's Blog](https://cstoku.dev/posts/2018/k8sdojo-23/)

## 周辺ツール

- [Krew](https://krew.sigs.k8s.io/) ... kubectl plugin manager
- [kubectx](https://github.com/ahmetb/kubectx) ... context, namespaceの切替を簡単にしてくれる
- [kustomize]({{< ref "/a/software/k8s/kustomize.md" >}}) ... Kubernetesのマニフェスト管理ツール。kubectl 1.14からkubectlに取り込まれた
- [lbolla/kube-secret-editor](https://github.com/lbolla/kube-secret-editor) ... secretをデコードした状態で編集することを可能にし、編集後にエンコードして保存してくれる

## 設定
### kubeconfig

環境設定ファイルkubeconfigを参照する順番:

> 1. `--kubeconfig` フラグで指定されたパス
> 1. `$KUBECONFIG` 環境変数に指定されたパス一覧
> 1. `~/.kube/config`

See [Organizing Cluster Access Using kubeconfig Files - Kubernetes](https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/)

参考:

- [kubectlの接続設定ファイル（kubeconfig）の概要 - Qiita](https://qiita.com/shoichiimamura/items/91208a9b30e701d1e7f2)

## ユースケース
### 環境設定 - config & context

```sh
## kubeconfig 表示
kubectl config view

## context
### 一覧表示
kubectl config get-contexts
### 現在のcontext
kubectl config current-context

### 変更
kubectl config use-context <context-name>
```

参考:

- [kubectl 用のクラスタ アクセスの構成 | Kubernetes Engine のドキュメント | Google Cloud](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl?hl=ja)

### 実行・公開

- run ... コンテナイメージを実行する。deploymentまたはjobが作られる。
- expose ... リソースをクラスタ外にServiceとして公開する。

```sh
## run
### 例
kubectl run nginx --image=nginx

## expose
### 例
kubectl expose deployment <deployment-name> --port=80 --target-port=8000

kubectl run <deployment-name> --image=<image-name> --port=<port>
kubectl expose deployment <deployment-name> --type=NodePort
```

### App Management

- autoscale
- scale ... 次のリソースのサイズを設定する:
  - Deployment, ReplicaSet, Replication Controller, StatefulSet


```sh
## scale
### ReplicaSet 'foo' を3に
kubectl scale --replicas=3 rs/foo

kubectl scale --replicas=3 -f foo.yml

### 今のサイズが2だったら3にする
kubectl scale --current-replicas=2 --replicas=3 deployment/mysql
```

### リソース管理
#### 作成・更新

- create/apply/replace ... JSON or YAMLのリソース定義ファイルを適用して、リソースを作成/更新する。
- patch ... YAML/JSONのマージを用いて、リソース定義を差分更新する

```sh
# create
kubectl create -f <Path or URL of config file>

## ファイルから Secret を作成
kubectl create secret generic my-secret --from-file=./secret/secret.json
## ファイルから ConfigMap を作成
kubectl create configmap my-config --from-file=./config/config.json


# apply
kubectl apply -f <Path or URL of config file>

## 例
kubectl apply -f https://k8s.io/docs/tasks/run-application/deployment.yaml
kubectl apply -f ./pod.json


# replace
kubectl replace -f <Path or URL of config file>


# patch
kubectl patch <Resource Type> <Name> --patch <YAML Content>

## 例
kubectl patch deployment patch-demo --patch "$(cat patch-file.yaml)"
```

参考:

- [Update API Objects in Place Using kubectl patch - Kubernetes](https://kubernetes.io/docs/tasks/run-application/update-api-object-kubectl-patch/)
- [Kubernetes 上で Credentials を扱う | tellme.tokyo](https://tellme.tokyo/post/2018/08/07/kubernetes-configmaps-secrets/)
- [Kubernetes道場 23日目 - kubectlを網羅する - Toku's Blog](https://cstoku.dev/posts/2018/k8sdojo-23/)
- [kubectl applyとkubectl replaceの違いは何ですか - コードログ](https://codeday.me/jp/qa/20190406/566540.html)


#### Pod操作

- exec ... コマンドをコンテナ内で実行する
- cp ... ファイルをクライアント環境とPod間でやりとり


```sh
## exec
kubectl exec <pod> -- <command> [args...]
### podにbashでログイン
kubectl exec -it <pod> -- /bin/bash -l

## cp
kubectl cp path/to/localfile <pod>:/path/to/remotefile
kubectl cp <pod>:/path/to/remotefile /path/to/localfile
```

参考:

- [kubernetes: コンテナイメージにログインする - Qiita](https://qiita.com/suzukihi724/items/515654f54538a2103ee0)


#### Node操作

- cordon ... ノードへのスケジュールを停止
- drain ... ノードからPodを削除

```sh
## cordon
kubectl cordon <node-name>

## drain
kubectl drain <node-name>
### DaemonSetで管理されてPodを停止するとき
kubectl drain <node-name> --ignore-daemonsets
```

参考:

- [kubernetesの無停止運用を意識した検証 – てっくぼっと！](https://blog.applibot.co.jp/2016/12/27/kubernetes-zero-downtime/)
- [Kubernetes の drain について検証した時のメモ - Qiita](https://qiita.com/toshihirock/items/d22fee20b1a561b9efea)

#### 表示

- get ... 単一・複数リソースの情報を表示する。
- describe ... 単一リソース or グループの情報を表示
- diff ... リソースファイルとクラスタの状態を差分表示

```sh
# get
kubectl get deploy[ments]
kubectl get po[ds] [-o json|yaml]

## フィルタの例
kubectl get pods -l app=nginx

# describe
kubectl describe pods # all pods
kubectl describe pod <pod-name>
kubectl describe deploy[ment] <deployment-name>

# diff
kubectl diff -f foo.yml
## kustomizeバージョン
kubectl diff -k .
```

#### 削除

```sh
## delete
kubectl delete deployment <deployment-name>
```

## サブコマンド
### apply

基本的な利用イメージは[ユースケース > リソース管理 > 作成更新](#作成更新)を見よ。

オプション:

 オプション | デフォルト | 機能
------------|------------|------
 `--prune` | `false` | α in 2020-0505. <br />指定されてないリソースを削除する。ただし、<br /> `--save-config` オプション付きで作られたものは除く。<br /> `-l` フィルタか `--all` オプションと同時に使うべし
 `--prune-whitelist` | `[]` | `--prune` で使うデフォルトのホワイトリストを上書きする

Examples:

```sh
# app=nginxラベルのリソースにマニフェストを適用し、マニフェスト外のリソースを削除する
kubectl apply --prune -f manifest.yaml -l app=nginx

# マニフェストに書かれていないConfigMapを全て削除
kubectl apply --prune -f manifest.yaml --all --prune-whitelist=core/v1/ConfigMap
```

### logs

```sh
## 基本構文
kubectl logs <Pod名> [Options]

## 10行 tail -f
kubectl logs <Pod名> --tail=10 -f
```

### proxy

API Proxyサーバを起動する

```sh
kubectl proxy --port=8080 &
curl http://localhost:8080/api/
```

See https://kubernetes.io/docs/tasks/administer-cluster/access-cluster-api/

## How-to
### EvictedなPodを一括削除するワンライナー

EvictionしたPodは手動削除しないといけないっぽい。

```sh
kubectl get pods | awk '{if ($3 ~ /Evicted/) system ("kubectl delete pods " $1)}'
```

PodのEvictionについてはSee [Concept#pod-eviction]({{< ref "/a/software/k8s/concept.md" >}}#pod-eviction)

参考:

- [k8sでEvictedされたpodを一括削除する - Qiita](https://qiita.com/keizokeizo3/items/84a3ece88cd86fde9f75)
- [What will happen to evicted pods in kubernetes? - Stack Overflow](https://stackoverflow.com/questions/46419163/what-will-happen-to-evicted-pods-in-kubernetes)

### 全てのマニフェストを取得したい

これでよさそう:

```sh
kubectl get all --export -o yaml
```

NOTE:

- ※v1.14で `--export` オプションはdeprecateされているが、2020-05-07, 代替手段は見つけられていない。
- 上だとPodもexport対象になるので、使い勝手悪いかも？

参考:

- [Is there a way to generate yml files that will produce the existing cluster? · Issue #24873 · kubernetes/kubernetes](https://github.com/kubernetes/kubernetes/issues/24873)
- [Deprecate --export flag from get command by soltysh · Pull Request #73787 · kubernetes/kubernetes](https://github.com/kubernetes/kubernetes/pull/73787)
- [Kubernetes 1.14: Urgent Upgrade Notes, Deprecations, Removed and deprecated metrics, API Changes - Qiita](https://qiita.com/tkusumi/items/a824e040475fc47d311a)
- [Dump Kubernetes cluster resources as YAML](https://gist.github.com/negz/c3ee465b48306593f16c523a22015bec) ... シェルスクリプトで頑張っている事例
