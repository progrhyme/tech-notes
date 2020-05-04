---
title: "kustomize"
linkTitle: "kustomize"
description: https://kustomize.io/
date: 2020-05-04T17:54:50+09:00
weight: 200
---

Kubernetesのマニフェスト管理ツール。

リポジトリ: https://github.com/kubernetes-sigs/kustomize

kubectl 1.14からkustomizeが統合されている。

## ドキュメント/情報リソース

- Reference: https://kubectl.docs.kubernetes.io/pages/reference/kustomize.html
- Examples: https://github.com/kubernetes-sigs/kustomize/tree/master/examples


## CLI Usage

```sh
kubectl kustomize

# kustomization.yaml を含むディレクトリで
## Apply the Resource Config
kubectl apply -k .

## View the Resources
kubectl get -k .
```

参考:

- https://kubectl.docs.kubernetes.io/pages/app_management/apply.html


## How-to
### ConfigMapの管理

1. configMapGeneratorで生成
  - (2020-03-18) `behavior` を `create`, `replace`, `merge` から選べるのだが、 `create` 以外だとdiffでエラーが出るのだが…
1. resourcesで管理
  - ConfigMapをYAMLで管理することになる。こっちの方が扱いやすいように感じた


## 参考

- [KustomizeでKubernetes YAMLを管理する | SOTA](https://deeeet.com/writing/2018/07/10/kustomize/)
- [Kustomizeで環境ごとに異なるマニフェストを作る | Goldstine研究所](https://blog.mosuke.tech/entry/2019/06/21/kustomize/)
