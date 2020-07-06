---
title: "Secret"
linkTitle: "Secret"
description: >
  [Secrets - Kubernetes](https://kubernetes.io/docs/concepts/configuration/secret/)
date: 2020-05-04T22:39:15+09:00
weight: 700
---

See also [ConfigMap]({{< ref "/a/software/k8s/configmap.md" >}})

## Overview

ConfigMapと同じような使い方ができるが、暗号化機構が備わっており、クレデンシャルなど機微情報を扱うのに向いている。

Podから環境変数として読み込むという使い方をすることが多いようだ。

参考:

- [Kubernetes Secrets の紹介 – データベースのパスワードやその他秘密情報をどこに保存するか？ – ゆびてく](https://ubiteku.oinker.me/2017/03/01/kubernetes-secrets/)

## Documents

- [design-proposals/secrets.md - kubernetes/community](https://github.com/kubernetes/community/blob/master/contributors/design-proposals/auth/secrets.md)

## Secretsの作成

例1) テキストファイルから作成

```Bash
echo -n 'admin' > ./username.txt
echo -n '1f2d1e2e67df' > ./password.txt

kubectl create secret generic db-user-pass --from-file=./username.txt --from-file=./password.txt
```

例2) 自分で定義ファイル(YAML)を作る

```Bash
echo -n 'admin' | base64
YWRtaW4=
echo -n '1f2d1e2e67df' | base64
MWYyZDFlMmU2N2Rm
```

```YAML
## secret.yaml
apiVersion: v1
kind: Secret
metadata:
  name: mysecret
type: Opaque
data:
  username: YWRtaW4=
  password: MWYyZDFlMmU2N2Rm
```

```Bash
kubectl apply -f ./secret.yaml
```

## Secretの参照

ワークロードからSecretを参照したい場合、次のやり方を取ることができる:

- 環境変数として直接Secretを参照する
- ボリュームとしてマウントし、ファイルを参照する

Example:

```YAML
apiVersion: v1
kind: Pod
metadata:
  name: run
spec:
  containers:
  - name: run-container
    image: debian
    env:
    - name: DB_PASSWORD
      valueFrom:
        secretKeyRef:
          name: db-credentials # Secret名
          key: password # Secretに含まれるキー名
    volumeMounts:
    - name: secret
      mountPath: "/app/.credentials"
  volumes:
  - name: secret
    secret:
      secretName: app-credentials
```

参考:

- [Kubernetes Secret - Qiita](https://qiita.com/propella/items/e6a6fd1f77a6e4417fda)
